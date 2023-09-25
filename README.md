# CRUD Application

This is a FastAPI CRUD (Create, Read, Update, Delete) application that provides a RESTful API for managing user data

## Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.

### Setting up a development environment

#### Step 1: Clone the repository

```bash
https://github.com/Benedicta-Asare/crud.git
```

#### Step 2: Create a virtual environment

```bash
python -m venv venv
```

```bash
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### Step 3: Installing Dependencies

```
pip install -r requirements.txt
```

#### Step 4: Run the Application

```
uvicorn app.main:app --reload
```

### API Documentation
Interactive API documentation is available using Swagger UI

Swagger UI: http://localhost:8000/docs

### Usage

#### *Create a User*

- Endpoint: `POST /api/`
- Request:

```json
{
  "name": "Benedicta"
}
```
- Response: The created user

```json
{
  "name": "Benedicta",
  "id": 1
}
```

#### *Get a User*

- Endpoint: `GET /api/{user_id}`
- Request: None
- Response: The user with the specified ID.
```json
{
  "name": "Benedicta",
  "id": 1
}
```

#### Update a User
- Endpoint: `PUT /api/{user_id}`
- Request:
```json
{
  "name": "Bene"
}
```
- Response: The updated user.
```json
{
  "name": "Bene",
  "id": 1
}
```

#### Delete a User
- Endpoint: `DELETE /api/{user_id}`
- Request: None
- Response: A message confirming the deletion
```json
{
  "message": "User with ID 2 deleted successfully"
}
```

### Models
- User:
- - `id` (int): The unique identifier for the user.
- - `name` (str): The name of the user. 

### Testing 
>  You can test the API using tools like Postman or by sending HTTP requests to the specified endpoints.

### Structure