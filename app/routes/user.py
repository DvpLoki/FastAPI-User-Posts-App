from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session


from .. import Models , utils
from ..schemas import user,user_return
from ..Database import connect_DB


app=APIRouter(prefix='/users',tags=['users'])

@app.post("/",status_code=status.HTTP_201_CREATED,response_model=user_return)
def create_user(data:user,db:Session=Depends(connect_DB)):

    data.password=utils.hash(data.password)
    add_user=Models.user(**data.model_dump())
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
  
    return add_user

@app.get("/{id}",response_model=user_return)
def get_user(id:int,db:Session=Depends(connect_DB)):
    user=db.query(Models.user).filter(Models.user.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id:{id} not found")
    
    return user