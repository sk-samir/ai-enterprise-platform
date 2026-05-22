from app.agents.sql_agent import SQLAgent


class DashboardDataAgent:

    @staticmethod
    def process():

        return SQLAgent.process(
            "Show dashboards"
        )