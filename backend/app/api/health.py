from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "AI Enterprise Backend",
        "version": "1.0.0"
    }