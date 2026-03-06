# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Mock bases - creation, return_value, side_effect,
#                 exceptions, verification des appels
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

from unittest.mock import Mock

# --- Creer un mock simple ---
print("=== Mock simple ===")
mon_mock = Mock()

# Utiliser le mock
resultat = mon_mock.ma_methode(1, 2, 3)
autre_resultat = mon_mock.autre_methode(nom="Alice")

# Verifier les appels
print(f"ma_methode appelee : {mon_mock.ma_methode.called}")          # True
print(f"ma_methode call_count : {mon_mock.ma_methode.call_count}")   # 1
print(f"autre_methode call_count : {mon_mock.autre_methode.call_count}")  # 1

# Le mock peut etre appele comme une fonction
mon_mock(42)
print(f"mon_mock appele : {mon_mock.called}")  # True

# --- Configurer le retour d'un mock ---
print("\n=== Mock avec return_value ===")
mock_addition = Mock(return_value=10)
resultat = mock_addition(5, 5)
print(f"resultat : {resultat}")  # 10

# --- Mock avec side_effect (valeurs successives) ---
print("\n=== Mock avec side_effect (valeurs successives) ===")
mock_compteur = Mock(side_effect=[1, 2, 3, 4])
print(f"appel 1 : {mock_compteur()}")  # 1
print(f"appel 2 : {mock_compteur()}")  # 2
print(f"appel 3 : {mock_compteur()}")  # 3
print(f"appel 4 : {mock_compteur()}")  # 4

# --- Mock qui leve une exception ---
print("\n=== Mock avec side_effect (exception) ===")
mock_erreur = Mock(side_effect=ValueError("Erreur de test"))

try:
    mock_erreur()
except ValueError as e:
    print(f"Exception capturee : {e}")
