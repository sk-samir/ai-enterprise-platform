from app.services.ai_service import AIService
from app.services.sql_executor_service import SQLExecutorService
from app.utils.sql_validator import SQLValidator
from app.utils.logger import logger
from app.schemas.tool_schema import ToolCall
from app.core.tool_executor import ToolExecutor

class SQLAgent:

    @staticmethod
    def process(user_message: str):

        prompt = f"""
        You are a MySQL SQL generator.

        Rules:
        1. Return ONLY SQL query
        2. Do NOT explain anything
        3. Do NOT use markdown
        4. Do NOT write comments
        5. Output must start with SELECT

        Table Name:
        dashboards

        Columns:
        id
        name
        description

        User Request:
        {user_message}
        """

        sql_query = AIService.generate_response(prompt)

        cleaned_query = sql_query.strip()

        # Remove markdown
        cleaned_query = cleaned_query.replace("```sql", "")
        cleaned_query = cleaned_query.replace("```", "")

        # Keep only SQL starting from SELECT
        select_index = cleaned_query.lower().find("select")

        if select_index != -1:
            cleaned_query = cleaned_query[select_index:]

        cleaned_query = cleaned_query.strip()

        logger.info(f"SQL_query before cleaning: {sql_query}")
        logger.info(f"Generated SQL: {cleaned_query}")

        if not SQLValidator.validate(cleaned_query):
            return {
                "generated_sql": cleaned_query,
                "error": "Only SELECT queries are allowed"
            }
           

        # results = SQLExecutorService.execute_query(cleaned_query)
        # logger.info(f"Query Results: {results}")
        # return {
        #     "generated_sql": cleaned_query,
        #     "results": results
        # }

        tool_call = ToolCall(
            tool="sql",
            query=cleaned_query
        )
        logger.info(f"Tool Call: {tool_call}")
        return ToolExecutor.execute(tool_call)