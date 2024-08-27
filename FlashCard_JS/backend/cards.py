from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Cards(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key = True)

    topic = Column(String)
    question = Column(String)
    answer = Column(String)
    last = Column(String)
    score = Column(Integer)