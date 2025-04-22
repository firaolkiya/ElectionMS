from ..utils.database import Base
from sqlalchemy import String,Column,Integer

class Voter(Base):
    
    __tablename__='voters'

    full_name=Column(String,nullable=False)
    user_id=Column(Integer,primary_key=True,nullable=False,autoincrement="auto")
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    
    