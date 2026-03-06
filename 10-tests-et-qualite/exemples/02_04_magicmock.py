# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : MagicMock - mock avec methodes magiques (__len__,
#                 __iter__, __eq__), simulation de base de donnees
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

from unittest.mock import MagicMock

# MagicMock supporte les operations Python
mock = MagicMock()

# On peut l'utiliser comme un conteneur
mock.__len__.return_value = 5
print(f"len(mock) : {len(mock)}")  # 5

# Comme un iterable
mock.__iter__.return_value = iter([1, 2, 3])
print("Iteration sur mock :", end=" ")
for item in mock:
    print(item, end=" ")  # 1 2 3
print()

# Avec des comparaisons
mock.__eq__.return_value = True
print(f'mock == "quelque chose" : {mock == "quelque chose"}')  # True

# Exemple plus realiste : simuler une classe
print("\n=== Simulation de base de donnees ===")


class FausseBaseDeDonnees(MagicMock):
    """Simule une base de donnees pour les tests."""
    pass


db = FausseBaseDeDonnees()
db.query.return_value = [{"id": 1, "nom": "Alice"}]
db.__len__.return_value = 10

resultats = db.query("SELECT * FROM users")
print(f"resultats : {resultats}")  # [{'id': 1, 'nom': 'Alice'}]
print(f"len(db) : {len(db)}")  # 10
