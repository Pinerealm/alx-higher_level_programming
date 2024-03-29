#!/usr/bin/python3
"""Lists all City objects from the database, hbtn_0e_101_usa
"""


from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for city in session.query(City).order_by(City.id):
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))
