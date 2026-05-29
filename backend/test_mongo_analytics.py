from app.services.mongo_analytics_service import (
    MongoAnalyticsService
)

print(
    MongoAnalyticsService.get_total_chat_count()
)

print(
    MongoAnalyticsService.get_today_chat_count()
)