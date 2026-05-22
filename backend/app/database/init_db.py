from app.database.mysql import engine
from app.models.dashboard_model import Base

Base.metadata.create_all(bind=engine)

print("Database tables created successfully")