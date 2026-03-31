# Файл: app/models.py
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class DBItem(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    weight = Column(Float)
    condition = Column(Integer)
    price = Column(Integer)