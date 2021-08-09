#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)    
    if (models.storage_used == "db"):
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            new_dict = []
            for key, value in storage.all:
                if (self.id == value.id):
                  new_dict[key] = value
            return (new_dict)
