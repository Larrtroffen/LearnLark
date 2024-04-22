"""
主页面：只有一个对话框
①知识学习（反复答题的形式，类似背单词软件。答题分多次，第一次调用题库里的题，
根据对错，使用大模型生成或者推荐类似的更难/更简单的题，三次都答对后通过，记录到数据库中。）
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

from AI_designer import langchain_utils

class LearnLark(object):
    def __init__(self):
        pass

    def generate_question(self):
        pass

    def evaluate_result(self):
        pass

    def study_knowledge(self):
        pass

    def test_knwledge(self):
        pass

    def generate_schedule(self):
        pass

if __name__ == "__main__":
    print('hello')