# ============================================================================
#   Section 11.4 : Requetes HTTP avec requests
#   Description : Utilisation de la bibliotheque requests - GET, POST, PUT,
#                 DELETE, parametres, headers, sessions, timeouts, erreurs
#   Fichier source : 04-requetes-http-requests.md
# ============================================================================

"""Requetes HTTP avec la bibliotheque requests.

Un serveur FastAPI local est demarre pour les tests.
"""

import threading
import time
import requests
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- Serveur FastAPI local pour les tests ---

api = FastAPI()
users_db: list[dict] = [
    {"id": 1, "username": "alice", "email": "alice@test.com"},
    {"id": 2, "username": "bob", "email": "bob@test.com"},
]


class UserCreate(BaseModel):
    username: str
    email: str


class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None


@api.get("/users")
def get_users(limit: int = 10, sort: str = "id"):
    return users_db[:limit]


@api.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouve")
    return user


@api.post("/users", status_code=201)
def create_user(user: UserCreate):
    new_user = {"id": len(users_db) + 1, **user.model_dump()}
    users_db.append(new_user)
    return new_user


@api.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    existing = next((u for u in users_db if u["id"] == user_id), None)
    if not existing:
        raise HTTPException(status_code=404, detail="Utilisateur non trouve")
    if user.username:
        existing["username"] = user.username
    if user.email:
        existing["email"] = user.email
    return existing


@api.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users_db
    before = len(users_db)
    users_db = [u for u in users_db if u["id"] != user_id]
    if len(users_db) == before:
        raise HTTPException(status_code=404, detail="Utilisateur non trouve")
    return {"message": f"Utilisateur {user_id} supprime"}


@api.get("/slow")
def slow_endpoint():
    time.sleep(5)
    return {"message": "Reponse lente"}


@api.get("/echo-headers")
def echo_headers(request_obj=None):
    from starlette.requests import Request
    from fastapi import Request as FRequest
    # Access via dependency
    return {"note": "headers echoes"}


# --- Demarrer le serveur en arriere-plan ---
def start_server():
    uvicorn.run(api, host="127.0.0.1", port=9999, log_level="error")


if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    time.sleep(1)  # Attendre que le serveur demarre

    BASE = "http://127.0.0.1:9999"

    # === GET : Recuperer des donnees ===
    print("=== GET /users ===")
    response = requests.get(f"{BASE}/users")
    print(f"  Status: {response.status_code}")
    print(f"  JSON: {response.json()}")
    print(f"  Content-Type: {response.headers['content-type']}")
    print(f"  Temps: {response.elapsed.total_seconds():.3f}s")

    # === GET avec parametres ===
    print("\n=== GET /users?limit=1&sort=name ===")
    params = {"limit": 1, "sort": "name"}
    response = requests.get(f"{BASE}/users", params=params)
    print(f"  URL: {response.url}")
    print(f"  JSON: {response.json()}")

    # === GET un utilisateur specifique ===
    print("\n=== GET /users/1 ===")
    response = requests.get(f"{BASE}/users/1")
    print(f"  {response.status_code}: {response.json()}")

    # === GET utilisateur inexistant ===
    print("\n=== GET /users/999 (404) ===")
    response = requests.get(f"{BASE}/users/999")
    print(f"  {response.status_code}: {response.json()}")

    # === Verifier le succes ===
    print("\n=== Verification du succes ===")
    response = requests.get(f"{BASE}/users/1")
    print(f"  response.ok = {response.ok}")
    print(f"  status_code = {response.status_code}")

    response = requests.get(f"{BASE}/users/999")
    print(f"  response.ok = {response.ok} (404)")

    # === raise_for_status ===
    print("\n=== raise_for_status ===")
    try:
        response = requests.get(f"{BASE}/users/999")
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"  HTTPError: {e.response.status_code}")

    # === POST : Creer une ressource ===
    print("\n=== POST /users ===")
    data = {"username": "charlie", "email": "charlie@test.com"}
    response = requests.post(f"{BASE}/users", json=data)
    print(f"  {response.status_code}: {response.json()}")

    # === PUT : Mettre a jour ===
    print("\n=== PUT /users/1 ===")
    update = {"username": "alice_updated", "email": "alice.new@test.com"}
    response = requests.put(f"{BASE}/users/1", json=update)
    print(f"  {response.status_code}: {response.json()}")

    # === DELETE ===
    print("\n=== DELETE /users/2 ===")
    response = requests.delete(f"{BASE}/users/2")
    print(f"  {response.status_code}: {response.json()}")

    # === Verifier apres modifications ===
    print("\n=== GET /users (apres modifications) ===")
    response = requests.get(f"{BASE}/users")
    for u in response.json():
        print(f"  id={u['id']}, username={u['username']}")

    # === Headers personnalises ===
    print("\n=== Headers personnalises ===")
    headers = {
        "User-Agent": "Mon Application Python/1.0",
        "Accept": "application/json",
        "X-Custom-Header": "valeur-test"
    }
    response = requests.get(f"{BASE}/users", headers=headers)
    print(f"  Status: {response.status_code}")
    print(f"  Request headers envoyes: User-Agent, Accept, X-Custom-Header")

    # === Session (partage headers/cookies) ===
    print("\n=== Session requests ===")
    with requests.Session() as session:
        session.headers.update({
            "User-Agent": "Session App/1.0",
            "Accept": "application/json"
        })
        r1 = session.get(f"{BASE}/users")
        r2 = session.get(f"{BASE}/users/1")
        print(f"  Requete 1: {r1.status_code}, {len(r1.json())} users")
        print(f"  Requete 2: {r2.status_code}, user={r2.json()['username']}")

    # === Timeout ===
    print("\n=== Timeout ===")
    try:
        response = requests.get(f"{BASE}/slow", timeout=1)
    except requests.exceptions.ReadTimeout:
        print("  Timeout: la requete a pris trop de temps (> 1s)")

    # === Gestion complete des erreurs ===
    print("\n=== Gestion des erreurs ===")

    def fetch_data(url):
        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print(f"  Timeout pour {url}")
        except requests.exceptions.ConnectionError:
            print(f"  Connexion impossible pour {url}")
        except requests.exceptions.HTTPError as e:
            print(f"  Erreur HTTP {e.response.status_code} pour {url}")
        except requests.exceptions.RequestException as e:
            print(f"  Erreur: {e}")
        return None

    data = fetch_data(f"{BASE}/users")
    print(f"  Succes: {len(data)} utilisateurs")

    fetch_data(f"{BASE}/users/999")  # 404
    fetch_data("http://127.0.0.1:1")  # connexion impossible

    # === Proprietes de la reponse ===
    print("\n=== Proprietes de Response ===")
    response = requests.get(f"{BASE}/users/1")
    print(f"  status_code: {response.status_code}")
    print(f"  ok: {response.ok}")
    print(f"  url: {response.url}")
    print(f"  encoding: {response.encoding}")
    print(f"  elapsed: {response.elapsed.total_seconds():.3f}s")
    print(f"  headers['content-type']: {response.headers['content-type']}")
