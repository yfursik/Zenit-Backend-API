from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Импортируем наши файлы: модели БД, базу и НОВЫЙ файл DTO
from app import models, database, dto

router = APIRouter(prefix="/inventory", tags=["Inventory"])


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. Получить всё (используем dto.Item вместо schemas.Item)
@router.get("/all", response_model=List[dto.Item])
async def get_all_loot(db: Session = Depends(get_db)):
    items = db.query(models.DBItem).all()
    return items


# 2. Добавить предмет
@router.post("/add")
async def add_item(item: dto.Item, db: Session = Depends(get_db)):
    new_item = models.DBItem(
        id=item.id,
        name=item.name,
        type=item.type,
        weight=item.weight,
        condition=item.condition,
        price=item.price
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return {"status": "success", "message": f"Item '{new_item.name}' saved to DB!"}


# 3. Эндпоинт: МГНОВЕННОЕ ЗАПОЛНЕНИЕ (SEED)
# Нажми эту кнопку один раз, и база наполнится вещами
@router.post("/seed")
async def seed_database(db: Session = Depends(get_db)):
    # Наш стартовый набор для игры (на английском!)
    starter_items = [
        {"id": 1, "name": "Rusty GPU", "type": "detail", "weight": 0.8, "condition": 15, "price": 45},
        {"id": 2, "name": "Blue Electrical Tape", "type": "tool", "weight": 0.1, "condition": 100, "price": 10},
        {"id": 3, "name": "Burnt Chip", "type": "trash", "weight": 0.01, "condition": 0, "price": 1},
        {"id": 4, "name": "Old Motherboard", "type": "detail", "weight": 1.2, "condition": 30, "price": 120},
        {"id": 5, "name": "Soviet Soldering Iron", "type": "tool", "weight": 0.5, "condition": 80, "price": 350},
        {"id": 6, "name": "Unknown Cable", "type": "trash", "weight": 0.2, "condition": 50, "price": 5},
    ]

    added_count = 0
    for item_data in starter_items:
        # Проверяем: если предмет с таким ID уже есть — пропускаем
        existing = db.query(models.DBItem).filter(models.DBItem.id == item_data["id"]).first()
        if not existing:
            # Создаем новый предмет из словаря (магия звездочек **)
            new_item = models.DBItem(**item_data)
            db.add(new_item)
            added_count += 1

    db.commit()
    return {"message": f"Успешно добавлено {added_count} новых предметов!"}
