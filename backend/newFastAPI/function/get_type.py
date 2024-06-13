from fastapi import  APIRouter

get_type = APIRouter()

type_data = [
    {
        "name": "三角函数",
        "id": "1"
    },
    {
        "name": "英语",
        "id": "2"
    },
    {
        "name": "语文",
        "id": "3"
    }
]

@get_type.get("/question_type")
async def get_question_type():

    return type_data
