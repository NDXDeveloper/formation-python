# Configuration VS Code pour Python

## Fichier `.vscode/settings.json`

Créer ce fichier à la racine du projet pour une configuration optimale :

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": [
    "--line-length=88"
  ],
  
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": false,
  "python.linting.mypyEnabled": true,
  "python.linting.mypyArgs": [
    "--ignore-missing-imports",
    "--follow-imports=silent",
    "--show-column-numbers"
  ],
  
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": [
    "tests"
  ],
  
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    },
    "editor.rulers": [88],
    "editor.tabSize": 4
  },
  
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

## Extensions VS Code recommandées

Créer le fichier `.vscode/extensions.json` :

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.black-formatter",
    "charliermarsh.ruff",
    "kevinrose.vsc-python-indent",
    "njpwerner.autodocstring",
    "yzhang.markdown-all-in-one",
    "tamasfe.even-better-toml",
    "github.copilot"
  ]
}
```

## Raccourcis utiles VS Code

| Raccourci | Action |
|-----------|--------|
| `Ctrl+Shift+P` | Palette de commandes |
| `F5` | Déboguer le fichier courant |
| `Shift+Alt+F` | Formater le document |
| `Ctrl+Shift+I` | Organiser les imports |
| `F12` | Aller à la définition |
| `Shift+F12` | Trouver toutes les références |
| `Ctrl+Space` | Suggestions IntelliSense |
| `Ctrl+\`` | Ouvrir le terminal intégré |

## Configuration Git dans VS Code

Créer le fichier `.vscode/tasks.json` pour automatiser les tâches :

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
      }
    },
    {
      "label": "Type Check",
      "type": "shell",
      "command": "mypy .",
      "group": "test"
    },
    {
      "label": "Format Code",
      "type": "shell",
      "command": "black .",
      "group": "build"
    }
  ]
}
```

## Snippets Python personnalisés

Créer le fichier `.vscode/python.code-snippets` :

```json
{
  "Type Hint Function": {
    "prefix": "deff",
    "body": [
      "def ${1:function_name}(${2:arg}: ${3:str}) -> ${4:None}:",
      "    \"\"\"${5:Description}\"\"\"",
      "    $0"
    ],
    "description": "Fonction avec type hints"
  },
  "FastAPI Route": {
    "prefix": "fastapi",
    "body": [
      "@app.${1|get,post,put,delete|}(\"/${2:endpoint}\")",
      "async def ${3:function_name}(${4:param}: ${5:str}) -> ${6:dict}:",
      "    \"\"\"${7:Description}\"\"\"",
      "    return {\"message\": \"$8\"}",
      "$0"
    ],
    "description": "Route FastAPI"
  },
  "Pydantic Model": {
    "prefix": "pydantic",
    "body": [
      "class ${1:ModelName}(BaseModel):",
      "    \"\"\"${2:Description}\"\"\"",
      "    ${3:field}: ${4:str}",
      "    $0"
    ],
    "description": "Modèle Pydantic"
  }
}
```

## Installation des extensions en ligne de commande

```bash
# Extensions essentielles
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.black-formatter
code --install-extension charliermarsh.ruff

# Extensions utiles
code --install-extension njpwerner.autodocstring
code --install-extension yzhang.markdown-all-in-one
code --install-extension tamasfe.even-better-toml
```

## Fichiers à créer dans `.vscode/`

```
.vscode/
├── settings.json       # Configuration de l'éditeur
├── extensions.json     # Extensions recommandées
├── tasks.json          # Tâches automatisées
└── python.code-snippets # Snippets personnalisés
```

## Configuration PyCharm alternative

Si vous utilisez PyCharm, voici les configurations recommandées :

### 1. Interpréteur Python
`Settings` → `Project` → `Python Interpreter` → Sélectionner `venv/bin/python`

### 2. Code Style
`Settings` → `Editor` → `Code Style` → `Python`
- Line length: 88
- Use spaces: ✓
- Tab size: 4

### 3. Inspections
`Settings` → `Editor` → `Inspections` → `Python`
- Enable: Type checker (mypy)
- Enable: PEP 8 coding style violation

### 4. Tools externes
`Settings` → `Tools` → `External Tools`
- Ajouter Black, mypy, pytest

---

## 🎯 Résumé

Ces configurations vous permettent de :
- ✅ Formater automatiquement avec Black
- ✅ Vérifier les types avec mypy
- ✅ Exécuter les tests avec pytest
- ✅ Auto-complétion intelligente avec Pylance
- ✅ Navigation facile dans le code
- ✅ Snippets pour gagner du temps

**Conseil** : Copiez ces fichiers dans votre projet pour une expérience de développement optimale !
