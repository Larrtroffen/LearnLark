from fastapi import  APIRouter
from pydantic import BaseModel

login = APIRouter()

class User(BaseModel):
    userEmail: str
    password: str

# 模拟用户信息的字典
users_info = {
    "user1": {
        "userEmail": "1",
        "password": "1"
    },
    "user2": {
        "userEmail": "1234567@163.com",
        "password": "password456"
    },
    "user3": {
        "userEmail": "1234567@126.com",
        "password": "password789"
    },
    "user4": {
        "userEmail": "1234567@gmail.com",
        "password": "password101"
    },
    "user5": {
        "userEmail": "user5@example.com",
        "password": "password202"
    }
}


@login.post("/login")
async def user_login(user: User):
    for user_info in users_info.values():
        if user_info["userEmail"] == user.userEmail and user_info["password"] == user.password:
            return {"success": True, "message": "登录成功"}  
    return {"success": False, "message": "用户名或密码错误"}  
