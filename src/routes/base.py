from fastapi import APIRouter

base_router = APIRouter()

@base_router.get("/")
def wellcome():
    return {
        "signal": "Çalışıyorum"
    }