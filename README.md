# fastapi-Users-Posts-App

## Introduction
This is a simple project to do CRUD operations based on a post created by users (social media API).


## Setup
To set up a development environment and run the code, follow these steps:

### 1. Clone the Repository
      git clone https://github.com/DvpLoki/FastAPI-User-Posts-App.git

### 2. Create a Virtual Environment (Optional but Recommended)
### On Windows
      python -m venv venv

### 3. Activate the Virtual Environment
### On Windows
      venv\Scripts\activate

### 4. Install Dependencies
      pip install -r requirements.txt

### 5. Run the Code
      uvicorn app.main:app 

## Docker
You can also run this FastAPI project using Docker. Follow these steps:
### 1. Pull the Docker Image
      docker pull lokeshdvp/fastapi:latest

### 2. Run the Docker Container
      docker run -d -p 80:80 lokeshdvp/fastapi:latest

## Environment variables

- *DB_URL* :database url (example: "postgresql://< user_name >:< password >@ < hostname >:5432/< DB_name >"  )
- *SECRET_key* :Master key for JWT
- *Token_Expire_Time_Min* : Time for access token expiration
- *Algorithm* : algorithm for JWT

## API link live on render.com
      https://fastapi-user-posts.onrender.com/

## live API interactive documentation (Swagger UI)
      https://fastapi-user-posts.onrender.com/docs


## User-Posts RESTAPI : simple social media API to do CRUD operations on posts created by users
- **Endpoints**: The following CRUD endpoints are available:
- **POSTS** :
  - `POST /posts`: Create a new post.
  - `GET /posts`: Retrieve all posts with pagination and filtering .
  - `GET /posts/{id}`: Retrieve a post by ID.
   - `GET /posts/latest`: Retrieve latest created posts.
  - `PUT /posts/{id}`: Update a post by ID.
  - `DELETE /posts/{id}`: Delete a post by ID.

  - **USERS** :
  - `POST /users/` : create a new user.
  - `GET /users/{id}` : retrieve user by id.

  - **LOGIN** :
  - `POST /login` : login endpoint for users.

- **Database**: PostgreSQL with SQLAlchemy ORM and Alembic database Migration.
- **User Authentication**: oAuth2 Authentication, dependency injection.
- **API authentication** : JWT based Authentication.
