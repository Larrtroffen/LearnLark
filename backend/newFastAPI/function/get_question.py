from fastapi import APIRouter, HTTPException
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

def parse_result(result: dict) -> dict:
    question = result.get('question', '')
    answer = result.get('answer', '')

    lines = question.split('\n')
    if len(lines) < 5:
        raise HTTPException(status_code=500, detail="Question data is not correctly formatted")

    content = lines[0]
    selections = lines[1:5]
    
    # Assuming answer is just one character like 'C' or 'D'
    correct_answer = answer

    if len(selections) < 4:
        raise HTTPException(status_code=500, detail="Selections data is not correctly formatted")

    structured_response = {
        "content": content,
        "selections_A": selections[0][3:],  # Remove the 'A. ' prefix
        "selections_B": selections[1][3:],  # Remove the 'B. ' prefix
        "selections_C": selections[2][3:],  # Remove the 'C. ' prefix
        "selections_D": selections[3][3:],  # Remove the 'D. ' prefix
        "correct_answer": correct_answer
    }

    return structured_response

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

    return parse_result(result)