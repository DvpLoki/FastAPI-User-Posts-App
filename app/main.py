from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from . import Models 
from .Database import engine
from .routes import post,user,Auth

Models.Base.metadata.create_all(bind=engine)


app=FastAPI(title="RESTAPI by Devarapu Lokesh",
        version="1.0",
        summary=" RESTAPI using python FastAPI",
        description="This is a simple API to do CRUD operations on posts created by users included with oAuth2  Authorization  and JWT based Authentication.",
        contact={
            "name":"Devarapu Lokesh",
            "email":"dvploki@gmail.com"
        },redoc_url=None,)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )


@app.get("/")
def root():
    return {"msg":"welcome to Fast API by Dev Lokesh"}



app.include_router(post.app)
app.include_router(user.app)
app.include_router(Auth.app)

