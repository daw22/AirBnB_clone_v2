#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key in kwargs.keys():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        new_datetime = datetime.fromisoformat(kwargs[key])
                        self.__dict__[key] = new_datetime
                    else:
                        self.__dict__[key] = kwargs[key]
            if self.id is None:
                self.id = str(uuid.uuid4())
            if self.created_at is None:
                self.created_at = datetime.now()
            if self.updated_at is None:
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = self.__class__.__name__
        dct = self.to_dict()
        dct.pop('__class__')
        return "[{}] ({}) {}".format(cls_name, self.id, dct)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           self.__class__.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get('_sa_instance_state') is not None:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes instance from storage"""
        storage.delete(self)
