# ============================================================================
#   Section 6.4 : Environnements virtuels et Git
#   Description : Créer un .gitignore Python, structure de projet recommandée,
#                 fichier requirements.txt, bonnes pratiques
#   Fichier source : 04-environnements-virtuels.md
# ============================================================================

from pathlib import Path
import shutil

# --- Créer un .gitignore Python ---
print("=== Contenu recommandé pour .gitignore ===")

gitignore_contenu = """\
# Environnements virtuels
venv/
env/
.venv/
ENV/
env.bak/
venv.bak/

# Fichiers Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Environnement
.env
.env.local
"""

print(gitignore_contenu)

# --- Structure de projet recommandée ---
print("=== Structure de projet recommandée ===")

base = Path('_temp_projet')

# Créer la structure
structure = {
    'src/__init__.py': '"""Module principal."""\n',
    'src/main.py': '''\
"""Point d\'entrée de l\'application."""


def main():
    """Fonction principale."""
    print("Application démarrée")


if __name__ == "__main__":
    main()
''',
    'src/utils.py': '''\
"""Fonctions utilitaires."""


def formater_nom(prenom, nom):
    """Formate un nom complet."""
    return f"{prenom.title()} {nom.upper()}"
''',
    'tests/test_main.py': '''\
"""Tests pour le module main."""
# from src.main import main
# def test_main(): ...
''',
    'requirements.txt': '''\
# Dépendances principales
# requests==2.31.0
# flask>=2.3.0
# pandas>=1.5.0,<2.0.0
''',
    '.gitignore': gitignore_contenu,
    '.env.example': '''\
DATABASE_URL=postgresql://localhost/mabase
SECRET_KEY=your_secret_key_here
API_KEY=your_api_key_here
''',
}

for chemin, contenu in structure.items():
    fichier = base / chemin
    fichier.parent.mkdir(parents=True, exist_ok=True)
    fichier.write_text(contenu, encoding='utf-8')

# Afficher la structure
def afficher_arbre(dossier, prefixe=""):
    items = sorted(dossier.iterdir(), key=lambda x: (x.is_file(), x.name))
    for i, item in enumerate(items):
        est_dernier = i == len(items) - 1
        connecteur = "--- " if est_dernier else "|-- "
        if item.name == 'venv':
            print(f"{prefixe}{connecteur}{item.name}/  (ignore par Git)")
            continue
        if item.is_dir():
            print(f"{prefixe}{connecteur}{item.name}/")
            extension = "    " if est_dernier else "|   "
            afficher_arbre(item, prefixe + extension)
        else:
            note = ""
            if item.name == '.gitignore':
                note = "  (committe)"
            elif item.name == '.env.example':
                note = "  (committe)"
            elif item.name == '.env':
                note = "  (ignore par Git)"
            elif item.name == 'requirements.txt':
                note = "  (committe)"
            print(f"{prefixe}{connecteur}{item.name}{note}")

afficher_arbre(base)

# --- Ce qu'il faut committer ---
print("\n=== Fichiers a committer vs ignorer ===")

a_committer = [
    "Code source (.py)",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "Fichiers de configuration",
    ".env.example",
]

a_ignorer = [
    "venv/ ou env/",
    "__pycache__/",
    "*.pyc",
    ".env (variables sensibles)",
    "dist/ et build/",
]

print("A COMMITTER :")
for item in a_committer:
    print(f"  [OK] {item}")

print("\nA NE PAS COMMITTER :")
for item in a_ignorer:
    print(f"  [X]  {item}")

# --- Bonnes pratiques ---
print("\n=== Bonnes pratiques ===")

bonnes_pratiques = [
    "Un environnement virtuel par projet",
    "Toujours activer le venv avant de travailler",
    "Nommer le venv : venv, .venv ou env",
    "Mettre a jour pip apres creation",
    "Maintenir requirements.txt a jour",
    "Documenter les prerequis dans README.md",
]

for i, pratique in enumerate(bonnes_pratiques, 1):
    print(f"  {i}. {pratique}")

# Nettoyage
shutil.rmtree(base)
print(f"\nNettoyage : {base} supprime")
