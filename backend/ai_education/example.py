from langchain_utils import Utils

import warnings
warnings.filterwarnings("ignore")

class Example(object):

    def __init__(self):
        self.llm = Utils.LLM

    def get_format_output(self):

        names = ['羊','牛']
        common_text = '如果有，则回答它的数量，如果否或未知，则回答 没有。'
        descriptions = [f'这个地方有{name}吗，{common_text}' for name in names]

        style = '有趣'
        about = '草原上的牛和羊'
        template = "请给我生成一段{style}的关于{about}的文本，谢谢你"

        # 生成输出格式
        out_parser = Utils.create_out_parsers(names=names,descriptions=descriptions)

        # 生成提示
        prompt = Utils.create_prompt(template_string=template,
                                     is_output_format=True,
                                     out_parser=out_parser,
                                     input_variables=['style','about'],
                                     style=style,
                                     about=about
                                    )

        print('prompt:', prompt)

        print(out_parser.parse(self.llm(prompt)))

    def get_conversation(self):

        # 以windows为样例
        conversation = Utils.create_conversation_chain(self.llm, 'windows', True, k=1)

        print(conversation.predict(input='你好，我是XinYiLea'))

        print(conversation.predict(input='我想知道你认识我吗'))

        print(conversation.predict(input='请问1+1在什么情况下等于3'))

    def get_router_chain(self):
        physics_template = """你是一个非常聪明的物理专家。 \
        你擅长用一种简洁并且易于理解的方式去回答问题。\
        当你不知道问题的答案时，你承认\
        你不知道.

        这是一个问题:
        {input}"""

        # 第二个提示适合回答数学问题
        math_template = """你是一个非常优秀的数学家。 \
        你擅长回答数学问题。 \
        你之所以如此优秀， \
        是因为你能够将棘手的问题分解为组成部分，\
        回答组成部分，然后将它们组合在一起，回答更广泛的问题。

        这是一个问题：
        {input}"""

        # 第三个适合回答历史问题
        history_template = """你是以为非常优秀的历史学家。 \
        你对一系列历史时期的人物、事件和背景有着极好的学识和理解\
        你有能力思考、反思、辩证、讨论和评估过去。\
        你尊重历史证据，并有能力利用它来支持你的解释和判断。

        这是一个问题:
        {input}"""

        # 第四个适合回答计算机问题
        computerscience_template = """ 你是一个成功的计算机科学专家。\
        你有创造力、协作精神、\
        前瞻性思维、自信、解决问题的能力、\
        对理论和算法的理解以及出色的沟通技巧。\
        你非常擅长回答编程问题。\
        你之所以如此优秀，是因为你知道  \
        如何通过以机器可以轻松解释的命令式步骤描述解决方案来解决问题，\
        并且你知道如何选择在时间复杂性和空间复杂性之间取得良好平衡的解决方案。

        这还是一个输入：
        {input}"""

        prompt_infos = [
            {
                "name": "物理学",
                "description": "擅长回答关于物理学的问题",
                "template": physics_template
            },
            {
                "name": "数学",
                "description": "擅长回答数学问题",
                "template": math_template
            },
            {
                "name": "历史",
                "description": "擅长回答历史问题",
                "template": history_template
            },
            {
                "name": "计算机科学",
                "description": "擅长回答计算机科学问题",
                "template": computerscience_template
            }
        ]

        chain = Utils.create_router_chain(self.llm, prompt_infos)

        result = chain.run("什么是数学")

        print(result)

    def get_summarize_text(self):

        result = Utils.summarize_text(self.llm,'LLM.md',chunk_size=500)

        print(result)

    def get_answer_temporary(self):

        database = Utils.create_vector_database('database_test',chunk_size=500)

        result = Utils.QA_based_temporary_database(self.llm,'社会保障与社会风险的关系是什么',database)

        print(result)

    def get_answer_exist(self):

        # 先创建本地数据库
        # database = Utils.create_vector_database('database_test', chunk_size=500,
        #                                          persist_directory='database_test',persist=True)

        result = Utils.QA_based_exist_database(self.llm, '什么是peft技术', 'database_test')

        print(result)

    def get_search_Google(self):

        result = Utils.network_search(self.llm,'昨天发生了什么大事',verbose=True)

        print(result)

if __name__ == '__main__':

    # Example().get_format_output()

    # Example().get_conversation()

    Example().get_router_chain()

    # Example().get_answer_exist()
    #
    # Example().get_search_Google()

    print('hello world')
