from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel

# 创建子路由对象
profile_change = APIRouter()

# 用户数据存储字典
users_db = {
    "1234567@qq.com": {"A": "User A"},
    "1234567@163.com": {"B": "User B"},
    "123456789@gmail.com": {"C": "User C"},
    "1234567@126.com": {"D": "User D"},
}


# 定义响应模型
class StatusResponse(BaseModel):
    status: str

# 更新用户信息端点
@profile_change.put("/change_user_info", response_model=StatusResponse)
async def change_user_info(userEmail: str = Query(None), newEmail: str = Query(None), name: str = Query(None)):
    #email/name不存在
    if userEmail is None or name is None:
        raise HTTPException(status_code=400, detail="userEmail and name must be provided")

    if userEmail not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    # 检查新邮箱是否已存在于用户字典中
    if newEmail != userEmail and newEmail in users_db:
        raise HTTPException(status_code=409, detail="New email already exists")

    # 更新用户信息
    users_db[userEmail]["name"] = name
    if newEmail != userEmail:
        users_db[newEmail] = users_db.pop(userEmail)

    return {"status": "success"}
