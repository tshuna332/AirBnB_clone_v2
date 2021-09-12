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
            cities_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if self.id == city.state_id:
                    cities_list.append(city)
            return cities_list
