from typing import List
from fastapi import APIRouter, Depends, status
import schemas, db, models, oauth2
from sqlalchemy.orm import Session
from repository import project
from datetime import datetime


get_db = db.get_db

router = APIRouter(
    prefix="/project",
    tags=['projects']
)

@router.get('/', response_model=List[schemas.ShowProject])
def all(db: Session = Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Project, db:Session = Depends(get_db), 
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.create(request, db)


@router.delete('/id/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.destroy(id, db)


@router.get('/id/{id}', status_code=200, response_model=schemas.ShowProject)
def show(id: int, db: Session = Depends(get_db), 
         current_user: schemas.User = Depends(oauth2.get_current_user)):

    return project.show(id, db)

@router.get('/date/')
def show_by_date(begin: str = "", end: str = "", db: Session = Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.show_by_date(begin, end, db)


    