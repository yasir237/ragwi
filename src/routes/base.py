from fastapi import APIRouter, Depends
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)



@base_router.get("/")
async def wellcome(settings: Settings = Depends(get_settings)):
    return {
        "signal": "OK",
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION
    }
