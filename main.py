from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql import crud, models, schemas
from sql.database import SessionLocal, engine

# 根据定义的模型创建数据库表
models.Base.metadata.create_all(bind=engine)

# 初始化FastAPI应用
app = FastAPI()

# 获取数据库会话的依赖项
def get_db():
    db = SessionLocal()  # 创建一个新的数据库会话
    try:
        yield db  # 生成会话以在请求中使用
    finally:
        db.close()  # 确保请求完成后关闭会话

# 创建新用户的端点
@app.post("/accounts/", response_model=schemas.account)
def create_account(account: schemas.accountCreate, db: Session = Depends(get_db)):
    # 检查是否已存在具有给定电子邮件的用户
    db_account = crud.get_account_by_email(db, mail=account.mail)
    if db_account:
        # 如果用户存在，则抛出HTTP 400错误
        raise HTTPException(status_code=400, detail="Email already registered")
    # 创建并返回新用户
    return crud.create_account(db=db, account=account)

# 读取多个用户的端点
@app.get("/accounts/", response_model=list[schemas.account])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # 使用分页获取用户
    accounts = crud.get_accounts(db, skip=skip, limit=limit)
    return accounts  # 返回用户列表

# 根据ID读取单个用户的端点
@app.get("/accounts/{account_id}", response_model=schemas.account)
def read_account(account_id: int, db: Session = Depends(get_db)):
    # 根据ID获取用户
    db_account = crud.get_account(db, account_id=account_id)
    if db_account is None:
        # 如果用户未找到，则抛出HTTP 404错误
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account  # 返回用户

#创建新问题的端点
@app.post("/questions/", response_model=schemas.questions)
def create_question(question: schemas.questionsCreate, db: Session = Depends(get_db)):
    # 创建并返回新问题
    return crud.create_question(db=db, question=question)

# 根据题目类型读取多个问题的端点
@app.get("/questions/{question_type}", response_model=list[schemas.questions])
def read_questions_by_type(question_type: str, db: Session = Depends(get_db)):
    # 根据题目类型获取问题
    questions = crud.get_questions_by_type(db, question_type=question_type)
    if not questions:
        # 如果没有找到问题，则抛出HTTP 404错误
        raise HTTPException(status_code=404, detail="Questions not found")
    return questions  # 返回问题列表

# 根据题目难度读取多个问题的端点
@app.get("/questions/difficulty/{difficulty}", response_model=list[schemas.questions])
def read_questions_by_difficulty(difficulty: int, db: Session = Depends(get_db)):
    # 根据题目难度获取问题
    questions = crud.get_questions_by_difficulty(db, question_difficulty=difficulty)
    if not questions:
        # 如果没有找到问题，则抛出HTTP 404错误
        raise HTTPException(status_code=404, detail="Questions not found")
    return questions  # 返回问题列表

# 根据题目ID读取单个问题的端点
@app.get("/questions/{question_id}", response_model=schemas.account)
def read_questions(question_id: int, db: Session = Depends(get_db)):
    # 根据ID获取用户
    db_question = crud.get_question(db, question_id=question_id)
    if db_question is None:
        # 如果用户未找到，则抛出HTTP 404错误
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question  # 返回用户

# 创建新任务的端点
@app.post("/accounts/{account_id}/missions", response_model=schemas.mission)
def create_mission(mission: schemas.missionCreate, account_id: int, db: Session = Depends(get_db)):
    # 创建并返回新任务
    return crud.create_mission(db=db, mission=mission, account_id=account_id)

# 根据mid读取单个任务的端点
@app.get("/missions/{mid}", response_model=schemas.mission)
def read_mission(mid: int, db: Session = Depends(get_db)):
    # 根据ID获取任务
    db_mission = crud.get_mission_by_mid(db, mid=mid)
    if db_mission is None:
        # 如果任务未找到，则抛出HTTP 404错误
        raise HTTPException(status_code=404, detail="Mission not found")
    return db_mission  # 返回任务

# 根据UID读取用户的全部任务的端点
@app.get("/missions/user/{uid}", response_model=list[schemas.mission])
def read_missions_by_user(uid: int, db: Session = Depends(get_db)):
    # 根据UID获取用户的任务
    missions = crud.get_mission_by_uid(db, uid=uid)
    if not missions:
        # 如果任务未找到，则抛出HTTP 404错误
        raise HTTPException(status_code=404, detail="Missions not found")
    return missions  # 返回任务列表


# 根据任务名称读取全部任务的端点
@app.get("/missions/name/{mission_name}", response_model=list[schemas.mission])
def read_missions_by_name(mission_name: str, db: Session = Depends(get_db)):
    # 根据任务名称获取任务
    missions = crud.get_mission_by_name(db, mission_name=mission_name)
    if not missions:
        # 如果任务未找到，则抛出HTTP 404错误
        raise HTTPException(status_code=404, detail="Missions not found")
    return missions  # 返回任务列表
