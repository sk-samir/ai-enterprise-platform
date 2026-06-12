from pydantic import BaseModel
from typing import Any

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    user_message: str
    response: Any