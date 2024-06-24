#!/usr/bin/python3
"""has the states table model and the instance Base"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """This is class to model the states table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    state_id = Column(String, ForeignKey("states.id"),
                      nullable=False, unique=True)
    cities = relationship("State", backref="city")
