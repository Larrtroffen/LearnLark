from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from education import LearnLark

# 创建子路由对象
get_question = APIRouter()


# 定义题目数据模型
class Get_Qestion(BaseModel):
    userEmail: str
    is_correct: bool
    is_first: bool
    knowledge_point: str
    question : str

# 创建 LearnLark 实例
learn_lark = LearnLark()


# 获取测试题目端点
@get_question.post("/get_question")
async def get_question_items(user_question: Get_Qestion):

    if user_question.is_first:
        # 如果是第一题，调用 generate_first_question 函数
        result = learn_lark.generate_first_question(
            knowledge=user_question.knowledge_point
        )

    else:

        result = learn_lark.generate_next_question(
            question=user_question.question,
            knowledge_point=user_question.knowledge_point,
            is_correct=user_question.is_correct
        )

    return result

