#!/usr/bin/python3
""" sdfsdfsdf asdf """
import models
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base, BaseModel
import sqlalchemy
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """ eklfnb fdsfkj  """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        url_conect = "{}+{}://{}:{}@{}:3306/{}".format(
            "mysql",
            "mysqldb",
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB
        )

        self.__engine = create_engine(url_conect, pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.MetaData.drop_all(self.__engine)

    def all(self, cls=None):
        """ asdfdsfsdfasdz """
        new_dict = {}
        if cls is None:
            for clas in self.__session.query(BaseModel,
                                             User, Place,
                                             State, City,
                                             Amenity,
                                             Review).all():
                clave = "{}.{}".format(type(clas).__name__, clas.id)
                new_dict[clave] = clas
        else:
            for clas in self.__session.query(cls).all():
                clave = "{}.{}".format(type(clas).__name__, clas.id)
                new_dict[clave] = clas

        return new_dict

    def new(self, obj):
        """ NEASDFas """
        self.__session.add(obj)

    def save(self):
        """ NEASDFas """
        self.__session.commit()

    def delete(self, obj=None):
        """ NEASDFas """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ NEASDFas """
        Base.metadata.create_all(self.__engine)
        setion = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(setion)
        self.__session = Session

    def close(self):
        """closes the current SQLAlchemy session"""
        self.__session.close()
