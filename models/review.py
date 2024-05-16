#!/usr/bin/python3
"""
contains

classes:
    Review - represents a review left by a user, mapped to the reviews table 
    in the database
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """
    Represents a review of a place left by a user, inherits from BaseModel.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
