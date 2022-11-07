from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    id: int
    name: Union[str, None] = None
    price: Union[float, None] = None
    is_offer: Union[bool, None] = None
