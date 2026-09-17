import shutil
from pathlib import Path

from fastapi import APIRouter, Request, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/music", tags=["music"])
templates = Jinja2Templates(directory="app/templates")

UPLOAD_DIR = Path("uploads/music")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXT = {".mp3", ".wav", ".ogg", ".m4a", ".flac"}


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def music_page(request: Request):
    files = sorted(
        [f.name for f in UPLOAD_DIR.iterdir() if f.is_file()],
        key=str.lower,
    )
    return templates.TemplateResponse(
        request=request,
        name="music.html",
        context={
            "message": "Music library",
            "files": files,
            "active": "music",
        },
    )


@router.post("/upload")
async def upload_music(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXT:
        raise HTTPException(
            status_code=400,
            detail=f"Недопустимый формат. Разрешено: {', '.join(sorted(ALLOWED_EXT))}",
        )

    safe_name = Path(file.filename).name
    dest = UPLOAD_DIR / safe_name

    with dest.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"ok": True, "filename": safe_name}


@router.get("/stream/{filename}")
async def stream_music(filename: str):
    safe_name = Path(filename).name
    path = UPLOAD_DIR / safe_name
    if not path.exists() or not path.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path)


@router.post("/delete/{filename}")
async def delete_music(filename: str):
    safe_name = Path(filename).name
    path = UPLOAD_DIR / safe_name
    if not path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    path.unlink()
    return {"ok": True}