from pydantic import BaseModel, Field
from typing import Optional, Any, List, Dict

class RootSchema(BaseModel):
    message: str = Field(None, description="basic message")


class HealthSchema(BaseModel):
    status: str = Field(..., description="service status")


class MenuSchema(BaseModel):
    message: str = Field(None, description="basic message")
    nextcloud_url: str = Field(..., description="nextcloud url")
    music_url: str = Field(..., description="music url")