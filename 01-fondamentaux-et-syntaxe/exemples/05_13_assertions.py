# ============================================================================
#   Section 5.14 : Assertions pour le débogage
#   Description : assert pour vérifier des conditions internes
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

# --- Assertions de base ---
def diviser(a, b):
    assert b != 0, "Le diviseur ne peut pas être zéro"
    return a / b

print(diviser(10, 2))  # 5.0

def calculer_moyenne(notes):
    assert len(notes) > 0, "La liste ne peut pas être vide"
    return sum(notes) / len(notes)

print(calculer_moyenne([12, 15, 18]))  # 15.0

age = 25
assert 0 <= age <= 150, "Âge invalide"
print(f"Âge validé : {age}")

# --- Test d'assertion échouée ---
try:
    assert 1 == 2, "1 n'est pas égal à 2"
except AssertionError as e:
    print(f"AssertionError : {e}")

# --- Bon usage : vérifier des conditions internes ---
def process(data):
    assert isinstance(data, list), "data doit être une liste"
    print(f"Traitement de {len(data)} éléments")

process([1, 2, 3])
