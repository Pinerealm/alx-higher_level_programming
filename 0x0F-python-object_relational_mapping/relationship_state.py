#!/usr/bin/python3
"""This module defines the State class for the hbtn_0e_14_usa database
accessible via SQLAlchemy"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """This class inherits from Base and links to the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
