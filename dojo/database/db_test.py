from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Binary, Integer
from sqlalchemy import Sequence

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                      self.name, self.fullname, self.password)

session.add_all([
User(name='wendy', fullname='Wendy Williams', password='foobar'),
User(name='mary', fullname='Mary Contrary', password='xxg527'),
User(name='fred', fullname='Fred Flinstone', password='blah')])
