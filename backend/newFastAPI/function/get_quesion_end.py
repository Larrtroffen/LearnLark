from fastapi import  APIRouter
from pydantic import BaseModel

get_quesion_end = APIRouter()

class Question_end(BaseModel):
    userEmail: str
    number: int


@get_quesion_end.post("/get_quesion_end")
async def get_quesion_result(end: Question_end):

    return True
