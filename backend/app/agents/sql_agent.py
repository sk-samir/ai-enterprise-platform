from app.services.ai_service import AIService
from app.services.sql_executor_service import SQLExecutorService
from app.utils.sql_validator import SQLValidator
from app.utils.logger import logger

class SQLAgent:

    @staticmethod
    def process(user_message: str):

        prompt = f"""
        You are a MySQL expert.

        Generate ONLY MySQL SELECT query.

        DO NOT generate DELETE, DROP, UPDATE, INSERT.

        Table:
        dashboards

        Columns:
        id
        name
        description

        User Request:
        {user_message}
        """

        sql_query = AIService.generate_response(prompt)

        cleaned_query = (
            sql_query
            .replace("```sql", "")
            .replace("```", "")
            .strip()
        )

        logger.info(f"Generated SQL: {cleaned_query}")

        if not SQLValidator.validate(cleaned_query):
            return {
                "generated_sql": cleaned_query,
                "error": "Only SELECT queries are allowed"
            }
           

        results = SQLExecutorService.execute_query(cleaned_query)
        logger.info(f"Query Results: {results}")
        return {
            "generated_sql": cleaned_query,
            "results": results
        }