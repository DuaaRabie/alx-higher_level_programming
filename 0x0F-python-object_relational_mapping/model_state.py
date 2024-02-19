#!/usr/bin/python3
""" Module for states select """
from sqlalchemy import create_engine, MetaData, Integer, String, \
            Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = "states"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql://username:password@localhost/dbname')

Base.metadata.create_all(engine)
