from typing import List
from fastapi import APIRouter, Depends, status
import schemas, db, models, oauth2
from sqlalchemy.orm import Session
from repository import bullet


get_db = db.get_db

router = APIRouter(
    prefix="/bullets",
    tags=['bullets']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BulletBase, db:Session = Depends(get_db), 
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return bullet.create(request, db)

