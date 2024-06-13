from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from education import LearnLark

# 创建子路由对象
get_question = APIRouter()

# 定义题目数据模型
class Get_Qestion(BaseModel):
    userEmail: str
    is_correct: bool
    is_first: bool
    knowledge_point: str
    question: Optional[str] = None

# 创建 LearnLark 实例
learn_lark = LearnLark()

# 获取测试题目端点
@get_question.post("/get_question")
async def get_question_items(user_question: Get_Qestion):

    if user_question.is_first:
        result = learn_lark.generate_first_question(
            knowledge=user_question.knowledge_point
        )
    else:
        result = learn_lark.generate_next_question(
            question=user_question.question,
            knowledge_point=user_question.knowledge_point,
            is_correct=user_question.is_correct
        )

    # 解析LLM返回的结果，并将其转换为前端需要的结构化格式
    structured_response = {
        "content": result['question'],
        "selections_A": result['answer'].split('\n')[0],
        "selections_B": result['answer'].split('\n')[1],
        "selections_C": result['answer'].split('\n')[2],
        "selections_D": result['answer'].split('\n')[3],
        "correct_answer": result['answer'].split('\n')[4].split(': ')[1]  # 假设答案格式如 "答案: A"
    }

    return structured_response