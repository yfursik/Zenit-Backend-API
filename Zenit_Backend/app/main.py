from fastapi import FastAPI
from app.routers import inventory, bunker
from app.database import engine
from app import models # Импортируем наши новые таблицы

# --- МАГИЯ: Создаем файл базы данных, если его нет ---
models.Base.metadata.create_all(bind=engine)
# -----------------------------------------------------

app = FastAPI(
    title="Project: ZENIT API",
    description="Control System",
    version="0.1.0"
)

app.include_router(inventory.router)
app.include_router(bunker.router)

@app.get("/")
async def root():
    return {"system": "ONLINE", "db_status": "Connected"}

