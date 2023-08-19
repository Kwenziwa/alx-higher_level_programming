#!/usr/bin/python3
"""
    The script that prints all City objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City
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

    # extract all my_scities in a state
    my_scities = session.query(State, City) \
                    .filter(State.id == City.state_id)

    # print all states

    for city in my_scities:
        print(f"{city.State.name}: ({city.City.id}) {city.City.name}")

    session.close()
