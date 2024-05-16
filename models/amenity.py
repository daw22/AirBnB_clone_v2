#!/usr/bin/python3
"""
contains

classes:
    Amenity - represents an amenity of a place, mapped to the amenities table 
    in the database
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    Represents some amenity (quality) of a place, inherits from BaseModel.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
