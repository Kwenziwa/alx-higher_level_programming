#!/usr/bin/python3
"""
    The script that prints the State object with the name passed as an argument
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
    my_state_data = session.query(State) \
                    .filter(State.name == sys.argv[4]).one_or_none()

    # print the state.id
    if my_state_data is None:
        print("Not found")
    else:
        print(my_state_data.id)

    session.close()
