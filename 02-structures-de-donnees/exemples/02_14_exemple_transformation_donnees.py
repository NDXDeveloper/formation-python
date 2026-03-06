# ============================================================================
#   Section 2.2 : Exemple pratique - Transformation de données
#   Description : Convertir données brutes en dictionnaires, augmenter salaires
#   Fichier source : 02-comprehensions.md
# ============================================================================

# Données brutes
employes = [
    "Alice:25:50000",
    "Bob:30:60000",
    "Charlie:35:70000"
]

# Convertir en liste de dictionnaires
employes_dict = [
    {
        "nom": ligne.split(':')[0],
        "age": int(ligne.split(':')[1]),
        "salaire": int(ligne.split(':')[2])
    }
    for ligne in employes
]

print("Employés :")
for e in employes_dict:
    print(f"  {e}")

# Augmenter le salaire de 10% pour les personnes de plus de 30 ans
salaires_augmentes = {
    e["nom"]: e["salaire"] * 1.1 if e["age"] > 30 else e["salaire"]
    for e in employes_dict
}
print(f"\nSalaires ajustés : {salaires_augmentes}")
# {'Alice': 50000, 'Bob': 60000, 'Charlie': 77000.0}
