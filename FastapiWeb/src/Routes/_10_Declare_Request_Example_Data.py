from fastapi import FastAPI, Body
from Models._10_Declare_Request_Example_Data import Item, Item2, Item3

app = FastAPI()

# Using Item which use Config and schema_extra to declare examples
@app.put("/items/{item_id}")
async def update_item(item_id: int, item:Item):
    result = {"item_id": item_id, "item": item}
    return result

# No examples declare
@app.put("/items2/{item_id}")
async def update_item(item_id: int, item:Item2):
    result = {"item_id": item_id, "item": item}
    return result

# Using Item 3 which use fields to declare example
@app.put("/items3/{item_id}")
async def update_item(item_id: int, item:Item3):
    result = {"item_id": item_id, "item": item}
    return result

# Using Body to declare an example
@app.put("/items4/{item_id}")
async def update_item(
    item_id: int,
    item:Item2 = Body(
        default=...,
        example={
            "name":"Foo",
            "description":"A very nice item",
            "price":35.2,
            "tax":3.2
        }
    ),
):
    result = {"item_id":item_id, "item":item}
    return result

# Using Body to declare multiple example
@app.put("/items5/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        default=...,
        examples={ # examples is used
            "normal": {
                "summary": "A normal example", # drop down name of example
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data", # drop down name of example
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error", # drop down name of example
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results