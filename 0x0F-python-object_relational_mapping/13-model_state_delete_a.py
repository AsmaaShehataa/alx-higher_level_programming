"""delete the States with A letter form the database"""

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
    states = my_local_session.query(State).filter(
        State.name.op('regexp')('.*a+.*'))  # get all states that contains  "A"

    for state in states:
        my_local_session.delete(state)
    my_local_session.commit()

    my_local_session.close()
    engine.dispose()
