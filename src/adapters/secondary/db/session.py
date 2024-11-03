from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.adapters.settings import db_settings

engine = create_engine(str(db_settings.db_sync_url))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
