# 🐍 Formation Python 3 - Développeur Avancé

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Formation complète et pratique pour maîtriser Python 3**

[🚀 Commencer](/SOMMAIRE.md)

## 📚 À propos

Formation progressive de **12 modules** avec exemples pratiques, exercices et projets pour devenir développeur Python avancé.

**✨ Points forts :** 60+ sujets • Guides markdown détaillés • Projets réels • Exercices corrigés

## 🎯 Objectifs

À la fin de cette formation :
- ✅ Maîtriser la syntaxe Python et les bonnes pratiques
- ✅ Développer des applications robustes (POO, tests, debug)
- ✅ Créer des APIs web et gérer la programmation concurrente
- ✅ Optimiser les performances et déployer des projets

## 📖 Modules

| Module | Sujet |
|--------|-------|
| **1-2** | Fondamentaux & Structures de données |
| **3-4** | POO & Gestion des fichiers |
| **5-6** | Programmation fonctionnelle & Modules |
| **7-8** | Bibliothèques standard & Concurrence |
| **9-10** | Debug & Tests |
| **11-12** | Web/APIs & Projets pratiques |


> 📋 [SOMMAIRE.md](SOMMAIRE.md) pour le programme détaillé

## 🚀 Installation

```bash
git clone https://github.com/NDXdev/formation-python.git
cd formation-python

# Environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

## 🗂️ Structure

```
formation-python/
├── 📚 docs/           # Guides markdown
├── 💻 examples/       # Code d'exemple
├── 🧪 exercises/      # Exercices + solutions
├── 🚀 projects/       # Projets pratiques
└── 📋 SOMMAIRE.md     # Programme détaillé
```

## 🛠️ Prérequis

- 🐍 **Python 3.8+** (recommandé : 3.11+)
- 💻 **Éditeur** (VS Code, PyCharm...)
- 📚 **Bases programmation** (variables, boucles, fonctions)

## 💡 Exemple rapide

```python
# Compréhensions + Collections (Modules 2.2-2.3)
from collections import Counter

# Analyser la fréquence des mots
texte = "python est génial python rocks"
mots = texte.split()
freq = Counter(mots)
print(freq.most_common())  # [('python', 2), ('est', 1), ...]

# Filtrer avec compréhension
mots_longs = [mot for mot in mots if len(mot) > 4]
print(mots_longs)  # ['python', 'génial', 'python']
```

## 📚 Ressources

- 📖 [Documentation Python](https://docs.python.org/3/)
- 🎨 [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- 📦 [PyPI - Packages](https://pypi.org/)



## 📄 Licence

MIT License - voir [LICENSE](LICENSE)

## 👤 Auteur

**Nicolas DEOUX** - [NDXdev@gmail.com](mailto:NDXdev@gmail.com) - [@NDXdev](https://github.com/NDXdev)

---

⭐ **Si cette formation vous aide, donnez une étoile au repo !** ⭐
