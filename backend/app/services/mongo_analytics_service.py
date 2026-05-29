from app.database.mongodb import mongodb
from datetime import datetime, UTC, time


class MongoAnalyticsService:

    @staticmethod
    def get_total_chat_count():

        collection = mongodb["chat_history"]

        return collection.count_documents({})

    @staticmethod
    def get_today_chat_count():

        collection = mongodb["chat_history"]

        today = datetime.now(UTC).date()

        start_of_day = datetime.combine(
            today,
            time.min,
            tzinfo=UTC
        )

        return collection.count_documents(
            {
                "timestamp": {
                    "$gte": start_of_day
                }
            }
        )