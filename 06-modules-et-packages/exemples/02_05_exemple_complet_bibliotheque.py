# ============================================================================
#   Section 6.2 : Exemple complet - Package de gestion de bibliothèque
#   Description : Package bibliotheque avec models/livre.py,
#                 services/gestion_livres.py, imports relatifs
#   Fichier source : 02-structure-des-packages.md
# ============================================================================

from pathlib import Path
import sys
import shutil

# --- Créer la structure complète ---
base = Path('_temp_biblio')

# models/
models_dir = base / 'bibliotheque' / 'models'
models_dir.mkdir(parents=True, exist_ok=True)

# services/
services_dir = base / 'bibliotheque' / 'services'
services_dir.mkdir(parents=True, exist_ok=True)

# bibliotheque/__init__.py
(base / 'bibliotheque' / '__init__.py').write_text('''\
"""Package de gestion de bibliothèque."""

__version__ = "1.0.0"

from .models import Livre
from .services import ajouter_livre, rechercher_livre, lister_livres

__all__ = ['Livre', 'ajouter_livre', 'rechercher_livre', 'lister_livres']
''', encoding='utf-8')

# models/__init__.py
(models_dir / '__init__.py').write_text('''\
from .livre import Livre
''', encoding='utf-8')

# models/livre.py
(models_dir / 'livre.py').write_text('''\
"""Modèle de données pour les livres."""

class Livre:
    """Représente un livre de la bibliothèque."""

    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        statut = "disponible" if self.disponible else "emprunté"
        return f"{self.titre} par {self.auteur} ({statut})"
''', encoding='utf-8')

# services/__init__.py
(services_dir / '__init__.py').write_text('''\
from .gestion_livres import ajouter_livre, rechercher_livre, lister_livres
''', encoding='utf-8')

# services/gestion_livres.py
(services_dir / 'gestion_livres.py').write_text('''\
"""Services de gestion des livres."""

from ..models.livre import Livre

_catalogue = []

def ajouter_livre(titre, auteur, isbn):
    livre = Livre(titre, auteur, isbn)
    _catalogue.append(livre)
    return livre

def rechercher_livre(titre):
    for livre in _catalogue:
        if titre.lower() in livre.titre.lower():
            return livre
    return None

def lister_livres():
    return _catalogue.copy()
''', encoding='utf-8')

# --- Utilisation ---
sys.path.insert(0, str(base))

print("=== Package bibliothèque ===")

from bibliotheque import ajouter_livre, rechercher_livre, lister_livres

# Ajouter des livres
livre1 = ajouter_livre("Python pour débutants", "John Doe", "123-456")
livre2 = ajouter_livre("JavaScript avancé", "Jane Smith", "789-012")
livre3 = ajouter_livre("Data Science avec Python", "Alice Martin", "345-678")

# Rechercher un livre
livre = rechercher_livre("Python")
print(f"Recherche 'Python' : {livre}")

# Lister tous les livres
print("\nCatalogue :")
for l in lister_livres():
    print(f"  - {l}")

# Version du package
import bibliotheque
print(f"\nVersion : {bibliotheque.__version__}")

# Nettoyage
sys.path.pop(0)
shutil.rmtree(base)
