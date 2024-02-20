#!/usr/bin/python3
""" Module for states select """
from sqlalchemy import create_engine, MetaData, Integer, \
        String, Column, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    name = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]
    engform = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(name, pd, db)
    engine = create_engine(engform)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    cities = session.query(State.name, City.id, City.name).join(State).all()
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
    session.commit()
