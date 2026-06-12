from app.models.dashboard_filter import DashboardFilter


class DashboardFilterService:

    MONTHS = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec"
    ]

    CATEGORIES = [
        "banking",
        "loan",
        "card"
    ]

    @staticmethod
    def extract_filters(user_input: str):

        user_input = user_input.lower()

        filters = DashboardFilter()

        for month in DashboardFilterService.MONTHS:

            if month in user_input:
                filters.month = month.title()

        for category in DashboardFilterService.CATEGORIES:

            if category in user_input:
                filters.category = category

        return filters