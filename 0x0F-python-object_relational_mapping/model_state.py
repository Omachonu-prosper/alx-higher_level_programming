#!/usr/bin/python3
"""contains the class definition of a State and an instance
Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

Base = declarative_base()


class State(Base):
    """User class representing the users table
    """
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name
