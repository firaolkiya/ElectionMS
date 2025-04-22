from pydantic import BaseModel,EmailStr

class Voter(BaseModel):
    full_name:str
    email:str
    password:str

class VoterResponse(BaseModel):
    full_name:str
    email:EmailStr
    user_id:int

class UpdateVote(BaseModel):
    full_name:str
    email:EmailStr
    user_id:int

class Login(BaseModel):
    email:str
    password:str
    

class Token(BaseModel):
    access_token:str
    token_type:str
    