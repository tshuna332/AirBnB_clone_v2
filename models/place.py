#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

if (models.storage_used == "db"):
    place_amenity = Table('place_amenity', Base.metadata, Column('place_id', String(60), ForeignKey('places.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True), Column('amenity_id', String(60), ForeignKey('amenities.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if (models.storage_used == "db"):
        reviews = relationship("Review", backref="place")
        reviews = relationship("Amenity", secondary="place_amenity", backref="place_amenities", viewonly=False)
    else:
        amenity_ids = []
        
        @property
        def reviews(self):
            """ asd asd """
            new_dict = []
            for key, value in storage.all:
                if (self.id == value.id):
                  new_dict[key] = value
            return (new_dict)

        @property
        def amenities(self):
            """ asd asd """
            new_dict = []
            for key, value in storage.all:
                if (self.id == value.id):
                  new_dict[key] = value
            return (new_dict)
