#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    if models.storage_t != "db":
        @property
        def cities(self):
            """Returns the list of City objects linked to the current State"""
            city_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
