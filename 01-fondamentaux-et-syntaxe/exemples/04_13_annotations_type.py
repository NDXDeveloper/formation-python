# ============================================================================
#   Section 4.13 : Annotations de type (aperçu)
#   Description : Type hints pour paramètres et retour, types complexes
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Type hints de base ---
def additionner(a: int, b: int) -> int:
    """Additionne deux nombres entiers."""
    return a + b

def saluer(nom: str) -> str:
    """Retourne un message de salutation."""
    return f"Bonjour {nom} !"

def diviser(a: float, b: float) -> float:
    """Divise deux nombres."""
    return a / b

print(additionner(5, 3))     # 8
print(saluer("Alice"))       # Bonjour Alice !
print(diviser(10.0, 3.0))    # 3.3333333333333335

# --- Types complexes (Python 3.10+) ---
print()

def traiter_nombres(nombres: list[int]) -> int:
    """Retourne la somme d'une liste d'entiers."""
    return sum(nombres)

def obtenir_info() -> tuple[str, int]:
    """Retourne un tuple (nom, age)."""
    return "Alice", 25

print(traiter_nombres([1, 2, 3, 4, 5]))  # 15

nom, age = obtenir_info()
print(f"{nom}, {age} ans")  # Alice, 25 ans

# --- Type pour paramètre avec valeur par défaut ---
print()

def creer_message(texte: str, majuscules: bool = False) -> str:
    if majuscules:
        return texte.upper()
    return texte

print(creer_message("bonjour"))              # bonjour
print(creer_message("bonjour", True))        # BONJOUR

# --- Types pour *args et **kwargs ---
print()

def somme(*nombres: int) -> int:
    return sum(nombres)

def afficher_info(**infos: str) -> None:
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")

print(somme(1, 2, 3))  # 6
afficher_info(nom="Alice", ville="Paris")
