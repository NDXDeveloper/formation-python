# Exemples - Chapitre 01 : Fondamentaux et syntaxe

Ce dossier contient **84 fichiers** d'exemples exécutables correspondant aux 6 sections du chapitre 01.

## Exécution

```bash
python3 nom_du_fichier.py
```

Certains fichiers contiennent des exemples interactifs (utilisant `input()`). Pour les exécuter :

```bash
python3 nom_du_fichier.py --interactif
```

## Prérequis

- Python 3.10+ (pour la syntaxe `match/case` et `type | None`)

---

## 01 - Installation et configuration

| Fichier | Description | Source |
|---------|-------------|--------|
| `01_01_bonjour_python.py` | Premier programme : print("Bonjour, Python !") | 01-installation-et-configuration.md |
| `01_02_premier_programme.py` | Programme hello.py avec deux print | 01-installation-et-configuration.md |

---

## 02 - Variables, types et opérateurs

| Fichier | Description | Source |
|---------|-------------|--------|
| `02_01_creation_variables.py` | Créer, utiliser et modifier des variables | 02-variables-types-et-operateurs.md |
| `02_02_regles_nommage.py` | Règles de nommage, noms valides et invalides | 02-variables-types-et-operateurs.md |
| `02_03_nombres_entiers.py` | Type int, grands nombres, underscores | 02-variables-types-et-operateurs.md |
| `02_04_nombres_flottants.py` | Type float, précision, notation scientifique | 02-variables-types-et-operateurs.md |
| `02_05_chaines_caracteres.py` | Chaînes : concaténation, indexing, méthodes | 02-variables-types-et-operateurs.md |
| `02_06_booleens.py` | Booléens et conversions | 02-variables-types-et-operateurs.md |
| `02_07_type_none.py` | Le type None | 02-variables-types-et-operateurs.md |
| `02_08_verifier_type.py` | Fonction type() | 02-variables-types-et-operateurs.md |
| `02_09_conversion_types.py` | Casting : int(), float(), str(), bool() | 02-variables-types-et-operateurs.md |
| `02_10_operateurs_arithmetiques.py` | Opérateurs +, -, *, /, //, %, ** et assignation composée | 02-variables-types-et-operateurs.md |
| `02_11_operateurs_comparaison.py` | Opérateurs ==, !=, >, <, >=, <= | 02-variables-types-et-operateurs.md |
| `02_12_operateurs_logiques.py` | and, or, not et tables de vérité | 02-variables-types-et-operateurs.md |
| `02_13_operateurs_appartenance.py` | Opérateurs in et not in | 02-variables-types-et-operateurs.md |
| `02_14_operateurs_identite.py` | Opérateurs is et is not | 02-variables-types-et-operateurs.md |
| `02_15_entree_utilisateur.py` | Fonction input() (--interactif) | 02-variables-types-et-operateurs.md |
| `02_16_formatage_chaines.py` | Concaténation, format(), f-strings | 02-variables-types-et-operateurs.md |
| `02_17_commentaires.py` | Commentaires en ligne et multi-lignes | 02-variables-types-et-operateurs.md |
| `02_18_conventions_pep8.py` | Conventions PEP 8 | 02-variables-types-et-operateurs.md |
| `02_19_erreurs_courantes.py` | Erreurs fréquentes : = vs ==, conversions, etc. | 02-variables-types-et-operateurs.md |

---

## 03 - Structures de contrôle

| Fichier | Description | Source |
|---------|-------------|--------|
| `03_01_instruction_if.py` | Instruction if de base | 03-structures-de-controle.md |
| `03_02_instruction_else.py` | Instruction if/else | 03-structures-de-controle.md |
| `03_03_instruction_elif.py` | Instruction elif pour conditions multiples | 03-structures-de-controle.md |
| `03_04_conditions_multiples.py` | Combinaison de conditions avec and, or, not | 03-structures-de-controle.md |
| `03_05_conditions_imbriquees.py` | Conditions imbriquées | 03-structures-de-controle.md |
| `03_06_operateur_ternaire.py` | Expression conditionnelle (ternaire) | 03-structures-de-controle.md |
| `03_07_boucle_while.py` | Boucle while avec compteur, somme, etc. | 03-structures-de-controle.md |
| `03_08_boucle_for.py` | Boucle for, range(), enumerate(), zip() | 03-structures-de-controle.md |
| `03_09_for_vs_while.py` | Comparaison for vs while | 03-structures-de-controle.md |
| `03_10_instruction_break.py` | Instruction break | 03-structures-de-controle.md |
| `03_11_instruction_continue.py` | Instruction continue | 03-structures-de-controle.md |
| `03_12_instruction_pass.py` | Instruction pass | 03-structures-de-controle.md |
| `03_13_boucles_imbriquees.py` | Boucles imbriquées et tables de multiplication | 03-structures-de-controle.md |
| `03_14_else_avec_boucles.py` | Clause else avec for et while | 03-structures-de-controle.md |
| `03_15_match_case.py` | Pattern matching (Python 3.10+) | 03-structures-de-controle.md |
| `03_16_bonnes_pratiques.py` | Bonnes pratiques des structures de contrôle | 03-structures-de-controle.md |
| `03_17_exemples_pratiques.py` | Exemples pratiques : nombres premiers, Pascal, PGCD (--interactif) | 03-structures-de-controle.md |
| `03_18_piege_range.py` | Piège courant avec range() | 03-structures-de-controle.md |

---

## 04 - Fonctions et portée

| Fichier | Description | Source |
|---------|-------------|--------|
| `04_01_fonction_simple.py` | Définir et appeler une fonction simple | 04-fonctions-et-portee.md |
| `04_02_fonctions_parametres.py` | Fonctions avec paramètres | 04-fonctions-et-portee.md |
| `04_03_instruction_return.py` | Instruction return et retours multiples | 04-fonctions-et-portee.md |
| `04_04_parametres_defaut.py` | Paramètres avec valeurs par défaut | 04-fonctions-et-portee.md |
| `04_05_arguments_nommes.py` | Arguments nommés (keyword arguments) | 04-fonctions-et-portee.md |
| `04_06_args_kwargs.py` | *args et **kwargs | 04-fonctions-et-portee.md |
| `04_07_docstrings.py` | Documentation avec docstrings | 04-fonctions-et-portee.md |
| `04_08_portee_variables.py` | Portée des variables (locale, globale, LEGB) | 04-fonctions-et-portee.md |
| `04_09_fonctions_imbriquees.py` | Fonctions imbriquées et closures | 04-fonctions-et-portee.md |
| `04_10_fonctions_premiere_classe.py` | Fonctions comme objets de première classe | 04-fonctions-et-portee.md |
| `04_11_fonctions_recursives.py` | Récursivité : factorielle, fibonacci, somme | 04-fonctions-et-portee.md |
| `04_12_fonctions_lambda.py` | Fonctions lambda | 04-fonctions-et-portee.md |
| `04_13_annotations_type.py` | Annotations de type pour les fonctions | 04-fonctions-et-portee.md |
| `04_14_exemples_pratiques.py` | Exemples : email, prix, mot de passe, statistiques | 04-fonctions-et-portee.md |
| `04_15_erreur_mutable_defaut.py` | Piège des paramètres mutables par défaut | 04-fonctions-et-portee.md |

---

## 05 - Gestion des erreurs

| Fichier | Description | Source |
|---------|-------------|--------|
| `05_01_exceptions_courantes.py` | Exceptions courantes : TypeError, ValueError, etc. | 05-gestion-des-erreurs.md |
| `05_02_try_except_base.py` | try/except de base | 05-gestion-des-erreurs.md |
| `05_03_exceptions_specifiques.py` | Capturer des exceptions spécifiques | 05-gestion-des-erreurs.md |
| `05_04_details_exception.py` | Accéder aux détails d'une exception (as e) | 05-gestion-des-erreurs.md |
| `05_05_clause_else.py` | Clause else avec try/except | 05-gestion-des-erreurs.md |
| `05_06_clause_finally.py` | Clause finally pour le nettoyage | 05-gestion-des-erreurs.md |
| `05_07_raise.py` | Lever des exceptions avec raise | 05-gestion-des-erreurs.md |
| `05_08_exceptions_personnalisees.py` | Créer des exceptions personnalisées | 05-gestion-des-erreurs.md |
| `05_09_hierarchie_exceptions.py` | Hiérarchie des exceptions Python | 05-gestion-des-erreurs.md |
| `05_10_validation_donnees.py` | Validation de données avec exceptions | 05-gestion-des-erreurs.md |
| `05_11_gestionnaire_config.py` | Gestionnaire de configuration JSON | 05-gestion-des-erreurs.md |
| `05_12_eafp_vs_lbyl.py` | EAFP vs LBYL : deux philosophies | 05-gestion-des-erreurs.md |
| `05_13_assertions.py` | Assertions pour le débogage | 05-gestion-des-erreurs.md |
| `05_14_bonnes_pratiques.py` | Bonnes pratiques de gestion des erreurs | 05-gestion-des-erreurs.md |

---

## 06 - Type hints et annotations

| Fichier | Description | Source |
|---------|-------------|--------|
| `06_01_type_hints_base.py` | Introduction : typage dynamique, annotations de base | 06-type-hints-et-annotations.md |
| `06_02_types_generiques.py` | Collections typées : list, dict, tuple, set | 06-type-hints-et-annotations.md |
| `06_03_types_optionnels_unions.py` | Type \| None, unions de types | 06-type-hints-et-annotations.md |
| `06_04_any_callable.py` | Any, object et Callable | 06-type-hints-et-annotations.md |
| `06_05_type_aliases.py` | Alias de types : Vector, Matrix, JSON | 06-type-hints-et-annotations.md |
| `06_06_typeddict.py` | TypedDict : dictionnaires avec structure fixe | 06-type-hints-et-annotations.md |
| `06_07_generiques.py` | Génériques : TypeVar, Generic, classe Pile | 06-type-hints-et-annotations.md |
| `06_08_literal_final.py` | Literal pour valeurs exactes, Final pour constantes | 06-type-hints-et-annotations.md |
| `06_09_classvar.py` | ClassVar pour attributs de classe | 06-type-hints-et-annotations.md |
| `06_10_valeurs_defaut_args.py` | Valeurs par défaut et annotations *args/**kwargs | 06-type-hints-et-annotations.md |
| `06_11_comprehensions.py` | Type hints dans les compréhensions | 06-type-hints-et-annotations.md |
| `06_12_forward_references.py` | Forward references et __future__ annotations | 06-type-hints-et-annotations.md |
| `06_13_gestionnaire_utilisateurs.py` | Exemple pratique : gestion d'utilisateurs (dataclass) | 06-type-hints-et-annotations.md |
| `06_14_statistiques.py` | Exemple pratique : calculateur de statistiques | 06-type-hints-et-annotations.md |
| `06_15_cache_generique.py` | Exemple pratique : cache générique avec expiration | 06-type-hints-et-annotations.md |
| `06_16_bonnes_pratiques.py` | Bonnes pratiques des type hints | 06-type-hints-et-annotations.md |
