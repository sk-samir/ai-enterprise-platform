from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.config.settings import settings

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{settings.MYSQL_USER}:"
    f"{settings.MYSQL_PASSWORD}@"
    f"{settings.MYSQL_HOST}:"
    f"{settings.MYSQL_PORT}/"
    f"{settings.MYSQL_DATABASE}"
)

print(f"Database URL: {DATABASE_URL}")  # Debugging line to check the constructed URL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)