from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Binary, Integer
from sqlalchemy import Sequence

# engine = create_engine('sqlite:///dojo_database.db')
Base = declarative_base()

class People(Base):
    """
    
    """
    __tablename__ = 'people'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    person_id = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    person_type = Column(String)
    wants_accommodation = Column(String)
    proom_name = Column(String)
    lroom_name = Column(String)

class Rooms(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    room_name = Column(String)
    members = Column(String)
    max_num = Column(String)
    room_type = Column(String)


class Lists(Base):
    __tablename__ = 'lists'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    list_name = Column(String)
    list_string = Column(String)

#Base.metadata.create_all(engine)
