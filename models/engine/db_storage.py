#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Implementationof the database storage engine

"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker


class DBStorage():
    """
    Implementation of the database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a DBStorage instance."""
        conn = "mysql+mysqldb://{}:{}@{}/{}"
        conn = conn.format(os.getenv("HBNB_MYSQL_USER"),
                           os.getenv("HBNB_MYSQL_PWD"),
                           os.getenv("HBNB_MYSQL_HOST"),
                           os.getenv("HBNB_MYSQL_DB"))
        self.__engine = create_engine(conn, pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            self.drop_all_tables()

    def all(self, cls=None):
        """Queries the database for and returns instances of a given class
        or all records/instances if a class is not given

        Args:
            cls: The class whose instances are returned

        Returns:
            dict: A dictionary whose values are instances of given class
        """
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User


        classes = [Amenity, City, Place, Review, State, User]

        objs = []
        if cls is not None:
            objs = self.__session.query(cls).all()
        else:
            for cls in classes:
                objs.extend(self.__session.query(cls).all())
        dct = {}
        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dct[key] = obj
        return (dct)

    def new(self, obj):
        """Adds a new object to the current session to possibly be committed
        to the database

        Args:
            obj: The object to be added
        """
        self.__session.add(obj)

    def save(self):
        """Commits changes to the database."""
        self.__session.commit()

    def delete(self, obj):
        """Removes an object from a current session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and creates current session."""
        from models.amenity import Amenity
        from models.base_model import Base
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User


        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

        Base.metadata.create_all(bind=self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def drop_all_tables(self):
        """Drops all tables in existing in the session."""
        Base = declarative_base()
        Base.metadata.drop_all(bind=self.__engine)
