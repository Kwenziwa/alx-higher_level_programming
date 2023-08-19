#!/usr/bin/python3
"""
    The script that changes teh name of a State object in hbtn_0e_6_usa
    name of State where id = 2 to New Mexico
    Username, password, dbname will be passed as arguments to the script.
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

    # fetch row to change
    update_sate = session.query(State) \
                          .filter(State.id == 2).first()
    update_sate.name = 'New Mexico'
    session.commit()

    session.close()
