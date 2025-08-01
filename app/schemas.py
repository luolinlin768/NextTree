from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ProcessBase(BaseModel):
    title: str
    description: Optional[str] = None

class ProcessCreate(ProcessBase):
    parent_id: Optional[int] = None

class Process(ProcessBase):
    id: int
    completed: bool
    parent_id: Optional[int]
    owner_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class ProcessTree(Process):
    children: List['ProcessTree'] = []
    
    class Config:
        orm_mode = True

ProcessTree.update_forward_refs()

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None