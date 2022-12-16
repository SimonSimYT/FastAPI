from fastapi import FastAPI, Form

app = FastAPI()

# OAuth2 required information to be send as form fields
@app.post("/login/")
async def login(username: str=Form(default=None), password: str=Form(default=None)):
    return {"username": username}