from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from app.service.auth import (
    authenticate_user,
    create_access_token
)
router = APIRouter(prefix="/auth")

class Token(BaseModel):
    access_token: str
    token_type: str

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

@router.post("/token", response_model=Token, responses={401: {"description": "Invalid username/password"}})
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_routine(form_data)

async def login_routine(form_data):
    user = await authenticate_user(form_data.username,form_data.password)

    access_token = create_access_token(
        subject={
            "sub": user['badge'],
            "UUID": form_data.client_id
        },
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token": access_token, "token_type": "bearer"}