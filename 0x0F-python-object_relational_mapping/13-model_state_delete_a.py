#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a
from the database, hbtn_0e_6_usa, using SQLAlchemy"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for state in session.query(State).filter(State.name.like('%a%')):
            session.delete(state)
        session.commit()
