from fastapi import FastAPI
from app.routes import employees

app = FastAPI()

app.include_router(employees.router, prefix="/employees", tags=["employees"])
