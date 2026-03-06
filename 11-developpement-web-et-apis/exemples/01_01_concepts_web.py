# ============================================================================
#   Section 11.1 : Introduction aux frameworks web
#   Description : Concepts fondamentaux du web - HTTP, URLs, routes,
#                 modele client-serveur (demonstration sans serveur)
#   Fichier source : 01-introduction-frameworks-web.md
# ============================================================================

"""Demonstration des concepts fondamentaux du web."""

from urllib.parse import urlparse, parse_qs

# --- Le protocole HTTP : les methodes ---
print("=== Methodes HTTP ===")

methodes_http = {
    "GET": "Recuperer des donnees (afficher une page)",
    "POST": "Envoyer des donnees (soumettre un formulaire)",
    "PUT": "Mettre a jour des donnees",
    "DELETE": "Supprimer des donnees",
}

for methode, description in methodes_http.items():
    print(f"  {methode:8s} : {description}")


# --- Anatomie d'une URL ---
print("\n=== Anatomie d'une URL ===")

url = "https://monsite.com/articles/123?page=2&tri=date"
parsed = urlparse(url)

print(f"  URL complete : {url}")
print(f"  Protocole    : {parsed.scheme}")
print(f"  Domaine      : {parsed.netloc}")
print(f"  Chemin       : {parsed.path}")
print(f"  Parametres   : {parse_qs(parsed.query)}")


# --- Simulation de routes ---
print("\n=== Systeme de routes (simulation) ===")

routes: dict[str, str] = {}


def route(chemin: str):
    """Decorateur simulant un systeme de routes."""
    def decorateur(func):
        routes[chemin] = func.__name__
        return func
    return decorateur


@route("/")
def accueil():
    return "Page d'accueil"


@route("/articles")
def liste_articles():
    return "Liste des articles"


@route("/contact")
def contact():
    return "Page de contact"


for chemin, fonction in routes.items():
    print(f"  {chemin:15s} -> {fonction}()")


# --- Simulation requete/reponse ---
print("\n=== Cycle requete/reponse (simulation) ===")


class RequeteHTTP:
    """Simule une requete HTTP."""
    def __init__(self, methode: str, chemin: str) -> None:
        self.methode = methode
        self.chemin = chemin


class ReponseHTTP:
    """Simule une reponse HTTP."""
    def __init__(self, code: int, contenu: str) -> None:
        self.code = code
        self.contenu = contenu


def traiter_requete(requete: RequeteHTTP) -> ReponseHTTP:
    """Simule le traitement d'une requete par un framework."""
    if requete.chemin == "/":
        return ReponseHTTP(200, "Bienvenue sur mon site !")
    elif requete.chemin == "/articles":
        return ReponseHTTP(200, "Liste des articles")
    else:
        return ReponseHTTP(404, "Page non trouvee")


requetes = [
    RequeteHTTP("GET", "/"),
    RequeteHTTP("GET", "/articles"),
    RequeteHTTP("GET", "/inconnu"),
]

for req in requetes:
    rep = traiter_requete(req)
    print(f"  {req.methode} {req.chemin:15s} -> {rep.code} : {rep.contenu}")


# --- Comparaison des frameworks ---
print("\n=== Frameworks web Python ===")

frameworks = [
    ("Django", "Full-stack", "Sites web complets"),
    ("Flask", "Micro-framework", "Petites apps, APIs"),
    ("FastAPI", "Framework API", "APIs modernes, microservices"),
]

print(f"  {'Framework':10s} {'Type':18s} {'Cas d usage'}")
print(f"  {'-'*10} {'-'*18} {'-'*30}")
for nom, type_fw, usage in frameworks:
    print(f"  {nom:10s} {type_fw:18s} {usage}")
