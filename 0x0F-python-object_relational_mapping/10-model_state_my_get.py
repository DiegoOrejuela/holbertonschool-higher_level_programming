#!/usr/bin/python3
"""
9-model_state_filter.py | Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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

    st = session.query(State).filter(State.name == sys.argv[4]).one_or_none()
    if st:
        print(st.id)
    else:
        print("Not found")

    session.close()
