#Pydantic模型文件
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class accountBase(BaseModel):
    mail:str
    name:str

class accountCreate(accountBase):
    password:str
class account(accountBase):
    uid:int
    is_active: bool
    class Config:
        from_attributes = True

class questionsBase(BaseModel):
    difficulty:int
    question_type: str
    content: str
    selections_A: str
    selections_B: str
    selections_C: str
    selections_D: str
    answer: str
class questionsCreate(questionsBase):
    pass
class questions(questionsBase):
    qid: int
    class Config:
        from_attributes = True

class recordBase(BaseModel):
    mid: int
    qid: int
    time: Optional[datetime] = None
    number: int

class recordCreate(recordBase):
    pass

class record(recordBase):
    rid:int
    class Config:
        from_attributes = True

class missionBase(BaseModel):
    uid: int
    day_total: int
    day_used: int
    mission_name: str
    question_type: str
class missionCreate(missionBase):
    pass

class mission(missionBase):
    mid:int
    class Config:
        from_attributes = True
class testBase(BaseModel):
    mid: int
    question_type: str
    test_time: datetime
    grade: int
class testCreate(testBase):
    pass

class test(testBase):
    tid: int
    class Config:
        from_attributes = True

class typeBase(BaseModel):
    question_type: str
class typeCreate(typeBase):
    pass

class type(typeBase):
    tyid:int
    class Config:
        from_attributes = True

