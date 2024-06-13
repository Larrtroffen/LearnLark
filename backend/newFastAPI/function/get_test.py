# imports
from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from education import LearnLark

# 创建子路由对象
get_test = APIRouter()

# 定义题目数据模型
class TestItem(BaseModel):
    content: str
    number: int
    correct_answer: str
    selections_A: str
    selections_B: str
    selections_C: str
    selections_D: str

# 创建LearnLark实例
learn_lark = LearnLark()

# 获取测试题目端点
@get_test.get("/get_test", response_model=List[TestItem])
async def get_test_items():
    user_situation = {'三角函数': [6, 10]}

    try:
        generated_questions = learn_lark.test_knowledge(user_situation)
        test_data = []
        for i, q in enumerate(generated_questions):
            question = q['question'].strip()
            answer = q['answer'].split(": ")[1]
            options = question.split("\n")[1:5]
            
            test_item = TestItem(
                content=question.split("\n")[0],
                number=i + 1,
                correct_answer=answer,
                selections_A=options[0].split(". ")[1],
                selections_B=options[1].split(". ")[1],
                selections_C=options[2].split(". ")[1],
                selections_D=options[3].split(". ")[1],
            )
            test_data.append(test_item)
        
        return test_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))