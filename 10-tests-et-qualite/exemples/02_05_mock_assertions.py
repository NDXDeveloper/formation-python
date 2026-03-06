# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Assertions avancees sur les mocks - called, call_count,
#                 assert_called_with, assert_has_calls, assert_not_called
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

from unittest.mock import Mock, call

# Creer un mock
mock = Mock()

# Utiliser le mock
mock.methode(1, 2, 3)
mock.methode(4, 5, 6)
mock.autre_methode(nom="Alice")

# Verifier qu'une methode a ete appelee
print(f"methode appelee : {mock.methode.called}")         # True
print(f"autre_methode appelee : {mock.autre_methode.called}")  # True

# Verifier le nombre d'appels
print(f"methode call_count : {mock.methode.call_count}")         # 2
print(f"autre_methode call_count : {mock.autre_methode.call_count}")  # 1

# Verifier les arguments du dernier appel
mock.methode.assert_called_with(4, 5, 6)
print("assert_called_with(4, 5, 6) : OK")

# Verifier tous les appels
mock.methode.assert_has_calls([
    call(1, 2, 3),
    call(4, 5, 6)
])
print("assert_has_calls : OK")

# Verifier qu'une methode n'a PAS ete appelee
mock_non_appele = Mock()
mock_non_appele.methode.assert_not_called()
print("assert_not_called : OK")

# --- Bonnes pratiques : spec ---
print("\n=== Utilisation de spec ===")


class VraieClasse:
    def methode_existante(self):
        pass


# Sans spec, tout est permis
mock_sans_spec = Mock()
mock_sans_spec.methode_qui_nexiste_pas()  # Pas d'erreur !
print("Sans spec : methode_qui_nexiste_pas() acceptee")

# Avec spec, les erreurs sont detectees
mock_avec_spec = Mock(spec=VraieClasse)
mock_avec_spec.methode_existante()  # OK
print("Avec spec : methode_existante() OK")
try:
    mock_avec_spec.methode_qui_nexiste_pas()
except AttributeError as e:
    print(f"Avec spec : methode_qui_nexiste_pas() -> AttributeError")
