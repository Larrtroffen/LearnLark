from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.database import Base
import datetime

class account(Base):
    __tablename__ = "account"

    uid = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mail = Column(String, index=True)
    passwd = Column(String)

class questions(Base):
    __tablename__ = "questions"

    qid = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    selections_A = Column(String)
    selections_B = Column(String)
    selections_C = Column(String)
    selections_D = Column(String)
    answer = Column(String)
    difficulty = Column(Integer)
    question_type = Column(String, ForeignKey("type.question_type"))

class record(Base):
    __tablename__ = "record"

    rid = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey("account.uid"))
    tid = Column(Integer, ForeignKey("questions.tid"))
    time = Column(DateTime, default=datetime.datetime.utcnow)
    number = Column(Integer)

class mission(Base):
    __tablename__ = "mission"

    mid = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey("account.uid"))
    day_total = Column(Integer)
    day_used = Column(Integer)
    mission_name = Column(String)
    mission_type = Column(String)

class test(Base):
    __tablename__ = "mission"

    tid = Column(Integer, primary_key=True, index=True)
    mid = Column(Integer, ForeignKey("mission.mid"))
    question_type = Column(String, ForeignKey("type.question_type"))
    test_time=Column(DateTime, default=datetime.datetime.utcnow)
    grade=Column(Integer)

class test(Base):
    __tablename__ = "mission"
    question_type = Column(String)


