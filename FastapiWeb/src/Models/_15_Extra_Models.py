from turtle import st
from typing import Union
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    type = "UserOut"

class UserInDB(UserIn):
    type = "UserInDB"
    hashed_password: str
    