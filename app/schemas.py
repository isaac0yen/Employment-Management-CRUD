from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    name: str
    position: str
    date_joined: date
    salary: int

class EmployeeUpdate(BaseModel):
    name: str
    position: str
    date_joined: date
    salary: int

class Employee(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True
