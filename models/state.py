#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, relationship, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class State(BaseModel, Base):
    """ State class """
    if (models.storage_used == "db"):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
