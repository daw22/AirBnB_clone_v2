#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = []
    if os.getenv('HBNB_TYPE_STORAGE', 'db') == 'db':
        cities = relationship('City', back_populates='state',
                              cascade='all, delete, delete-orphan')
    elif os.getenv('HBNB_TYPE_STORAGE', 'db') == 'file':
        cities = [city for city in storage.all(City) if city.state_id == self.id]


City.state = relationship('State', back_populates='cities')
