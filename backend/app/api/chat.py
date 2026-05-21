from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.logger import logger

router = APIRouter()

class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):
    logger.info(f"Chat request received: {req.message}")
    return {
        "user_message": req.message,
        "response": f"You said: {req.message}",
        "agent": "basic-chat-agent"
    }