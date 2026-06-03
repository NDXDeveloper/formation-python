# ============================================================================
#   Section 2.1 : Les Dictionnaires - Modifier un dictionnaire
#   Description : Modifier valeurs, ajouter clés, update(), fusion avec | (3.9+)
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Modifier une valeur existante
personne["age"] = 26
print(personne)  # {'nom': 'Alice', 'age': 26, 'ville': 'Paris'}

# Ajouter une nouvelle paire clé-valeur
personne["profession"] = "Ingénieure"
print(personne)  # {'nom': 'Alice', 'age': 26, 'ville': 'Paris', 'profession': 'Ingénieure'}

# Mettre à jour plusieurs valeurs à la fois
personne.update({"age": 27, "ville": "Lyon", "telephone": "0123456789"})
print(personne)

# --- Fusionner des dictionnaires avec | (Python 3.9+) ---
defaut = {"couleur": "noir", "taille": "M"}
choix = {"taille": "L", "motif": "rayé"}

fusion = defaut | choix          # nouveau dict ; en cas de clé commune, la droite l'emporte
print(fusion)  # {'couleur': 'noir', 'taille': 'L', 'motif': 'rayé'}

defaut |= choix                  # fusion en place (comme update())
print(defaut)  # {'couleur': 'noir', 'taille': 'L', 'motif': 'rayé'}
