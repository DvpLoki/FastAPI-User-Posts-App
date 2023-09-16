from jose import JWTError,jwt
from datetime import datetime,timedelta
from . import schemas
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import Database,Models
from .config import settings
auth_scheme=OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data:dict):
    encode=data.copy()

    expire=datetime.utcnow()+timedelta(minutes=settings.Token_Expire_Time_Min)
    encode.update({"exp":expire})
    encoded_jwt=jwt.encode(encode,settings.SECRET_key,algorithm=settings.Algorithm)

    return encoded_jwt    


def verify_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,settings.SECRET_key,algorithms=settings.Algorithm)
        id=payload.get("user_id")
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return id
    

def get_current_user(token:str=Depends(auth_scheme),db:Session=Depends(Database.connect_DB)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="could not validate credentials",headers={"www-Authenticate":"Bearer"})
    id=verify_token(token,credentials_exception)
    user=db.query(Models.user).filter(Models.user.id==id).first()

    return user
