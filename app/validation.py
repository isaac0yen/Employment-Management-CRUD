from pydantic import ValidationError
from .schemas import EmployeeCreate, EmployeeUpdate

def validate_employee_create(employee_data):
    try:
        return EmployeeCreate(**employee_data)
    except ValidationError as e:
        return None, e.errors()

def validate_employee_update(employee_data):
    try:
        return EmployeeUpdate(**employee_data)
    except ValidationError as e:
        return None, e.errors()
