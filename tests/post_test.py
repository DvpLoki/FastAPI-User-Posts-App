from .db import client,session


#get_all_posts
def test_get_all_posts(authorize_client,test_post):
    res=authorize_client.get("/posts/")
    assert res.status_code==200

def test_unauthorized_user_get_all_posts(client,test_post):
    client.headers['authorization']=''
    res=client.get('/posts/')
    assert res.status_code==401


#get_one_posts
def test_get_one_post(authorize_client,test_post):
    res=authorize_client.get(f'/posts/{test_post[0].id}')
    assert res.json().get('id')==test_post[0].id
    

def test_unauthorized_user_get_one_posts(client,test_post):
    client.headers['authorization']=''
    res=client.get(f'/posts/{test_post[0].id}')
    assert res.status_code==401

  
def test_get_one_post_not_exist(authorize_client,test_post):
    res=authorize_client.get(f'/posts/24')
    assert res.status_code==404



#create_posts
def test_create_post(authorize_client):
    res=authorize_client.post("/posts/",json={'title':'test tile',"content":'test content',"published":True})
    assert res.status_code==201

def test_unauthorized_user_create_post(client):
    client.headers['authorization']=''
    res=client.post("/posts/",json={'title':'test tile',"content":'test content',"published":True})
    assert res.status_code==401




#update_posts
def test_update_post(authorize_client,test_post):
    data={
        "title":"updated ",
        "content":"updated"
       }
    res=authorize_client.put(f'/posts/{test_post[0].id}',json=data)
    assert res.status_code==200

def test_unauthorized_update_post(client,test_post):
    data={
        "title":"updated ",
        "content":"updated"
       }
    client.headers['authorization']=''
    res=client.put(f'/posts/{test_post[0].id}',json=data)
    assert res.status_code==401


def test_update_post_not_exist(authorize_client,test_post):
    data={
        "title":"updated ",
        "content":"updated"
       }
    res=authorize_client.put(f'/posts/33',json=data)
    assert res.status_code==404

def test_update_other_user_post_(authorize_client,test_post):
    data={
        "title":"updated ",
        "content":"updated"
       }
    res=authorize_client.put(f'/posts/{test_post[1].id}',json=data)
    assert res.status_code==403




#delete_post
def test_delete_post(authorize_client,test_post):
    res=authorize_client.delete(f"/posts/{test_post[0].id}")
    assert res.status_code==204

def test_unauthorized_user_delete_post(client,test_post):
    client.headers['authorization']=''
    res=client.delete(f"/posts/{test_post[0].id}")
    assert res.status_code==401

def test_delete_post_not_exist(authorize_client):
    res=authorize_client.delete(f"/posts/33")
    assert res.status_code==404

def test_delete_other_user_post(authorize_client,test_post):
    res=authorize_client.delete(f"/posts/{test_post[1].id}")
    assert res.status_code==403

