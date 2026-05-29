from app.services.dashboard_service import DashboardService


class DashboardTool:

    @staticmethod
    def create_dashboard(user_input: str):

        dashboard = DashboardService.generate_dashboard(
            user_input
        )

        return dashboard.model_dump()