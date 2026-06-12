from dataclasses import dataclass


@dataclass
class DashboardFilter:

    month: str | None = None

    category: str | None = None