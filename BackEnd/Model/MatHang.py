from pydantic import BaseModel
from typing import Union

class MatHang(BaseModel):
    id: int
    name: Union[str, None] = None
    unit: Union[str, None] = None
    price: Union[float, None] = None
    quantity: Union[int, None] = None

    def amount(self):
        return self.price * self.quantity

# Khi input cần để amount = price * quantity