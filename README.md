# JWT Authentication with Django REST Framework

## Description

This is a simple JWT Authentication system built using Django Rest Framework (DRF) and django-rest-framework-simplejwt. It provides secure registration, login, logout, and token refreshing for your applications.

## Key Features

- **User Registration**: Register new users with email, first name, last name and phone number.
- **JWT Authentication**: Secure authentication using **Access Tokens** and **Refresh Tokens**. Access tokens are short-lived, and refresh tokens allow for seamless access renewal.
- **Login**: Login users with email and password to obtain access and refresh tokens.
- **Logout**: Secure logout that blacklists the refresh token to invalidate the user session.
- **Token Refresh**: Refresh access tokens using a valid refresh token.
- **User Profile**: Retrieve the authenticated user's profile information from the `accounts/me/` endpoint.

## Technologies Used

- **Django**
- **Django REST Framework (DRF)** for API development
- **Python**

## API Endpoints

| Method | Endpoint                       | Description                                     |
|--------|--------------------------------|------------------------------------------------ |
| `POST` | `/accounts/register/`          | Register a new user.                            |
| `POST` | `/accounts/login/`             | Login a user and get access and refresh tokens. |
| `POST` | `/accounts/refresh/`           | Refresh an access token using a refresh token.  |
| `POST` | `/accounts/logout/`            | Logout a user by blacklisting the refresh token.|
| `GET`  | `/accounts/me/`                | Get the authenticated user's profile details.   |

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yousefi653/auth-api.git
cd auth-api/
```

### 2. Install Dependencies

Create a virtual environment and install the required dependencies.

# Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

# Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Database

Run database migrations:
```bash
python manage.py migrate
```
### 4. Create a Superuser 

If you'd like to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

Now you can run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 to start testing the API.

# Example Requests and Responses
### 1. Register

- **Request**:
```bash
POST /accounts/register/
{
  "email": "yousef.gh653@gmail.com",
  "first_name": "Yousef",
  "last_name": "Ghasemi",
  "phone": "1234567890",
  "password": "password123",
  "password2": "password123"
}
```

- **Response**:
```bash
{
  "message": "User registered successfully",
  "user": {
    "email": "yousef.gh653@gmail.com",
    "first_name": "Yousef",
    "last_name": "Ghasemi"
  }
}
```
### 2. Login

- **Request**:
```bash
POST /accounts/login/
{
  "email": "yousef.gh653@gmail.com",
  "password": "password123"
}
```

- **Response**:
```bash
{
  "access": "<access_token>",
  "refresh": "<refresh_token>",
  "user": {
    "email": "yousef.gh653@gmail.com",
    "first_name": "Yousef",
    "last_name": "Ghasemi"
  }
}
```
### 3. Logout

- **Request**:
```bash
POST /accounts/logout/
{
  "refresh": "<refresh_token>"
}
```

- **Response**:
```bash
{
  "message": "Logout successfully!"
}
```
### 4. Get User Profile (Authenticated User)

- **Request**:

GET /accounts/me/


- **Response**:
```bash
{
  "email": "yousef.gh653@gmail.com",
  "first_name": "Yousef",
  "last_name": "Ghasemi",
  "phone": "1234567890"
}
```

## Author

***Yousef Ghasemi***
