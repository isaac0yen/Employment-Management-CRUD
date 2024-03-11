# Employment Management CRUD App

The Employment Management CRUD App is a web application built with FastAPI that allows users to perform CRUD (Create, Read, Update, Delete) operations on employee records. It provides an intuitive interface for managing employee information efficiently.

## Installation

To run the Employment Management CRUD App locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/isaac0yen/Employment-Management-CRUD.git
   ```

2. Navigate to the project directory:

   ```
   cd Employment-Management-CRUD-App
   ```

3. Set up a virtual environment:

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Run the FastAPI server:

   ```
   uvicorn main:app --reload
   ```

7. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore available endpoints and interact with the API.

## Usage

The Employment Management CRUD App provides the following API endpoints for managing employee records:

- **Create**: POST `/employees/`
- **Read**: GET `/employees/{employee_id}`
- **Update**: PUT `/employees/{employee_id}`
- **Delete**: DELETE `/employees/{employee_id}`
- **List**: GET `/employees/`
- **Search**: GET `/employees/?position={position}&salary={salary}`

## Documentation

The API documentation is automatically generated using OpenAPI and JSON Schema. You can access the documentation by navigating to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) when the server is running. It includes information about request/response formats, required fields, and example requests.

## Sample Requests

Here are some sample requests to demonstrate how to interact with the API:

1. **Create Employee**:

   ```http
   POST /employees/
   Content-Type: application/json

   {
       "name": "John Doe",
       "position": "Software Engineer",
       "date_joined": "2022-01-01",
       "salary": 50000
   }
   ```

2. **Read Employee**:

   ```http
   GET /employees/1
   ```

3. **Update Employee**:

   ```http
   PUT /employees/1
   Content-Type: application/json

   {
       "name": "Jane Smith",
       "position": "Senior Software Engineer",
       "date_joined": "2021-06-15",
       "salary": 60000
   }
   ```

4. **Delete Employee**:

   ```http
   DELETE /employees/1
   ```

5. **List Employees**:

   ```http
   GET /employees/
   ```

6. **Search Employees**:

   ```http
   GET /employees/?position=Software%20Engineer&salary=50000
   ```

## Dependencies

The Employment Management CRUD App relies on the following dependencies:

- FastAPI
- SQLAlchemy
- Uvicorn
- psycopg2-binary (for PostgreSQL support)
- Other dependencies specified in `requirements.txt`

## Contributing

Contributions to the Employment Management CRUD App are welcome! If you encounter any issues, have feature requests, or want to contribute enhancements, please open an issue or submit a pull request on GitHub.
