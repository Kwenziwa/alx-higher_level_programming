#!/usr/bin/python3
"""
    0x0F. Python - Object-relational mapping - task 16. List relationship
"""

if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City

    if len(argv) != 4:
        exit('Use: 101-relationship_states_cities_list.py <mysql username> '
             '<mysql password> <database name>')

    my_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(my_engine)
    Base.metadata.create_all(my_engine)  # creates decprecated warning 1681

    for my_state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(my_state.id, my_state.name))
        for my_city in my_state.cities:
            print("\t{}: {}".format(my_city.id, my_city.name))
    session.close()
