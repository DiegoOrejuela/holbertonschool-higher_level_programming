#!/usr/bin/python3
"""
8-model_state_fetch_first.py | cript that prints the first State object from
the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    if len(session.query(State).all()) == 0:
        print("Nothing")
    else:
        state = session.query(State).order_by(State.id).first()
        print("{}: {}".format(state.id, state.name))
    session.close()
