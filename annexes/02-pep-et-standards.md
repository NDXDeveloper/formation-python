🔝 Retour au [Sommaire](/SOMMAIRE.md)

# Annexe B — Récapitulatif des PEP et standards

Une **PEP** (*Python Enhancement Proposal*) est un document décrivant une évolution proposée du langage ou de son écosystème. Cette annexe synthétise les PEP **réellement utiles** pour comprendre les choix de cette formation, regroupées par thème.

> 💡 Référence officielle : [peps.python.org](https://peps.python.org/). La colonne « Version » indique la version de Python qui a introduit la fonctionnalité (— pour les PEP de processus/conventions).

---

## 🐍 Le langage : syntaxe et fonctionnalités

| PEP | Apport | Version | Chapitre |
|-----|--------|---------|----------|
| **PEP 20** | *The Zen of Python* (`import this`) — la philosophie du langage | — | transversal |
| **PEP 498** | f-strings : `f"{nom}"` | 3.6 | 1.2 |
| **PEP 572** | Opérateur *walrus* `:=` (affectation dans une expression) | 3.8 | 1.3 |
| **PEP 343** | Instruction `with` et gestionnaires de contexte | 2.5 | 4.1, 12.3 |
| **PEP 255 / 342 / 380** | Générateurs, `yield`, puis `yield from` | 2.2 → 3.3 | 5.4 |
| **PEP 492 / 525 / 530** | `async`/`await`, générateurs et compréhensions asynchrones | 3.5-3.6 | 8.2 |
| **PEP 318** | Décorateurs de fonctions et de méthodes (`@`) | 2.4 | 3.4, 5.3 |
| **PEP 3119** | Classes de base abstraites (`abc`, `@abstractmethod`) | 3.0 | 3, 12.3 |
| **PEP 557** | `dataclasses` (`@dataclass`) | 3.7 | 3, 12.3 |
| **PEP 634-636** | *Structural pattern matching* (`match`/`case`) | 3.10 | 1.3 |
| **PEP 703** | *Free-threading* (interpréteur sans GIL), **expérimental** | 3.13 | 8.1, 12.4 |
| **PEP 744** | Compilateur JIT, **expérimental** | 3.13 | 12.4 |

---

## 🏷️ Le typage (annotations de types)

| PEP | Apport | Version | Chapitre |
|-----|--------|---------|----------|
| **PEP 484** | Annotations de types (`def f(x: int) -> str`) | 3.5 | 1.6, 10.6 |
| **PEP 526** | Annotations de variables (`x: int = 0`) | 3.6 | 1.6 |
| **PEP 585** | Génériques natifs : `list[int]` au lieu de `List[int]` | 3.9 | 7.6 |
| **PEP 604** | Unions avec `\|` : `int \| None` au lieu de `Optional[int]` | 3.10 | 7.6 |
| **PEP 612 / 646 / 655** | `ParamSpec`, génériques variadiques, `TypedDict` requis/optionnel | 3.10-3.11 | 7.6 |
| **PEP 695** | Nouvelle syntaxe des génériques et alias `type` | 3.12 | 7.6 |
| **PEP 563 / 649** | Évaluation différée des annotations | 3.7 / 3.14 | 7.6 |

> ⚠️ **Socle de la formation** : Python **3.12+**. On privilégie donc `list[str]`, `dict[str, int]`, `X | None` (PEP 585/604) plutôt que `typing.List`, `typing.Optional`.

---

## 📝 Style et documentation

| PEP | Apport | Chapitre |
|-----|--------|----------|
| **PEP 8** | Guide de style officiel (indentation, nommage, espaces) | 10.5 |
| **PEP 257** | Conventions de *docstrings* | 10.4 |
| **PEP 287** | Docstrings reStructuredText (optionnel) | 10.4 |

Outils qui appliquent ces standards : **Ruff** (lint + format), **Black**, **mypy** *(ch. 10, 12.1)*.

---

## 📦 Packaging et projets

| PEP | Apport | Chapitre |
|-----|--------|----------|
| **PEP 517 / 518** | Système de *build* standardisé via `pyproject.toml` | 12.1, 12.5 |
| **PEP 621** | Métadonnées de projet dans le tableau `[project]` | 12.1, 12.5 |
| **PEP 440** | Schéma de versions ; **PEP 508** : spécification des dépendances | 6.3 |
| **PEP 427 / 660** | Format *wheel* (`.whl`) et installations éditables (`pip install -e`) | 12.5 |
| **PEP 735** | Groupes de dépendances (`[dependency-groups]`) | 12.1 |
| **PEP 405** | Environnements virtuels (`venv`) | 6.4 |

> 💡 Outillage moderne (2026) reposant sur ces PEP : **uv**, **Poetry 2.x**, **hatchling**, **build**/**twine** *(ch. 12.1, 12.5)*.

---

## ⚙️ Le processus Python

| PEP | Apport |
|-----|--------|
| **PEP 1** | Définit ce qu'est une PEP et son cycle de vie |
| **PEP 602** | Cadence de publication **annuelle** (une version mineure par an) |
| **PEP 387** | Politique de rétrocompatibilité et de dépréciation |

**Cycle de versions** : une version de Python est publiée chaque **octobre**, avec ~5 ans de support (2 ans de corrections de bugs, puis sécurité uniquement).

---

## Comment lire une PEP ?

1. **Abstract** : le résumé (lisez-le toujours en premier).
2. **Motivation** : le problème résolu.
3. **Specification** : les détails techniques.
4. **Rationale / Rejected Ideas** : les choix de conception et alternatives écartées.

Les PEP les plus utiles à connaître par cœur pour le quotidien : **PEP 8** (style), **PEP 20** (philosophie), **PEP 484** (typage), **PEP 621** (packaging).

---

🔝 Retour au [Sommaire](/SOMMAIRE.md) · Annexe précédente : [Glossaire](01-glossaire.md) · Annexe suivante : [Aide-mémoire](03-aide-memoire.md) ⏭️
