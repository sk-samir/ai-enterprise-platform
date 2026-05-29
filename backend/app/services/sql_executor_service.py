from sqlalchemy import text
from decimal import Decimal

from app.database.mysql import engine


class SQLExecutorService:

    @staticmethod
    def execute_query(query: str):

        with engine.connect() as connection:

            result = connection.execute(
                text(query)
            )

            rows = result.fetchall()

            columns = result.keys()

            formatted_results = []

            for row in rows:

                formatted_row = {}

                for column, value in zip(columns, row):

                    # Convert Decimal to float
                    if isinstance(value, Decimal):

                        value = float(value)

                    formatted_row[column] = value

                formatted_results.append(
                    formatted_row
                )

            return formatted_results