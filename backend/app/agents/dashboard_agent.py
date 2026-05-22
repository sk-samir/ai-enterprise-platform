from app.services.ai_service import AIService


class DashboardAgent:

    @staticmethod
    def process(user_message: str):

        prompt = f"""
        You are an enterprise dashboard analytics assistant.

        Generate dashboard insights for:

        {user_message}
        """

        return AIService.generate_response(prompt)