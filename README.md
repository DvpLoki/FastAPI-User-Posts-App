# fastapi-Users-Posts-App

## Introduction
This is a simple project to do CRUD operations based on a post created by users (social media API).



## Setup
To set up a development environment and run the code, follow these steps:

### 1. Clone the Repository
git clone [url]

### 2. Create a Virtual Environment (Optional but Recommended)
### On Windows
python -m venv venv

### 3. Activate the Virtual Environment
### On Windows
venv\Scripts\activate

### 4. Install Dependencies
pip install -r requirements.txt

### 5. Run the Code
### uvicorn app.main:app 


## Docker

You can also run this FastAPI project using Docker. Follow these steps:
### 1. Pull the Docker Image
docker pull lokeshdvp/fastapi:latest

### 2. Run the Docker Container
docker run -d -p 80:80 lokeshdvp/fastapi:latest


## app: simple social media API to do CRUD operations on posts created by users
- **Overview**: Version 3 plans to enhance the project with SQLAlchemy ORM and Alembic for data migrations.
- **Endpoints**: The following CRUD endpoints are available:
- **POSTS** :
  - `POST /posts`: Create a new post.
  - `GET /posts`: Retrieve all posts.
  - `GET /posts/{id}`: Retrieve a post by ID.
   - `GET /posts/latest`: Retrieve latest created posts.
  - `PUT /posts/{id}`: Update a post by ID.
  - `DELETE /posts/{id}`: Delete a post by ID.

  - **USERS** :
  - `POST /users/` : create a new user.
  - `GET /users/{id}` : retrieve user by id.

  - **LOGIN** :
  - `POST /login` : login endpoint for users.

- **Database Changes**: PostgreSQL database used for data storage.
- **User Authentication**: added (only logged in user can perform CRUD operations )
- **API authentication** : JWT based Authentication
### in order to run this  below Environment variables have to be created
- *DB_URL* :database url (example: "postgresql://<user>:<password>@<hostname>:5432/<DB_name>"  )
- *SECRET_key* :Master key for JWT
- *Token_Expire_Time_Min* : Time for access token expiration
- *Algorithm* : algorithm for JWT
