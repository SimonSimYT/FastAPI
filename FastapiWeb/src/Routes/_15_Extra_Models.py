from fastapi import FastAPI, Query
from Models._15_Extra_Models import UserIn, UserOut, UserInDB
from Dependencies._15_Extra_Models import fake_save_user
from typing import Union, List, Dict

app = FastAPI()

# Using more than 2 models
@app.post("/user/", response_model=UserInDB)
async def create_user(user_in:UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# Response model of 2 type
user_saved = {
    "UserOut": {"username":"User","email":"email", "full_name":"fullname", "type":"UserOut"},
    "UserInDB" : {
        "username":"User1",
        "email":"email1", 
        "full_name":"fullname1", 
        "password":"password", 
        "type":"UserInDB", 
        "hashed_password":"hashed_password"},
}

@app.get("/user1/", response_model=Union[UserInDB, UserOut])
async def read_user(users: str = Query(default=..., example="UserOut")):
    return user_saved[users]

# Response model of list
user_saved = [
    {"username":"User","email":"email", "full_name":"fullname","password":"password","type":"UserOut"},
    {"username":"User1","email":"email1", "full_name":"fullname1","password":"password1","type":"UserOut"}
]
@app.get("/user2", response_model=List[UserOut])
async def read_user():
    return user_saved

# Response model with arbitrary dict
@app.get("/user3/", response_model=Dict[str, float])
async def read_user():
    return {"user1":1.0, "user2":2.0}