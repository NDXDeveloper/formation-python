# ============================================================================
#   Section 11.2.3 : Endpoints asynchrones et performances
#   Description : Programmation asynchrone avec FastAPI - async/await,
#                 asyncio.gather, background tasks, middleware timing,
#                 timeouts, semaphore
#   Fichier source : 02.3-endpoints-asynchrones.md
# ============================================================================

"""Endpoints asynchrones et performances avec FastAPI."""

from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.testclient import TestClient
import asyncio
import time

app = FastAPI()

# --- Cache simple en memoire ---
cache = {}

# --- Middleware de timing ---
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(round(process_time, 4))
    return response


# --- Endpoint synchrone ---
@app.get("/sync")
def endpoint_sync():
    return {"message": "Hello World (sync)"}


# --- Endpoint asynchrone ---
@app.get("/async")
async def endpoint_async():
    return {"message": "Hello World (async)"}


# --- Simulation d'operations async ---
@app.get("/utilisateur/{id}")
async def lire_utilisateur(id: int):
    await asyncio.sleep(0.1)  # Simule requete DB
    return {"id": id, "nom": f"Utilisateur {id}"}


# --- asyncio.gather : operations paralleles ---
@app.get("/multi-fetch")
async def recuperer_multiple():
    async def fetch_data(id: int):
        await asyncio.sleep(0.1)
        return {"id": id, "data": f"Donnees {id}"}

    resultats = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
        fetch_data(4),
        fetch_data(5)
    )
    return list(resultats)


# --- Calcul intensif (synchrone, pas async) ---
@app.get("/calcul")
def calculer_fibonacci(n: int):
    def fib(x):
        if x <= 1:
            return x
        return fib(x - 1) + fib(x - 2)
    return {"n": n, "resultat": fib(n)}


# --- Timeout ---
@app.get("/avec-timeout")
async def endpoint_avec_timeout():
    async def operation_longue():
        await asyncio.sleep(10)
        return {"data": "Termine"}

    try:
        resultat = await asyncio.wait_for(
            operation_longue(),
            timeout=0.5
        )
        return resultat
    except asyncio.TimeoutError:
        return {"erreur": "L'operation a pris trop de temps"}


# --- Semaphore : limiter la concurrence ---
@app.get("/avec-limite")
async def avec_limite():
    semaphore = asyncio.Semaphore(3)

    async def fetch_with_limit(id: int):
        async with semaphore:
            await asyncio.sleep(0.05)
            return {"id": id}

    resultats = await asyncio.gather(*[fetch_with_limit(i) for i in range(10)])
    return list(resultats)


# --- Background tasks ---
taches_effectuees: list[str] = []


def envoyer_email(destinataire: str):
    taches_effectuees.append(f"Email envoye a {destinataire}")


@app.post("/inscription")
async def inscription(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(envoyer_email, email)
    return {"message": "Inscription reussie, email en cours d'envoi"}


@app.get("/taches")
def voir_taches():
    return {"taches": taches_effectuees}


# --- Cache simple ---
@app.get("/meteo/{ville}")
async def obtenir_meteo(ville: str):
    if ville in cache:
        return {"source": "cache", "ville": ville, "temperature": cache[ville]}

    await asyncio.sleep(0.1)  # Simule appel API
    temperature = len(ville) * 3 + 10  # Temperature fictive
    cache[ville] = temperature

    return {"source": "api", "ville": ville, "temperature": temperature}


@app.delete("/cache")
async def vider_cache():
    cache.clear()
    return {"message": "Cache vide avec succes"}


# --- Tests ---
if __name__ == "__main__":
    client = TestClient(app)

    print("=== Endpoint synchrone ===")
    r = client.get("/sync")
    print(f"  {r.status_code}: {r.json()}")
    print(f"  X-Process-Time: {r.headers.get('X-Process-Time')}s")

    print("\n=== Endpoint asynchrone ===")
    r = client.get("/async")
    print(f"  {r.status_code}: {r.json()}")

    print("\n=== Utilisateur async (simule DB) ===")
    r = client.get("/utilisateur/42")
    print(f"  {r.status_code}: {r.json()}")

    print("\n=== Multi-fetch (asyncio.gather) ===")
    r = client.get("/multi-fetch")
    data = r.json()
    print(f"  {r.status_code}: {len(data)} resultats")
    for item in data:
        print(f"    {item}")

    print("\n=== Calcul Fibonacci (synchrone CPU) ===")
    r = client.get("/calcul?n=10")
    print(f"  {r.status_code}: fib(10) = {r.json()['resultat']}")

    print("\n=== Timeout (0.5s pour operation de 10s) ===")
    r = client.get("/avec-timeout")
    print(f"  {r.status_code}: {r.json()}")

    print("\n=== Semaphore (10 taches, max 3 simultanees) ===")
    r = client.get("/avec-limite")
    data = r.json()
    print(f"  {r.status_code}: {len(data)} resultats")

    print("\n=== Background tasks ===")
    r = client.post("/inscription?email=alice@test.com")
    print(f"  POST inscription: {r.json()}")
    r = client.get("/taches")
    print(f"  Taches effectuees: {r.json()}")

    print("\n=== Cache meteo ===")
    r = client.get("/meteo/Paris")
    print(f"  1er appel Paris: {r.json()}")
    r = client.get("/meteo/Paris")
    print(f"  2eme appel Paris: {r.json()}")
    r = client.get("/meteo/Lyon")
    print(f"  1er appel Lyon: {r.json()}")
    r = client.delete("/cache")
    print(f"  Vider cache: {r.json()}")
    r = client.get("/meteo/Paris")
    print(f"  Apres vidage Paris: {r.json()}")
