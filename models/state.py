#!/usr/bin/python3
"""
contains

classes:
    State - Inherits from BaseModel, represents a real-life state, mapped to the
    states table in the database
"""
import os
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


strg = os.getenv('HBNB_TYPE_STORAGE', "file")


class State(BaseModel, Base):
    """
    Represents a real-life state.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = None
    if strg == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """
            Getter for the cities attribute when using file storage
            """
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]

        @cities.setter
        def cities(self, obj):
            self.cities = None
