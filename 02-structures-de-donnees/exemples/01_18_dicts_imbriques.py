# ============================================================================
#   Section 2.1 : Les Dictionnaires - Dictionnaires imbriqués
#   Description : Dictionnaires contenant d'autres dictionnaires, accès imbriqué
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Dictionnaire contenant d'autres dictionnaires
entreprise = {
    "nom": "Tech Corp",
    "employes": {
        "dev1": {
            "nom": "Alice",
            "poste": "Développeuse",
            "salaire": 50000
        },
        "dev2": {
            "nom": "Bob",
            "poste": "Développeur",
            "salaire": 55000
        }
    },
    "localisation": "Paris"
}

# Accès aux valeurs imbriquées
print(entreprise["employes"]["dev1"]["nom"])  # Alice

# Parcourir les employés
for id_employe, infos in entreprise["employes"].items():
    print(f"{id_employe}: {infos['nom']} - {infos['poste']}")
