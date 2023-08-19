#!/usr/bin/python3
"""
    The script that lists all State objects from hbtn_0e_6_usa that conatin
    the letter a from teh database.
    Username, password and dbname wil be passed as arguments to the script.
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

    # pull first state
    my_state_data = session.query(State).filter(State.name.ilike('%a%')) \
                    .order_by(State.id).all()

    # print my_state_data
    for state in my_state_data:
        print(f"{state.id}: {state.name}")

    session.close()
