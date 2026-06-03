# ============================================================================
#   Section 6.2 : Exemple complet - Package de gestion de bibliothèque
#   Description : Package bibliotheque complet (models : livre/auteur/emprunt,
#                 services : gestion_livres/gestion_emprunts), imports relatifs
#   Fichier source : 02-structure-des-packages.md
# ============================================================================

from pathlib import Path
import sys
import shutil

# --- Créer la structure complète ---
base = Path('_temp_biblio')

models_dir = base / 'bibliotheque' / 'models'
models_dir.mkdir(parents=True, exist_ok=True)

services_dir = base / 'bibliotheque' / 'services'
services_dir.mkdir(parents=True, exist_ok=True)

# bibliotheque/__init__.py
(base / 'bibliotheque' / '__init__.py').write_text('''\
"""Package de gestion de bibliothèque."""

__version__ = "1.0.0"

from .models import Livre, Auteur, Emprunt
from .services import (
    ajouter_livre,
    rechercher_livre,
    emprunter_livre,
    retourner_livre,
)

__all__ = [
    'Livre', 'Auteur', 'Emprunt',
    'ajouter_livre', 'rechercher_livre', 'emprunter_livre', 'retourner_livre',
]
''', encoding='utf-8')

# models/__init__.py
(models_dir / '__init__.py').write_text('''\
"""Sous-package des modèles de données."""

from .livre import Livre
from .auteur import Auteur
from .emprunt import Emprunt
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

# models/auteur.py
(models_dir / 'auteur.py').write_text('''\
"""Modèle de données pour les auteurs."""

class Auteur:
    """Représente un auteur."""

    def __init__(self, nom, nationalite=None):
        self.nom = nom
        self.nationalite = nationalite

    def __str__(self):
        return self.nom
''', encoding='utf-8')

# models/emprunt.py
(models_dir / 'emprunt.py').write_text('''\
"""Modèle de données pour les emprunts."""

from datetime import date

class Emprunt:
    """Représente l'emprunt d'un livre par une personne."""

    def __init__(self, livre, emprunteur):
        self.livre = livre
        self.emprunteur = emprunteur
        self.date_emprunt = date.today()
''', encoding='utf-8')

# services/__init__.py
(services_dir / '__init__.py').write_text('''\
"""Sous-package des services métier."""

from .gestion_livres import ajouter_livre, rechercher_livre, lister_livres
from .gestion_emprunts import emprunter_livre, retourner_livre
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

# services/gestion_emprunts.py
(services_dir / 'gestion_emprunts.py').write_text('''\
"""Services de gestion des emprunts."""

def emprunter_livre(livre):
    """Marque un livre comme emprunté."""
    livre.disponible = False
    return livre

def retourner_livre(livre):
    """Marque un livre comme disponible."""
    livre.disponible = True
    return livre
''', encoding='utf-8')

# --- Utilisation ---
sys.path.insert(0, str(base))

print("=== Package bibliothèque ===")

from bibliotheque import ajouter_livre, rechercher_livre, emprunter_livre
# lister_livres n'est pas ré-exporté par bibliotheque/__init__.py : on y accède via le sous-package services
from bibliotheque.services import lister_livres

# Ajouter des livres
ajouter_livre("Python pour débutants", "John Doe", "123-456")
ajouter_livre("JavaScript avancé", "Jane Smith", "789-012")
ajouter_livre("Data Science avec Python", "Alice Martin", "345-678")

# Rechercher un livre
livre = rechercher_livre("Python")
print(f"Recherche 'Python' : {livre}")

# Lister tous les livres
print("\nCatalogue :")
for l in lister_livres():
    print(f"  - {l}")

# Emprunter le livre trouvé, puis vérifier son statut
emprunter_livre(livre)
print(f"\nAprès emprunt : {rechercher_livre('Python')}")

# Version du package
import bibliotheque
print(f"\nVersion : {bibliotheque.__version__}")
print(f"Exports : {bibliotheque.__all__}")

# Nettoyage
sys.path.pop(0)
shutil.rmtree(base)
