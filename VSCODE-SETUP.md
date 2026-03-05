# Configuration VS Code pour Python

Guide de configuration de Visual Studio Code pour un environnement de développement Python moderne et productif.

---

## Fichier `.vscode/settings.json`

Créer ce fichier à la racine du projet pour une configuration optimale :

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",

  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    },
    "editor.rulers": [88],
    "editor.tabSize": 4
  },

  "ruff.lineLength": 88,

  "mypy-type-checker.args": [
    "--ignore-missing-imports",
    "--follow-imports=silent",
    "--show-column-numbers"
  ],

  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": [
    "tests"
  ],

  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true,
    "**/.mypy_cache": true,
    "**/venv": true
  },

  "files.associations": {
    "*.md": "markdown"
  },

  "editor.minimap.enabled": true,
  "editor.suggestSelection": "first",
  "editor.snippetSuggestions": "top"
}
```

> **Note :** Depuis 2023, les paramètres `python.formatting.provider` et `python.linting.*` sont dépréciés. Le formatage et le linting utilisent désormais des extensions dédiées (Ruff, Black, mypy) avec leurs propres paramètres.

---

## Extensions VS Code recommandées

Créer le fichier `.vscode/extensions.json` :

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.mypy-type-checker",
    "charliermarsh.ruff",
    "kevinrose.vsc-python-indent",
    "njpwerner.autodocstring",
    "yzhang.markdown-all-in-one",
    "tamasfe.even-better-toml"
  ]
}
```

### Description des extensions

| Extension | Rôle |
|-----------|------|
| **Python** (`ms-python.python`) | Support Python de base (IntelliSense, débogage, notebooks) |
| **Pylance** (`ms-python.vscode-pylance`) | Serveur de langage rapide (auto-complétion, navigation, types) |
| **Mypy Type Checker** (`ms-python.mypy-type-checker`) | Vérification statique des types en temps réel |
| **Ruff** (`charliermarsh.ruff`) | Linter et formateur ultra-rapide (remplace Black, Flake8, isort) |
| **Python Indent** (`kevinrose.vsc-python-indent`) | Indentation intelligente après `def`, `if`, `for`, etc. |
| **autoDocstring** (`njpwerner.autodocstring`) | Génération automatique de docstrings |
| **Markdown All in One** (`yzhang.markdown-all-in-one`) | Édition Markdown avancée (aperçu, raccourcis, table des matières) |
| **Even Better TOML** (`tamasfe.even-better-toml`) | Support des fichiers `pyproject.toml` |

---

## Raccourcis utiles VS Code

### Raccourcis généraux

| Raccourci | Action |
|-----------|--------|
| `Ctrl+Shift+P` | Palette de commandes |
| `Ctrl+P` | Recherche rapide de fichier |
| `Ctrl+Shift+F` | Rechercher dans tous les fichiers |
| <code>Ctrl+`</code> | Ouvrir le terminal intégré |

### Raccourcis Python

| Raccourci | Action |
|-----------|--------|
| `F5` | Déboguer le fichier courant |
| `Ctrl+F5` | Exécuter sans débogage |
| `F12` | Aller à la définition |
| `Alt+F12` | Aperçu de la définition (popup) |
| `Shift+F12` | Trouver toutes les références |
| `Ctrl+Space` | Suggestions IntelliSense |
| `Shift+Alt+F` | Formater le document |
| `F9` | Ajouter/retirer un point d'arrêt |

### Raccourcis d'édition

| Raccourci | Action |
|-----------|--------|
| `Alt+↑` / `Alt+↓` | Déplacer une ligne |
| `Shift+Alt+↑` / `Shift+Alt+↓` | Dupliquer une ligne |
| `Ctrl+D` | Sélectionner l'occurrence suivante |
| `Ctrl+Shift+K` | Supprimer une ligne |
| `Ctrl+/` | Commenter/décommenter |

---

## Tâches automatisées

Créer le fichier `.vscode/tasks.json` pour lancer les outils de qualité :

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "pytest",
      "group": {
        "kind": "test",
        "isDefault": true
      },
      "problemMatcher": []
    },
    {
      "label": "Type Check",
      "type": "shell",
      "command": "mypy .",
      "group": "test"
    },
    {
      "label": "Lint (Ruff)",
      "type": "shell",
      "command": "ruff check .",
      "group": "test"
    },
    {
      "label": "Format (Ruff)",
      "type": "shell",
      "command": "ruff format .",
      "group": "build"
    }
  ]
}
```

> **Astuce :** Utilisez `Ctrl+Shift+P` puis tapez "Run Task" pour exécuter ces tâches.

---

## Configuration de débogage

Créer le fichier `.vscode/launch.json` pour déboguer vos scripts Python :

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python : fichier courant",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python : pytest",
      "type": "debugpy",
      "request": "launch",
      "module": "pytest",
      "args": ["-v"],
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "FastAPI : serveur",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": ["main:app", "--reload"],
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

> **Astuce :** Appuyez sur `F5` pour lancer le débogage, `F9` pour placer un point d'arrêt, et `F10`/`F11` pour avancer pas à pas.

---

## Snippets Python personnalisés

Créer le fichier `.vscode/python.code-snippets` :

```json
{
  "Type Hint Function": {
    "prefix": "deff",
    "body": [
      "def ${1:function_name}(${2:arg}: ${3:str}) -> ${4:None}:",
      "    \"\"\"${5:Description}.\"\"\"",
      "    $0"
    ],
    "description": "Fonction avec type hints"
  },
  "FastAPI Route": {
    "prefix": "fastapi",
    "body": [
      "@app.${1|get,post,put,delete|}(\"/${2:endpoint}\")",
      "async def ${3:function_name}(${4:param}: ${5:str}) -> ${6:dict}:",
      "    \"\"\"${7:Description}.\"\"\"",
      "    return {\"message\": \"$8\"}",
      "$0"
    ],
    "description": "Route FastAPI"
  },
  "Pydantic Model": {
    "prefix": "pydantic",
    "body": [
      "class ${1:ModelName}(BaseModel):",
      "    \"\"\"${2:Description}.\"\"\"",
      "",
      "    ${3:field}: ${4:str}",
      "    $0"
    ],
    "description": "Modèle Pydantic"
  },
  "Main Guard": {
    "prefix": "main",
    "body": [
      "if __name__ == \"__main__\":",
      "    $0"
    ],
    "description": "if __name__ == '__main__'"
  }
}
```

---

## Installation des extensions en ligne de commande

```bash
# Extensions essentielles
code --install-extension ms-python.python  
code --install-extension ms-python.vscode-pylance  
code --install-extension ms-python.mypy-type-checker  
code --install-extension charliermarsh.ruff  

# Extensions utiles
code --install-extension kevinrose.vsc-python-indent  
code --install-extension njpwerner.autodocstring  
code --install-extension yzhang.markdown-all-in-one  
code --install-extension tamasfe.even-better-toml  
```

---

## Fichiers à créer dans `.vscode/`

```
.vscode/
├── settings.json         # Configuration de l'éditeur et des extensions
├── extensions.json       # Extensions recommandées pour le projet
├── launch.json           # Configurations de débogage
├── tasks.json            # Tâches automatisées (tests, lint, format)
└── python.code-snippets  # Snippets personnalisés
```

---

## Configuration PyCharm (alternative)

Si vous utilisez PyCharm, voici les configurations recommandées :

### 1. Interpréteur Python
`Settings` → `Project` → `Python Interpreter` → Sélectionner `venv/bin/python`

### 2. Code Style
`Settings` → `Editor` → `Code Style` → `Python`
- Line length: 88
- Use spaces: oui
- Tab size: 4

### 3. Inspections
`Settings` → `Editor` → `Inspections` → `Python`
- Activer : Type checker (mypy)
- Activer : PEP 8 coding style violation

### 4. Plugins recommandés
- **Ruff** : Linter et formateur intégré
- **Pydantic** : Support avancé des modèles Pydantic

### 5. Outils externes
`Settings` → `Tools` → `External Tools`
- Ajouter Ruff, mypy, pytest

---

## 🎯 Résumé

Ces configurations vous permettent de :
- ✅ Formater et corriger automatiquement avec **Ruff** à la sauvegarde  
- ✅ Vérifier les types en temps réel avec **mypy**  
- ✅ Exécuter les tests avec **pytest** depuis VS Code  
- ✅ Bénéficier d'une auto-complétion intelligente avec **Pylance**  
- ✅ Naviguer facilement dans le code (définitions, références)  
- ✅ Gagner du temps avec les **snippets** personnalisés

**Conseil :** Copiez ces fichiers dans votre projet pour une expérience de développement optimale !
