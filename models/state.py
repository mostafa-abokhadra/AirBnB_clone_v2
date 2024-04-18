#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            """Get all cities"""
            city_instances = models.storage.all(City)
            return [city for city in city_instances.values()
                    if city.state_id == self.id]
