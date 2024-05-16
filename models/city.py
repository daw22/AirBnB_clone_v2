#!/usr/bin/python3
"""
contains

classes:
    City - represents a real-life city, mapped to the cities table in the db
"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Represents a real-life city, inherits from BaseModel.
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
