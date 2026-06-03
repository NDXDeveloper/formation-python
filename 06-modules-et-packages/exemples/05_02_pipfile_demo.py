# ============================================================================
#   Section 6.5 : Outils modernes - Pipfile (Pipenv)
#   Description : Créer et lire un Pipfile, comprendre la structure,
#                 comparer pip/venv vs Pipenv vs Poetry
#   Fichier source : 05-outils-modernes-poetry-pipenv.md
# ============================================================================

from pathlib import Path
import sys

# --- Créer un Pipfile de démonstration ---
print("=== Exemple de Pipfile (Pipenv) ===")

pipfile_contenu = """\
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"
flask = "*"
pandas = "*"
numpy = "*"
django = "==4.2.0"

[dev-packages]
pytest = "*"
black = "*"
flake8 = "*"

[requires]
python_version = "3.11"
"""

fichier = Path('_demo_Pipfile')
fichier.write_text(pipfile_contenu, encoding='utf-8')
print(pipfile_contenu)

# --- Parser le Pipfile (format TOML) ---
print("=== Lecture du Pipfile ===")

if sys.version_info >= (3, 11):
    import tomllib
    with open(fichier, 'rb') as f:
        config = tomllib.load(f)

    # Sources
    sources = config.get('source', [])
    for src in sources:
        print(f"Source : {src.get('name')} -> {src.get('url')}")
        print(f"  SSL : {src.get('verify_ssl')}")

    # Packages principaux
    packages = config.get('packages', {})
    print(f"\nPackages principaux ({len(packages)}) :")
    for nom, version in packages.items():
        print(f"  {nom} = {version}")

    # Packages de développement
    dev_packages = config.get('dev-packages', {})
    print(f"\nPackages de dev ({len(dev_packages)}) :")
    for nom, version in dev_packages.items():
        print(f"  {nom} = {version}")

    # Version Python requise
    requires = config.get('requires', {})
    print(f"\nPython requis : {requires.get('python_version')}")
else:
    print("(tomllib nécessaire en Python 3.11+, simulation)")

# --- Comparaison des fichiers de configuration ---
print("\n=== Comparaison des formats ===")

comparaison = [
    ("Fonctionnalité", "pip + venv", "Pipenv", "Poetry", "uv"),
    ("-" * 18, "-" * 17, "-" * 14, "-" * 15, "-" * 14),
    ("Fichier config", "requirements.txt", "Pipfile", "pyproject.toml", "pyproject.toml"),
    ("Lock file", "Non", "Pipfile.lock", "poetry.lock", "uv.lock"),
    ("Gestion venv", "Manuelle", "Automatique", "Automatique", "Automatique"),
    ("Dev vs Prod", "Fichiers séparés", "[dev-packages]", "Groupes", "Groupes"),
    ("Build packages", "setuptools", "Limité", "Intégré", "Intégré"),
    ("Publication PyPI", "twine", "Non", "poetry publish", "uv publish"),
    ("Vitesse", "Rapide", "Lente", "Rapide", "Très rapide"),
]

for ligne in comparaison:
    print(f"  {ligne[0]:18s} {ligne[1]:17s} {ligne[2]:14s} {ligne[3]:15s} {ligne[4]:14s}")

# --- Quand utiliser quel outil ---
print("\n=== Quand utiliser quel outil ? ===")

recommandations = {
    "pip + venv": [
        "Débutant avec Python",
        "Projet simple, peu de dépendances",
        "Script rapide ou prototype",
    ],
    "Pipenv": [
        "Projet de taille moyenne",
        "Migration facile depuis requirements.txt",
        "Outil maintenu par la PyPA (mais en perte de vitesse)",
    ],
    "Poetry": [
        "Nouveau projet professionnel",
        "Package à publier sur PyPI",
        "Workflow moderne et complet",
    ],
    "uv": [
        "Nouveau projet en 2026 (choix par défaut conseillé)",
        "Vitesse d'installation critique (CI, Docker)",
        "Un seul outil rapide pour tout (écrit en Rust)",
    ],
}

for outil, cas in recommandations.items():
    print(f"\n  {outil} :")
    for c in cas:
        print(f"    - {c}")

# --- Workflow typique Poetry ---
print("\n=== Workflow typique Poetry ===")

etapes = [
    "poetry new mon_projet        # Créer le projet",
    "cd mon_projet",
    "poetry add requests flask     # Ajouter des dépendances",
    "poetry add --group dev pytest # Ajouter des deps de dev",
    "poetry install                # Installer tout",
    "poetry run python app.py      # Exécuter",
    "poetry run pytest             # Tester",
    "poetry build                  # Construire le package",
    "poetry publish                # Publier sur PyPI",
]

for i, etape in enumerate(etapes, 1):
    print(f"  {i}. {etape}")

# --- Workflow typique Pipenv ---
print("\n=== Workflow typique Pipenv ===")

etapes_pipenv = [
    "mkdir mon_projet && cd mon_projet",
    "pipenv install                # Initialiser",
    "pipenv install flask          # Ajouter un package",
    "pipenv install --dev pytest   # Ajouter un package de dev",
    "pipenv shell                  # Activer l'environnement",
    "python app.py                 # Exécuter",
    "pipenv run pytest             # Tester sans activer",
    "pipenv graph                  # Voir les dépendances",
    "exit                          # Quitter le shell",
]

for i, etape in enumerate(etapes_pipenv, 1):
    print(f"  {i}. {etape}")

# --- Workflow typique uv ---
print("\n=== Workflow typique uv ===")

etapes_uv = [
    "uv init mon_projet            # Créer le projet",
    "cd mon_projet",
    "uv add requests flask         # Ajouter des dépendances",
    "uv add --dev pytest           # Ajouter une dépendance de dev",
    "uv run python app.py          # Exécuter (venv géré automatiquement)",
    "uv run pytest                 # Tester",
    "uv sync                       # Synchroniser depuis uv.lock",
]

for i, etape in enumerate(etapes_uv, 1):
    print(f"  {i}. {etape}")

# Nettoyage
fichier.unlink()
