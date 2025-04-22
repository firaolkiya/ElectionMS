import jwt

from datetime import timedelta,datetime

from ..schemas.voter import Login,Token
from ..config import setting
from ..utils.database import get_db
from fastapi import APIRouter,Depends,HTTPException,status
from ..models import voter
from sqlalchemy.orm import Session
from ..utils.password import verify_password


router=APIRouter(
    tags=['Login/Authenticate']
)

# create token
def create_token(data:dict):
    to_encode=data.copy()
    to_encode.update({'exp':datetime.now()+timedelta(minutes=int(setting.access_token_expire_minutes))})
    encoded_jwt=jwt.encode(to_encode,setting.secret_key,algorithm=setting.algorithm)
    return encoded_jwt
    


# get user from token
# @router.post('/token',response_model=voter.VoterResponse)
# def get_current_user(data,db:Session=Depends(get_db)):
#     token=data
#     decoded=jwt.decode(token,setting.secret_key,algorithms=setting.algorithm)
#     user=db.query(voter.Voter).filter(voter.Voter.email==decoded['email'])
#     return user
    


# check if the token is active

# login 
@router.post('/login')
def login(user:Login,db:Session=Depends(get_db)):
    # get user with email
    user_db=db.query(voter.Voter).filter(voter.Voter.email==user.email).first()
    if not user_db:
        raise HTTPException(
            detail={"msg":"incorrect credintial"},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    if not verify_password(user.password,user_db.password):
        raise HTTPException(
            detail={"msg":"incorrect credintial"},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    
    token= create_token(user.dict())
    return Token(
        access_toke=token,
        token_type='bearer'
    )
    
