#!/usr/bin/python3
"""
contains

classes:
    User - Inherits from BaseModel, represents a user, mapped to the users table
    in the database
"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Represents a user of the service, inherits from BaseModel.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan")
    reviews = relationship("Review", backref="user",
                           cascade="all, delete, delete-orphan")
