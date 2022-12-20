from fastapi import APIRouter
import db, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from repository import user

router = APIRouter(
    prefix="/user",
    tags=['users']
)

get_db = db.get_db

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show(id, db)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request, db)
