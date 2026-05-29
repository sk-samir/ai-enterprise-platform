from app.schemas.tool_schema import ToolCall
from app.tools.sql_tool import SQLTool
from app.tools.mongo_tool import MongoTool
from app.utils.logger import logger
from app.tools.web_tool import WebTool

class ToolExecutor:

    @staticmethod
    def execute(tool_call: ToolCall):
        logger.info(f"Executing tool: {tool_call.tool} with query: {tool_call.query}")
        if tool_call.tool == "sql":
            return SQLTool.run(tool_call.query)
        
        elif tool_call.tool == "mongo":
            action = tool_call.payload.get("action")

            if action == "insert":
                return MongoTool.insert(
                    tool_call.collection,
                    tool_call.payload.get("data")
                )

            if action == "fetch":
                return MongoTool.fetch(
                    tool_call.collection
                )
            
        elif tool_call.tool == "web":
            return WebTool.search(tool_call.query)

        return {
            "error": "Unknown tool"
        }