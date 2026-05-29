from app.services.sql_executor_service import SQLExecutorService
from app.utils.sql_validator import SQLValidator
from app.utils.logger import logger

class SQLTool:

    @staticmethod
    def run(query: str):
        logger.info(f"Received SQL query: {query}")
        if not SQLValidator.validate(query):
            return {
                "error": "SQL query blocked"
            }

        results = SQLExecutorService.execute_query(query)

        return {
            "query": query,
            "results": results
        }