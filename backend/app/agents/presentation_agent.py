from app.services.presentation_service import (
    PresentationService
)


class PresentationAgent:

    @staticmethod
    def process(topic: str):

        file_path = (
            PresentationService
            .create_presentation(topic)
        )

        return {
            "status": "success",
            "file_path": file_path
        }