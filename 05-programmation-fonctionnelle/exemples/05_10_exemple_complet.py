# ============================================================================
#   Section 5.5 : Exemple complet - Traitement fonctionnel de données
#   Description : Pipeline complet sur données d'étudiants : ajouter
#                 moyenne, filtrer admis, extraire noms
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

# --- Données ---
etudiants = [
    {"nom": "Alice", "notes": [15, 18, 16, 17]},
    {"nom": "Bob", "notes": [12, 14, 13, 15]},
    {"nom": "Charlie", "notes": [17, 19, 18, 16]},
    {"nom": "David", "notes": [10, 11, 9, 12]},
]

# --- Style fonctionnel : pipeline de transformations ---
print("=== Pipeline fonctionnel ===")

# 1. Ajouter la moyenne
def ajouter_moyenne(etudiant):
    notes = etudiant['notes']
    moyenne = sum(notes) / len(notes)
    return {**etudiant, 'moyenne': moyenne}

# 2. Filtrer les admis (moyenne >= 12)
def est_admis(etudiant):
    return etudiant['moyenne'] >= 12

# 3. Extraire le nom
def extraire_nom(etudiant):
    return etudiant['nom']

# Pipeline complet
etudiants_avec_moyenne = list(map(ajouter_moyenne, etudiants))
etudiants_admis = list(filter(est_admis, etudiants_avec_moyenne))
noms_admis = list(map(extraire_nom, etudiants_admis))

print("Étudiants admis :", noms_admis)
# Étudiants admis : ['Alice', 'Bob', 'Charlie']

# Détails
print("\nDétails :")
for e in etudiants_avec_moyenne:
    statut = "admis" if est_admis(e) else "refusé"
    print(f"  {e['nom']}: moyenne {e['moyenne']:.1f} ({statut})")

# --- Version compacte fonctionnelle ---
print("\n=== Version compacte ===")

noms_admis = list(map(
    extraire_nom,
    filter(est_admis, map(ajouter_moyenne, etudiants))
))
print("Admis :", noms_admis)

# --- Version pythonique avec compréhension ---
print("\n=== Version pythonique ===")

noms_admis = [
    etudiant['nom']
    for etudiant in etudiants
    if sum(etudiant['notes']) / len(etudiant['notes']) >= 12
]
print("Admis :", noms_admis)
