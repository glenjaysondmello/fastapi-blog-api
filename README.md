# FastAPI Blog Application

## Overview
This project is a **FastAPI-based Blog Application** that provides user authentication, blog creation, retrieval, update, and deletion functionalities. It implements JWT authentication and uses SQLAlchemy as the ORM with a SQLite database.

## Features
- **User Authentication**: Secure user authentication using JWT tokens.
- **Password Hashing**: Utilizes `bcrypt` for hashing passwords.
- **Blog Management**: Users can create, retrieve, update, and delete blogs.
- **User Management**: Users can be created and retrieved along with their associated blogs.
- **Database Integration**: Uses SQLAlchemy ORM with SQLite.
- **Dependency Injection**: Utilizes FastAPI's dependency injection system.

## Technologies Used
- **FastAPI**: High-performance Python web framework.
- **SQLAlchemy**: ORM for database interactions.
- **JWT (JSON Web Token)**: Token-based authentication.
- **Passlib**: Secure password hashing.
- **Pydantic**: Data validation and serialization.
- **SQLite**: Lightweight database for persistence.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/glenjaysondmello/fastapi-blog-api.git
   cd fastapi-blog
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Apply database migrations:
   ```bash
   python -m main
   ```
   This will create the `blog.db` file in the root directory.

2. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

3. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/docs
   ```
   This will open the interactive API documentation (Swagger UI).

## API Endpoints

### Authentication
- **`POST /login/`** - User login and JWT token generation.

### User Management
- **`POST /user/`** - Create a new user.
- **`GET /user/`** - Retrieve all users with their blogs.
- **`GET /user/{id}`** - Retrieve a specific user by ID.

### Blog Management
- **`POST /blog/`** - Create a new blog (authentication required).
- **`GET /blog/`** - Retrieve all blogs (authentication required).
- **`GET /blog/{id}`** - Retrieve a specific blog by ID (authentication required).
- **`PUT /blog/{id}`** - Update a blog by ID (authentication required).
- **`DELETE /blog/{id}`** - Delete a blog by ID (authentication required).

## Project Structure
```
fastapi-blog/
│-- main.py            # Entry point of the application
│-- database.py        # Database connection and session management
│-- models.py          # SQLAlchemy models for User and Blog
│-- schemas.py         # Pydantic models for request/response validation
│-- hashing.py         # Password hashing functions
│-- JWTtoken.py        # JWT token generation and validation
│-- routers/           # API route handlers
│   ├── blog.py        # Blog-related endpoints
│   ├── user.py        # User-related endpoints
│   ├── auth.py        # Authentication endpoints
│-- repositories/      # Business logic functions
│   ├── blog.py        # Blog repository functions
│   ├── user.py        # User repository functions
│   ├── auth.py        # Authentication repository functions
│-- requirements.txt   # Project dependencies
```

## Security Measures
- Passwords are hashed using **bcrypt** before storing in the database.
- JWT tokens are used for authentication and include expiration times.
- FastAPI's **OAuth2PasswordBearer** is used for secure authentication.

## Future Enhancements
- Implement refresh tokens for better authentication handling.
- Add role-based access control (RBAC) for users.
- Extend support for PostgreSQL/MySQL.
- Add frontend integration using React or Vue.js.

## License
This project is licensed under the MIT License. Feel free to modify and use it for your own purposes.

