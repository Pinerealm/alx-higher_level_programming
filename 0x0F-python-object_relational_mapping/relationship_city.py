#!/usr/bin/python3
"""This module defines the City class for the hbtn_0e_14_usa database
accessible via SQLAlchemy"""


#!/usr/bin/python3
"""This module defines the City class for the hbtn_0e_14_usa database
accessible via SQLAlchemy"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """This class inherits from Base and links to the cities table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
