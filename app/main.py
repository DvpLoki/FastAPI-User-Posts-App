from fastapi import FastAPI 

from . import Models 
from .Database import engine
from .routes import post,user,Auth

from fastapi.middleware.cors import CORSMiddleware

Models.Base.metadata.create_all(bind=engine)


app=FastAPI()

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