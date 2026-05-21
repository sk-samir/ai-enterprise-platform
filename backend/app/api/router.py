from fastapi import APIRouter
from app.api import health, chat, dashboard, presentation

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(chat.router)
api_router.include_router(dashboard.router)
api_router.include_router(presentation.router)