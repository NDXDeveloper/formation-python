# ============================================================================
#   Section 9.3 : Techniques de debogage
#   Description : Debogage avec print() (moyenne, types, separateurs),
#                 assertions (racine carree, types, liste vide)
#   Fichier source : 03-techniques-de-debogage.md
# ============================================================================

# ==========================================
# 1. Debogage avec print()
# ==========================================
print("=== Debogage avec print() ===\n")

def calculer_moyenne(notes):
    total = 0
    for note in notes:
        print(f"  Note actuelle : {note}")
        total += note
    print(f"  Total : {total}")
    moyenne = total / len(notes)
    print(f"  Moyenne calculee : {moyenne}")
    return moyenne

notes = [15, 18, 12, 16]
resultat = calculer_moyenne(notes)

# Afficher le type d'une variable
print("\n--- Afficher le type ---")
valeur = "123"
print(f"  Valeur : {valeur}, Type : {type(valeur)}")

# Afficher plusieurs variables
print("\n--- Afficher plusieurs variables ---")
nom = "Alice"
age = 25
ville = "Paris"
print(f"  Nom: {nom}, Age: {age}, Ville: {ville}")

# Separateurs visuels
print("\n--- Separateurs visuels ---")
print("=" * 50)
print("DEBUT DU DEBOGAGE")
print("=" * 50)
print("  ... code ici ...")
print("=" * 50)
print("FIN DU DEBOGAGE")
print("=" * 50)

# ==========================================
# 2. Assertions
# ==========================================
print("\n=== Assertions ===\n")

# Verifier qu'une valeur est positive
def calculer_racine_carree(nombre):
    assert nombre >= 0, "Le nombre doit etre positif"
    return nombre ** 0.5

print(f"  racine(16) = {calculer_racine_carree(16)}")  # 4.0

try:
    print(calculer_racine_carree(-5))
except AssertionError as e:
    print(f"  AssertionError : {e}")

# Verifier le type d'une variable
def concatener_textes(texte1, texte2):
    assert isinstance(texte1, str), "texte1 doit etre une chaine"
    assert isinstance(texte2, str), "texte2 doit etre une chaine"
    return texte1 + " " + texte2

resultat = concatener_textes("Bonjour", "monde")
print(f"  concatener('Bonjour', 'monde') = '{resultat}'")

try:
    resultat = concatener_textes("Bonjour", 123)
except AssertionError as e:
    print(f"  AssertionError : {e}")

# Verifier qu'une liste n'est pas vide
def obtenir_premier_element(liste):
    assert len(liste) > 0, "La liste ne peut pas etre vide"
    return liste[0]

ma_liste = [1, 2, 3]
print(f"  premier([1, 2, 3]) = {obtenir_premier_element(ma_liste)}")

try:
    liste_vide = []
    print(obtenir_premier_element(liste_vide))
except AssertionError as e:
    print(f"  AssertionError : {e}")
