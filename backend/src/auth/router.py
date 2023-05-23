from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.auth.dependencies import security
from src.auth.schema import UserLogin, User
from src.database.db import SessionLocal
from src.auth.model import UserModel
from src.auth.jwt import decode_access_token, create_access_token

auth_router = APIRouter()


@auth_router.post("/login")
def login(user_login: UserLogin):
    db = SessionLocal()
    user = db.query(UserModel).filter(UserModel.username == user_login.username).first()
    db.close()
    if not user or user.password != user_login.password:
        return {"message": "Invalid username or password"}
    access_token = create_access_token(data={"user_id": user.id, "username": user.username})
    return {"message": "Logged in successfully", "token": access_token}


@auth_router.post("/register")
def register(user: User):
    db = SessionLocal()
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        return {"message": "Username already exists"}
    db_user = UserModel(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return {"message": "User registered successfully"}


@auth_router.get("/verify-token")
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer":
        raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    token = credentials.credentials.split(" ")[-1]
    decoded_token = decode_access_token(token)
    if not decoded_token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "Token is valid"}


@auth_router.get("/current-user")
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    decoded_token = decode_access_token(token)
    if not decoded_token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": decoded_token.get("username")}