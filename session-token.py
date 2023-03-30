import os

import requests

BASE_URL = "https://superset-pilotage.cleverapps.io"


session = requests.session()

jwt_token = session.post(
    url=f"{BASE_URL}/api/v1/security/login",
    json={
        "username": "admin",
        "password": os.getenv("SUPERSET_ADMIN_PASSWORD"),
        "refresh": False,
        "provider": "db",
    },
).json()["access_token"]
print(f"{jwt_token=}")

csrf_token = session.get(
    url=f"{BASE_URL}/api/v1/security/csrf_token/",
    headers={
        "Authorization": f"Bearer {jwt_token}",
    },
).json()["result"]

print(f"{csrf_token=}")

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwt_token}",
    "X-CSRFToken": csrf_token,
}
print(f"{headers=}")

response = session.post(
    f"{BASE_URL}/api/v1/security/guest_token/",
    json={
        "user": {"username": "embedder", "first_name": "embedder", "last_name": "embedder"},
        "resources": [
            {"type": "dashboard", "id": "b5f13922-14b8-43fe-991a-221785eef7d4"}
        ],
        "rls": [
            {"dataset": 26, "clause": "region = 'Bretagne'"}
        ],
    },
    headers=headers,
)

print(response.json())


session.close()
