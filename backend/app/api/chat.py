from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.router_agent import RouterAgent
from app.utils.logger import logger
from app.services.chat_history_service import ChatHistoryService

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):

    logger.info(f"User message: {req.message}")

    response = RouterAgent.route(req.message)
    logger.info(f"AI response: {response}")
    # Save chat history
    ChatHistoryService.save_chat(req.message, response) 

    return {
        "user_message": req.message,
        "response": response
    }

    
    