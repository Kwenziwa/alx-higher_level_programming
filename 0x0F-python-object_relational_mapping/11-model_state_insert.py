#!/usr/bin/python3
"""
    The script that adds the State object 'Louisiana' to hbtn_0e_6_usa
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

    # create the object and add it
    my_new_state = State(name='Louisiana')
    session.add(my_new_state)
    session.commit()

    # print the state.id
    add_state = session.query(State).filter(State.name == 'Louisiana').one()
    print(add_state.id)

    session.close()
