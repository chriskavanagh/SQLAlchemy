# database_sqlalchemy.py
# 3rd commit


import sqlite3, sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# map classes to tables through Base Class
Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    

# create engine for Session connection
engine = create_engine('sqlite:///database_sqlalchemy.db')

# create all tables in engine ('CREATE TABLE' in raw SQL)
Base.metadata.create_all(engine)

# create configured 'Session' class
Session = sessionmaker(bind=engine)

# create session
session = Session()


class Data:
    '''Gather User Data'''

    def get_data(self):
        self.name = raw_input("What's The Name? ")
        self.age = input("What's The Age? ")

    def add_data(self):
        new_person = Test(name=self.name, age=self.age)
        session.add(new_person)
        session.commit()


if __name__ == '__main__':
    person = Data()
    person.get_data()
    person.add_data()
    print("User: %s added. . ." % person.name)
        
    
    more_users = 'y'
    while more_users == 'y':
        more_users = raw_input("Would You Like To Add Another User? ")
        if more_users == 'n':
            print("Goodbye")
            break
        person = Data()
        person.get_data()
        person.add_data()        
        
    session.close()
