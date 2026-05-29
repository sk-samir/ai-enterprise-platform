from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class DashboardWidget(BaseModel):

    widget_id: str

    title: str

    widget_type: str

    chart_type: Optional[str] = None

    data: List[Dict[str, Any]]

    description: Optional[str] = None


class DashboardMetadata(BaseModel):

    generated_by: str

    generated_at: str

    data_source: str

    dashboard_version: Optional[str] = None


class DashboardResponse(BaseModel):

    dashboard_name: str

    metadata: DashboardMetadata

    widgets: List[DashboardWidget]