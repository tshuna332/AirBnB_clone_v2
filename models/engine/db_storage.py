#!/usr/bin/python3
"""  """
import models
from sqlalchemy import create_engine, URL
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
    
    __engine = None
    __session = None

    def __init__(self):
        """  """
        print("ARMANDO")
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        driver = 'mysql+mysqldb'
        self.url = URL(driver, HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, '3306', HBNB_MYSQL_DB)

        self.__engine = create_engine(self.url, pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.MetaData.drop_all(self.__engine)

    def all(self, cls=None):
        """  """
        new_dict = {}

        if cls not in self.classes:
            
            return

        obj = self.classes[cls]
        print(obj)
        result = self.__engine.execute("SELECT * FROM " + obj.__table__)
        for row in result:
            print("username:", row['username'])



    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        setion = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(setion)
        self.__session = Session
