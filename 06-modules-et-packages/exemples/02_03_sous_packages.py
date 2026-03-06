# ============================================================================
#   Section 6.2 : Packages imbriqués et imports relatifs
#   Description : Sous-packages texte/formatage et texte/validation,
#                 imports relatifs avec . et .., __all__
#   Fichier source : 02-structure-des-packages.md
# ============================================================================

from pathlib import Path
import sys
import shutil

# --- Créer la structure du package avec sous-packages ---
base = Path('_temp_pkg3')

# utilitaires/texte/formatage.py
fmt_dir = base / 'utilitaires' / 'texte'
fmt_dir.mkdir(parents=True, exist_ok=True)

(base / 'utilitaires' / '__init__.py').write_text(
    '"""Package utilitaires principal."""\n__version__ = "1.0.0"\nfrom . import texte\n',
    encoding='utf-8'
)

(fmt_dir / 'formatage.py').write_text('''\
"""Module de formatage de texte."""

def mettre_en_majuscules(texte):
    return texte.upper()

def mettre_en_minuscules(texte):
    return texte.lower()

def capitaliser(texte):
    return texte.title()

def nettoyer(texte):
    return ' '.join(texte.split())
''', encoding='utf-8')

(fmt_dir / 'validation.py').write_text('''\
"""Module de validation de texte."""
import re

def est_email_valide(email):
    pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'
    return bool(re.match(pattern, email))

def est_telephone_valide(telephone):
    pattern = r'^0[1-9](\\d{2}){4}$'
    return bool(re.match(pattern, telephone.replace(' ', '')))

def contient_chiffres(texte):
    return bool(re.search(r'\\d', texte))
''', encoding='utf-8')

(fmt_dir / '__init__.py').write_text('''\
"""Sous-package pour le traitement de texte."""

from .formatage import mettre_en_majuscules, mettre_en_minuscules, capitaliser, nettoyer
from .validation import est_email_valide, est_telephone_valide, contient_chiffres

__all__ = [
    'mettre_en_majuscules', 'mettre_en_minuscules', 'capitaliser', 'nettoyer',
    'est_email_valide', 'est_telephone_valide', 'contient_chiffres'
]
''', encoding='utf-8')

sys.path.insert(0, str(base))

# --- Utilisation des sous-packages ---
print("=== Import complet ===")

import utilitaires.texte.formatage

texte = "bonjour le monde"
resultat = utilitaires.texte.formatage.mettre_en_majuscules(texte)
print(resultat)  # BONJOUR LE MONDE

# --- Import avec alias ---
print("\n=== Import avec alias ===")

from utilitaires.texte import formatage as fmt

resultat = fmt.capitaliser("bonjour le monde")
print(resultat)  # Bonjour Le Monde

# --- Import direct des fonctions ---
print("\n=== Import direct ===")

from utilitaires.texte import mettre_en_majuscules, est_email_valide

print(mettre_en_majuscules("python"))  # PYTHON
print(est_email_valide("test@example.com"))  # True
print(est_email_valide("invalide"))  # False

# --- Import du sous-package ---
print("\n=== Import sous-package ===")

from utilitaires import texte

resultat = texte.nettoyer("  trop    d'espaces  ")
print(resultat)  # trop d'espaces

print(texte.contient_chiffres("abc123"))  # True
print(texte.contient_chiffres("abc"))  # False

print(texte.est_telephone_valide("01 23 45 67 89"))  # True
print(texte.est_telephone_valide("123"))  # False

# Nettoyage
sys.path.pop(0)
shutil.rmtree(base)
