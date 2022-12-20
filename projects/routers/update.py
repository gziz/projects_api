from typing import List
from fastapi import APIRouter, Depends, status
import schemas, db, models, oauth2
from sqlalchemy.orm import Session
from repository import update


get_db = db.get_db

router = APIRouter(
    prefix="/updates",
    tags=['updates']
)

@router.get('/', response_model=List[schemas.ShowUpdate])
def all(db: Session = Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    return update.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.UpdateBase, db:Session = Depends(get_db), 
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return update.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return update.destroy(id, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUpdate)
def show(id, db: Session = Depends(get_db), 
         current_user: schemas.User = Depends(oauth2.get_current_user)):
    return update.show(id, db)