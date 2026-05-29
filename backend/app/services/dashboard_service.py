from datetime import datetime

from app.schemas.dashboard_schema import (
    DashboardResponse,
    DashboardMetadata
)

from app.services.widget_factory_service import (
    WidgetFactoryService
)

from app.services.dashboard_sql_service import (
    DashboardSQLService
)

from app.services.mongo_analytics_service import (
    MongoAnalyticsService
)


class DashboardService:

    @staticmethod
    def generate_dashboard(user_input: str):

        widgets = []
        
        if "revenue" in user_input.lower():

            revenue_data = (
                DashboardSQLService
                .get_revenue_data()
            )

            widgets.append(

                WidgetFactoryService.create_bar_chart(
                    title="Revenue Analytics",
                    data=revenue_data,
                    description="Monthly revenue trend"
                )
            )
        
        if "transaction" in user_input.lower():

            transaction_data = (
                DashboardSQLService
                .get_transaction_data()
            )

            widgets.append(

                WidgetFactoryService.create_bar_chart(
                    title="Monthly Transactions",
                    data=transaction_data,
                    description="Live transaction data"
                )
            )

        if "customer" in user_input.lower():

            customer_data = (
                DashboardSQLService
                .get_customer_data()
            )

            widgets.append(

                WidgetFactoryService.create_line_chart(
                    title="Customer Growth",
                    data=customer_data,
                    description="Live customer data"
                )
            )

        total_revenue = (
            DashboardSQLService
            .get_total_revenue()
        )

        total_customers = (
            DashboardSQLService
            .get_total_customers()
        )

        total_transactions = (
            DashboardSQLService
            .get_total_transactions()
        )

        widgets.append(

            WidgetFactoryService.create_kpi_card(
                title="Total Revenue",
                value=total_revenue[0]["total_revenue"],
                description="Overall revenue"
            )
        )

        widgets.append(

            WidgetFactoryService.create_kpi_card(
                title="Total Customers",
                value=total_customers[0]["total_customers"],
                description="Overall customer count"
            )
        )

        widgets.append(

            WidgetFactoryService.create_kpi_card(
                title="Total Transactions",
                value=total_transactions[0]["total_transactions"],
                description="Overall transaction count"
            )
        )
        
        total_chats = (
            MongoAnalyticsService
            .get_total_chat_count()
        )

        today_chats = (
            MongoAnalyticsService
            .get_today_chat_count()
        )
        widgets.append(

            WidgetFactoryService.create_kpi_card(
                title="Total AI Chats",
                value=total_chats,
                description="Overall chat interactions"
            )
        )
        widgets.append(

            WidgetFactoryService.create_kpi_card(
                title="Today's Chats",
                value=today_chats,
                description="Chat interactions today"
            )
        )

        metadata = DashboardMetadata(
            generated_by="AI Dashboard Engine",
            generated_at=str(datetime.now()),
            data_source="MySQL & MongoDB",
            dashboard_version="1.0"
        )

        return DashboardResponse(
            dashboard_name="Enterprise Dashboard",
            metadata=metadata,
            widgets=widgets
        )