#!/usr/bin/python3
""" create a table schema """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """ state class for state table"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
