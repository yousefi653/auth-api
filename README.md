# JWT Authentication API

A REST API for user registration and authentication built with **Python**, **Django**, and **Django REST Framework**. It uses JWT access and refresh tokens through `djangorestframework-simplejwt`.

## Features

- User registration with email, first name, last name, and phone number
- Login with email and password
- JWT access and refresh token issuance
- Refreshing access tokens
- Logout by blacklisting a refresh token
- Retrieving the authenticated user's profile

## Tech Stack

- Python
- Django
- Django REST Framework
- djangorestframework-simplejwt

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/accounts/register/` | Register a new user |
| `POST` | `/accounts/login/` | Authenticate and receive tokens |
| `POST` | `/accounts/refresh/` | Refresh an access token |
| `POST` | `/accounts/logout/` | Blacklist a refresh token |
| `GET` | `/accounts/me/` | Retrieve the authenticated user's profile |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yousefi653/auth-api.git
cd auth-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Example Requests

### Register

```http
POST /accounts/register/
Content-Type: application/json
```

```json
{
  "email": "user@example.com",
  "first_name": "Jane",
  "last_name": "Doe",
  "phone": "09120000000",
  "password": "change-this-password",
  "password2": "change-this-password"
}
```

### Login

```http
POST /accounts/login/
Content-Type: application/json
```

```json
{
  "email": "user@example.com",
  "password": "change-this-password"
}
```

### Refresh Token

```http
POST /accounts/refresh/
Content-Type: application/json
```

```json
{
  "refresh": "<refresh_token>"
}
```

### Logout

```http
POST /accounts/logout/
Content-Type: application/json
```

```json
{
  "refresh": "<refresh_token>"
}
```

### Retrieve Current User

```http
GET /accounts/me/
Authorization: Bearer <access_token>
```

## Notes

- Replace the example credentials with your own test values.
- This project is intended as a learning and portfolio project. Review the implementation and deployment settings before using it in a production environment.

## License

No license is specified yet.
