from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class Project(BaseModel):
    title: str
    class Config():
        orm_mode = True

class UpdateBase(BaseModel):
    title: str
    project_id: int
    class Config():
        orm_mode = True

class BulletBase(BaseModel):
    body: str
    update_id: int
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str


class BulletForUpdate(BaseModel):
    body:str
    class Config():
        orm_mode = True

class UpdateForBlog(BaseModel):
    title: str
    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True

class ShowProject(BaseModel):
    title: str
    updates: List[UpdateForBlog]
    class Config():
        orm_mode = True

class ShowUpdate(BaseModel):
    title: str
    project_id: int
    bullets: List[BulletForUpdate]
    class Config():
        orm_mode = True

class ShowBullet(BaseModel):
    body: str
    update_id: int
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
