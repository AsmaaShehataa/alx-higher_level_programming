#!/usr/bin/python3
"""update the State object “Louisiana” to "New Mexico" the database"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    my_local_session = Session()
    state = my_local_session.query(State).filter(State.id == 2).first()
    State.name = 'New Mexico'
    my_local_session.commit()

    my_local_session.close()
    engine.dispose()
