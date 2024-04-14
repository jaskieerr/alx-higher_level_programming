#!/usr/bin/python3
'''prints state passed as arg '''

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    st_name = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            st_name = True
            break
    if st_name is False:
        print("Not found")
