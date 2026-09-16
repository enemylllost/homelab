from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.config import NEXTCLOUD_URL, MUSIC_URL

router = APIRouter(prefix="/menu", tags=["menu"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="menu.html",
        context={
            "message": "All urls on server",
            "nextcloud_url": NEXTCLOUD_URL,
            "music_url": MUSIC_URL,
            "active": "menu",
        },
    )