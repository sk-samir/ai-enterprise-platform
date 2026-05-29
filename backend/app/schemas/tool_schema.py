from pydantic import BaseModel
from typing import Optional, Literal


class ToolCall(BaseModel):

    tool: Literal["sql", "mongo", "web", "chat"]

    query: Optional[str] = None

    collection: Optional[str] = None

    payload: Optional[dict] = None