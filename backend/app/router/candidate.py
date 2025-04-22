from fastapi import APIRouter,HTTPException,Response,Depends,status,Header
from sqlalchemy.orm import Session
from ..models.candidate import Candidate
from ..utils.database import get_db
from ..schemas import candidate
from ..utils.password import hash_password
from typing import Annotated
router=APIRouter(
    prefix='/candidates',
    tags=['Candidates']
)


@router.get('/',response_model=list[candidate.CandidateResponse])
def get_all_candidates(db:Session=Depends(get_db)):
    
    candidates=db.query(Candidate).all()
    return candidates
    
@router.post('/',response_model=candidate.CandidateResponse)
def create_candidates(new_candidate:candidate.CreateCandidate,db:Session=Depends(get_db)):
    
    new_candidate.password=hash_password(new_candidate.password)
    
    # check if email is exist
    exist_user=db.query(Candidate).filter(Candidate.email==new_candidate.email)
    if exist_user.first():
        raise HTTPException(
            detail={'msg':'email already taken'},
            status_code=status.HTTP_400_BAD_REQUEST
        )
    candidate_model=Candidate(**new_candidate.dict())
    db.add(candidate_model)
    
    db.commit()
    db.refresh(candidate_model)
    return candidate_model

@router.get('/{user_id}',response_model=candidate.CandidateResponse)
def get_candidate(user_id:int,db:Session=Depends(get_db)):
    
    query=db.query(Candidate).filter(Candidate.user_id==user_id).first()
    if not query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'msg':'candidate with that id doest exist'}
        )
    return query

@router.delete('/{user_id}')
def delete_candidate(user_id:int,response:Response,db:Session=Depends(get_db)):
    result_candidate=db.query(Candidate).filter(Candidate.user_id==user_id)
    
    if not result_candidate.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'msg':'candidate with that id doest found'}
        )
    result_candidate.delete(synchronize_session=False)
    db.commit()
    
    response.status_code=status.HTTP_204_NO_CONTENT
    return {
        'message':'candidate successfully deleted'
    }
    
@router.put('/{user_id}',response_model=candidate.CandidateResponse)
def update_candidate(
        updated_candidate:candidate.BaseCandidates,
        user_id:int,
        db:Session=Depends(get_db)):
    
    query=db.query(Candidate).filter(Candidate.user_id==user_id)
    if not query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'msg':'candidate doest found'}
        )
    query.update(updated_candidate.model_dump(),synchronize_session=False)
    db.commit()
    return query.first()
    
@router.post('/follow/')
def follow_candidate(
        user_id:int,
        header:Annotated[str | None, Header(convert_underscores=False)],
        db:Session=Depends(get_db)):
    return {"welcome":header}
    