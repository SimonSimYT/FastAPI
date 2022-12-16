from pydantic import BaseModel, Field
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(default=None, title="Title",)
    price: float = Field(default=None, gt=0,)
    tax: Union[float, None] = None