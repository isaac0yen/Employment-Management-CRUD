from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, validation
from app.database import SessionLocal, engine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Employee)
def create_employee(employee_data: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, **employee_data.dict())

@router.get("/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee_data: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    employee = crud.update_employee(db, employee_id, **employee_data.dict())
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.delete("/{employee_id}", response_model=schemas.Employee)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.get("/", response_model=list[schemas.Employee])
def list_employees(db: Session = Depends(get_db)):
    return crud.list_employees(db)

@router.get("/search/", response_model=list[schemas.Employee])
def search_employees(position: str, salary: int, db: Session = Depends(get_db)):
    return crud.search_employees(db, position, salary)
