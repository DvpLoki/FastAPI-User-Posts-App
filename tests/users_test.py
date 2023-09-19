from .db import session,client
from app import schemas
from app.config import settings
from jose import jwt
import pytest


def test_create_user(client):
    res=client.post('/users/',json={"email":"lokitest@gmail.com","password":"testpaswd"})
    user=schemas.user_return(**res.json())
    assert res.status_code==201



def test_user_login(client,test_user):
        res=client.post('/login',data={"username":test_user['email'],"password":test_user['password']})

        payload=jwt.decode(res.json().get("access_token"),settings.SECRET_key,algorithms=settings.Algorithm)
        id=payload.get("user_id")
        assert id==test_user['id']
        assert res.json().get('token_type')=='Bearer'
        assert res.status_code==200
  

@pytest.mark.parametrize("email,password,status_code",[('loki@gmail.com','paswd',403),('lokitest@gmail.com','passs',403),(None,'passwd',422),('lokitest@gmail.com',None,422)])
def test_incorrect_user_login(client,email,password,status_code):
      res=client.post('/login',data={"username":email,"password":password})

      assert res.status_code==status_code

