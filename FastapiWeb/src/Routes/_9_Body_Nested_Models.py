from fastapi import FastAPI
from Models._9_Body_Nested_Models import Item, Offer, Image
from typing import List, Dict

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item:Item):
    result = {"item_id": item_id, "item": item}
    return result

# deeply nested, refer to models._9_Body_Nested_Models.py
@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# Bodies of pure lists
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images

# Bodies of arbitrary dicts, to take not that json only support str as keys
# pydantic will convert and validate them
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights