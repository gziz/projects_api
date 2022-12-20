from sqlalchemy import Column, Integer, String, ForeignKey, Date
from db import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    projects = relationship('Project', back_populates="creator")


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created = Column(Date, default=datetime.today)
    updates = relationship('Update', back_populates='project')

    creator = relationship("User", back_populates="projects")


class Update(Base):
    __tablename__ = 'updates'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'))
    created = Column(Date, default=datetime.today)
    
    project = relationship('Project', back_populates="updates")
    bullets = relationship('Bullet', back_populates="update")


class Bullet(Base):
    __tablename__ = 'bullets'

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    update_id = Column(Integer, ForeignKey('updates.id'))
    
    update = relationship('Update', back_populates="bullets")
