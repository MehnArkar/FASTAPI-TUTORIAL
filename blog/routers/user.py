from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from .. import schemas, database, models, hashing,oauth2
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=["User"]
)
get_db = database.get_db

@router.post("/",response_model=schemas.ShowUser)
def create_user(request:schemas.User,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create(request,db)

router
@router.get("/",response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
   return user.get_all(db)
    

@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.show(id,db)