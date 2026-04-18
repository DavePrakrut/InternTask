# 🚀 FastAPI Task Manager

## 📌 Project Overview

This is a simple Task Manager web application built for a technical evaluation using FastAPI. It supports user authentication and task management with filtering and pagination.

The application allows users to:

* Register and login using JWT authentication
* Create, view, update, and delete tasks
* Filter tasks (completed/pending)
* Paginate task results
* Access only their own tasks

---

## 🛠 Tech Stack

* FastAPI
* SQLAlchemy
* SQLite (default)
* Pydantic v2 + pydantic-settings
* python-jose (JWT)
* passlib[bcrypt]
* HTML/CSS/Vanilla JavaScript
* pytest

---

## 📂 Folder Structure

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

## 🚀 Live Demo

* 🌐 Frontend: https://interntask-2i4l.onrender.com/
* 📘 API Docs: https://interntask-2i4l.onrender.com/docs

---

## ⚙️ Local Setup Instructions

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

copy .env.example .env   # Windows
# cp .env.example .env   # macOS/Linux

uvicorn backend.main:app --reload
```

Open:

* http://localhost:8000/docs
* http://localhost:8000/

---

## 🔑 Environment Variables

| Variable                    | Description       | Example                     |
| --------------------------- | ----------------- | --------------------------- |
| SECRET_KEY                  | JWT secret key    | your-secret-key             |
| ALGORITHM                   | JWT algorithm     | HS256                       |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiry time | 30                          |
| DATABASE_URL                | Database URL      | sqlite:///./task_manager.db |

---

## 📡 API Endpoints

| Method | Path        | Auth | Description                                 |
| ------ | ----------- | ---- | ------------------------------------------- |
| POST   | /register   | ❌    | Register user                               |
| POST   | /login      | ❌    | Login user                                  |
| POST   | /tasks      | ✅    | Create task                                 |
| GET    | /tasks      | ✅    | Get tasks (supports filtering & pagination) |
| GET    | /tasks/{id} | ✅    | Get single task                             |
| PUT    | /tasks/{id} | ✅    | Update task                                 |
| DELETE | /tasks/{id} | ✅    | Delete task                                 |

---

## 🔐 Authentication

All protected routes require:

Authorization: Bearer <access_token>

---

## 📦 Example

```bash
POST /login

Response:
{
  "access_token": "your_token_here",
  "token_type": "bearer"
}
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 🌐 Deployment (Render)

1. Push project to a public GitHub repository
2. Create a new Web Service on Render
3. Connect your repository
4. Ensure start command:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

5. Add environment variables in Render:

* SECRET_KEY
* ALGORITHM=HS256
* ACCESS_TOKEN_EXPIRE_MINUTES=30
* DATABASE_URL=sqlite:///./task_manager.db

6. Deploy and verify:

* https://interntask-2i4l.onrender.com/
* https://interntask-2i4l.onrender.com/docs

---

## 🧪 How to Test (Evaluator Quick Flow)

### Using UI:

1. Open https://interntask-2i4l.onrender.com/
2. Register a new user
3. Login
4. Add a task
5. Mark it as completed
6. Delete the task

### Using API Docs:

1. Open https://interntask-2i4l.onrender.com/docs
2. Register → Login → copy token
3. Click **Authorize 🔒**
4. Paste token
5. Test `/tasks` endpoints

---

## 🔒 Security Notes

* Passwords are hashed using bcrypt
* JWT tokens are used for authentication
* Users can only access their own tasks
* `.env` file is NOT committed
* `.env.example` is provided

---

## ✅ Submission Checklist

* ✔ Public GitHub repository
* ✔ Live deployment link
* ✔ Working frontend and backend
* ✔ `/docs` accessible
* ✔ `.env` not committed
* ✔ `.env.example` included
* ✔ `requirements.txt` included
* ✔ Dockerfile included

---

## 📌 Notes

* UI is intentionally simple but functional
* Focus is on backend correctness and API behavior
* Fully aligned with evaluation requirements

---

## 🌟 Live Application

👉 https://interntask-2i4l.onrender.com/
