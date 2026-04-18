# FastAPI Task Manager

## Project Overview
This project is a production-ready Task Manager web application built with FastAPI, SQLAlchemy, JWT authentication, and a Vanilla JavaScript frontend.

The app supports:
- User registration and login
- JWT-based protected routes
- Task creation, listing, filtering, pagination, update, and deletion
- Per-user task isolation (users can only access their own tasks)
- Automated tests using pytest
- Deployment configuration for Render

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite (default)
- Pydantic v2 + pydantic-settings
- python-jose (JWT)
- passlib[bcrypt]
- pytest + TestClient
- HTML/CSS/Vanilla JavaScript frontend

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
│       ├── init.py
│       ├── users.py
│       └── tasks.py
├── frontend/
│   └── index.html
├── tests/
│   ├── init.py
│   ├── conftest.py
│   └── test_main.py
├── .env.example
├── .gitignore
├── Dockerfile
├── render.yaml
├── requirements.txt
└── README.md
```

## Local Setup Instructions
1. Clone repository:
```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
```bash
copy .env.example .env
```
Then update values in `.env`.

5. Run the server:
```bash
uvicorn backend.main:app --reload
```

6. Open:
- API docs: `http://localhost:8000/docs`
- Frontend: `http://localhost:8000/`

## Environment Variables
| Variable | Required | Description | Example |
|---|---|---|---|
| `DATABASE_URL` | Yes | Database connection URL. SQLite by default. | `sqlite:///./task_manager.db` |
| `JWT_SECRET_KEY` | Yes | Secret key used to sign JWT tokens. Use a long random value. | `your_super_secure_secret` |
| `JWT_ALGORITHM` | Yes | JWT signing algorithm. | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Yes | Access token expiry in minutes. | `60` |

## Running Tests
```bash
pytest tests/
```

## API Endpoints
| Method | Path | Auth Required | Description |
|---|---|---|---|
| POST | `/register` | No | Register a new user |
| POST | `/login` | No | Login and get JWT token |
| POST | `/tasks` | Yes | Create a new task |
| GET | `/tasks` | Yes | List user tasks with optional filtering/pagination |
| GET | `/tasks/{id}` | Yes | Get one task by ID |
| PUT | `/tasks/{id}` | Yes | Partially update task (including completion) |
| DELETE | `/tasks/{id}` | Yes | Delete task |

## Render Deployment Instructions
1. Push this project to a public GitHub repository.
2. Create a new Web Service on Render.
3. Connect your GitHub repository.
4. Render auto-detects `render.yaml`; confirm service settings.
5. Ensure Start Command is:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```
6. Add environment variables in Render:
- `DATABASE_URL=sqlite:///./task_manager.db`
- `JWT_SECRET_KEY=<your-production-secret>`
- `JWT_ALGORITHM=HS256`
- `ACCESS_TOKEN_EXPIRE_MINUTES=60`
7. Deploy and verify:
- `https://your-render-url.onrender.com/docs`
- `https://your-render-url.onrender.com/`

## Docker
Build and run locally:
```bash
docker build -t task-manager .
docker run -p 8000:8000 --env-file .env task-manager
```

## Live Demo
Replace with your deployed URL:
- `https://your-live-demo-link`

## Mandatory Submission Checklist
- Public GitHub repository link
- Live deployment link (Render/Railway/Vercel)
- Accessible frontend and backend from the hosted link
- Accessible docs at `/docs`
- `.env` is not committed
- `.env.example` is included
- `requirements.txt` is included
- `Dockerfile` is included

## Rubric Compliance Notes
- Authentication: implemented with JWT + bcrypt hashing
- Task API: create, list, get-by-id, update, delete
- Authorization: users can only access their own tasks
- Pagination: `GET /tasks?skip=...&limit=...`
- Filtering: `GET /tasks?completed=true`
- Tests: pytest coverage for auth + tasks + ownership checks
- Frontend: responsive UI with auth/task actions integrated
- Structure: separated `backend/` and `frontend/` folders

## Deployment (Step-by-Step)
1. Push project to a public GitHub repository.
2. Confirm secrets are not committed:
	- Keep `.env` local only.
	- Keep `.env.example` in repository.
3. In Render, create a new Blueprint deployment and connect your repo.
4. Render will read `render.yaml`; keep these commands:
	- Build: `pip install -r requirements.txt`
	- Start: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5. Set environment variables in Render:
	- `JWT_SECRET_KEY` (required, secure random value)
	- `JWT_ALGORITHM=HS256`
	- `ACCESS_TOKEN_EXPIRE_MINUTES=60`
	- `DATABASE_URL`:
	  - Demo: `sqlite:///./task_manager.db`
	  - Preferred: Render Postgres URL
6. Deploy and wait for the service to become healthy.
7. Verify hosted app:
	- `<your-live-url>/`
	- `<your-live-url>/docs`
8. Run this functional check on the live app:
	- Register user
	- Login
	- Create task
	- Mark task completed
	- Delete task
9. Update this README section with your final live URL before submission.