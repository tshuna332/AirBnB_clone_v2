#!/usr/bin/python3
""" City Module for HBNB project """

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, relationship, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if (models.storage_used == "db"):
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        name = ""
        state_id = ""
