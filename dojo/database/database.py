from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Binary, Integer

engine = create_engine('sqlite:///dojo_state.db')
Base = declarative_base()

class DojoDatabase(Base):
    __tablename__ = 'dojo_state'
    id = Column(Integer, primary_key = True)
    state_name = Column(String)
    state_file = Column(Binary)

Base.metadata.create_all(engine)
