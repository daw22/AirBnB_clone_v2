#!/usr/bin/python
"""
Implements database storage
"""
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """Implementationof database storage."""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new instance."""
        conn = "mysql+mysqldb://{}:{}@{}/{}"
        conn = conn.format(environ.get('HBNB_MYSQL_USER'),
                           environ.get('HBNB_MYSQL_PWD'),
                           environ.get('HBNB_MYSQL_HOST'),
                           environ.get('HBNB_MYSQL_DB'))
        self.__engine = create_engine(conn, pool_pre_ping=True)
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Queries database."""
        objs = []
        if cls is not None:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(User, State, City, Review,
                                        Amenity, Place, Review)
        dct = {}
        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dct[key] = obj
        return (dct)

    def new(self, obj):
        """Adds a new obj to the database."""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an obj from the database."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database, and creates current database
        session."""
        from models.base_model import Base
        from models import base_model, user, state
        from models import city, amenity, place, review

        classes = {
            "BaseModel": base_model.BaseModel,
            "User": user.User,
            "State": state.State,
            "City": city.City,
            "Amenity": amenity.Amenity,
            "Place": place.Place,
            "Review": review.Review
        }
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                      expire_on_commit=False))
