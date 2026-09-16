from fastapi import APIRouter

from app.schemas import HealthSchema

router = APIRouter(prefix="/health", tags=["health"])

@router.get("", response_model=HealthSchema)
async def health():
    return HealthSchema(
        status="200"
    )