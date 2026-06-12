from app.agents.chat_agent import ChatAgent
from app.agents.dashboard_agent import DashboardAgent
from app.agents.presentation_agent import PresentationAgent
from app.agents.sql_agent import SQLAgent
from app.agents.web_agent import WebAgent
from app.utils.logger import logger
from app.constants.routing_constants import (
    SQL_KEYWORDS, 
    WEB_KEYWORDS, 
    DASHBOARD_KEYWORDS, 
    PRESENTATION_KEYWORDS, 
    MONGO_KEYWORDS
)
from app.agents.mongo_agent import MongoAgent


class RouterAgent:

    @staticmethod
    def route(user_message: str):

        message = user_message.lower()

        if any(word in message for word in WEB_KEYWORDS):
            logger.info("Routing to Web Agent")
            return WebAgent.process(user_message)

        elif any(word in message for word in DASHBOARD_KEYWORDS):
            logger.info("Routing to Dashboard Agent")
            return DashboardAgent.process(user_message)

        elif any(word in message for word in PRESENTATION_KEYWORDS):
            logger.info("Routing to Presentation Agent")
            return PresentationAgent.process(user_message)

        elif any(word in message for word in SQL_KEYWORDS):
            logger.info("Routing to SQL Agent")
            return SQLAgent.process(user_message)
        
        elif any(word in message for word in MONGO_KEYWORDS):
            logger.info("Routing to Mongo Agent")
            return MongoAgent.process(user_message)

        else:
            logger.info("Routing to Chat Agent")
            return ChatAgent.process(user_message)