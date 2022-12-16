from email.policy import default
from fastapi import FastAPI, Header
from typing import Union, List

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}

# Duplicated Header
@app.get("/items1/")
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    return {"X-Token values": x_token}