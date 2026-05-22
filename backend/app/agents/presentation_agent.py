from app.services.ai_service import AIService


class PresentationAgent:

    @staticmethod
    def process(user_message: str):

        prompt = f"""
        You are a PowerPoint presentation generation assistant.

        Create slide content for:

        {user_message}
        """

        return AIService.generate_response(prompt)