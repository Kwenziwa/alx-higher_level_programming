#!/usr/bin/python3
"""
    The script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    my_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=my_engine)
    Base.metadata.create_all(my_engine)

    # start session
    session = Session()

    # extract all states
    my_data = session.query(State).order_by(State.id).all()

    # print all states
    for state in my_data:
        print(f"{state.id}: {state.name}")

    session.close()
