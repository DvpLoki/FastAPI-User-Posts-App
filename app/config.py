from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    DB_URL:str
    SECRET_key:str
    Token_Expire_Time_Min:int
    Algorithm:str
    
    model_config = SettingsConfigDict(env_file=".env")


settings=Settings()