from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/health", tags=["health"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/health", response_class=HTMLResponse)
async def health(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="health.html",
        context={"status": "200", "active": "health"},
    )