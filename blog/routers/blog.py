from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)
get_db = database.get_db

@router.get("/",response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request : schemas.Blog, db : Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)


@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def show_blogs(id:int,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.show(id,db)

@router.put("/{id}",status_code=status.HTTP_200_OK)
def update_blog(id:int,request : schemas.Blog,db : Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)


@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_blog(id : int,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.delete(id,db)