# File: backend/app/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import os

from app import models, schemas
from app.dependencies import get_db, get_current_user
from app.auth import get_password_hash, verify_password, create_access_token

router = APIRouter()

# Config
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

# Register new user
@router.post("/register", response_model=schemas.UserOut, tags=["auth"])
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Login and return JWT
@router.post("/token", tags=["auth"])
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    token = create_access_token({"sub": db_user.email}, SECRET_KEY, ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

# Get
