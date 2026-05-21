import os
import ollama

from dotenv import load_dotenv

load_dotenv()


class AIService:

    MODEL_NAME = os.getenv("OLLAMA_MODEL")


    @staticmethod
    def generate_response(user_message: str):

        response = ollama.chat(
            model=AIService.MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response["message"]["content"]