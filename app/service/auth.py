from datetime import datetime,timedelta
from typing import Union,Any
from jose import jwt
from jose.constants import ALGORITHMS
from jose.exceptions import ExpiredSignatureError,JWEError
from fastapi import Depends, HTTPException, status as HTTPStatus
from app.env import (
    JWT_SECRET
)
# async def decodejwt(encode,algorithms="HS256"):
#     try:
#         payload = jwt.decode(encode,SECRET_KEY,algorithms=algorithms)
#         return payload
#     except ExpiredSignatureError as e:
#         raise HTTPException(status_code=400,detail="驗證已過期")
#     except JWEError as e:
#         raise HTTPException(status_code=400,detail="驗證失敗")
#
# 產生token
def create_access_token(subject:dict,expires_delta:timedelta=None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        #config.ACCESS_TOKEN_EXPIRE_MINUTRES
        expire = datetime.utcnow() + timedelta(minutes=5)

    to_encode = subject.copy()
    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(to_encode,JWT_SECRET,algorithm=ALGORITHMS.HS256)

    return encode_jwt

# 確認user 是否存在且密碼無錯誤
async def authenticate_user(badge:str,password: str):

    # user = await get_worker_by_badge(badge)
    user: dict = {"password_hash":"foxlink","badge":"test1"}

    if user is None:
        raise HTTPException(
            status_code=HTTPStatus.HTTP_401_UNAUTHORIZED, detail="找不到具有此 ID 的用户"
        )
    
    if not verify_password(password , user['password_hash']):
        raise HTTPException(
            status_code=HTTPStatus.HTTP_401_UNAUTHORIZED, detail="密码不正确"
        )
    return user


def verify_password(user_hashed_password: str, db_hashed_password: str):
    return user_hashed_password == db_hashed_password
