from app import Models ,main
from fastapi.testclient import TestClient
from app.Database import connect_DB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
import pytest
engine=create_engine(settings.DB_URL+'_test')

testing_sessionlocal=sessionmaker(autocommit=False,bind=engine,autoflush=False)

Models.Base.metadata.create_all(engine)



@pytest.fixture(scope="module")
def session():
    db=testing_sessionlocal()
    try:
        yield db
        
    finally:
        db.close()

@pytest.fixture(scope="module")
def client(session):
    Models.Base.metadata.drop_all(engine)
    Models.Base.metadata.create_all(engine)
    def override():
        try:
         yield session
        
        finally:
            session.close()
    main.app.dependency_overrides[connect_DB]=override
    yield TestClient(main.app)

