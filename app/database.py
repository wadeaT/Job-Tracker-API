from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


#the engine manages connections to PostgreSQL
#the SessionLocal uses the engine 
engine = create_engine(settings.database_url, echo=True) 
print("after creating the engine")
#a factory that creates sessions
SessionLocal = sessionmaker(bind=engine)
print("after creating the session")
class Base(DeclarativeBase):
    pass


def get_db():
    print("called the get_db function")
    db = SessionLocal()
    try:
        print("get into the try block")
        yield db
    finally:
        print("finally block")
        db.close()