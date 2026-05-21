from app.services.ai_service import AIService


class ChatAgent:

    @staticmethod
    def process(user_message: str):

        enhanced_prompt = f"""
        You are an enterprise AI banking assistant.

        User Question:
        {user_message}
        """

        return AIService.generate_response(enhanced_prompt)