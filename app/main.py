from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud, auth
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境中应该更严格
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 认证路由
@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: auth.OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# 用户路由
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(auth.get_current_active_user)):
    return current_user

# 进程路由
@app.post("/processes/", response_model=schemas.Process)
def create_process(
    process: schemas.ProcessCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    return crud.create_process(db=db, process=process, user_id=current_user.id)

@app.get("/processes/", response_model=List[schemas.ProcessTree])
def read_processes(
    parent_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    # 获取进程树
    def get_process_tree(parent_id: Optional[int] = None):
        processes = crud.get_processes(db, parent_id=parent_id, user_id=current_user.id, skip=skip, limit=limit)
        for process in processes:
            process.children = get_process_tree(parent_id=process.id)
        return processes
    
    return get_process_tree(parent_id)

@app.get("/processes/{process_id}", response_model=schemas.ProcessTree)
def read_process(
    process_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    db_process = crud.get_process(db, process_id=process_id, user_id=current_user.id)
    if db_process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    
    # 递归获取子进程
    def get_process_with_children(process):
        process.children = crud.get_processes(db, parent_id=process.id, user_id=current_user.id)
        for child in process.children:
            get_process_with_children(child)
        return process
    
    return get_process_with_children(db_process)

@app.put("/processes/{process_id}", response_model=schemas.Process)
def update_process(
    process_id: int,
    process: schemas.ProcessCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    db_process = crud.get_process(db, process_id=process_id, user_id=current_user.id)
    if db_process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    return crud.update_process(db=db, process_id=process_id, process=process, user_id=current_user.id)

@app.post("/processes/{process_id}/toggle", response_model=schemas.Process)
def toggle_process_complete(
    process_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    db_process = crud.get_process(db, process_id=process_id, user_id=current_user.id)
    if db_process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    
    # 如果标记为完成，检查所有子进程是否已完成
    if not db_process.completed:
        children = crud.get_processes(db, parent_id=process_id, user_id=current_user.id)
        if any(not child.completed for child in children):
            raise HTTPException(
                status_code=400,
                detail="Cannot complete process with incomplete children"
            )
    
    return crud.toggle_process_complete(db=db, process_id=process_id, user_id=current_user.id)

@app.delete("/processes/{process_id}", response_model=schemas.Process)
def delete_process(
    process_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    db_process = crud.get_process(db, process_id=process_id, user_id=current_user.id)
    if db_process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    return crud.delete_process(db=db, process_id=process_id, user_id=current_user.id)