#!/usr/bin/python3
"""
14-model_state_delete.py | prints all City objects from the database
hbtn_0e_14_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    records = session.query(State.name, City.id, City.name)\
                     .select_from(State)\
                     .join(City)\
                     .order_by(City.id)\
                     .all()

    for row in records:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
