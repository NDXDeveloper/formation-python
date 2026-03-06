# ============================================================================
#   Section 5.3 : Cas d'usage avancés
#   Description : Validation des types, rate limiting, convertir des
#                 exceptions, décorateur de dépréciation
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

import time
import warnings
from functools import wraps

# --- Validation des types ---
print("=== Validation des types ===")

def valider_types(**type_attendu):
    """Valide les types des arguments."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            for nom_arg, valeur in kwargs.items():
                if nom_arg in type_attendu:
                    type_requis = type_attendu[nom_arg]
                    if not isinstance(valeur, type_requis):
                        raise TypeError(
                            f"{nom_arg} doit être de type {type_requis.__name__}, "
                            f"pas {type(valeur).__name__}"
                        )
            return fonction(*args, **kwargs)
        return wrapper
    return decorateur

@valider_types(nom=str, age=int)
def creer_personne(nom, age):
    return {"nom": nom, "age": age}

# Fonctionne
personne1 = creer_personne(nom="Alice", age=30)
print(personne1)  # {'nom': 'Alice', 'age': 30}

# Lève une erreur
try:
    personne2 = creer_personne(nom="Bob", age="trente")
except TypeError as e:
    print(f"Erreur : {e}")
    # TypeError: age doit être de type int, pas str

# --- Rate limiting ---
print("\n=== Rate limiting ===")

def rate_limit(appels_max, periode):
    """Limite le nombre d'appels dans une période donnée."""
    def decorateur(fonction):
        appels = []

        @wraps(fonction)
        def wrapper(*args, **kwargs):
            maintenant = time.time()

            # Supprimer les appels trop anciens
            appels[:] = [t for t in appels if maintenant - t < periode]

            if len(appels) >= appels_max:
                temps_attente = periode - (maintenant - appels[0])
                print(f"[limite] Trop de requêtes. Attendez {temps_attente:.1f} secondes")
                return None

            appels.append(maintenant)
            return fonction(*args, **kwargs)

        return wrapper
    return decorateur

@rate_limit(appels_max=3, periode=10)
def rechercher(terme):
    print(f"[recherche] Recherche de : {terme}")
    return f"Résultats pour {terme}"

rechercher("Python")   # OK
rechercher("Django")   # OK
rechercher("Flask")    # OK
rechercher("FastAPI")  # Trop de requêtes

# --- Convertir des exceptions ---
print("\n=== Convertir exceptions ===")

def convertir_exceptions(exception_source, exception_cible):
    """Convertit un type d'exception en un autre."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            try:
                return fonction(*args, **kwargs)
            except exception_source as e:
                raise exception_cible(f"Erreur convertie: {e}") from e
        return wrapper
    return decorateur

class ErreurMetier(Exception):
    """Exception personnalisée pour la logique métier."""
    pass

@convertir_exceptions(ValueError, ErreurMetier)
def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b

try:
    resultat = diviser(10, 0)
except ErreurMetier as e:
    print(f"Erreur métier : {e}")
    # Erreur métier : Erreur convertie: Division par zéro

# --- Dépréciation ---
print("\n=== Dépréciation ===")

def deprecie(message="Cette fonction est dépréciée"):
    """Marque une fonction comme dépréciée."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{fonction.__name__} est déprécié. {message}",
                category=DeprecationWarning,
                stacklevel=2
            )
            return fonction(*args, **kwargs)
        return wrapper
    return decorateur

@deprecie("Utilisez nouvelle_fonction() à la place")
def ancienne_fonction():
    """Ancienne implémentation."""
    return "Ancienne version"

def nouvelle_fonction():
    """Nouvelle implémentation."""
    return "Nouvelle version"

# Appel avec avertissement capturé
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    resultat = ancienne_fonction()
    if w:
        print(f"Avertissement : {w[0].message}")
    print(f"Résultat : {resultat}")

print(f"Nouvelle version : {nouvelle_fonction()}")
