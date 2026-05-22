from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.connection import Settings


DATABASE_URL = (
    f"mysql+pymysql://"
    f"{Settings.MYSQL_USER}:"
    f"{Settings.MYSQL_PASSWORD}@"
    f"{Settings.MYSQL_HOST}:"
    f"{Settings.MYSQL_PORT}/"
    f"{Settings.MYSQL_DATABASE}"
)

print(f"Database URL: {DATABASE_URL}")  # Debugging line to check the constructed URL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)