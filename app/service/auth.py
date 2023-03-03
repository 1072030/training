from datetime import datetime,timedelta
from typing import Union,Any
from jose import jwt
from jose.exceptions import ExpiredSignatureError,JWEError
from fastapi import HTTPException
def decodejwt(encode,algorithms="HS256"):
    try:
        payload = jwt.decode(encode,SECRET_KEY,algorithms=algorithms)
        return payload
    except ExpiredSignatureError as e:
        raise HTTPException(status_code=400,detail="驗證已過期")
    except JWEError as e:
       raise HTTPException(status_code=400,detail="驗證失敗")
def create_access_token(subject:Union[str,Any],expires_delta:timedelta=None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        #config.ACCESS_TOKEN_EXPIRE_MINUTRES
        expire = datetime.utcnow() + timedelta(minutes=5)
    to_encode = {"exp":expire,"sub":str(subject)}
    encode_jwt = jwt.encode(to_encode,"AAAA",algorithm="HS256")
    return

if __name__ == "__main__":
    SECRET_KEY="question"

    expire_date = datetime.utcnow() + timedelta(minutes=5)

    to_encode = {"exp":expire_date,"sub":str(123),"uid":"12345"}

    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm="HS256")
    print(encode_jwt)
    print(decodejwt(encode_jwt))
