from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/bunker", tags=["Bunker Systems"])

class BunkerState(BaseModel):
    oxygen: float
    temp: float
    power: bool
    alarm: bool

# Начальное состояние
state = BunkerState(oxygen=98.5, temp=12.0, power=True, alarm=False)

@router.get("/status")
async def get_status():
    return state

@router.post("/toggle_alarm")
async def toggle_alarm(active: bool):
    state.alarm = active
    return {"message": f"Сирена переключена: {active}"}

@router.post("/fix_power")
async def fix_power():
    state.power = True
    return {"message": "Питание восстановлено!"}