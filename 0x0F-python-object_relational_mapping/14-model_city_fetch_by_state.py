#!/usr/bin/python3
"""Print the states table"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    states = session.query(State, City).order_by(City.id).join(State).all()
    for state, city in states:
        print("{}: ({}){}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
