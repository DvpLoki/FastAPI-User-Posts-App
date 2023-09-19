import pytest
from app.auth2 import create_access_token
from app import Models


@pytest.fixture(scope='module')
def test_user(client):
    res=client.post('/users/',json={"email":"lokitest1@gmail.com","password":"testpaswd"})
    assert res.status_code==201
    new_user=res.json()
    new_user['password']='testpaswd'
    return new_user


@pytest.fixture(scope='module')
def test_user2(client):
    res=client.post('/users/',json={"email":"lokitest2@gmail.com","password":"testpaswd"})
    assert res.status_code==201
    new_user=res.json()
    new_user['password']='testpaswd'
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({'user_id':test_user['id']})

@pytest.fixture
def authorize_client(client,token):
    client.headers['authorization']=''
    client.headers['authorization']=f'Bearer {token}'
    
    return client


@pytest.fixture(scope='module')
def test_post(session,test_user,test_user2):
    session.add_all((Models.post(title='1st title',content='1st content',published=True,user_id=test_user['id']),
                Models.post(title='1st title',content='1st content',published=True,user_id=test_user2['id'])))
    session.commit()
    return session.query(Models.post).all()


   


