from app.schemas.dashboard_schema import (
    DashboardWidget
)


class WidgetFactoryService:

    @staticmethod
    def create_bar_chart(
        title,
        data,
        description=""
    ):

        return DashboardWidget(
            
            widget_id=title.lower().replace(" ", "_"),
            title=title,
            widget_type="chart",
            chart_type="bar",
            data=data,
            description=description
        )

    @staticmethod
    def create_line_chart(
        title,
        data,
        description=""
    ):

        return DashboardWidget(
            widget_id=title.lower().replace(" ", "_"),
            title=title,
            widget_type="chart",
            chart_type="line",
            data=data,
            description=description
        )

    @staticmethod
    def create_table(
        title,
        data,
        description=""
    ):

        return DashboardWidget(
            widget_id=title.lower().replace(" ", "_"),
            title=title,
            widget_type="table",
            data=data,
            description=description
        )

    @staticmethod
    def create_kpi_card(
        title,
        value,
        description=""  
    ):

        return DashboardWidget(
            widget_id=title.lower().replace(" ", "_"),
            title=title,
            widget_type="kpi",
            data=[
                {
                    "value": value
                }
            ],
            description=description
        )