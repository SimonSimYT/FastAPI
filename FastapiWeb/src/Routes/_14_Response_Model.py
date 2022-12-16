
from email.policy import default
from urllib import response
from fastapi import FastAPI, Path
from Models._14_Response_Model import UserIn, UserOut

app = FastAPI()

# Using response model to determine output result
@app.post("/user/", response_model=UserOut) # use to determine the output data
async def create_user(user:UserIn):
    return user

# Using response model to exclude unchange parameters
users = {
    "user1": {"name": "user1","email": "email1"},
    "user2": {"name": "user2","email": "email2", "password":"password"},
    "user3": {"name": "user2","email": "email2", "password":"password","full_name":"fullname"}
}

# No Exclusion
@app.get("/user2/{user}", response_model=UserOut, response_model_exclude_unset=False)
async def read_user(user:str=Path(default=..., example="user1")):
    return users[user]

# With Exclusion
@app.get("/user3/{user}", response_model=UserOut, response_model_exclude_unset=True)
async def read_user(user:str=Path(default=..., example="user1")):
    return users[user]

# Using respones model include/exclude, take in set of str, only used if 1 pydantic model
# {"name"} equivalent to set(["name"])
@app.get("/user4/{user}", response_model=UserOut, response_model_include={"name"})
async def read_user(user:str = Path(default=..., example="user1")):
    return users[user]

@app.get("/user5/{user}", response_model=UserOut, response_model_exclude={"email"})
async def read_user(user:str = Path(default=..., example="user1")):
    return users[user]
