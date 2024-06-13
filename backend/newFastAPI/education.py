"""
主页面：只有一个对话框
①知识学习（反复答题的形式，类似背单词软件。答题分多次，第一次调用题库里的题，
根据对错，使用大模型生成或者推荐类似的更难/更简单的题【看看能不能实现】，三次都答对后通过，记录到数据库中。）
②知识测试（一次性答题，表单。使用的题目可以是由模型根据用户答题情况推荐的题库中的题目。
答完后可以显示结果，并记录在数据库中。）
③任务制定（出几道问题或者让用户自己选，一天可以刷多少道题啊啥的，搞个日历，
根据模型或者艾宾浩斯这种理论做个简单的时间安排给用户看。）
④学习记录（个人界面，可以简单整理分析呈现，正确率等。）


具体实现：
chain
1.展示知识点
  调用题库生成题目————如果答错，生成解析————根据第一题的错误生成简单合适的题目
                ————如果答对，生成对应知识点类下的更难的问题————答对三次后该知识点通过————记录数据
2.调用数据库分析用户数据————根据数据筛选或生成对应题目————用户答题————展示结果
3.调用数据库分析用户数据————根据用户的请求制定任务（根据一些理论，比如艾宾浩斯）
4.学习记录————与我无关
"""
import sys
from os import path
# 这里相当于把相对路径 .. 添加到pythonpath中
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate

from ai_education.langchain_utils import Utils

class LearnLark(object):
    def __init__(self):
        self.llm = Utils.LLM

    def generate_first_question(
            self,
            knowledge:str
    ):
        """
        根据知识点生成第一题
        :param knowledge:知识点
        :return: 第一题 + 答案
        结构为{'question':  ,'answer':  , }
        """

        name = ["question", "answer"]
        description = ["题目和选项",
                       "题目的答案，简短直接"]
        out_parsers = Utils.create_out_parsers(name, description)

        input_variables = ['knowledge_point']

        instruction = """本次我学习的是以下知识点：{knowledge_point}，请为我生成一道与该知识点相关的题目，题目要求选择题，需要有4个选项。请你
                    用中文生成问题与答案。例如{{'第1题': '已知sinθ=3/5，求cosθ的值。\nA. 2/5\nB. 4/5\nC. 1/5\nD. 3/5\n答案: A'}}。请你一定要生成选项"""

        prompt = Utils.create_prompt(template_string=instruction,
                                     input_variables=input_variables,
                                     out_parser=out_parsers,
                                     is_output_format=True,
                                     knowledge_point=knowledge
                                     )

        output = self.llm(prompt)

        return out_parsers.parse(output)

    def generate_next_question(
            self,
            question:str,
            knowledge_point:str,
            is_correct:bool
    )->dict:
        """
        根据上述内容生成题目用于日常练习
        :param question:题目
        :param knowledge_point: 知识点
        :param is_correct: 题目回答情况
        :return: 更简单/难的题 + 答案
        结构为{'question':  ,'answer':  ,}
        """

        name = ["question", "answer"]
        description = ["题目和选项",
                       "题目的答案，简短直接"]
        out_parsers = Utils.create_out_parsers(name, description)

        input_variables = ['knowledge_point','question']

        instruction = "本次我学习的是以下知识点：{knowledge_point}，我已经答了这道题：{question}，"
        if is_correct:
            instruction = instruction + """并且答对了，请为我生成一道与该知识点相关，并且更难的题目，生成题目与答案。题目要求选择题，需要有4个选项。请你
                                用中文生成问题与答案。例如{{'第1题': '已知sinθ=3/5，求cosθ的值。\nA. 2/5\nB. 4/5\nC. 1/5\nD. 3/5\n答案: A'}}。请你一定要生成选项"""
        else:
            instruction = instruction + """并且答错了，请为我生成一道与该知识点相关，难度与原题目类似的题目，题目要求选择题，需要有4个选项。请你
                                用中文生成问题与答案。例如例如{{'第1题': '已知sinθ=3/5，求cosθ的值。\nA. 2/5\nB. 4/5\nC. 1/5\nD. 3/5\n答案: A'}}。请你一定要生成选项"""

        prompt = Utils.create_prompt(template_string=instruction,
                                     input_variables=input_variables,
                                     out_parser=out_parsers,
                                     is_output_format=True,
                                     question=question,
                                     knowledge_point=knowledge_point
                                     )

        output = self.llm(prompt)

        return out_parsers.parse(output)

    def test_knowledge(self, user_situation: dict) -> list:
        """
        根据用户数据库情况生成测试，会根据历史作答总数与正确率生成测试题，总共生成10道选择题
        :param user_situation: 用户的现有知识点答题情况，包含每个知识点回答的问题总数与回答的正确数
        结构为 {'knowledge_point':[correct_num,all_answer_num]......}
        :return: 生成的题目与答案
        结构为 [{'question':  ,'answer':  },{'question':  ,'answer':  }......]
        """
        while True:  # 重复执行直到成功执行
            try:
                # 获取正确率
                correct = {knowledge_point: info[0] / info[1]
                           for knowledge_point, info in user_situation.items()}

                name = [f"第{i + 1}题" for i in range(10)]
                descriptions = [f"第{i + 1}题的题目与答案" for i in range(10)]

                out_parsers = Utils.create_out_parsers(name, descriptions)

                template_string = """我想生成一套共有10道题的试卷，我将给你提供我的现有的作答情况，作答情况分为正确率与作答总数
                                其中，正确率的格式为{{知识点:正确率}}，正确率： {correct}；作答总数的格式为{{知识点:作答总数}}
                                作答总数：{total}
                                请你帮我生成该试卷，要求：正确率越低题目越简单，正确率越高题目越困难，作答比较少的题目在
                                试卷中体现的需要多一些，请你权衡好这两个指标，生成题目与答案。题目要求选择题，需要有4个选项。请你
                                用中文生成问题与答案。例如{{'第1题': '已知sinθ=3/5，求cosθ的值。\nA. 2/5\nB. 4/5\nC. 1/5\nD. 3/5\n答案: A'}}"""

                correct = [f"{knowledge_point}:{info}"
                           for knowledge_point, info in correct.items()]
                correct_str = ",".join(correct)
                correct_str = "{{{}}}".format(correct_str)

                total = [f"{knowledge_point}:{info[1]}"
                         for knowledge_point, info in user_situation.items()]
                total_str = ",".join(total)
                total_str = "{{{}}}".format(total_str)

                input_variables = ['correct', 'total']
                prompt = Utils.create_prompt(template_string, input_variables,
                                             True, out_parsers, correct=correct_str, total=total_str)

                output = out_parsers.parse(self.llm(prompt))
                print(output)
                output = [{'question': info[:info.index("答案")],
                           'answer': info.split("\n")[-1]} for _, info in output.items()]
                return output
            except Exception as e:
                print(f"Error occurred: {e}. Retrying...")


    def study_knowledge(
            self,
            knowledge_point: str
    )->str:
        """
        根据知识点生成学习内容
        :param knowledge_point: 知识点
        :return: 知识点对应的内容
        """

        input_variables = ['knowledge_point']

        instruction = """我正在学习知识点：{knowledge_point}，请为我生成知识点的相关信息，要求尽可能的详细，
                         能为初学者了解并深入掌握这个知识点提供很好的学习参考。"""

        prompt = Utils.create_prompt(template_string=instruction,
                                     input_variables=input_variables,
                                     knowledge_point=knowledge_point
                                     )

        output = self.llm(prompt)

        return output


    def generate_schedule(
            self,
            task:str,
            time:int,
    )->dict:
        """
        使用LLM帮助制定计划，制定的计划需要反馈到前端并显示
        显示：时间+要干的事情（具体）
        :param time: 完成这项任务的时间
        :param task: 需要制定的任务描述，越详细越好
        :return:制定的计划
        结构为{'第一天':  ,'第二天':  ,}
        """
        name = [f"第{i+1}天" for i in range(time)]
        name.append('总体做法')
        descriptions = ["需要尽量的详细" for i in range(time+1)]

        out_parsers = Utils.create_out_parsers(name, descriptions)

        template_string = """我想完成一项任务，这是该任务的具体描述，请帮我分析并制定计划：{task}，我需要在{time}天内完成
                  要求：给出具体的天数同时给出每天应该做些什么"""
        input_variables = ['task','time']

        prompt = Utils.create_prompt(template_string,input_variables,
                                     True,out_parsers,task=task,time=time)

        output = out_parsers.parse(self.llm(prompt))
        return output


if __name__ == "__main__":

    print(LearnLark().generate_next_question("已知双曲函数sinh(x) = (e^x - e^-x)/2，"
                                             "求cosh(x)的导函数","圆锥曲线",True))
    # print("--------------------------------------------------")
    print(LearnLark().generate_first_question("圆锥曲线"))
    # print("--------------------------------------------------")
    # print(LearnLark().study_knowledge("三角函数"))
    # print("--------------------------------------------------")
    # print(LearnLark().test_knowledge({"三角函数":[3,5],"圆锥曲线":[4,10]}))
    # print("--------------------------------------------------")
    # print(LearnLark().generate_schedule("我想背完3500词",40))