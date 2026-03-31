from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    type: str
    weight: float
    condition: int
    price: int

    class Config:
        from_attributes = True