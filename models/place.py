#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models import storage
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = None
    if os.getenv("HBNB_TYPE_STORAGE", "db") == "db":
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete, delete-orphan")
    elif os.getenv("HBNB_TYPE_STORAGE", "db") == "file":
        reviews = [review for review in storage.all(Review)
                   if review.place_id == self.id]

Review.place = relationship("Place", back_populates="reviews")
