"""
LangChain Encapsulation
created by XinYiLea(li ao)
2024.3.10

If you want to study LangChain, please use the follow resources:
https://datawhalechina.github.io/prompt-engineering-for-developers/#/
https://liaokong.gitbook.io/llm-kai-fa-jiao-cheng

Important Environment:
    langchain 0.1.11
    langchain-community 0.0.25
    langchain-core 0.1.30
    openAI 0.28.0
    transformers 4.38.2
    pytorch 1.11.0

All functions have been debugged in the LearnLark environment and are ready for direct use.
"""

import warnings

import torch

warnings.filterwarnings("ignore")

import os
# CloseAI by XinYiLea
os.environ["OPENAI_API_BASE"] = 'https://api.openai-proxy.org/v1'
os.environ["OPENAI_API_KEY"] = 'sk-AMNe3weytZcweN2e4v1vPcNpjxXEGO1tN45dzgRzq013SARq'

import langchain
import langchain_core
import langchain_community
import os.path

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline,BitsAndBytesConfig
import bitsandbytes as bnb
from trl import setup_chat_format


from langchain.agents import load_tools,initialize_agent,AgentType,Tool
from langchain.chains import RetrievalQA, ConversationChain,LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain,RouterOutputParser
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter,CharacterTextSplitter
from langchain.tools import BaseTool
from langchain.output_parsers import ResponseSchema,StructuredOutputParser
import langchain.memory as LCmemory

from langchain_core.prompts import PromptTemplate

from langchain_community.vectorstores import Chroma
from langchain_community.llms import OpenAI,HuggingFacePipeline
from langchain_community.document_loaders import (UnstructuredFileLoader,DirectoryLoader,
                                                  PyPDFLoader,CSVLoader,Docx2txtLoader
                                                  )

class Utils(object):

    """
    langchain六大核心概念：
    Agents Chains Indexes(Document) Memory Models Prompts

    该类实现以下功能
    1.支持通过模板生成prompt
    2.支持json格式化LLM的输出，更加方便的提取信息
    3.支持四种类型的对话Memory，便于进行长对话理解
    4.支持设置LLM chain，通过路由选择更好的prompt辅助生成
    5.支持基础agent设置
    6.支持基于文档的QA，包含PDF,md,csv,docx,txt文档（对目录数据库还有部分类型不支持）
    7.支持使用Google Search联网辅助LLM
    8.支持构建本地llm Models完成任务（由于模型参数文件过大，暂时无法测试）
    9.支持通过目录建立临时或本地数据库Indexes

    by XinYiLea
    2024.3.12
    """

    LLM = OpenAI(model_name="gpt-3.5-turbo")
    SERPAPI_API_KEY = '77100720bf8583743dfc13de885b5d92b1b58cb9f3372e21db74000158efe30e'
    MULTI_PROMPT_ROUTER_TEMPLATE = """给语言模型一个原始文本输入，\
            让其选择最适合输入的模型提示。\
            系统将为您提供可用提示的名称以及最适合改提示的描述。\
            如果你认为修改原始输入最终会导致语言模型做出更好的响应，\
            你也可以修改原始输入。


            << 格式 >>
            返回一个带有JSON对象的markdown代码片段，该JSON对象的格式如下：
            ```json
            {{{{
                "destination": 字符串 \ 使用的提示名字或者使用 "DEFAULT"
                "next_inputs": 字符串 \ 原始输入的改进版本
            }}}}

            记住：“destination”必须是下面指定的候选提示名称之一，\
            或者如果输入不太适合任何候选提示，\
            则可以是 “DEFAULT” 。
            记住：如果您认为不需要任何修改，\
            则 “next_inputs” 可以只是原始输入。

            << 候选提示 >>
            {destinations}

            << 输入 >>
            {{input}}

            << 输出 (记得要包含 ```json)>>

            样例:
            << 输入 >>
            "什么是黑体辐射?"
            << 输出 >>
            ```json
            {{{{
                "destination": 字符串 \ 使用的提示名字或者使用 "DEFAULT"
                "next_inputs": 字符串 \ 原始输入的改进版本
            }}}}

            """

    def __init__(self):
        pass

    @staticmethod
    def create_agent(
        llm,
        tool_list:list,
        agent_type = AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose = False
    ):
        """
        该函数创建agent
        在langchain中自定义tool：只需要在函数上面添加 @tool，然后传入[function_name]即可
        其实这个函数没多大必要，但是为了满足langchain6大概念还是加进来了，处理操作也很简单
        """

        tools = load_tools(tool_list,llm)
        agent = initialize_agent(
            tools,
            llm,
            agent=agent_type,
            verbose=verbose,
            handle_parsing_errors=True
        )

        return agent

    @staticmethod
    def create_local_llm(
        model_path:str
    ):
        """
        创建本地LLM，暂时不支持自定义其他参数，仅传入模型权重文件即可
        该函数还未经过测试，请不要使用
        """

        tokenizer = AutoTokenizer.from_pretrained(model_path)

        bnb_config = BitsAndBytesConfig(
            load_in_4bit = True,
            bnb_4bit_quant_type = 'nf4',
            bnb_4bit_compute_dtype = torch.float16,
            bnb_4bit_use_double_quant = True
        )

        model = AutoModelForCausalLM.from_pretrained(model_path,
                                                     device_map = torch.device("cuda" if torch.cuda.is_available() else ""),
                                                     torch_dtype=torch.float16,
                                                     quantization_config=bnb_config)

        model,tokenizer = setup_chat_format(model,tokenizer)

        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=100
        )

        local_llm = HuggingFacePipeline(pipe)

        return local_llm

    @staticmethod
    def create_prompt(
        template_string:str,
        input_variables:list,
        is_output_format:bool = False,
        out_parser = None,
        **kwargs
    ):
        """
        使用提示模板可以方便的重复使用设计好的prompt
        eg: 模板为'生成一段风格为{style}的关于{about}的文本'，则需要添加style、about参数
        format_instructions:当需要格式化输出时使用，使用create_out_parsers()生成输出解释器
        """

        # format_instructions:str
        format_instructions = out_parser.get_format_instructions()

        if is_output_format:
            prompt_template = PromptTemplate(input_variables=input_variables,
                                             partial_variables={"format_instructions": format_instructions},
                                             template=template_string + '\n{format_instructions}')
        else:
            prompt_template = PromptTemplate(input_variables=input_variables,
                                             template=template_string)

        prompt = prompt_template.format_prompt(**kwargs)

        return prompt.to_string()

    @staticmethod
    def create_out_parsers(
        names:list,
        descriptions:list
    ):
        """
        create_out_parsers函数用于规定输出格式，更好的提取输出信息
        names与descriptions为传入的json的键值对
        eg:gift_schema = ResponseSchema(name="礼物",
                                 description="这件物品是作为礼物送给别人的吗？\
                                如果是，则回答 是的，\
                                如果否或未知，则回答 不是。")
        """

        response_schemas = []

        for name,description in zip(names,descriptions):
            response_schemas.append(ResponseSchema(
                name=name,
                description = description
            ))

        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

        return  output_parser

    @staticmethod
    def create_vector_database(
            directory_path: str,
            chunk_size: int = 250,
            chunk_overlap: int = 0,
            persist: bool = False,
            persist_directory: str = None
    ):
        """
        构建向量索引数据库：文档之间的相关性是通过向量计算的，所以需要构建向量数据库
        可以创建临时数据库与永久数据库
        Chroma是个本地向量数据库
        DirectoryLoader是使用Unstructured库导入全部的数据，所以需要pip对应文件类型的库
        """
        # 加载该目录下的所有文件，可以用glob进行筛选，这里还存在一些问题，无法直接从目录导入pdf与csv文件
        loader = DirectoryLoader(directory_path,exclude=['*.pdf','*.csv'])
        documents = loader.load() # 返回值是一个文档的list


        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        split_docs = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()

        if persist:
            database = Chroma.from_documents(documents, embeddings, persist_directory=persist_directory)
            # 设置数据库持久化
            database.persist()
        else:
            database = Chroma.from_documents(split_docs, embeddings)

        return database

    @staticmethod
    def create_conversation_chain(
        llm,
        memory_type:str,
        verbose:bool=False,
        **kwargs
    ):
        """
        该函数选择对话缓存的形式并创建，可以更好的支持长对话
        """
        allowed_values = ['default','windows','summarize','token']
        if memory_type not in allowed_values:
            raise ValueError(f"Parameter 'param' must be one of {allowed_values}")
        elif memory_type == 'default':
            memory = LCmemory.ConversationBufferMemory()
        elif memory_type == 'windows':
            memory = LCmemory.ConversationBufferWindowMemory(**kwargs)
        elif memory_type == 'summarize':
            memory = LCmemory.ConversationSummaryBufferMemory(llm=llm,**kwargs)
        elif memory_type == 'token':
            memory = LCmemory.ConversationTokenBufferMemory(llm=llm,**kwargs)

        conversation = ConversationChain(llm=llm, memory=memory, verbose=verbose)

        return conversation

    @staticmethod
    def create_router_chain(
        llm,
        prompt_infos,
        verbose:bool = False,
    ):
        """
        该函数创建一个路由链，可以组合多种chain，让LLM判断使用哪个chain
        支持自定义多条chain，但无法修改默认chain，默认chain为直接将输出给LLM
        prompt_infos的输入必须有且仅有三个key: name template description

        eg:
        physics_template = "你是一个非常聪明的物理专家。 \
                        你擅长用一种简洁并且易于理解的方式去回答问题。\
                        当你不知道问题的答案时，你承认\
                        你不知道.

                        这是一个问题:
                        {input}"

        {
        "name": "物理学",
        "description": "擅长回答关于物理学的问题",
        "template": physics_template
        }

        """

        # 目标链
        destination_chains = {}
        for p_info in prompt_infos:
            name = p_info["name"]
            prompt_template = p_info["template"]
            prompt = PromptTemplate.from_template(template=prompt_template)
            chain = LLMChain(llm=llm, prompt=prompt)
            destination_chains[name] = chain
        destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
        # 得到一个包含所有字符串元素的单独字符串，用/n分割
        destinations_str = "\n".join(destinations)

        # 默认目标链：直接给模型输入
        default_prompt = PromptTemplate.from_template("{input}")
        default_chain = LLMChain(llm=llm, prompt=default_prompt)

        # 多提示路由模板，固定代码无需修改
        router_template = Utils.MULTI_PROMPT_ROUTER_TEMPLATE.format(
            destinations=destinations_str
        )

        router_prompt = PromptTemplate(
            template=router_template,
            input_variables=["input"],
            output_parser=RouterOutputParser(),
        )

        router_chain = LLMRouterChain.from_llm(llm, router_prompt)

        # 让路由链路选择目标链路与默认链路
        chain = MultiPromptChain(router_chain=router_chain,  # 路由链路
                                 destination_chains=destination_chains,  # 目标链路
                                 default_chain=default_chain,  # 默认链路
                                 verbose=verbose
                                 )
        return chain

    @staticmethod
    def network_search(
        llm,
        search_text:str,
        verbose:bool = False,
        serpapi_api_key:str=SERPAPI_API_KEY,
    ):
        """
        Search用于llm联网获取请求内容
        需要提前获取SERPAPI_API_KEY
        zero-shot-react-description: 根据工具的描述与请求内容做决定
        """

        os.environ["SERPAPI_API_KEY"] = serpapi_api_key
        tools = ["serpapi"]

        agent = Utils.create_agent(llm,tools,verbose=verbose)

        result = agent.run(search_text)

        return result

    @staticmethod
    def summarize_text(
        llm,
        text_path:str,
        chunk_size:int = 250,
        chunk_overlap:int = 0,
        chain_type:str = 'refine',
        verbose:bool = False,
        **kwargs
    )->str:
        """
        Summarize_text用于总结一个文件中的内容，支持 md,pdf,csv,docx,txt类型
        请参照这个教程https://www.jianshu.com/p/fd501b927b72
        在https://github.com/nltk/nltk_data/tree/gh-pages?tab=readme-ov-file下载nltk相关文件
        chunk_overlap: 每个分割的文档之间的关联
        """

        document = Utils().__determine_file_type(text_path,**kwargs)
        print(f'documents:{len(document)}')

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap= chunk_overlap
        )
        split_documents = text_splitter.split_documents(document)
        print(split_documents)
        print(f'documents:{len(split_documents)}')

        chain = load_summarize_chain(llm,chain_type=chain_type,verbose=verbose)
        result = chain.run(split_documents)
        return result

    @staticmethod
    def QA_based_temporary_database(
        llm,
        query:str,
        database,
        chain_type:str = "stuff"
    ) ->dict :
        """
        基于数据库的问答，该数据库可以是临时数据库也可以是本地数据库
        query:需要问的问题
        docsearch:向量索引数据库
        """

        qa = RetrievalQA.from_chain_type(llm, chain_type=chain_type,
                                         retriever=database.as_retriever(),
                                         return_source_documents=True)
        result = qa({"query":query})
        return result

    @staticmethod
    def QA_based_exist_database(
        llm,
        query,
        database_path,
        chain_type: str = "stuff"
    ):

        embeddings = OpenAIEmbeddings()

        database = Chroma(persist_directory=database_path, embedding_function=embeddings)


        qa = RetrievalQA.from_chain_type(llm, chain_type=chain_type,
                                         retriever=database.as_retriever(),
                                         return_source_documents=True)

        result = qa({"query": query})

        return result


    def __determine_file_type(self,text_path, **kwargs):

        if text_path.endswith('.pdf'):
            loader = PyPDFLoader(text_path, **kwargs)
        elif text_path.endswith('.txt') or text_path.endswith('.md'):
            loader = UnstructuredFileLoader(text_path, **kwargs)
        elif text_path.endswith('.csv'):  # 第一行会被当成列名而无法加载进
            loader = CSVLoader(text_path, encoding='utf-8')
        elif text_path.endswith('.docx'):
            loader = Docx2txtLoader(text_path)  # 无需额外参数

        else:
            return None
        return loader.load()


if __name__ == '__main__':

    print('hello world')
