from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
import os
from .database import insert_json, get_json

# 初始化 FastAPI
app = FastAPI()


# 密码哈希配置
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT 配置
SECRET_KEY = "your-super-secret-key-change-in-production"  # 请更换！
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 模拟用户数据库
fake_users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": pwd_context.hash("secret"),
        "role": "user"
    }
}

# 自定义中间件：JWT 鉴权
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path in ["/login"]:
        return await call_next(request)

    # 获取 Authorization 头
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="缺少或无效的 Token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = auth_header.split(" ")[1]  # 提取 token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="无效的 Token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        # 将用户信息附加到 request 对象
        request.state.user = payload
    except JWTError:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token 解码失败",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 继续处理请求
    response = await call_next(request)
    return response


# 生成 JWT Token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# 登录接口
@app.post("/login")
async def login(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not pwd_context.verify(password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(
        data={"sub": username, "role": user["role"]}
    )
    return {"access_token": token, "token_type": "bearer"}


# 受保护的路由示例, 所有非/login 路由都需要鉴权

@app.get("/task_list/{user_id}")
async def get_user_task_list(user_id):
    return get_json(user_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
