from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    updates = db.query(models.Update).all()
    return updates


def create(request: schemas.Project, db: Session):
    new_update = models.Update(title=request.title,
                               project_id=request.project_id)
    db.add(new_update)
    db.commit()
    db.refresh(new_update)
    return new_update


def destroy(id:int,db: Session):
    proj = db.query(models.Update).filter(models.Update.id == id)

    if not proj.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    proj.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id:int,request:schemas.UpdateBase, db:Session):
    proj = db.query(models.Update).filter(models.Update.id == id)

    if not proj.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    proj.update(request)
    db.commit()
    return 'updated'


def show(id:int,db:Session):
    proj = db.query(models.Update).filter(models.Update.id == id).first()
    if not proj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return proj