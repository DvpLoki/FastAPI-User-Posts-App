from passlib.context import CryptContext

pwd_context=CryptContext(schemes=['bcrypt'])

def hash(p:str):
    return pwd_context.hash(p)

def verify(pswd,hpswd):
    return pwd_context.verify(pswd,hpswd)