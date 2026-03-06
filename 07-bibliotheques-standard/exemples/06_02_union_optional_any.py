# ============================================================================
#   Section 7.6 : Le module typing - Annotations avancées
#   Description : Union (|), valeurs optionnelles (X | None), Any,
#                 TypeAlias pour alias de types
#   Fichier source : 06-typing-annotations-avancees.md
# ============================================================================

from typing import Any, TypeAlias

# ==========================================
# 1. Opérateur | - Plusieurs types possibles
# ==========================================
print("=== Union avec | (Python 3.10+) ===")

nombre: int | float = 42
print(f"nombre = {nombre} (type: {type(nombre).__name__})")
nombre = 3.14
print(f"nombre = {nombre} (type: {type(nombre).__name__})")

identifiant: str | int | None = "ABC123"
print(f"\nidentifiant = {identifiant}")
identifiant = 12345
print(f"identifiant = {identifiant}")
identifiant = None
print(f"identifiant = {identifiant}")

def traiter_donnee(valeur: int | str | float) -> str:
    """Traite différents types de données"""
    if isinstance(valeur, int):
        return f"Entier: {valeur}"
    elif isinstance(valeur, float):
        return f"Flottant: {valeur:.2f}"
    else:
        return f"Chaîne: {valeur}"

print(f"\n{traiter_donnee(42)}")
print(traiter_donnee(3.14))
print(traiter_donnee("test"))

# ==========================================
# 2. Valeur ou None (X | None)
# ==========================================
print("\n=== X | None (remplace Optional) ===")

nom: str | None = None
print(f"nom = {nom}")
nom = "Alice"
print(f"nom = {nom}")

def trouver_utilisateur(id: int) -> str | None:
    """Cherche un utilisateur par ID, retourne None si introuvable"""
    utilisateurs = {1: "Alice", 2: "Bob"}
    return utilisateurs.get(id)

resultat: str | None = trouver_utilisateur(1)
if resultat is not None:
    print(f"Utilisateur trouvé: {resultat}")
else:
    print("Utilisateur introuvable")

resultat2 = trouver_utilisateur(99)
if resultat2 is not None:
    print(f"Utilisateur trouvé: {resultat2}")
else:
    print("Utilisateur introuvable")

# ==========================================
# 3. Any - Type quelconque
# ==========================================
print("\n=== Any ===")

valeur: Any = 42
print(f"valeur = {valeur} (type: {type(valeur).__name__})")
valeur = "texte"
print(f"valeur = {valeur} (type: {type(valeur).__name__})")
valeur = [1, 2, 3]
print(f"valeur = {valeur} (type: {type(valeur).__name__})")
valeur = {"clé": "valeur"}
print(f"valeur = {valeur} (type: {type(valeur).__name__})")

def afficher(valeur: Any) -> None:
    """Affiche n'importe quelle valeur"""
    print(f"  afficher: {valeur}")

afficher(42)
afficher("test")
afficher([1, 2])

# ==========================================
# 4. TypeAlias - Alias de types
# ==========================================
print("\n=== TypeAlias ===")

UserId: TypeAlias = int
Email: TypeAlias = str
Coordonnees: TypeAlias = tuple[float, float]
Utilisateur: TypeAlias = dict[str, str]
ListeUtilisateurs: TypeAlias = list[Utilisateur]

def creer_utilisateur(id: UserId, email: Email) -> Utilisateur:
    """Crée un utilisateur"""
    return {"id": str(id), "email": email}

def obtenir_position() -> Coordonnees:
    """Retourne des coordonnées GPS"""
    return (48.8566, 2.3522)

users: ListeUtilisateurs = [
    {"nom": "Alice", "email": "alice@example.com"},
    {"nom": "Bob", "email": "bob@example.com"}
]

user = creer_utilisateur(1, "alice@example.com")
print(f"Utilisateur créé: {user}")

pos = obtenir_position()
print(f"Position: {pos}")

print(f"Liste d'utilisateurs:")
for u in users:
    print(f"  {u}")
