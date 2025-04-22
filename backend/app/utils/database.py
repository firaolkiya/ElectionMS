from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import setting

DATABASE_URL=f'postgresql://{setting.database_username}:{setting.database_password}@ep-damp-bird-a46s9e47-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require'
engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
    )

Base=declarative_base()

async def get_db():
    try:
        db=  SessionLocal()
        yield db
    finally:
        db.close()