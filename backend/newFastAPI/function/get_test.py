from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# 创建子路由对象
get_test = APIRouter()

# 定义题目数据模型
class TestItem(BaseModel):
    content: str
    number: str
    correct_answer: str
    selections_A: str
    selections_B: str
    selections_C: str
    selections_D: str


# 获取测试题目端点
@get_test.get("/get_test", response_model=List[TestItem])
async def get_test_items(userEmail: Optional[str] = Query(None, description="User's email address")):
    # 检查是否提供了 userEmail 参数
    if userEmail is None:
        raise HTTPException(status_code=400, detail="userEmail must be provided")

    # 生成十道题目
    test_data = []
    for i in range(1, 11):
        test_data.append({
            "content": f"Question {i}: This is the content of question {i}",
            "number": str(i),
            "correct_answer": f"Answer {i}",
            "selections_A": f"Option A for question {i}",
            "selections_B": f"Option B for question {i}",
            "selections_C": f"Option C for question {i}",
            "selections_D": f"Option D for question {i}"
        })

    return test_data
