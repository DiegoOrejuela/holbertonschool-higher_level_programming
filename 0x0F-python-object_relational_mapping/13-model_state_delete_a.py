#!/usr/bin/python3
"""
13-model_state_delete.py | deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
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

    object_delete = session.query(State).filter(State.name.like("%a%")).all()

    for record in object_delete:
        session.delete(record)
    session.commit()
    session.close()
