from fastapi import APIRouter
from app.utils.logger import logger

router = APIRouter()

@router.post("/presentation")
def presentation():
    logger.info("Presentation request received")

    return {
        "slides": [
            {"title": "Slide 1", "content": "Introduction"},
            {"title": "Slide 2", "content": "Key Insights"},
            {"title": "Slide 3", "content": "Conclusion"}
        ],
        "status": "mock-ppt"
    }