from fastapi import FastAPI

from app.schemas import RootSchema
from app.routers import health, menu

app = FastAPI()

app.include_router(menu.router)
app.include_router(health.router)

@app.get("/", response_model=RootSchema)
async def root():
    return RootSchema(
        message="hello. go to /menu"
    )