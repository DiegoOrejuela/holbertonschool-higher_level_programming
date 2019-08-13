#!/usr/bin/python3
"""
14-model_state_delete.py | prints all City objects from the database
hbtn_0e_14_usa.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    list_states = session.query(State).order_by(State.id.asc()).all()

    for each_state in list_states:
        print("{}: {}".format(each_state.id, each_state.name))
        for cities in each_state.cities:
            print("    {}: {}".format(cities.id, cities.name))

    session.close()
