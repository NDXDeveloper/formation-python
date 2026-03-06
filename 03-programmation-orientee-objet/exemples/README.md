# Exemples - Chapitre 03 : Programmation orientée objet

67 fichiers d'exemples exécutables, répartis sur 5 fichiers source.

## Fichier 01 : Classes et objets (9 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `01_01_premiere_classe.py` | 3.1 | Première classe, `__init__`, attributs d'instance | Rex (Labrador), 3 ans |
| `01_02_methodes_instance.py` | 3.1 | Méthodes d'instance (aboyer, se_presenter, vieillir) | Rex aboie, se présente, vieillit à 4 ans |
| `01_03_attributs_classe.py` | 3.1 | Attributs de classe vs instance | espece=Canis familiaris, nb_pattes=4 partagés |
| `01_04_compte_bancaire.py` | 3.1 | Classe CompteBancaire complète | 1500 -> 1300 -> intérêts 26.00 -> historique |
| `01_05_classe_personne.py` | 3.1 | Classe Personne avec anniversaire et majorité | Alice 30 ans, est_majeur, anniversaire -> 31 |
| `01_06_modification_attributs.py` | 3.1 | Modification directe d'attributs | Voiture change de couleur et kilométrage |
| `01_07_instances_independantes.py` | 3.1 | Instances indépendantes (Compteur) | compteur1=2, compteur2=11 (indépendants) |
| `01_08_bonnes_pratiques.py` | 3.1 | Bonnes pratiques (Livre, Rectangle, Etudiant) | Surface 15/70, moyenne 15.0/16.0 |
| `01_09_gestionnaire_taches.py` | 3.1 | Gestionnaire de tâches complet | 3 tâches, 1/3 terminées, filtrage par priorité |

**Fichier source** : `01-classes-et-objets.md`

## Fichier 02 : Héritage et polymorphisme (10 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `02_01_heritage_base.py` | 3.2 | Héritage de base Animal/Chien | Rex mange, aboie |
| `02_02_hierarchie_employes.py` | 3.2 | Hiérarchie Employe/Developpeur/Manager | Salaire augmenté 45000 -> 49500 |
| `02_03_super_constructeur.py` | 3.2 | super() dans constructeur et méthodes | Rectangle 10*5 = surface 50 |
| `02_04_surcharge_methodes.py` | 3.2 | Surcharge de méthodes (Animal/Chien/Chat/Vache) | Wouf, Miaou, Meuh |
| `02_05_polymorphisme.py` | 3.2 | Polymorphisme des formes géométriques | Cercle 78.54, Carré 16, Triangle 9.0 |
| `02_06_systeme_paiement.py` | 3.2 | Système de paiement polymorphe | 4 types de paiement traités |
| `02_07_isinstance_issubclass.py` | 3.2 | isinstance et issubclass | Vérifications de type True/False |
| `02_08_heritage_multiple.py` | 3.2 | Héritage multiple et MRO | Ordre de résolution des méthodes |
| `02_09_systeme_fichiers.py` | 3.2 | Système de fichiers (Fichier, Dossier) | Taille totale 3000 Ko |
| `02_10_heritage_vs_composition.py` | 3.2 | Héritage vs composition | Comparaison des deux approches |

**Fichier source** : `02-heritage-et-polymorphisme.md`

## Fichier 03 : Méthodes spéciales (10 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `03_01_str_repr.py` | 3.3 | `__str__` et `__repr__` | Personne affichée, Livre avec liste |
| `03_02_operateurs_arithmetiques.py` | 3.3 | `__add__`, `__sub__`, etc. (Vecteur, Nombre) | Vecteur(3,7), Nombre 13/7/30/3.33 |
| `03_03_classe_argent.py` | 3.3 | Classe Argent avec opérateurs | 80.50, 70.50, 100.00 EUR |
| `03_04_comparaisons.py` | 3.3 | Opérateurs de comparaison (Personne) | Tri par âge : Bob 25, Alice 30, Charlie 30 |
| `03_05_len_getitem_setitem.py` | 3.3 | Playlist avec indexation et slicing | Accès par index, slice, del |
| `03_06_iter_next.py` | 3.3 | `__iter__`/`__next__` (Compte, Bibliothèque) | Compte 1-5, itération livres |
| `03_07_contains_call_bool.py` | 3.3 | `__contains__`, `__call__`, `__bool__` | Equipe/Multiplicateur/Panier |
| `03_08_context_manager.py` | 3.3 | `__enter__`/`__exit__` (FichierLog, Chronomètre) | Log écrit, calcul chronométré |
| `03_09_vecteur_complet.py` | 3.3 | Classe Vecteur complète | abs=5.0, toutes les opérations |
| `03_10_fraction.py` | 3.3 | Classe Fraction avec arithmétique | 1/2+1/3=5/6, simplification 4/8=1/2 |

**Fichier source** : `03-methodes-speciales.md`

## Fichier 04 : Propriétés et décorateurs (15 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `04_01_property_base.py` | 3.4 | Problème d'accès direct vs @property | Accès contrôlé à l'âge |
| `04_02_cercle_proprietes.py` | 3.4 | Propriétés en lecture seule (Cercle) | Diamètre, surface, périmètre calculés |
| `04_03_property_setter_deleter.py` | 3.4 | Setter et deleter de propriétés | Temperature °C/°F, Personne avec deleter |
| `04_04_rectangle_proprietes.py` | 3.4 | Rectangle avec propriétés calculées | 5*3=15, 10*4=40, est_carre=True/False |
| `04_05_personne_validation.py` | 3.4 | Validation dans les setters | Nom DUPONT, prénom Marie, email lowercase |
| `04_06_decorateur_base.py` | 3.4 | Premier décorateur (avant/après, chronomètre) | Messages avant/après, temps d'exécution |
| `04_07_decorateur_arguments.py` | 3.4 | Décorateur avec *args et **kwargs | Logger affichant arguments et résultat |
| `04_08_decorateur_cache.py` | 3.4 | Décorateur de cache (mémoïsation) | fibonacci(5)=5 avec cache |
| `04_09_decorateur_validation.py` | 3.4 | Décorateur de validation (positif) | 15 ok, -5 ValueError |
| `04_10_decorateur_compteur.py` | 3.4 | Compteur d'appels de fonction | 3 appels comptés |
| `04_11_decorateur_parametres.py` | 3.4 | Décorateurs avec paramètres | repeter(3), debug(niveau) |
| `04_12_empiler_decorateurs.py` | 3.4 | Empiler décorateurs + décorateur de classe | `<b><i><u>Python</u></i></b>`, Produit #1/#2/#3 |
| `04_13_staticmethod_classmethod.py` | 3.4 | @staticmethod et @classmethod | 8, 28, factory method, Demo comparaison |
| `04_14_exemple_complet_utilisateur.py` | 3.4 | Classe Utilisateur complète | Properties + décorateurs combinés |
| `04_15_functools_wraps.py` | 3.4 | functools.wraps pour métadonnées | __name__ et __doc__ préservés |

**Fichier source** : `04-proprietes-et-decorateurs.md`

## Fichier 05 : Métaclasses et programmation avancée (23 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `05_01_tout_est_objet.py` | 3.5 | Tout est objet en Python | int, str, function, type |
| `05_02_metaclasse_type.py` | 3.5 | La métaclasse par défaut : type | Classe créée avec syntaxe et type() |
| `05_03_creer_classe_type.py` | 3.5 | Créer des classes avec type() | Classe vide, attributs, héritage |
| `05_04_metaclasse_personnalisee.py` | 3.5 | Métaclasses personnalisées | Timestamp, validation faire_bruit |
| `05_05_new_vs_init_metaclasse.py` | 3.5 | `__new__` vs `__init__` dans métaclasses | Ordre de création/initialisation |
| `05_06_singleton_pattern.py` | 3.5 | Singleton Pattern | config1 is config2 = True |
| `05_07_enregistrement_classes.py` | 3.5 | Enregistrement automatique (Registry) | PDFPlugin, ExcelPlugin, ImagePlugin |
| `05_08_conversion_attributs.py` | 3.5 | Conversion noms en majuscules | ATTRIBUT, AUTRE_ATTRIBUT, METHODE |
| `05_09_orm_simple.py` | 3.5 | Mini-ORM avec métaclasse | Utilisateur(nom=Alice...), Produit(nom=Livre...) |
| `05_10_call_metaclasse.py` | 3.5 | `__call__` dans les métaclasses | Interception de la création d'instance |
| `05_11_attributs_dynamiques.py` | 3.5 | Attributs calculés dynamiquement | Valeur différente à chaque accès |
| `05_12_descripteurs.py` | 3.5 | Descripteurs (IntegerField, ValidatedString) | Validation type int, taille min/max |
| `05_13_classes_abstraites.py` | 3.5 | Classes abstraites ABC | Rectangle 15/16, Cercle 50.27/25.13 |
| `05_14_verification_abstraite.py` | 3.5 | Vérification implémentation + propriétés abstraites | Wouf, Je cours, Vitesse max 200 km/h |
| `05_15_init_subclass.py` | 3.5 | `__init_subclass__` (alternative métaclasses) | 3 plugins enregistrés, validation méthodes |
| `05_16_dataclass_base.py` | 3.5 | Dataclass vs classe classique | Point(x=1.0, y=2.0, label='A'), True |
| `05_17_dataclass_parametres.py` | 3.5 | frozen=True, order=True | FrozenInstanceError, versions triées |
| `05_18_dataclass_field.py` | 3.5 | field() et default_factory | Configuration avec options et metadata |
| `05_19_dataclass_post_init.py` | 3.5 | `__post_init__` (champs calculés) | email généré automatiquement |
| `05_20_dataclass_heritage.py` | 3.5 | Héritage de dataclasses | Chien(nom='Rex', age=5, race=...) |
| `05_21_slots.py` | 3.5 | `__slots__` optimisation mémoire | 344 bytes vs 48 bytes |
| `05_22_duck_typing_protocoles.py` | 3.5 | Duck typing et typing.Protocol | Logger avec fake_file, Circle/Square |
| `05_23_bonnes_pratiques.py` | 3.5 | Bonnes pratiques avancées | init_subclass, ABC, slots, MyMeta |

**Fichier source** : `05-metaclasses-et-prog-avancee.md`

## Exécution

Chaque fichier peut être exécuté indépendamment :

```bash
python3 01_01_premiere_classe.py
python3 05_23_bonnes_pratiques.py
```

Pour exécuter tous les fichiers et vérifier qu'il n'y a pas d'erreur :

```bash
for f in *.py; do echo "=== $f ===" && python3 "$f" || echo "ERREUR: $f"; done
```
