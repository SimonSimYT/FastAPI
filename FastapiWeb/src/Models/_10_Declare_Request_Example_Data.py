from typing import Union
from pydantic import BaseModel, Field

# Adding example into the Schema
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    # Using Config and schema_extra to declare an example, schema will contain
    # example information
    class Config:
        schema_extra={
            "example":{
                "name":"Foo",
                "description":"A very nice item",
                "price": 35.4,
                "tax":3.2,
            }
        }

class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

# Adding example using the Field object
class Item3(BaseModel):
    name: str = Field(example="Foo")
    description: Union[str, None] = Field(default=None, example="A very nice item")
    price: float = Field(example=35.4)
    tax: Union[float, None] = Field(example=3.2)


