# Exemples - Chapitre 04 : Gestion des données et fichiers

35 fichiers d'exemples exécutables, répartis sur 4 fichiers source.

## Fichier 01 : Lecture et écriture de fichiers (7 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `01_01_lecture_fichier.py` | 4.1 | Quatre méthodes de lecture (read, readline, readlines, itération) | 3 lignes lues de 4 manières différentes |
| `01_02_ecriture_fichier.py` | 4.1 | Mode 'w' (écrasement), mode 'a' (ajout), writelines() | 2 lignes, puis 4 lignes, liste de courses |
| `01_03_gestionnaire_contexte.py` | 4.1 | with pour ouverture/fermeture automatique, transformation | Texte en minuscules transformé en majuscules |
| `01_04_gestion_erreurs.py` | 4.1 | try/except FileNotFoundError, PermissionError | "Le fichier n'existe pas !" |
| `01_05_fichiers_binaires.py` | 4.1 | Écriture, lecture, copie, lecture par morceaux de binaires | 6 octets, copie, 1024+1024+512 octets |
| `01_06_verifier_existence.py` | 4.1 | pathlib.Path exists(), is_file(), stat() | Existe, fichier, 16 octets |
| `01_07_exemples_pratiques.py` | 4.1 | Compter mots, log, CSV simple, sauvegarder/relire liste | 11 mots, 3 logs, 3 lignes CSV, 4 noms |

**Fichier source** : `01-lecture-ecriture-fichiers.md`

## Fichier 02 : Formats de données JSON, CSV, XML (10 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `02_01_json_lire_ecrire.py` | 4.2 | json.load() et json.dump() | Dupont, 28, compétences, fichier JSON indenté |
| `02_02_json_conversion.py` | 4.2 | json.dumps() et json.loads() sans fichier | JSON string, dict Python |
| `02_03_json_liste_erreurs.py` | 4.2 | Liste de personnes, gestion erreurs JSON | 3 personnes, FileNotFoundError, JSONDecodeError |
| `02_04_csv_lecture.py` | 4.2 | csv.reader() et csv.DictReader() | 3 employés avec colonnes nommées |
| `02_05_csv_ecriture.py` | 4.2 | csv.writer() et csv.DictWriter() | Fichiers CSV avec en-têtes |
| `02_06_csv_delimiteurs_filtrage.py` | 4.2 | Délimiteur point-virgule, filtrage par service | 2 informaticiens exportés |
| `02_07_xml_lecture.py` | 4.2 | Parser un fichier XML avec ElementTree | 2 livres avec ID, titre, auteur, prix |
| `02_08_xml_ecriture.py` | 4.2 | Construire et sauvegarder un arbre XML | XML indenté avec 2 livres |
| `02_09_xml_modification_xpath.py` | 4.2 | Modifier XML, recherche XPath, parser RSS | Prix modifié, 1 livre 2024, 2 articles RSS |
| `02_10_conversion_formats.py` | 4.2 | Conversion CSV->JSON, JSON->CSV, XML->JSON | 3 conversions réussies |

**Fichier source** : `02-formats-de-donnees.md`

## Fichier 03 : Sérialisation avec pickle (8 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `03_01_pickle_base.py` | 4.3 | dump/load : listes, dictionnaires, objets multiples | Liste [1..3.14], dict Dupont, Alice 30 ans |
| `03_02_pickle_bytes.py` | 4.3 | dumps/loads sans fichier (sérialisation en bytes) | bytes, ~81 octets, données restaurées |
| `03_03_pickle_objets_personnalises.py` | 4.3 | Sauvegarder/charger une classe Personne | Marie, 28 ans, Paris (sauvée et rechargée) |
| `03_04_pickle_jeu.py` | 4.3 | Système de sauvegarde de jeu complet | Joueur Alice, 100pts, Épée+Potion, sauvegarde/chargement |
| `03_05_pickle_cache.py` | 4.3 | Cache de résultats avec pickle | Calcul n=10 -> 100, puis résultat en cache |
| `03_06_pickle_erreurs_securite.py` | 4.3 | Fonctions sécurisées, protocoles, versioning | Sauvegarde/chargement sécurisés, protocole 5 |
| `03_07_pickle_vs_json.py` | 4.3 | Comparaison pickle vs JSON | Pickle gère tuples/sets/bytes, JSON échoue |
| `03_08_pickle_limitations.py` | 4.3 | Objets non sérialisables, fonctions réutilisables | Erreur TextIOWrapper, erreur lambda |

**Fichier source** : `03-serialisation-pickle.md`

## Fichier 04 : Gestion des chemins avec pathlib (10 fichiers)

| Fichier | Section | Description | Sortie attendue |
|---------|---------|-------------|-----------------|
| `04_01_path_creation.py` | 4.4 | Créer des Path, opérateur /, joinpath() | Chemins construits progressivement |
| `04_02_proprietes_chemin.py` | 4.4 | name, stem, suffix, suffixes, parent, parts | script.py, .py, ['.tar','.gz'], parents |
| `04_03_chemins_absolus_relatifs.py` | 4.4 | absolute(), resolve(), relative_to(), home(), cwd() | Chemins absolus, relatifs, spéciaux |
| `04_04_verifications.py` | 4.4 | exists(), is_file(), is_dir(), analyse complète | Fichier 15 octets, dossier 0 éléments |
| `04_05_operations_dossiers.py` | 4.4 | mkdir(), rename(), copy(), unlink(), rmtree() | Création, renommage, copie, suppression |
| `04_06_glob_recherche.py` | 4.4 | glob(), rglob(), iterdir(), filtrage extensions | 3 .py trouvés, recherche récursive |
| `04_07_infos_fichiers.py` | 4.4 | stat(), taille, dates, fonction infos détaillées | 42 octets, date modification, extension |
| `04_08_lecture_ecriture_pathlib.py` | 4.4 | read_text(), write_text(), read_bytes(), traitement | Texte lu, 5 octets binaires, comptage lignes/mots |
| `04_09_organiser_fichiers.py` | 4.4 | Organiser des fichiers par extension | 6 fichiers classés en jpg/, pdf/, py/, etc. |
| `04_10_backup_fichiers.py` | 4.4 | Backup horodaté d'un dossier complet | 3 fichiers copiés avec structure préservée |

**Fichier source** : `04-gestion-chemins-pathlib.md`

## Exécution

Chaque fichier peut être exécuté indépendamment :

```bash
python3 01_01_lecture_fichier.py
python3 04_10_backup_fichiers.py
```

Tous les fichiers créent et nettoient leurs fichiers temporaires automatiquement.

Pour exécuter tous les fichiers et vérifier qu'il n'y a pas d'erreur :

```bash
for f in *.py; do echo "=== $f ===" && python3 "$f" || echo "ERREUR: $f"; done
```
