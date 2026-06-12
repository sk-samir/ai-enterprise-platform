from fastapi import APIRouter
from app.utils.logger import logger
from app.schemas.dashboard_api_schema import (
    DashboardRequest
)

from app.services.dashboard_service import (
    DashboardService
)

router = APIRouter()

@router.post("/dashboard")

def generate_dashboard(
    request: DashboardRequest
):

    dashboard = DashboardService.generate_dashboard(
        request.query
    )

    return {
        "dashboard": dashboard
    }