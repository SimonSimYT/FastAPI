from typing import Union, List
from pydantic import BaseModel

class UserIn(BaseModel):
    name: str
    password: Union[str, None] = None
    email: str
    full_name: Union[str, None] = None

class UserOut(BaseModel):
    name:str
    email: str
    full_name: Union[str, None] = None

