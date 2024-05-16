#!/usr/bin/python3
"""
contains

classes:
    BaseModel - A base class to be inherited by the other models/classes of the
                project
"""
import uuid
from datetime import datetime
from models import storage
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BaseModel:
    """
    Base class for other class to inherit from.
    """
    # Inherited attributes to be mapped to a table
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a newly created instance of the class.

        Args:
            args: tuple of positional arguments.
            kwargs: dictionary of keyword/named arguments.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key in kwargs.keys():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        new_datetime = datetime.fromisoformat(kwargs[key])
                        self.__dict__[key] = new_datetime
                    else:
                        self.__dict__[key] = kwargs[key]

    def __str__(self):
        """
        Returns an informal representation of an instance.
        """
        class_name = self.__class__.__name__
        dct = self.__dict__.copy()
        if dct.get("_sa_instance_state") is not None:
            del dct["_sa_instance_state"]
        return "[{}] ({}) {}".format(class_name, self.id, dct)

    def save(self):
        """
        Updates the updated_at attribute of an instance to the current time.
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all necessary attributes of an instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        if obj_dict.get("_sa_instance_state") is not None:
            del obj_dict["_sa_instance_state"]
        return (obj_dict)

    def delete(self):
        """
        Deletes instance from the storage
        """
        storage.delete(self)
