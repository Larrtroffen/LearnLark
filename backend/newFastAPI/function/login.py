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
        "userEmail": "user2@example.com",
        "password": "password456"
    },
    "user3": {
        "userEmail": "user3@example.com",
        "password": "password789"
    },
    "user4": {
        "userEmail": "user4@example.com",
        "password": "password101"
    },
    "user5": {
        "userEmail": "user5@example.com",
        "password": "password202"
    }
}


@login.get("/login")
async def user_login(user: User):
    for user_info in users_info.values():
        if user_info["userEmail"] == user.userEmail and user_info["password"] == user.password:
            return True
    return False
