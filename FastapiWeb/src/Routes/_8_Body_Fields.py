from fastapi import Body, FastAPI
from Models._8_Body_Fields import Item

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id:int, item:Item=Body(default=None, embed=True)):
    result = {"item_id": item_id, "item": item}
    return result