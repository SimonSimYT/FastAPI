from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name":"Foo"},
    {"item_name":"Bar"},
    {"item_name":"Baz"},
]

# function parameters that are not part of the path parameters are interpreted
# as query parameters
@app.get("/items/")
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip:skip + limit]


# Optional Parameters with default value, item_id = path param, q = query param
# bool type is auto converted localhost/items/foo?short=1|True|true|on|yes
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool=False):
    item = {"item_id":item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description":"include long description"})
    return item


# multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None]=None, short: bool=False
):
    item = {"item_id":item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description":"include long description"})
    return item