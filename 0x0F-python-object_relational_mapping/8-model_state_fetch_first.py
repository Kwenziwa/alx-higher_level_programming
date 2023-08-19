#!/usr/bin/python3
"""
    The script that returns the first State object from hbtn_0e_6_usa
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
    my_data = session.query(State).order_by(State.id).first()

    # print state
    if my_data is None:
        print("Nothing")
    else:
        print("{}: {}".format(my_data.id, my_data.name))

    session.close()
