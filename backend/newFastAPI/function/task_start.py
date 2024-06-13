from fastapi import  APIRouter
from pydantic import BaseModel

task_start = APIRouter()

class Task(BaseModel):
    days: int
    questionType: str
    startDate: str
    taskName: str
    userEmail: str


@task_start.post("/mission_save")
async def mission_save(task: Task):
    return {"success": True, "message": "设置成功"}  
