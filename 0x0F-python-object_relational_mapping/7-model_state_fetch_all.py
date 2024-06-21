#!/usr/bin/python3
"""print the states table"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        "root", "root", "hbtn_0e_0_usa"), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    # HERE: no SQL query, only objects!
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
