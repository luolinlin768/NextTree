import sqlite3
import json
import atexit

# 全局连接
_conn = sqlite3.connect('data.db')
_cursor = _conn.cursor()

# 创建表
_cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL
    )
''')
_conn.commit()

# 定义退出时要执行的函数
def _close_db():
    if _conn:
        _conn.close()
        print("✅ 数据库连接已自动关闭")

# 注册退出函数
atexit.register(_close_db)

# 插入 JSON 数据
def insert_json(user_id, data_dict):
    json_str = json.dumps(data_dict, ensure_ascii=False)
    _cursor.execute("INSERT OR REPLACE INTO items (id, data) VALUES (?, ?)", (user_id, json_str))
    _conn.commit()
    return user_id

# 按 id 读取 JSON 数据
def get_json(user_id):
    _cursor.execute("SELECT data FROM items WHERE id = ?", (user_id,))
    row = _cursor.fetchone()
    return json.loads(row[0]) if row else None