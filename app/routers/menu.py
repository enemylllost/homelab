from fastapi import APIRouter

from config.config import NEXTCLOUD_URL, MUSIC_URL
from app.schemas import MenuSchema

router = APIRouter(prefix="/menu", tags=["menu"])

@router.get("", response_model=MenuSchema)
async def menu():
    return MenuSchema(
        message="All urls on server",
        nextcloud_url=NEXTCLOUD_URL,
        music_url=MUSIC_URL
    )