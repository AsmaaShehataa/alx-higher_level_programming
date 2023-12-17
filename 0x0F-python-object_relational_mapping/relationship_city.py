#!/usr/bin/python3
"""
Creation of City class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State

Base = declarative_base()


class City(Base):
    """
    this Class City is an instance of Base class
    Linked to MySQL table "city"
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
