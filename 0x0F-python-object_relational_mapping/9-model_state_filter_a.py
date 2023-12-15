#!/usr/bin/python3
""" script for task 9 """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        username, passwd, host, port, db_name),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    my_local_session = Session()
    my_states = my_local_session.query(State).filter(
            State.name.op('regexp')('.*a+.*')).order_by(State.id)
    my_local_session.close()

    for state in my_states:
        print('{}: {}'.format(state.id, state.name))
