def test_register_new_user(client):
    response = client.post(
        "/register",
        json={"username": "alice", "email": "alice@example.com", "password": "Secret@123"},
    )
    assert response.status_code == 201


def test_duplicate_user_registration(client):
    payload = {"username": "bob", "email": "bob@example.com", "password": "Secret@123"}
    first = client.post("/register", json=payload)
    second = client.post("/register", json=payload)
    assert first.status_code == 201
    assert second.status_code == 400


def test_register_weak_password_rejected(client):
    response = client.post(
        "/register",
        json={"username": "weak", "email": "weak@example.com", "password": "weakpass1"},
    )
    assert response.status_code == 400


def test_login_correct_credentials_returns_token(client):
    payload = {
        "username": "charlie",
        "email": "charlie@example.com",
        "password": "Secret@123",
    }
    client.post("/register", json=payload)
    response = client.post(
        "/login", json={"identifier": payload["username"], "password": payload["password"]}
    )
    assert response.status_code == 200
    body = response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_login_with_email_returns_token(client):
    payload = {
        "username": "charlie2",
        "email": "charlie2@example.com",
        "password": "Secret@123",
    }
    client.post("/register", json=payload)
    response = client.post(
        "/login", json={"identifier": payload["email"], "password": payload["password"]}
    )
    assert response.status_code == 200
    body = response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_login_wrong_credentials(client):
    payload = {
        "username": "dave",
        "email": "dave@example.com",
        "password": "Secret@123",
    }
    client.post("/register", json=payload)
    response = client.post("/login", json={"identifier": "dave", "password": "wrongpass"})
    assert response.status_code == 401


def test_create_task(client, auth_headers):
    response = client.post(
        "/tasks",
        json={"title": "Write tests", "description": "Cover all endpoints"},
        headers=auth_headers,
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Write tests"


def test_get_tasks_list_pagination(client, auth_headers):
    client.post("/tasks", json={"title": "Task 1", "description": "First"}, headers=auth_headers)
    client.post("/tasks", json={"title": "Task 2", "description": "Second"}, headers=auth_headers)

    response = client.get("/tasks?skip=1&limit=1", headers=auth_headers)
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1


def test_get_tasks_returns_all_by_default(client, auth_headers):
    for i in range(11):
        client.post(
            "/tasks",
            json={"title": f"Task {i}", "description": "Bulk"},
            headers=auth_headers,
        )

    response = client.get("/tasks", headers=auth_headers)
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 11


def test_get_tasks_filter_completed(client, auth_headers):
    completed_task = client.post(
        "/tasks",
        json={"title": "Done", "description": "completed task"},
        headers=auth_headers,
    ).json()
    client.put(
        f"/tasks/{completed_task['id']}",
        json={"completed": True},
        headers=auth_headers,
    )

    client.post(
        "/tasks",
        json={"title": "Pending", "description": "pending task"},
        headers=auth_headers,
    )

    response = client.get("/tasks?completed=true", headers=auth_headers)
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["completed"] is True


def test_mark_task_completed_put_works(client, auth_headers):
    create_response = client.post(
        "/tasks", json={"title": "Complete me", "description": "Pending"}, headers=auth_headers
    )
    task_id = create_response.json()["id"]

    update_response = client.put(f"/tasks/{task_id}", json={"completed": True}, headers=auth_headers)
    assert update_response.status_code == 200
    assert update_response.json()["completed"] is True


def test_delete_task_returns_204(client, auth_headers):
    create_response = client.post(
        "/tasks", json={"title": "Delete me", "description": "Temporary"}, headers=auth_headers
    )
    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}", headers=auth_headers)
    assert delete_response.status_code == 204


def test_get_specific_task_by_id(client, auth_headers):
    create_response = client.post(
        "/tasks", json={"title": "Specific task", "description": "Find me"}, headers=auth_headers
    )
    task_id = create_response.json()["id"]

    get_response = client.get(f"/tasks/{task_id}", headers=auth_headers)
    assert get_response.status_code == 200
    body = get_response.json()
    assert body["id"] == task_id
    assert body["title"] == "Specific task"


def test_user_cannot_view_another_users_task(client):
    user_one = {
        "username": "owner_user",
        "email": "owner@example.com",
        "password": "Secret@123",
    }
    user_two = {
        "username": "intruder_user",
        "email": "intruder@example.com",
        "password": "Secret@123",
    }

    client.post("/register", json=user_one)
    client.post("/register", json=user_two)

    owner_login = client.post(
        "/login", json={"identifier": user_one["username"], "password": user_one["password"]}
    )
    intruder_login = client.post(
        "/login", json={"identifier": user_two["username"], "password": user_two["password"]}
    )

    owner_headers = {"Authorization": f"Bearer {owner_login.json()['access_token']}"}
    intruder_headers = {"Authorization": f"Bearer {intruder_login.json()['access_token']}"}

    created_task = client.post(
        "/tasks",
        json={"title": "Private task", "description": "Owner only"},
        headers=owner_headers,
    )
    task_id = created_task.json()["id"]

    intruder_get = client.get(f"/tasks/{task_id}", headers=intruder_headers)
    intruder_update = client.put(
        f"/tasks/{task_id}", json={"completed": True}, headers=intruder_headers
    )
    intruder_delete = client.delete(f"/tasks/{task_id}", headers=intruder_headers)

    assert intruder_get.status_code == 404
    assert intruder_update.status_code == 404
    assert intruder_delete.status_code == 404