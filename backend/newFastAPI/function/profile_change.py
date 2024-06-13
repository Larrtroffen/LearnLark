from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# 创建子路由对象
profile_change = APIRouter()

# 用户数据存储字典
users_db = {
    "1": {"name": "User A"},
    "1234567@163.com": {"name": "User B"},
    "123456789@gmail.com": {"name": "User C"},
    "1234567@126.com": {"name": "User D"},
}

# 定义测试请求模型
class ChangeUserInfoRequest(BaseModel):
    userEmail: str
    newEmail: str = None
    name: str

# 定义响应模型
class StatusResponse(BaseModel):
    status: str

# 更新用户信息端点
@profile_change.post("/profile_change", response_model=StatusResponse)
async def change_user_info(request: ChangeUserInfoRequest):

    userEmail = request.userEmail
    newEmail = request.newEmail
    name = request.name

    # 检查email/name是否存在
    if userEmail is None or name is None:
        raise HTTPException(status_code=400, detail="userEmail and name must be provided")
    
    if userEmail not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    # 检查新邮箱是否已存在于用户字典中
    if newEmail and newEmail != userEmail and newEmail in users_db:
        raise HTTPException(status_code=409, detail="New email already exists")

    # 更新用户信息
    users_db[userEmail]["name"] = name
    if newEmail and newEmail != userEmail:
        users_db[newEmail] = users_db.pop(userEmail)

    return {"status": "success"}