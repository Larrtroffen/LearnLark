from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Optional

# 创建子路由对象
save_test_router = APIRouter()

# 定义请求体模型
class SaveTestRequest(BaseModel):
    userEmail: str
    grade: int

# 定义响应模型
class TestStatusResponse(BaseModel):
    status: str
    grade: Optional[int] = None

# 保存测试成绩端点
@save_test_router.post("/save_test", response_model=TestStatusResponse)
async def save_test_handler(request: SaveTestRequest = Body(...)):
    return TestStatusResponse(status="Test saved successfully", grade=request.grade)