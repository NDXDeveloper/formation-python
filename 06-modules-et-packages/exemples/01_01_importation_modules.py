# ============================================================================
#   Section 6.1 : Importation de modules
#   Description : import simple, alias, from import, import *,
#                 modules de la bibliothèque standard
#   Fichier source : 01-importation-et-creation-modules.md
# ============================================================================

# --- Importation simple ---
print("=== import simple ===")

import math

resultat = math.sqrt(16)
print(resultat)  # 4.0

print(math.pi)   # 3.141592653589793

# --- Importation avec alias ---
print("\n=== import avec alias ===")

import math as m

resultat = m.sqrt(25)
print(resultat)  # 5.0

print(m.pi)      # 3.141592653589793

# --- Importation d'éléments spécifiques ---
print("\n=== from import ===")

from math import sqrt, pi

resultat = sqrt(36)
print(resultat)  # 6.0

print(pi)        # 3.141592653589793

# --- Alias sur éléments ---
print("\n=== alias sur éléments ===")

from math import sqrt as racine_carree

resultat = racine_carree(49)
print(resultat)  # 7.0

# --- import * ---
print("\n=== import * ===")

from math import *

resultat = sqrt(64)
print(resultat)  # 8.0

# --- Modules de la bibliothèque standard ---
print("\n=== Modules standard ===")

import datetime

maintenant = datetime.datetime.now()
print(f"Date actuelle : {maintenant.strftime('%Y-%m-%d')}")

import os

chemin_actuel = os.getcwd()
print(f"Répertoire : {chemin_actuel}")

import re

texte = "Mon email est exemple@email.com"
email = re.search(r'\S+@\S+', texte)
print(email.group())  # exemple@email.com
