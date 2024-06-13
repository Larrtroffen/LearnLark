from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel

# 创建子路由对象
get_profile = APIRouter()

# 用户数据存储字典
users_db = {
    "1": {
        "record": {
            "complete": ["task1", "task2"],
            "incomplete": ["task3"]
        },
        "name": "A"
    },
    "1234567@163.com": {
        "record": {
            "complete": ["task4"],
            "incomplete": ["task5", "task6"]
        },
        "name": "B"
    },
    "1234567@gmail.com": {
        "record": {
            "complete": ["task7"],
            "incomplete": ["task8"]
        },
        "name": "C"
    },
    "1234567@126.com": {
        "record": {
            "complete": ["task9"],
            "incomplete": ["task10", "task11"]
        },
        "name": "D"
    }
}

# 定义响应模型
class Record(BaseModel):
    complete: list[str]
    incomplete: list[str]

class UserInfoResponse(BaseModel):
    record: Record
    name: str

# 获取用户信息端点
@get_profile.get("/get_profile", response_model=UserInfoResponse)
async def get_user_info(userEmail: str = Query(...)):
    if userEmail not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    user_info = users_db[userEmail]
    return user_info


