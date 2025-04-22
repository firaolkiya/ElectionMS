from .voter import Base
from sqlalchemy import Column,String,Integer,text
class Candidate(Base):
    __tablename__='candidates'
    
    user_id=Column(Integer,primary_key=True,nullable=False)
    full_name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    party_name=Column(String,unique=True,nullable=False)
    profile_url=Column(String,server_default='')
    password=Column(String,nullable=False)

    