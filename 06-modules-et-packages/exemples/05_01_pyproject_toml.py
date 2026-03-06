# ============================================================================
#   Section 6.5 : Outils modernes - pyproject.toml
#   Description : Créer et lire un pyproject.toml (Poetry),
#                 comprendre la structure, les groupes de dépendances
#   Fichier source : 05-outils-modernes-poetry-pipenv.md
# ============================================================================

from pathlib import Path
import sys

# --- Créer un pyproject.toml de démonstration ---
print("=== Exemple de pyproject.toml (Poetry) ===")

pyproject_contenu = """\
[tool.poetry]
name = "mon-api"
version = "0.1.0"
description = "Une API RESTful avec FastAPI"
authors = ["Votre Nom <email@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.104.0"
uvicorn = {extras = ["standard"], version = "^0.24.0"}
sqlalchemy = "^2.0.0"
pydantic-settings = "^2.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
ruff = "^0.1.0"
mypy = "^1.5.0"
httpx = "^0.25.0"

[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
sphinx = "^7.0.0"

[tool.poetry.scripts]
mon-api = "mon_api.main:start"

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""

fichier = Path('_demo_pyproject.toml')
fichier.write_text(pyproject_contenu, encoding='utf-8')
print(pyproject_contenu)

# --- Lire et parser le TOML ---
print("=== Lecture du pyproject.toml ===")

# tomllib est disponible depuis Python 3.11
if sys.version_info >= (3, 11):
    import tomllib
    with open(fichier, 'rb') as f:
        config = tomllib.load(f)
else:
    # Pour Python < 3.11, on simule
    config = None
    print("(tomllib necessaire Python 3.11+, simulation)")

if config:
    poetry = config.get('tool', {}).get('poetry', {})

    print(f"Nom du projet : {poetry.get('name')}")
    print(f"Version : {poetry.get('version')}")
    print(f"Description : {poetry.get('description')}")
    print(f"Auteurs : {poetry.get('authors')}")

    # Dépendances principales
    deps = poetry.get('dependencies', {})
    print(f"\nDependances principales ({len(deps)}) :")
    for nom, version in deps.items():
        if isinstance(version, dict):
            print(f"  {nom} = {version}")
        else:
            print(f"  {nom} = {version}")

    # Dépendances de développement
    dev_deps = poetry.get('group', {}).get('dev', {}).get('dependencies', {})
    print(f"\nDependances de dev ({len(dev_deps)}) :")
    for nom, version in dev_deps.items():
        print(f"  {nom} = {version}")

    # Dépendances optionnelles (docs)
    docs_deps = poetry.get('group', {}).get('docs', {}).get('dependencies', {})
    if docs_deps:
        print(f"\nDependances docs ({len(docs_deps)}) :")
        for nom, version in docs_deps.items():
            print(f"  {nom} = {version}")

    # Scripts
    scripts = poetry.get('scripts', {})
    if scripts:
        print(f"\nScripts (entry points) :")
        for nom, cible in scripts.items():
            print(f"  {nom} -> {cible}")

    # Build system
    build = config.get('build-system', {})
    print(f"\nBuild system :")
    print(f"  requires : {build.get('requires')}")
    print(f"  backend  : {build.get('build-backend')}")

# --- Notation des versions ---
print("\n=== Notation des versions (Poetry) ===")

notations = [
    ("^2.31.0", ">=2.31.0, <3.0.0", "Compatible version majeure"),
    ("~2.31.0", ">=2.31.0, <2.32.0", "Compatible version mineure"),
    ("==2.31.0", "Exactement 2.31.0", "Version exacte"),
    (">=2.28.0,<3.0.0", "Entre 2.28.0 et 3.0.0", "Intervalle explicite"),
    ("*", "N'importe quelle version", "Aucune contrainte"),
]

for notation, equivalent, description in notations:
    print(f"  {notation:20s} -> {equivalent:30s} ({description})")

# Nettoyage
fichier.unlink()
