# 连接sqlite3数据库
def connect_db():
    return sqlite3.connect('database.db')
