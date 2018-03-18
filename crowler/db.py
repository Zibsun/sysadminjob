from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

engine = create_engine('sqlite:///mybase.db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Hh_vacancy(Base):
    __tablename__ = 'hh_vacancy'
    id = Column(Integer, primary_key=True)
    salary_from = Column(String(10))
    salary_to = Column(String(10))
    currency = Column(String(10))
    gross = Column(String(10))
    name = Column(String(20))
    area_name = Column(String(10))
    responsibility = Column(Text)
    requirement = Column(Text)
    vacancy_id = Column(Integer, unique=True)
    employer_name = Column(String(20))
    employer_id = Column(String(20))
    vacancy = relationship('Vacancy', backref='details')

    def __init__(self, salary_from=None, salary_to=None, currency=None, gross=None, name=None, area_name=None, responsibility=None, requirement=None, vacancy_id=None, employer_id=None, employer_name=None):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.gross = gross
        self.name = name
        self.area_name = area_name
        self.responsibility = responsibility
        self.requirement = requirement
        self.employer_id = employer_id
        self.employer_name = employer_name
        self.vacancy_id = vacancy_id

    def __repr__(self):
        return '<User {} {}>'.format(self.employer_name, self.name)



class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    salary_from = Column(String(10))
    salary_to = Column(String(10))
    name = Column(String(20))
    responsibility = Column(Text)
    requirement = Column(Text)
    experience = Column(String(20))
    hh_id = Column(Integer, ForeignKey('hh_vacancy.id'))

    def __init__(self, salary_from=None, salary_to=None, name=None, responsibility=None, requirement=None, experience=None, hh_id=None):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.name = name
        self.responsibility = responsibility
        self.requirement = requirement
        self.experience = experience
        self.hh_id = hh_id
    def __repr__(self):
        return '<User {} {}>'.format(self.name, self.salary_from)

class Responsibility(Base):
    __tablename__ = 'responsibility'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(Text)

    def __init__(self,  description=None,name=None):
        self.description =  description
        self.name = name

    def __repr__(self):
        return '<User {} {}>'.format(self.name, self.description)

class Requirement(Base):
    __tablename__ = 'requirement'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(Text)

    def __init__(self,  description=None,name=None):
        self.description =  description
        self.name = name

    def __repr__(self):
        return '<User {} {}>'.format(self.name, self.description)

class Vacancy_responsibility(Base):
    __tablename__ = 'vacancy_responsibility'
    vacancy_id = Column(Integer, ForeignKey('hh_vacancy.id'),  primary_key=True)
    responsibility_id = Column(Integer, ForeignKey('responsibility.id'),  primary_key=True)


class Vacancy_requirement(Base):
    __tablename__ = 'vacancy_requirement'
    vacancy_id = Column(Integer, ForeignKey('hh_vacancy.id'), primary_key=True)
    requirement_id = Column(Integer, ForeignKey('requirement.id'),  primary_key=True)

class Сompanies(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)

    def __init__(self,  description=None,name=None):
        self.description =  description
        self.name = name

    def __repr__(self):
        return '<User {} {}>'.format(self.name, self.description)



if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)