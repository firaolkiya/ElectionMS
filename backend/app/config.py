from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    
    database_password:str
    database_username:str
    secret_key:str 
    algorithm:str 
    access_token_expire_minutes:str 
    
    class Config:
        env_file='.env'
    

setting=Setting()
