from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position = Column(String)
    date_joined = Column(Date)
    salary = Column(Integer)
