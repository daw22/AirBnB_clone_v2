#!/usr/bin/python3
"""
contains

classes:
    Place - Represents a real-life place (to be rented), mapped to the places 
    table in the database
"""
import os
from models import storage
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"), primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), primary_key=True))


class Place(BaseModel, Base):
    """
    Represents a place to be rented on the app, inherits from BaseModel.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if storage.__class__.__name__ == "DBStorage":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    elif storage.__class__.__name__ == "FileStorage":
        @property
        def reviews(self):
            """Getter property for the reviews attribute."""
            reviews = [review for review in storage.all(Review)
                       if review.place_id == self.id]


        @property
        def amenities(self):
            return (self.amenity_ids)

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenities.append(obj)
