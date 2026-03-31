# Файл: app/schemas.py
from pydantic import BaseModel


# Это схема для обмена данными (JSON)
class Item(BaseModel):
    id: int
    name: str
    type: str
    weight: float
    condition: int
    price: int

    # Эта магическая настройка нужна, чтобы Pydantic дружил с Базой Данных
    class Config:
        from_attributes = True