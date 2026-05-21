from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.chat_agent import ChatAgent
from app.utils.logger import logger

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):

    logger.info(f"Chat request received: {req.message}")

    response = ChatAgent.process(req.message)

    return {
        "user_message": req.message,
        "response": response,
        "agent": "enterprise-chat-agent"
    }