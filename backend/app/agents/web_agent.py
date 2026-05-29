from app.schemas.tool_schema import ToolCall
from app.core.tool_executor import ToolExecutor


class WebAgent:

    @staticmethod
    def process(user_message: str):

        tool_call = ToolCall(
            tool="web",
            query=user_message
        )

        return ToolExecutor.execute(tool_call)