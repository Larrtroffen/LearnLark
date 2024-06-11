# main.py-->路由分发
# 1. 引入FastAPI
# 2. 引入include_router
# 3. 引入路由分发
import uvicorn
from fastapi import FastAPI
from function.login import login
from function.get_type import get_type
from function.task_start import task_start
from function.get_question import get_question
from function.get_quesion_end import get_quesion_end
from function.get_profile import get_profile
from function.get_test import get_test
from function.profile_change import profile_change
from function.save_test import save_test_router


app = FastAPI()

# 包含用户路由
app.include_router(login, prefix="/api", tags=["LearnLark登录"])
app.include_router(get_type, prefix="/api", tags=["LearnLark题目类型获取"])
app.include_router(task_start, prefix="/api", tags=["LearnLark任务创建"])
app.include_router(get_question, prefix="/api", tags=["LearnLark题目获取"])
app.include_router(get_quesion_end, prefix="/api", tags=["LearnLark日常学习上传结果"])
app.include_router(get_profile, prefix="/api", tags=["LearnLark用户信息获取"])
app.include_router(get_test, prefix="/api", tags=["LearnLark测试"])
app.include_router(profile_change, prefix="/api", tags=["LearnLark用户信息修改"])
app.include_router(save_test_router, prefix="/api", tags=["LearnLark测试结果保存"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)