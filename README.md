# Stay Connected

## Overview

Stay Connected is a Q&A platform inspired by StackOverflow, built using Django and Django Rest Framework. The application allows users to create, answer, and interact with questions across various topics.

## Features

### User Management
- User registration and authentication
- JWT-based token authentication
- User profiles with avatars
- Leaderboard ranking system based on user contributions

### Question and Answer System
- Create, read and delete questions
- Post answers to questions
- Tag-based question organization
- Marking correct answers
- User rating system based on answer quality

## Technology Stack

- Backend: Django 5.1.1
- Database: PostgreSQL
- Authentication: Django Simple JWT
- API Documentation: drf-spectacular
- CORS Handling: django-cors-headers

## Project Structure

### Apps
- `user`: Handles user authentication, profiles, and avatars
- `posts`: Manages questions, answers, and tags

### Key Models
#### User App
- `User`: Custom user model with email-based authentication
- `Avatar`: Predefined user avatar options

#### Posts App
- `Question`: Represents user-created questions
- `Answer`: Answers to questions
- `Tag`: Categorization for questions

## Local Development Setup

### Prerequisites
- Python 3.10+
- PostgreSQL
- pip

### Installation Steps

1. Clone the repository
```bash
git https://github.com/TBC-CrossLab-Group-15/stayConnected-Backend.git
cd stayConnected-Backend
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

## API Documentation

The project uses drf-spectacular to generate OpenAPI (Swagger) documentation. 

- Access Swagger UI: `http://localhost:8000/api/swagger`
- Access ReDoc: `http://localhost:8000/api/schema/redoc/`

## Authentication Workflow

1. Register a new user via `/api/user/register/`
2. Obtain JWT tokens via `/api/user/login/`
3. Use the access token in the Authorization header for authenticated requests
   - Format: `Authorization: Bearer <access_token>`

## Key Endpoints

### User
- `POST /api/user/register/`: User registration
- `POST /api/user/login/`: User login
- `POST /api/user/logout/`: User logout
- `GET /api/user/leaderboard/`: User leaderboard
- `GET /api/user/currentuser/`: Current user profile
- `GET /api/user/avatars/`: List available avatars
- `GET /api/user/currentuserquestions/`: Current user's questions

### Questions
- `GET /api/posts/questions/`: List questions
- `POST /api/posts/questions/`: Create a new question
- `GET /api/posts/search/`: Search questions by tag
- `GET /api/posts/search/question/`: Search questions by title and text

### Answers
- `POST /api/posts/answers/`: Create an answer
- `PUT /api/posts/answers/{id}/`: Update an answer

### Tags
- `GET /api/posts/tags/`: List available tags

## Tokens
- `POST /api/user/token/refresh/`: Refresh access token
