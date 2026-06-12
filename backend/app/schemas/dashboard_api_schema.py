from pydantic import BaseModel


class DashboardRequest(BaseModel):

    query: str