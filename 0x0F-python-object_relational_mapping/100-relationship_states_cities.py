#!/usr/bin/python3
"""
    0x0F. Python - Object-relational mapping - task 15. City relationship
"""
if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City

    if len(argv) != 4:
        exit('Use: 100-relationship_states_cities.py <mysql username> '
             '<mysql password> <database name>')

    my_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(my_engine)
    Base.metadata.create_all(my_engine)  # creates decprecated warning 1681

    my_state = State(name='California')
    my_city = City(name='San Francisco', state_id=my_state.id)
    my_state.cities.append(my_city)
    session.add_all([my_state, my_city])
    session.commit()
    session.close()
