from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import Database,schemas,Models,utils,auth2




app=APIRouter(tags=['authentication'])

@app.post("/login",response_model=schemas.token)
def login(user_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(Database.connect_DB)):

    user=db.query(Models.user).filter(Models.user.email==user_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid Email')
    
    if not utils.verify(user_data.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid password")
    
    access_token=auth2.create_access_token(data={"user_id":user.id})
    
    return {"access_token":access_token,"token_type":"Bearer"}


