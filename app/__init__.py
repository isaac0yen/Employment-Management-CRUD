from .database import engine
from .models import Base
from .database import create_tables

# Call the create_tables function to create tables when the app starts
create_tables()

Base.metadata.create_all(bind=engine)
