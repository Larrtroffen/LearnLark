from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from typing import Optional

# 创建子路由对象
save_test_router = APIRouter()

# 定义响应模型
class TestStatusResponse(BaseModel):
    status: str

# 保存测试成绩端点
@save_test_router.post("/save_test", response_model=TestStatusResponse)
async def save_test_handler(
        userEmail: Optional[str] = Query(None, description="User's email address"),
        grade: Optional[str] = Query(None, description="Test grade in percentage")
):
    # 检查参数是否存在
    if userEmail is None and grade is None:
        raise HTTPException(status_code=400, detail="At least one of userEmail or grade must be provided")

    # 模拟保存操作，这里可以是数据库操作或其他存储操作
    if userEmail and grade:
        # 保存成功，返回状态
        return TestStatusResponse(status="Test saved successfully")
    elif userEmail:
        return TestStatusResponse(status="Email provided but no grade")
    elif grade:
        return TestStatusResponse(status="Grade provided but no email")
    else:
        return TestStatusResponse(status="No data provided")

