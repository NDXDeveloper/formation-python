# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Patch - decorateur, context manager, patch.object,
#                 patcher plusieurs choses
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

from unittest.mock import patch, Mock


# --- Classe de demonstration ---

class MaClasse:
    def methode_originale(self):
        return "original"


# --- patch.object : patcher un attribut specifique ---
print("=== patch.object ===")
obj = MaClasse()

with patch.object(obj, 'methode_originale', return_value="mocké"):
    resultat = obj.methode_originale()
    print(f"Pendant le patch : {resultat}")  # mocké
    assert resultat == "mocké"

# Apres le contexte, la methode est restauree
resultat_apres = obj.methode_originale()
print(f"Apres le patch : {resultat_apres}")  # original
assert resultat_apres == "original"


# --- Demonstration avec un module reel ---
print("\n=== patch comme context manager ===")

# Patcher os.path.exists
import os
with patch('os.path.exists', return_value=True) as mock_exists:
    resultat = os.path.exists("/fichier/inexistant")
    print(f"os.path.exists mocke : {resultat}")  # True
    mock_exists.assert_called_once_with("/fichier/inexistant")
    print("assert_called_once_with : OK")

# Apres le contexte, os.path.exists est revenu a la normale
resultat_reel = os.path.exists("/fichier/inexistant")
print(f"os.path.exists reel : {resultat_reel}")  # False


# --- patch comme decorateur ---
print("\n=== patch comme decorateur ===")


@patch('os.path.getsize', return_value=1024)
def test_avec_patch(mock_getsize):
    """Test avec patch en decorateur."""
    taille = os.path.getsize("/un/fichier")
    print(f"os.path.getsize mocke : {taille}")  # 1024
    assert taille == 1024
    mock_getsize.assert_called_once_with("/un/fichier")
    print("assert_called_once_with : OK")


test_avec_patch()


# --- Patcher plusieurs choses ---
print("\n=== Patcher plusieurs choses ===")


@patch('os.path.getsize', return_value=2048)
@patch('os.path.exists', return_value=True)
def test_multi_patch(mock_exists, mock_getsize):
    """Attention : l'ordre est inverse !"""
    assert os.path.exists("/test") is True
    assert os.path.getsize("/test") == 2048
    print(f"exists mocke : {os.path.exists('/test')}")
    print(f"getsize mocke : {os.path.getsize('/test')}")
    print("Multi-patch : OK")


test_multi_patch()

# Ou avec context manager
print("\n=== Multi-patch avec context manager ===")
with patch('os.path.exists') as mock1, \
     patch('os.path.getsize') as mock2:
    mock1.return_value = True
    mock2.return_value = 4096
    print(f"exists : {os.path.exists('/test')}")
    print(f"getsize : {os.path.getsize('/test')}")
    print("Multi-patch context manager : OK")
