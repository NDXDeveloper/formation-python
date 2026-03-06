# ============================================================================
#   Section 6.17 : Bonnes pratiques des type hints
#   Description : Fonctions publiques annotées, alias pour types complexes,
#                 éviter l'abus de Any, syntaxe | None, annotations utiles
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

# --- 1. Commencez par les fonctions publiques ---
# API publique : annotations obligatoires
def calculer_prix(prix_ht: float, quantite: int, tva: float = 0.20) -> float:
    """Calcule le prix TTC."""
    return prix_ht * quantite * (1 + tva)

# Fonction interne privée : annotations optionnelles
def _arrondir(valeur):
    return round(valeur, 2)

print(f"Prix TTC : {_arrondir(calculer_prix(100.0, 3))}€")  # 360.0€

# --- 2. Utilisez des alias pour les types complexes ---
DonneesComplexes = dict[str, list[dict[str, int]]]

def traiter(data: DonneesComplexes) -> list[str]:
    """Extrait les clés de tous les sous-dictionnaires."""
    resultats: list[str] = []
    for cle, sous_liste in data.items():
        for d in sous_liste:
            resultats.extend(d.keys())
    return resultats

data: DonneesComplexes = {
    "groupe1": [{"a": 1, "b": 2}],
    "groupe2": [{"c": 3}]
}
print(f"Clés extraites : {traiter(data)}")

# --- 3. Évitez l'abus de Any ---
# Soyez aussi spécifique que possible
def traiter_specifique(data: dict[str, int]) -> list[str]:
    return [f"{k}={v}" for k, v in data.items()]

print(f"Spécifique : {traiter_specifique({'x': 1, 'y': 2})}")

# Si vraiment variable, utilisez |
def traiter_union(data: str | int | float) -> str:
    return str(data)

print(f"Union : {traiter_union(42)}")

# --- 4. Syntaxe | None ---
def chercher(id: int) -> str | None:
    utilisateurs = {1: "Alice", 2: "Bob"}
    return utilisateurs.get(id)

print(f"chercher(1) = {chercher(1)}")    # Alice
print(f"chercher(99) = {chercher(99)}")  # None

# --- 5. Annotez quand le type n'est pas évident ---
# Type évident : pas besoin d'annotation
nom = "Alice"
age = 25

# Type non évident : annotation utile
resultats: list[int] = []
utilisateur: str | None = None

resultats.append(42)
utilisateur = "Bob"
print(f"resultats = {resultats}, utilisateur = {utilisateur}")

# --- 6. Résumé ---
print("\nBonnes pratiques :")
print("  1. Annotez les fonctions publiques en priorité")
print("  2. Utilisez des alias pour les types complexes")
print("  3. Évitez l'abus de Any")
print("  4. Préférez str | None à Optional[str]")
print("  5. Annotez quand le type n'est pas évident")
print("  6. Ajoutez les type hints progressivement")
