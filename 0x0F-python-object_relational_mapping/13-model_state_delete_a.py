#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from
the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in (session.query(State)).all():
        if "a" in state.name:
            session.delete(state)
    session.commit()
    session.close()
