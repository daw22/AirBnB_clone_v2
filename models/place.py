#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models import storage
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), primary_key=True))


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
    amenities = None
    if os.getenv("HBNB_TYPE_STORAGE", "db") == "db":
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    elif os.getenv("HBNB_TYPE_STORAGE", "db") == "file":
        reviews = [review for review in storage.all(Review)
                   if review.place_id == self.id]

        @amenities.getter
        def amenities(self):
            return [amenity for amenity in storage.all(Amenity)
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            if type(amenity) is Amenity:
                self.amenity_ids.append(amenity.id)


Review.place = relationship("Place", back_populates="reviews")
