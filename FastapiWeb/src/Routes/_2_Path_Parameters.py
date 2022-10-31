from Resources._2_Path_Parameters import ModelName
from fastapi import FastAPI

app = FastAPI()


# this will return a item_id that is of string type
@app.get("/items/order_1")
async def read_items(item_id):
    return {"item_id":item_id}


# this will return a item_id that is of int type
@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id":item_id}


# this will be ignore as path will be thinking that order_2 is a parameter
# and still require item_id to be an int, test it on swagger
@app.get("/items/order_2")
async def read_items(item_id: str):
    return {"item_id":item_id}


# Using Predefined Values
@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name1": model_name}

    if model_name.value == "lenet":
        return {"model_name2": model_name}

    return {"model_name3": model_name}