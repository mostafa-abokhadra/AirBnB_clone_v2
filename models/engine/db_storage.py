#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity
from os import getenv


class DBStorage:
    """ class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadate.drop_all(self.__engine)

    def all(self, cls=None):
        """
            return all objects depending of the
            class name or all classes
        """
        classes = []
        if cls is None:
            classes = [City, Place, State, User, Review, Amenity]
        #elif cls is str:
            #classes = [eval(cls)]
        else:
            classes = [cls]
        objects = {}
        for clas in classes:
            for obj in self.__session.query(clas).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """ add new object """
        self.__session.add(obj)

    def save(self):
        """save all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
