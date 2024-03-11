from sqlalchemy.orm import Session
from . import models
from datetime import date

def create_employee(db: Session, name: str, position: str, date_joined: date, salary: int):
    new_employee = models.Employee(name=name, position=position, date_joined=date_joined, salary=salary)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, name: str, position: str, date_joined: date, salary: int):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee:
        employee.name = name
        employee.position = position
        employee.date_joined = date_joined
        employee.salary = salary
        db.commit()
        db.refresh(employee)
    return employee

def delete_employee(db: Session, employee_id: int):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
    return employee

def list_employees(db: Session):
    return db.query(models.Employee).all()

def search_employees(db: Session, position: str, salary: int):
    return db.query(models.Employee).filter(models.Employee.position == position, models.Employee.salary == salary).all()
