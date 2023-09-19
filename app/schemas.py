from pydantic import BaseModel,EmailStr
from datetime import datetime

class post(BaseModel):
   
    title:str
    content:str
    published:bool=True



class user(BaseModel):
    email:EmailStr
    password:str        



class user_login(BaseModel):
    email:EmailStr
    password:str


class user_return(BaseModel):    
    id:int 
    email:EmailStr  
    created_at:datetime 
    
    class config:
        orm_mode=True

class post_return(post):    
    created_at:datetime 
    id:int  
    owner:user_return

    
    class config:
        orm_mode=True


class token(BaseModel):
    access_token:str
    token_type:str    

    