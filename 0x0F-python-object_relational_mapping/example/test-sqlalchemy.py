from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "hbtn_0e_0_usa"), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()