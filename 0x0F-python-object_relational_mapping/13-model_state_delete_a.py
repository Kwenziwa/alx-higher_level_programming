#!/usr/bin/python3
"""
    The script that deletes all State objects from hbtn_0e_6_usa that conatin
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    my_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=my_engine)
    Base.metadata.create_all(my_engine)

    # start session
    session = Session()

    # extract states with a in them
    my_states = session.query(State).filter(State.name.ilike('%a%')).all()

    # delete states
    for state in my_states:
        session.delete(state)

    session.commit()

    session.close()
