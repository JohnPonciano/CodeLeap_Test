
# CodeLeap project

Project required the creation of a CRUD in Python using Django Rest Framework.

I made some improvements, such as in the POST /careers where the username was required to create the 'Job', it is not necessary, since I implemented an Auth TOKEN so it already knows who the user is by TOKEN.

Let's Go!


## Installation
Clone Repository
```bash
   git clone 
   cd backend
```
Config virtual env
```bash 
    python -m venv venv
    source venv/bin/activate 
```
Install requirements
```bash 
    pip install -r requirements.txt
```
Start Migration
```bash
    python manage.py migrate
```

Execute server
```bash
    python3 manage.py runserver
```
## API Reference
## Endpoints

### Authentication

- **Login:**
  - Endpoint: `/login/`
  - Method: POST
  - Parameters:
    - `username`: User's username.
    - `password`: User's password.
  - Example Usage:
    ```bash
    curl --location 'http://localhost:8000/api/login/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "username": "your_username",
      "password": "your_password"
    }'
    ```

- **Register:**
  - Endpoint: `/register/`
  - Method: POST
  - Parameters:
    - `username`: User's username.
    - `password`: User's password.
  - Example Usage:
    ```bash
    curl --location 'http://localhost:8000/api/register/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "username": "new_user",
      "password": "new_password"
    }'
    ```

### Careers

- **List and Create Careers:**
  - Endpoint: `/careers/`
  - Methods: GET (public) and POST (requires authentication)
  - Parameters (for POST):
    - `title`: Career title.
    - `content`: Career content.
  - Example Usage (POST):
    ```bash
    curl --location 'http://localhost:8000/careers/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Token your_token_here' \
    --data-raw '{
      "title": "Career Title",
      "content": "Career Content"
    }'
    ```

- **View, Update, and Delete Careers:**
  - Endpoint: `/careers/{id}/`
  - Methods: GET (public), PATCH, and DELETE (requires authentication)
  - Example Usage (PATCH):
    ```bash
    curl --location 'http://localhost:8000/careers/1/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Token your_token_here' \
    --data-raw '{
      "title": "New Title"
      "content": "New Content"
    }'
    ```.
