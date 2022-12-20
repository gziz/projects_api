from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException,status


def create(request: schemas.Project, db: Session):
    new_bullet = models.Bullet(body=request.body, update_id=request.update_id)
    db.add(new_bullet)
    db.commit()
    db.refresh(new_bullet)
    return new_bullet


def show(id:int,db:Session):
    proj = db.query(models.Bullet).filter(models.Bullet.id == id).first()
    if not proj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return proj