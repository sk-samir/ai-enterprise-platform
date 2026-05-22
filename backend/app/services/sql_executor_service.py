from sqlalchemy import text

from app.database.mysql import engine


class SQLExecutorService:

    @staticmethod
    def execute_query(query: str):

        with engine.connect() as connection:

            result = connection.execute(text(query))

            rows = result.fetchall()

            return [dict(row._mapping) for row in rows]