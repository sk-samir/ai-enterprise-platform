from fastapi import APIRouter
from app.utils.logger import logger
from app.schemas.presentation_api_schema import (
    PresentationRequest
)

from app.agents.presentation_agent import (
    PresentationAgent
)

router = APIRouter()

@router.post("/presentation")

def create_presentation(
    request: PresentationRequest
):

    return PresentationAgent.process(
        request.topic
    )