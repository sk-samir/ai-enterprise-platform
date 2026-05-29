from app.tools.dashboard_tool import DashboardTool


class DashboardAgent:

    @staticmethod
    def process(user_message: str):

        return DashboardTool.create_dashboard(
            user_message
        )