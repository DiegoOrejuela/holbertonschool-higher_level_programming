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

    list_states = session.query(State, City)\
                         .select_from(State)\
                         .join(City).order_by(State.id.asc(),
                                              City.id.asc()).all()
    if list_states:
        last_state = list_states[0][0]
        print("{}: {}".format(list_states[0][0].id, list_states[0][0].name))
    for each_state in list_states:
        if not each_state[0] is last_state:
            print("{}: {}".format(each_state[0].id, each_state[0].name))
        last_state = each_state[0]
        print("    {}: {}".format(each_state[1].id, each_state[1].name))

    session.close()
