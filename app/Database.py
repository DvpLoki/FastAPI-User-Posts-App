from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

engine=create_engine(settings.DB_URL)

sessionlocal=sessionmaker(bind=engine,autoflush=False)


def connect_DB():
    db=sessionlocal()
    try:
        yield db
        
    finally:
        db.close()