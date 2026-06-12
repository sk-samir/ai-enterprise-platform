from datetime import datetime, UTC

from app.database.mongodb import mongodb


class ChatHistoryService:

    @staticmethod
    def save_chat(user_message: str, ai_response: str):

        collection = mongodb["chat_history"]

        document = {
            "user_message": user_message,
            "ai_response": ai_response,
            "created_at": datetime.now(UTC)
        }

        collection.insert_one(document)