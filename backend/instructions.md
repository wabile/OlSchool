# FastAPI Project Structure

This document describes the project structure for a FastAPI application integrated with a frontend using JavaScript Fetch API.

## Student

- `schema.py`: Defines the schema or data validation models for student-related data.
- `model.py`: Contains the database models for students.
- `controlor.py`: Implements the business logic and operations related to students.
- `router.py`: Defines the API endpoints for student operations.
- `crud.py`: Includes the CRUD (Create, Read, Update, Delete) operations for students.

## Instructor

- `schema.py`: Defines the schema or data validation models for instructor-related data.
- `model.py`: Contains the database models for instructors.
- `controlor.py`: Implements the business logic and operations related to instructors.
- `router.py`: Defines the API endpoints for instructor operations.
- `crud.py`: Includes the CRUD operations for instructors.

## Auth

- `schema.py`: Defines the schema or data validation models for authentication-related data.
- `model.py`: Contains the database models for authentication.
- `router.py`: Defines the API endpoints for authentication.

## Database

- `db.py`: Handles database connections and operations.

## Integration with Frontend

The FastAPI backend is integrated with the frontend using JavaScript Fetch API. This allows the frontend to make HTTP requests to the backend API endpoints and retrieve or send data.

To run the FastAPI application, follow these steps:

1. Make sure you have Python installed on your system.
2. Create a virtual environment for the project (optional but recommended).
```shell
cd backend/
python -m venv venv
source venv/bin/activate
```
3. Install the required dependencies using the following command:
```shell
pip install -r requirements.txt
```
4. Set up the database connection and configuration in the `db.py` file.
5. Run the FastAPI application using the following command:
```shell
uvicorn main:app --reload
```
6. The FastAPI application will be running at `http://localhost:8000`.
7. Access the frontend application in a web browser by opening the corresponding HTML file.

Ensure that you have the necessary environment variables and configurations set up for the application to run successfully.
