from app.services.sql_executor_service import (
    SQLExecutorService
)


class DashboardSQLService:

    @staticmethod
    def get_transaction_data():

        query = """
        SELECT
            month,
            transaction_count
        FROM banking_analytics
        """

        results = SQLExecutorService.execute_query(
            query
        )

        return results

    @staticmethod
    def get_customer_data():

        query = """
        SELECT
            month,
            customer_count
        FROM banking_analytics
        """

        results = SQLExecutorService.execute_query(
            query
        )

        return results

    @staticmethod
    def get_revenue_data():

        query = """
        SELECT
            month,
            revenue
        FROM banking_analytics
        """

        results = SQLExecutorService.execute_query(
            query
        )

        return results
    
    @staticmethod
    def get_total_revenue():

        query = """
        SELECT
            SUM(revenue) as total_revenue
        FROM banking_analytics
        """

        results = SQLExecutorService.execute_query(
            query
        )

        return results


    @staticmethod
    def get_total_customers():

        query = """
        SELECT
            SUM(customer_count) as total_customers
        FROM banking_analytics
        """

        results = SQLExecutorService.execute_query(
            query
        )

        return results


    @staticmethod
    def get_total_transactions():

        query = """
        SELECT
            SUM(transaction_count)
                as total_transactions
        FROM banking_analytics
        """

        results = SQLExecutorService.execute_query(
            query
        )

        return results