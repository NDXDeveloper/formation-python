# 🐍 Formation Python - Du Débutant à l'Avancé

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Modules](https://img.shields.io/badge/Modules-13-brightgreen.svg)
![Language](https://img.shields.io/badge/Langue-Français-blue.svg)
![Status](https://img.shields.io/badge/Status-Actif-success.svg)

**Formation complète Python 3, des fondamentaux jusqu'aux concepts avancés (FastAPI, Data Science, Type Hints).**

![Python Banner](https://www.python.org/static/community_logos/python-logo-generic.svg)

---

## 📖 Table des matières

- [À propos](#-à-propos)
- [Contenu](#-contenu-de-la-formation)
- [Installation](#-démarrage-rapide)
- [Structure](#-structure-du-projet)
- [Utilisation](#-comment-utiliser-cette-formation)
- [Technologies](#-technologies-couvertes)
- [Licence](#-licence)
- [Contact](#-contact)

---

## 📋 À propos

Formation progressive et complète sur **Python 3** couvrant l'intégralité du langage, des bases jusqu'aux techniques professionnelles les plus récentes. Conçue pour les débutants comme pour les développeurs expérimentés souhaitant se perfectionner.

**✨ Points clés :**
- 📚 **13 modules progressifs** du niveau débutant à expert
- 🎯 **75+ sujets** couverts avec exemples concrets
- 🆕 **Technologies modernes** (FastAPI, Type Hints, Poetry, SQLAlchemy)
- 📊 **Module Data Science** complet (NumPy, Pandas, Matplotlib)
- 🔥 **Édition 2025-2026** avec les dernières pratiques Python
- 🇫🇷 **100% en français** et gratuit (MIT License)

**Durée estimée :** 40-60 heures • **Niveau :** Tous niveaux • **Prérequis :** Aucun

---

## 📚 Contenu de la formation

### 🎓 Modules Fondamentaux (1-4)

**Module 1 : Fondamentaux** - Installation, variables, structures de contrôle, fonctions, gestion des erreurs, **Type Hints** 🆕  
**Module 2 : Structures de données** - Listes, dicts, sets, compréhensions, collections spécialisées  
**Module 3 : POO** - Classes, héritage, polymorphisme, méthodes spéciales, métaclasses  
**Module 4 : Fichiers** - Lecture/écriture, JSON/CSV/XML, sérialisation (pickle), pathlib  

### 🚀 Modules Intermédiaires (5-8)

**Module 5 : Programmation fonctionnelle** - Lambda, map/filter/reduce, décorateurs, générateurs, closures  
**Module 6 : Modules** - Packages, pip, venv, **Poetry/Pipenv** 🆕  
**Module 7 : Bibliothèques standard** - os/sys, datetime, math/random, itertools, logging, **typing avancé** 🆕  
**Module 8 : Concurrence** - Threading, multiprocessing, asyncio, patterns  

### 🎯 Modules Avancés (9-13)

**Module 9 : Débogage** - Exceptions, debugging, profiling, optimisation  
**Module 10 : Tests** - unittest, pytest, mocking, couverture de code, documentation, PEP 8, **mypy** 🆕  
**Module 11 : Web/APIs** - **FastAPI** 🆕, Flask, REST, **SQLAlchemy** 🆕  
**Module 12 : Bonnes pratiques** - Architecture, Git, design patterns, optimisation, déploiement  
**Module 13 : Data Science** 📊 - **NumPy, Pandas, Matplotlib/Plotly** 🆕 *(optionnel)*  

> 📋 Consultez [SOMMAIRE.md](SOMMAIRE.md) pour la table des matières complète

---

## 🚀 Démarrage rapide

### Installation de Python

```bash
# Vérifier la version de Python
python --version  # ou python3 --version

# Télécharger Python 3.10+ (recommandé : 3.13+)
# 🌐 https://www.python.org/downloads/
```

### Configuration de l'environnement

```bash
# Cloner cette formation
git clone https://github.com/NDXDeveloper/formation-python.git  
cd formation-python  

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
source venv/bin/activate      # 🐧 Linux/Mac
# venv\Scripts\activate       # 🪟 Windows

# Installer les dépendances avec pip
pip install fastapi uvicorn flask requests sqlalchemy pydantic  # Modules web  
pip install numpy pandas matplotlib plotly                       # Modules data science  
```

### Alternative avec Poetry (recommandé)

```bash
# Installer Poetry (si pas encore installé)
pip install poetry

# Installer toutes les dépendances
poetry install --all-extras

# Ou seulement les dépendances web
poetry install -E web

# Ou seulement les dépendances data science
poetry install -E data
```

### Votre premier programme

```python
# 👋 hello.py
def saluer(nom: str) -> str:
    """Retourne un message de bienvenue personnalisé."""
    return f"Bonjour {nom}, bienvenue dans Python ! 🐍"

if __name__ == "__main__":
    print(saluer("Développeur"))
```

```bash
python hello.py
# Sortie : Bonjour Développeur, bienvenue dans Python ! 🐍
```

---

## 📁 Structure du projet

```
formation-python-complete/
├── 📄 README.md
├── 📋 SOMMAIRE.md (table des matières détaillée)
├── 🛠️ VSCODE-SETUP.md (configuration VS Code)
├── 📜 LICENSE
├── 📦 pyproject.toml (dépendances Poetry)
├── 📂 01-fondamentaux-et-syntaxe/
│   ├── README.md
│   ├── 01-installation-et-configuration.md
│   ├── 02-variables-types-et-operateurs.md
│   └── ...
├── 📂 02-structures-de-donnees/
├── 📂 03-programmation-orientee-objet/
├── 📂 04-gestion-donnees-et-fichiers/
├── 📂 05-programmation-fonctionnelle/
├── 📂 06-modules-et-packages/
├── 📂 07-bibliotheques-standard/
├── 📂 08-programmation-concurrente/
├── 📂 09-erreurs-et-debogage/
├── 📂 10-tests-et-qualite/
├── 📂 11-developpement-web-et-apis/
├── 📂 12-projets-et-bonnes-pratiques/
└── 📂 13-introduction-data-science/ (optionnel)
```

---

## 🎯 Comment utiliser cette formation

### 🌱 Débutant complet
👉 Commencez par le [Module 1](01-fondamentaux-et-syntaxe/) et suivez l'ordre chronologique

### 🌿 Développeur intermédiaire
👉 Sautez au [Module 5](05-programmation-fonctionnelle/) ou [Module 8](08-programmation-concurrente/)

### 🌳 Développeur avancé
👉 Explorez les modules avancés : [Module 11 (FastAPI)](11-developpement-web-et-apis/) ou [Module 13 (Data Science)](13-introduction-data-science/)

### 📚 Besoin d'une référence rapide
👉 Consultez le [SOMMAIRE.md](SOMMAIRE.md) avec tous les liens

**💡 Conseil :** Créez un dossier d'entraînement et testez tous les exemples de code !

```bash
mkdir mon-apprentissage-python  
cd mon-apprentissage-python  
python -m venv venv  
source venv/bin/activate  
```

---

## 🗓️ Parcours suggéré

| Niveau | Modules | Durée | Objectif |
|--------|---------|-------|----------|
| 🌱 **Débutant** | 1-4 | 12-15h | Maîtriser la syntaxe et les structures |
| 🌿 **Intermédiaire** | 5-8 | 15-20h | POO, fonctionnel, concurrence |
| 🌳 **Avancé** | 9-12 | 15-20h | Tests, web, APIs, bonnes pratiques |
| 📊 **Spécialisation** | 13 | 10-15h | Data Science (optionnel) |

---

## 🛠️ Technologies couvertes

### Langage & Outils
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Type Hints](https://img.shields.io/badge/Type_Hints-mypy-blue)
![Poetry](https://img.shields.io/badge/Poetry-Package_Manager-60A5FA)

### Frameworks Web
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?logo=flask&logoColor=white)

### Données & ORM
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243?logo=numpy&logoColor=white)

### Tests & Qualité
![pytest](https://img.shields.io/badge/pytest-7.0+-0A9EDC?logo=pytest&logoColor=white)
![mypy](https://img.shields.io/badge/mypy-Type_Checker-blue)

### Visualisation
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-11557c)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-3F4F75?logo=plotly&logoColor=white)

---

## 🎓 Ce que vous apprendrez

✅ Écrire du code Python propre, maintenable et professionnel  
✅ Maîtriser la **POO** et les **design patterns**  
✅ Créer des **APIs REST modernes** avec FastAPI  
✅ Gérer les bases de données avec **SQLAlchemy**  
✅ Écrire des **tests unitaires** et assurer la qualité du code  
✅ Utiliser le **typage statique** (Type Hints + mypy)  
✅ Développer des applications **asynchrones** performantes  
✅ Analyser des données avec **NumPy** et **Pandas**  
✅ Créer des visualisations avec **Matplotlib** et **Plotly**  
✅ Suivre les **bonnes pratiques** de l'industrie

---

## 💡 Exemple de code moderne

```python
# Module 11 : FastAPI + Type Hints + SQLAlchemy
from fastapi import FastAPI, Depends, HTTPException  
from sqlalchemy.orm import Session  
from pydantic import BaseModel  

app = FastAPI()

class Utilisateur(BaseModel):
    id: int
    nom: str
    email: str

@app.get("/utilisateurs", response_model=list[Utilisateur])
async def obtenir_utilisateurs(db: Session = Depends(get_db)):
    """Récupère tous les utilisateurs de la base de données."""
    utilisateurs = db.query(UtilisateurModel).all()
    return utilisateurs

@app.post("/utilisateurs", response_model=Utilisateur, status_code=201)
async def creer_utilisateur(user: Utilisateur, db: Session = Depends(get_db)):
    """Crée un nouvel utilisateur avec validation Pydantic."""
    db_user = UtilisateurModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    return db_user
```

---

## ❓ FAQ

**Q : Dois-je avoir des connaissances préalables en programmation ?**
R : Non ! Le Module 1 commence vraiment à zéro. Si vous avez déjà programmé dans un autre langage, vous progresserez plus vite.

**Q : Combien de temps faut-il pour terminer la formation ?**
R : Entre 40 et 60 heures selon votre rythme. Comptez 4-8 semaines à raison de 1-2h par jour.

**Q : Le Module 13 (Data Science) est-il obligatoire ?**
R : Non, c'est un module optionnel pour ceux qui s'intéressent à l'analyse de données.

**Q : Puis-je utiliser cette formation pour enseigner ?**
R : Oui ! La licence MIT vous permet d'utiliser, modifier et partager ce contenu librement.

**Q : Quelle version de Python dois-je utiliser ?**
R : Python 3.10 ou supérieur est recommandé. Les exemples utilisent la syntaxe moderne (type hints natifs comme `list[str]`, `dict[str, int]`, match/case, etc.). Python 3.13+ est idéal pour bénéficier des dernières améliorations.

---

## 📚 Ressources complémentaires

### Documentation officielle
- 📖 [Documentation Python](https://docs.python.org/fr/3/)
- 📘 [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- 📦 [PyPI - Python Package Index](https://pypi.org/)

### Tutoriels et communautés
- 🎓 [Real Python](https://realpython.com/)
- 💬 [r/learnpython](https://www.reddit.com/r/learnpython/)
- 🐦 [Python France](https://www.python.org/community/user-groups/france/)

### Outils recommandés
- 💻 **IDE** : [VS Code](https://code.visualstudio.com/) + [Extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- 💻 **IDE** : [PyCharm Community](https://www.jetbrains.com/pycharm/)
- 🔧 **Linting** : [Ruff](https://github.com/astral-sh/ruff) (ultra-rapide)

---

## 📝 Licence

Ce projet est sous licence **MIT**.

✅ Vous êtes libre d'utiliser, modifier, distribuer et utiliser commercialement ce contenu.

Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👨‍💻 Auteur

**Nicolas DEOUX**

- 📧 Email : [NDXDev@gmail.com](mailto:NDXDev@gmail.com)
- 💼 LinkedIn : [Nicolas DEOUX](https://www.linkedin.com/in/nicolas-deoux-ab295980/)
- 🐙 GitHub : [GitHub @NDXDeveloper](https://github.com/NDXDeveloper)

---

## 🙏 Remerciements

Merci à la communauté Python, aux créateurs de frameworks open source (FastAPI, Flask, Django), et à tous ceux qui rendent Python accessible et puissant ! 🎉

**Ressources qui ont inspiré cette formation :**
[Automate the Boring Stuff](https://automatetheboringstuff.com/) • [Python Crash Course](https://nostarch.com/pythoncrashcourse2e) • [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

<div align="center">

**🐍 Bon apprentissage avec Python ! 🐍**

[![Python](https://img.shields.io/badge/Made_with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Love](https://img.shields.io/badge/Made_with-❤️-red)](https://github.com/NDXDeveloper)

**[⬆ Retour en haut](#-formation-python---du-débutant-à-lavancé)**

*Dernière mise à jour : Mars 2026*

</div>
