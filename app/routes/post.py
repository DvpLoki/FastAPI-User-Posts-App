from fastapi import APIRouter,HTTPException,status,Response,Depends
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc


from .. import Models ,auth2
from ..schemas import post,post_return
from ..Database import connect_DB

app=APIRouter(prefix='/posts',tags=['posts'])


@app.post("/", status_code=status.HTTP_201_CREATED,response_model=post_return)
def create_post(data:post, db:Session=Depends(connect_DB), current_user:int=Depends(auth2.get_current_user)):
    add_post=Models.post(user_id=current_user.id,**data.model_dump())
    db.add(add_post)
    db.commit()
    db.refresh(add_post)
    return add_post


@app.get("/",response_model=list[post_return])
def get_posts(db:Session=Depends(connect_DB), current_user=Depends(auth2.get_current_user),
               limit:int=10, skip:int=0, search:Optional[str]=""):
    posts=db.query(Models.post).filter(Models.post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

@app.get("/latest",response_model=list[post_return])
def get_latest_posts(db:Session=Depends(connect_DB),current_user:int=Depends(auth2.get_current_user)):
    posts=db.query(Models.post).order_by(desc(Models.post.id)).all()
    return posts

@app.get("/{id}",response_model=post_return)
def get_post(id:int,db:Session=Depends(connect_DB),current_user:int=Depends(auth2.get_current_user)):
    posts=db.query(Models.post).filter(Models.post.id==id).first()
    if posts==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} not found ")
    return posts


@app.delete("/{id}")
def delete_post(id:int,db:Session=Depends(connect_DB),current_user:int=Depends(auth2.get_current_user)):
    post_query=db.query(Models.post).filter(Models.post.id==id)
    post=post_query.first()
    if post==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} doesn't exist."
        )
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorised to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/{id}")
def update_post(data:post,id:int,db:Session=Depends(connect_DB),current_user:int=Depends(auth2.get_current_user)):

    post_query=db.query(Models.post).filter(Models.post.id==id)
    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id :{id} doesnt exist')
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorised to perform requested action")
    post_query.update(data.model_dump(),synchronize_session=False)
    db.commit()
    return post_query.first()


