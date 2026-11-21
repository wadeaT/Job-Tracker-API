from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, security, schemas
from app.database import get_db

router = APIRouter(
    prefix = "/api/user",
    tags = ["Users"]
)


@router.post("",status_code = status.HTTP_201_CREATED, response_model = schemas.UserOut)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    
    statement = select(models.User).where(models.User.email == user_in.email)

    existing_user = db.scalar(statement)

    if existing_user is not None:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = "Email already registered")   

    new_user = models.User(email = user_in.email, password_hash = security.hash_password(user_in.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user