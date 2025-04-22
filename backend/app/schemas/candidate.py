from pydantic import BaseModel,EmailStr

class BaseCandidates(BaseModel):
    email:EmailStr
    full_name:str
    party_name:str
    profile_url:str=''

class CandidateResponse(BaseCandidates):
    user_id:int

class CreateCandidate(BaseCandidates):
    password:str

