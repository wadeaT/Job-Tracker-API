from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


#the engine manages connections to PostgreSQL
#the SessionLocal uses the engine 
engine = create_engine(settings.database_url, echo=True) 

#a factory that creates sessions
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()