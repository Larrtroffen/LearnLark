import bcrypt
from sqlalchemy.orm import Session
from sql import models, schemas

# 根据用户ID获取用户的函数
def get_account(db:Session,account_id:int):
    return db.query(models.account).filter(models.account.uid==account_id).first()

# 根据用户邮箱获取用户的函数
def get_account_by_email(db: Session, mail: str):
    return db.query(models.account).filter(models.account.mail == mail).first()

# 获取用户列表的函数，带分页功能
def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    # 查询 User 表，获取用户列表，应用跳过和限制参数进行分页
    return db.query(models.account).offset(skip).limit(limit).all()

# 创建新用户的函数
def create_account(db: Session, account: schemas.accountCreate):
    # 使用 bcrypt 生成密码的哈希值
    password = bcrypt.hashpw(account.password.encode('utf-8'), bcrypt.gensalt())
    # 创建一个新的 User 对象，设置邮箱、哈希密码和昵称
    db_account = models.account(mail=account.mail, password=password.decode('utf-8'),name=account.name)
     # 将新的 User 对象添加到会话中
    db.add(db_account)
    # 提交会话，将新的 User 对象保存到数据库
    db.commit()
    # 刷新会话，更新 User 对象，获取数据库可能设置的变化（例如，设置ID）
    db.refresh(db_account)
    # 返回新创建的 User 对象
    return db_account

# 根据题目ID获取问题的函数
def get_question(db:Session,question_id:int):
    return db.query(models.questions).filter(models.questions.qid==question_id).first()

# 根据题目难度获取问题的函数
def get_questions_by_difficulty(db: Session, question_difficulty: int):
    return db.query(models.questions).filter(models.questions.difficulty == question_difficulty).all()

# 根据题目类型获取问题的函数
def get_questions_by_type(db: Session, question_type: str):
    return db.query(models.questions).filter(models.questions.question_type == question_type).all()

# 创建新问题的函数
def create_question(db: Session, question: schemas.questionsCreate):
    # 创建一个新的问题，设置题目、选项、答案、问题类型、问题难度
    db_question = models.questions(content=question.content,selections_A=question.selections_A,selections_B=question.selections_B,
                                 selections_C=question.selections_C,selections_D=question.selections_D,
                                 answer=question.answer,question_type=question.question_type,difficulty=question.difficulty,)
     # 将新的question对象添加到会话中
    db.add(db_question)
    # 提交会话，将新的question对象保存到数据库
    db.commit()
    # 刷新会话，更新 User 对象，获取数据库可能设置的变化
    db.refresh(db_question)
    # 返回新创建的question对象
    return db_question

# 根据mid获取用户的任务
def get_mission_by_mid(db: Session, mid: int):
    return db.query(models.mission).filter(models.mission.mid == mid).first()

# 根据uid获取用户的任务
def get_mission_by_uid(db: Session, uid: int):
    return db.query(models.mission).filter(models.mission.uid == uid).all()

# 根据name获取用户的任务
def get_mission_by_name(db: Session,mission_name: str):
    return db.query(models.mission).filter(models.mission.mission_name == mission_name).all()

# 创建用户新任务的函数

def create_mission(db: Session, mission: schemas.missionCreate, account_id: int):
    # 创建一个新的任务，设置学习任务名称、学习任务总天数和题目类型
    db_mission = models.mission(mission_name=mission.mission_name,day_used=mission.day_used,day_total=mission.day_total,question_type=mission.question_type,uid=account_id)
     # 将新的mission对象添加到会话中
    db.add(db_mission)
    # 提交会话，将新的mission对象保存到数据库
    db.commit()
    # 刷新会话，更新mission对象，获取数据库可能设置的变化
    db.refresh(db_mission)
    # 返回新创建的mission对象
    return db_mission

