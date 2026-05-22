from app.agents.chat_agent import ChatAgent
from app.agents.dashboard_agent import DashboardAgent
from app.agents.presentation_agent import PresentationAgent
from app.agents.sql_agent import SQLAgent
from app.utils.logger import logger

class RouterAgent:

    @staticmethod
    def route(user_message: str):

        message = user_message.lower()

        if "notdashboard" in message:
            logger.info("Routing to Dashboard Agent")
            return DashboardAgent.process(user_message)

        elif "presentation" in message or "ppt" in message:
            logger.info("Routing to Presentation Agent")
            return PresentationAgent.process(user_message)

        elif (
            "sql" in message
            or "database" in message
            or "dashboard data" in message
            or "show dashboards" in message
        ):
            logger.info("Routing to SQL Agent")
            return SQLAgent.process(user_message)

        else:
            logger.info("Routing to Chat Agent")
            return ChatAgent.process(user_message)