# FastAPI Task Manager

## Project Overview

This is a simple Task Manager built for a technical evaluation using FastAPI. It supports user authentication and task management with filtering and pagination.

---

## Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic v2 + pydantic-settings
* JWT (python-jose)
* passlib[bcrypt]
* HTML/CSS/Vanilla JS
* pytest

---

## Folder Structure

```text
task-manager/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── config.py
│   └── routers/
│       ├── __init__.py
│       ├── users.py
│       └── tasks.py
├── frontend/
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_main.py
├── .env.example
├── .gitignore
├── Dockerfile
├── render.yaml
├── requirements.txt
└── README.md
```

---

## Setup Instructions

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

copy .env.example .env

uvicorn backend.main:app --reload
```

Open:

* http://localhost:8000/docs
* http://localhost:8000/

---

## Environment Variables

| Variable                    | Description    |
| --------------------------- | -------------- |
| SECRET_KEY                  | JWT secret key |
| ALGORITHM                   | HS256          |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiry   |
| DATABASE_URL                | DB connection  |

---

## API Endpoints

| Method | Path        | Auth | Description   |
| ------ | ----------- | ---- | ------------- |
| POST   | /register   | ❌    | Register user |
| POST   | /login      | ❌    | Login         |
| POST   | /tasks      | ✅    | Create task   |
| GET    | /tasks      | ✅    | List tasks    |
| GET    | /tasks/{id} | ✅    | Get task      |
| PUT    | /tasks/{id} | ✅    | Update task   |
| DELETE | /tasks/{id} | ✅    | Delete task   |

---

## Authentication

All protected routes require:

Authorization: Bearer <access_token>

---

## Example

```bash
POST /login

Response:
{
  "access_token": "...",
  "token_type": "bearer"
}
```

---

## Run Tests

```bash
pytest tests/
```

---

## Deployment

* Deploy on Render
* Start command:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

After deploy:

* https://your-url.onrender.com/
* https://your-url.onrender.com/docs

---

## How to Test

1. Register user
2. Login
3. Click Authorize in /docs
4. Create task
5. Mark complete
6. Delete task

---

## Notes

* `.env` is NOT committed
* `.env.example` is included
* Uses JWT authentication
* Users can only access their own tasks
