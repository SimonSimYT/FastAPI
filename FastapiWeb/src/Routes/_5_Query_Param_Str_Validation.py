from typing import Union, List
from pydantic import Required
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
        return result

# Additional validation for query parameter
@app.get("/items1/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=5)):
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
    return result

# Regular expression validation
@app.get("/items2/")
async def read_items(q: Union[str, None] = Query(default=None, regex="^fixedquery$")):
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
    return result

# Require field validation using Eclispe ..., Required
@app.get("/items3/")
async def read_items(q:str, q1:str=..., q2:str=Required):
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    result.update({"q":q},{"q1":q1},{"q2":q2})
    return result

# Multiple value for query parameter
@app.get("/items4/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_item = {"q":q}
    return query_item

# Adding Metadata
@app.get("/items5/")
async def read_items(q: Union[str, None] = Query(
    default=None, 
    title="Query str",
    description="short description",
    alias="item-query",
    deprecated=True)):
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
    return result

# Exclude from openAPI schema and thus auto documentation
@app.get("/item6/")
async def read_item(q: Union[str, None] = Query(
    default=None, include_in_schema=False)):
    if q:
        return {"q":q}
    else:
        return {"q":"Not found"}