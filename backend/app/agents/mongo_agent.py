from app.tools.mongo_tool import MongoTool


class MongoAgent:

    @staticmethod
    def process(user_message: str):

        message = user_message.lower()

        if "count chat history" in message:

            return MongoTool.count(
                "chat_memory"
            )

        if "chat history" in message:

            return MongoTool.fetch(
                "chat_memory"
            )

        return {
            "message": "Mongo request not recognized"
        }