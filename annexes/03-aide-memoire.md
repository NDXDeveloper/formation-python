🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Annexe C — Aide-mémoire (*cheat-sheets*)

Rappels condensés des syntaxes et commandes les plus utilisées. Pour les détails, reportez-vous au chapitre indiqué.

> ⚠️ **Note de maintenance** : les commandes d'outils (versions, options) évoluent vite — en cas de doute, la documentation officielle fait foi. Socle de la formation : **Python 3.12+**.
>
> 💡 Chaque ligne de code est **autonome et copiable** (`...` représente du code à compléter).

---

## Structures de données *(ch. 2)*

```python
liste = [1, 2, 3]          # mutable, ordonnée
tuple_ = (1, 2, 3)         # immuable
ensemble = {1, 2, 3}       # valeurs uniques, non ordonnées
dico = {"a": 1, "b": 2}    # paires clé-valeur

liste[0]                   # premier élément
liste[-1]                  # dernier élément
liste[1:3]                 # slice [début:fin]
liste.append(4)            # ajoute à la fin
liste.pop()                # retire et renvoie le dernier
dico.get("c", 0)           # valeur par défaut si clé absente
"a" in dico                # test d'appartenance (O(1) pour dict/set)
```

## Compréhensions *(ch. 2.2)*

```python
[x * 2 for x in xs if x > 0]            # liste
{k: v for k, v in items}                # dictionnaire
{x for x in xs}                         # set
(x * 2 for x in xs)                     # générateur (paresseux)
```

## Chaînes et f-strings *(ch. 1.2, 2.4)*

```python
f"{nom} a {age} ans"                    # interpolation
f"{prix:.2f} €"                         # 2 décimales
f"{n:>10}"                              # alignement à droite sur 10
f"{valeur=}"                            # debug : affiche "valeur=..."
texte.strip().lower()                   # nettoyage + minuscules
texte.split(",")                        # découpe en liste
"-".join(liste)                         # assemble avec un séparateur
texte.replace("a", "b")                 # remplacement
texte.startswith("http")                # test de préfixe

import re
re.findall(r"\d+", texte)               # toutes les suites de chiffres
```

## Fonctions *(ch. 1.4, 5)*

```python
def f(a, b=0, *args, **kwargs):         # positionnels, défaut, variadiques
    ...

carre = lambda x: x * 2                  # fonction anonyme

list(map(str, xs))                       # applique une fonction
list(filter(None, xs))                   # garde les valeurs « vraies »

from functools import reduce, lru_cache, cache
```

## Exceptions *(ch. 1.5, 9)*

```python
try:
    ...
except (ValueError, KeyError) as e:
    ...
else:                          # si aucune exception
    ...
finally:                       # toujours exécuté
    ...

raise ValueError("message") from cause   # chaînage d'exceptions

# Groupes d'exceptions (3.11+) : except* (ne se mélange pas avec except)
try:
    ...
except* TypeError:
    ...
```

## Fichiers et chemins *(ch. 4)*

```python
from pathlib import Path

chemin = Path("data") / "fichier.txt"   # construction de chemin
chemin.exists()                          # le fichier existe-t-il ?
contenu = chemin.read_text(encoding="utf-8")

with open(chemin, "w", encoding="utf-8") as f:
    f.write("contenu")

import json
obj = json.load(f)                       # lecture JSON
json.dump(obj, f)                        # écriture JSON
```

## Programmation orientée objet *(ch. 3)*

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def norme(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

class Enfant(Parent):
    def __init__(self, *args):
        super().__init__(*args)          # appel au parent
```

## Annotations de types *(ch. 1.6, 7.6)*

```python
def f(noms: list[str], age: int | None = None) -> dict[str, int]:
    ...

type Vecteur = list[float]               # alias de type (PEP 695, 3.12+)

from typing import Protocol, TypeVar, Self
```

## Concurrence *(ch. 8)*

```python
import asyncio

async def fetch(u):
    await asyncio.sleep(1)
    return u

async def main():
    return await asyncio.gather(*(fetch(u) for u in urls))

asyncio.run(main())

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor() as ex:         # idéal pour l'E/S
    resultats = list(ex.map(telecharger, urls))
```

---

## 🛠️ Outils en ligne de commande *(ch. 6, 10, 12)*

### uv — gestion de projet (le plus rapide)
```bash
uv init mon_projet         # nouveau projet
uv add requests            # ajoute une dépendance
uv add --dev pytest ruff   # dépendances de développement
uv run python app.py       # exécute dans l'environnement
uv run pytest              # lance les tests
uv sync                    # synchronise depuis le fichier de verrouillage
uv lock                    # met à jour uv.lock
uv python install 3.12     # installe une version de Python
uv build                   # construit sdist + wheel
uv publish                 # publie sur PyPI
uvx ruff check .           # outil ponctuel (sans l'installer)
```

### venv + pip (classique, sans uv) *(ch. 6.4)*
```bash
python -m venv .venv              # crée un environnement virtuel
source .venv/bin/activate         # active (Linux/macOS)
.venv\Scripts\activate            # active (Windows)
pip install requests              # installe un paquet
pip install -r requirements.txt   # installe depuis un fichier
pip freeze > requirements.txt     # fige les versions installées
```

### Ruff — lint + format
```bash
ruff check .               # analyse (linting)
ruff check --fix .         # corrige ce qui peut l'être
ruff format .              # formate (remplace Black)
```

### pytest / mypy
```bash
pytest                     # tous les tests
pytest -v --cov=src        # verbeux + couverture
pytest tests/test_x.py     # un fichier précis
mypy src/                  # vérification des types
```

### Git (essentiel) *(ch. 12.2)*
```bash
git status                 # état du dépôt
git add .                  # prépare toutes les modifications
git commit -m "feat: ..."  # enregistre un commit
git push                   # envoie vers le distant
git switch -c feature/x    # crée et bascule sur une branche
git switch main            # bascule sur main
git merge feature/x        # fusionne une branche
git log --oneline --graph  # historique condensé
git restore <fichier>      # annule les modifications non indexées
git revert <hash>          # annule un commit (par un nouveau commit)
```

---

## 📊 NumPy *(ch. 13.1)*

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
np.zeros((2, 3))           # tableau de zéros
np.arange(0, 10, 2)        # 0,2,4,6,8
a.shape                    # dimensions (lignes, colonnes)
a.dtype                    # type des éléments
a * 2                      # opération vectorisée (élément par élément)
a @ b                      # produit matriciel
a.sum(axis=0)              # somme par colonne
a[a > 2]                   # masque booléen

rng = np.random.default_rng()   # générateur moderne (recommandé)
rng.integers(0, 10, 5)          # 5 entiers dans [0, 10[
```

## 🐼 pandas *(ch. 13.2)*

```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head()                  # premières lignes
df.info()                  # types et valeurs manquantes
df.describe()              # statistiques descriptives
df["col"]                  # une colonne (Series)
df[["a", "b"]]             # plusieurs colonnes
df[df["age"] > 18]         # filtrage par condition
df.loc[i, "col"]           # accès par étiquette
df.iloc[0]                 # accès par position
df["x"] = df["a"] * df["b"]              # nouvelle colonne
df.groupby("ville")["ventes"].sum()      # agrégation par groupe
df.isnull().sum()          # NaN par colonne
df["c"] = df["c"].fillna(df["c"].mean()) # remplissage par la moyenne
df.merge(autre, on="id")   # jointure type SQL
df.sort_values("col", ascending=False)   # tri
```

> ⚠️ **pandas 3.0+** : l'assignation chaînée avec `inplace=True` ne fonctionne plus (Copy-on-Write). Préférez **la réassignation** : `df["c"] = df["c"].fillna(0)`.

---

🔝 Retour au [Sommaire](/SOMMAIRE.md) · Annexe précédente : [PEP et standards](02-pep-et-standards.md) · Annexe suivante : [Pour aller plus loin](04-pour-aller-plus-loin.md) ⏭️
