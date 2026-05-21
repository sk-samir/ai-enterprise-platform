from fastapi import APIRouter
from app.utils.logger import logger

router = APIRouter()

@router.post("/dashboard")
def dashboard():
    logger.info("Dashboard request received")

    return {
        "metrics": {
            "users": 1200,
            "transactions": 4500,
            "revenue": 98000
        },
        "status": "mock-data"
    }