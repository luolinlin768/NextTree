from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = "fakehashed" + user.password  # 实际应用中应该使用真正的哈希
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_process(db: Session, process_id: int, user_id: int):
    return db.query(models.Process).filter(
        models.Process.id == process_id,
        models.Process.owner_id == user_id
    ).first()

def get_processes(db: Session, user_id: int, parent_id: Optional[int] = None, skip: int = 0, limit: int = 100):
    query = db.query(models.Process).filter(models.Process.owner_id == user_id)
    if parent_id is None:
        query = query.filter(models.Process.parent_id.is_(None))
    else:
        query = query.filter(models.Process.parent_id == parent_id)
    return query.offset(skip).limit(limit).all()

def create_process(db: Session, process: schemas.ProcessCreate, user_id: int):
    db_process = models.Process(
        **process.dict(),
        owner_id=user_id,
        updated_at=datetime.utcnow()
    )
    db.add(db_process)
    db.commit()
    db.refresh(db_process)
    return db_process

def update_process(db: Session, process_id: int, process: schemas.ProcessCreate, user_id: int):
    db_process = get_process(db, process_id, user_id)
    if db_process:
        for key, value in process.dict().items():
            setattr(db_process, key, value)
        db_process.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_process)
    return db_process

def toggle_process_complete(db: Session, process_id: int, user_id: int):
    db_process = get_process(db, process_id, user_id)
    if db_process:
        db_process.completed = not db_process.completed
        db_process.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_process)
    return db_process

def delete_process(db: Session, process_id: int, user_id: int):
    db_process = get_process(db, process_id, user_id)
    if db_process:
        db.delete(db_process)
        db.commit()
    return db_process