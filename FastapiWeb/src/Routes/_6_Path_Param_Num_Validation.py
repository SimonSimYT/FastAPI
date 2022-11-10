from typing import Union
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(default=..., title="Id of the item"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    result = {"item_id":item_id}
    if q:
        result.update({"q":q})
    return result

# tricks to order parameter as needed, * following param are kwargs
@app.get("/item1/{item_id}")
async def read_items(*, item_id: int=Path(default=..., title="Id of the item"), q:str):
    result = {"item_id":item_id}
    if q:
        result.update({"q":q})
    return result

# number validations
@app.get("/item2/{item_id}")
async def read_items(
    *, item_id: int = Path(default=..., title="Id of the item", ge=1), q:str
):
    result = {"item_id":item_id}
    if q:
        result.update({"q":q})
    return result