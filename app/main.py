from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import get_db



app = FastAPI(title="Jobtrack API")

@app.get("/api/health")
def get_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1 ")).all()
    return {"status": "ok"}

