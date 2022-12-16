from typing import Union, List, Set
from pydantic import BaseModel, HttpUrl

class Image(BaseModel):
    url: HttpUrl # Special data type HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    list_tags: List[str] = [] # list type
    set_tags: Set[str] = set() # set type
    submodel_tags_image: Union[Image, None] = None # Submodel
    images: Union[List[Image], None] = None # List and Submodel

class Offer(BaseModel):
    name: str
    items: List[Item]
