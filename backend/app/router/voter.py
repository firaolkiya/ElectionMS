from fastapi import APIRouter,Response,status,Depends,HTTPException
from ..schemas import voter as schemas
from ..models import voter as models
from ..utils.password import hash_password
from ..utils.database import get_db
from sqlalchemy.orm import Session


router=APIRouter(
    prefix='/vouters',
    tags=['Voter Api']
)



@router.post('/',response_model=schemas.VoterResponse)
def register_voter(voter:schemas.Voter,response:Response,db:Session=Depends(get_db)):
    
    try:
        password=voter.password
        voter.password=hash_password(password)
        exist_user=db.query(models.Voter).filter(models.Voter.email==voter.email)
        if exist_user.first():
            raise HTTPException(
                detail={'msg':'email already taken'},
                status_code=status.HTTP_400_BAD_REQUEST
            )
        voter_model=models.Voter(**voter.dict())
        
        db.add(voter_model)
        db.commit()
        db.refresh(voter_model)
        return voter_model
    except Exception:
        response.status_code=status.HTTP_400_BAD_REQUEST
        return {
            "message":"wrong message format"
        }
    

@router.delete('/{user_id}')    
def delete_voter(user_id:int,db:Session=Depends(get_db)):
    query=db.query(models.Voter).filter(models.Voter.user_id==user_id)
    
    if not query or not query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='no such user_id is found'
            )
    query.delete(synchronize_session=False)
    db.commit()
    return {'message':"successfully deleted"}

@router.put('/',response_model=schemas.VoterResponse)
def update_voter(voter:schemas.UpdateVote,response:Response,db:Session=Depends(get_db)):
    query=db.query(models.Voter).filter(models.Voter.user_id==voter.user_id)
    if not query.first():
        raise HTTPException(detail={"message":"id doesnt found"},status_code=status.HTTP_404_NOT_FOUND)
    
    query.update(voter.dict(),synchronize_session=False)
    db.commit()
    return query.first()


    
    
    
    
    