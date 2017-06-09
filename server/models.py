from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    func,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import backref, relationship

from database import Base


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey("departments.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))

    department = relationship(
        Department,
        backref=backref(
            "employees",
            uselist=True,
            cascade="delete,all",
        ),
    )

    role = relationship(
        Role,
        backref=backref(
            "roles",
            uselist=True,
            cascade="delete,all",
        ),
    )


class Pokemon(Base):
    __tablename__ = "pokemons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Numeric)
    type = Column(String)
    url = Column(String)
