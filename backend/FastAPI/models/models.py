from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.database import Base
import datetime

class account(Base):
    __tablename__ = "account" # 用户账户数据表

    uid = Column(Integer, primary_key=True, index=True) # 用户名索引id
    name = Column(String, index=True) # 用户名
    mail = Column(String, index=True) # 注册邮箱
    passwd = Column(String) # 密码

class questions(Base):
    __tablename__ = "questions" # 题目数据表

    qid = Column(Integer, primary_key=True, index=True) # 题目索引id
    content = Column(String) # 题目内容
    selections_A = Column(String) # 选项A
    selections_B = Column(String) # 选项B
    selections_C = Column(String) # 选项C
    selections_D = Column(String) # 选项D
    answer = Column(String) # 正确答案
    difficulty = Column(Integer) # 题目难度
    tyid = Column(Integer, ForeignKey("type.tyid")) # 题目类型

class record(Base):
    __tablename__ = "record" # 学习记录数据表

    rid = Column(Integer, primary_key=True, index=True) # 学习记录索引id
    mid = Column(Integer, ForeignKey("mission.mid")) # 任务索引id（外键）
    qid = Column(Integer, ForeignKey("questions.qid")) # 题目索引id（外键）
    time = Column(DateTime, default=datetime.datetime.utcnow) # 学习完成时间
    number = Column(Integer) 
    # 答题次数，由于题目设置为连续答对三次后通过，
    # 该项记录该次学习的总答题次数，三次为最佳，数值越高正确率越低。

class mission(Base):
    __tablename__ = "mission" # 学习任务数据表

    mid = Column(Integer, primary_key=True, index=True) # 学习任务索引id
    uid = Column(Integer, ForeignKey("account.uid")) # 用户索引id（外键）
    day_total = Column(Integer) # 学习任务总天数
    day_used = Column(Integer) # 学习任务已用天数
    mission_name = Column(String) # 学习任务名称
    tyid = Column(Integer, ForeignKey("type.tyid")) # 题目类型（外键）

class test(Base):
    __tablename__ = "test"

    tid = Column(Integer, primary_key=True, index=True) # 测试索引id
    mid = Column(Integer, ForeignKey("mission.mid")) # 任务索引id（外键）
    question_type = Column(String, ForeignKey("type.question_type")) # 题目类型（外键）
    test_time=Column(DateTime, default=datetime.datetime.utcnow) # 测试完成时间
    grade=Column(Integer) # 测试成绩

class type(Base):
    __tablename__ = "type"
    tyid = Column(Integer, primary_key=True, index=True) # 题目类型索引id
    question_type = Column(String) # 题目类型


