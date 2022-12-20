from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException,status, Depends
import datetime


def get_all(db: Session, response_model=Page[schemas.ShowProject]):
    projs = db.query(models.Project).all()
    return projs


def create(request: schemas.Project, db: Session):
    new_proj = models.Project(title=request.title, user_id=1)
    db.add(new_proj)
    db.commit()
    db.refresh(new_proj)
    return new_proj


def destroy(id:int,db: Session):
    proj = db.query(models.Project).filter(models.Project.id == id)

    if not proj.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    proj.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id:int, request:schemas.Project, db:Session):
    proj = db.query(models.Project).filter(models.Project.id == id)

    if not proj.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    proj.update(request)
    db.commit()
    return 'updated'


def show(id:int, db:Session):
    proj = db.query(models.Project).filter(models.Project.id == id).first()
    if not proj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return proj


def show_by_date(begin: str, end: str, db:Session):
    if begin != "":
        begin = datetime.strptime(begin, "%m-%d-%Y")
    else:
        begin = datetime.datetime.min
    if end != "":
        end = datetime.strptime(end, "%m-%d-%Y")
    else:
        end = datetime.datetime.now()

    projs = db.query(models.Project).filter(models.Project.created >= begin,
                                            models.Project.created <= end).all()

    return projs