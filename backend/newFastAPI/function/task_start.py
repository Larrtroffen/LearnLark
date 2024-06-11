from fastapi import  APIRouter
from pydantic import BaseModel

task_start = APIRouter()

class Task(BaseModel):
    days: str
    startDate: str
    taskName: str
    question_type: str
    userEmail: str


@task_start.post("/mission_save")
async def mission_save(task: Task):

    return True
