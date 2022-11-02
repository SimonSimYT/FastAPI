from fastapi import FastAPI
from Models._4_Request_Body import Item

app = FastAPI()


@app.post("/items/")
async def create_items(item:Item):
    return item


# Using path and model at the same time
@app.put("/items/{item_id}")
async def create_item(item_id:int, item:Item):
    return {"item_id":item_id, **item.dict()}