🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4.4 : Gestion des chemins avec pathlib

## Introduction

La gestion des chemins de fichiers et dossiers est une tâche courante en programmation. Traditionnellement, Python utilisait le module `os.path` avec des chaînes de caractères, mais depuis Python 3.4, le module `pathlib` offre une approche moderne et orientée objet qui est plus intuitive et plus puissante.

## Qu'est-ce que pathlib ?

### Avantages de pathlib
- **Approche orientée objet** : Les chemins sont des objets avec des méthodes
- **Multi-plateforme** : Gère automatiquement les différences Windows/Linux/Mac
- **Plus lisible** : Code plus clair et expressif
- **Fonctionnalités intégrées** : Opérations courantes incluses
- **Type-safe** : Meilleure intégration avec les IDE et outils

### Comparaison rapide

```python
# Ancienne méthode avec os.path
import os
chemin = os.path.join('dossier', 'sous_dossier', 'fichier.txt')
if os.path.exists(chemin):
    taille = os.path.getsize(chemin)

# Nouvelle méthode avec pathlib
from pathlib import Path
chemin = Path('dossier') / 'sous_dossier' / 'fichier.txt'
if chemin.exists():
    taille = chemin.stat().st_size
```

## Les bases de pathlib

### Création de chemins

```python
from pathlib import Path

# Différentes façons de créer un chemin
chemin1 = Path('mon_fichier.txt')
chemin2 = Path('dossier', 'sous_dossier', 'fichier.txt')
chemin3 = Path('dossier/sous_dossier/fichier.txt')

# Chemin actuel
chemin_actuel = Path.cwd()  # Current Working Directory
print(f"Répertoire actuel: {chemin_actuel}")

# Répertoire home de l'utilisateur
chemin_home = Path.home()
print(f"Répertoire home: {chemin_home}")

# Chemin absolu
chemin_absolu = Path('/usr/local/bin')  # Linux/Mac
chemin_absolu_win = Path(r'C:\Program Files')  # Windows
```

### L'opérateur `/` pour joindre des chemins

```python
from pathlib import Path

# L'opérateur / est surcharge pour joindre des chemins
base = Path('documents')
sous_dossier = base / 'projets'
fichier = sous_dossier / 'mon_projet.py'

print(f"Chemin complet: {fichier}")

# Équivalent à:
fichier_equivalent = Path('documents/projets/mon_projet.py')

# Mélange avec des chaînes
autre_chemin = Path('home') / 'utilisateur' / 'documents'
print(f"Autre chemin: {autre_chemin}")
```

### Propriétés de base des chemins

```python
from pathlib import Path

fichier = Path('documents/projets/mon_script.py')

print(f"Chemin complet: {fichier}")
print(f"Nom du fichier: {fichier.name}")  # mon_script.py
print(f"Nom sans extension: {fichier.stem}")  # mon_script
print(f"Extension: {fichier.suffix}")  # .py
print(f"Toutes les extensions: {fichier.suffixes}")  # ['.py']
print(f"Dossier parent: {fichier.parent}")  # documents/projets
print(f"Tous les parents: {list(fichier.parents)}")  # [documents/projets, documents, .]

# Exemple avec plusieurs extensions
fichier_tar = Path('archive.tar.gz')
print(f"Extension simple: {fichier_tar.suffix}")  # .gz
print(f"Toutes extensions: {fichier_tar.suffixes}")  # ['.tar', '.gz']

# Chemin absolu
print(f"Chemin absolu: {fichier.absolute()}")
print(f"Chemin résolu: {fichier.resolve()}")  # Résout les liens symboliques
```

## Vérification d'existence et de type

### Tests d'existence

```python
from pathlib import Path

# Créons quelques exemples pour les tests
Path('test_dossier').mkdir(exist_ok=True)
Path('test_dossier/fichier_test.txt').write_text('Contenu de test')

# Tests d'existence
chemin_fichier = Path('test_dossier/fichier_test.txt')
chemin_dossier = Path('test_dossier')
chemin_inexistant = Path('nexiste_pas.txt')

print("=== Tests d'existence ===")
print(f"Le fichier existe: {chemin_fichier.exists()}")
print(f"Le dossier existe: {chemin_dossier.exists()}")
print(f"Chemin inexistant: {chemin_inexistant.exists()}")

# Tests de type
print("\n=== Tests de type ===")
print(f"Est un fichier: {chemin_fichier.is_file()}")
print(f"Est un dossier: {chemin_fichier.is_dir()}")
print(f"Est un dossier: {chemin_dossier.is_dir()}")
print(f"Est un fichier: {chemin_dossier.is_file()}")

# Tests avancés
print(f"Est un lien symbolique: {chemin_fichier.is_symlink()}")
print(f"Est un socket: {chemin_fichier.is_socket()}")
print(f"Est un périphérique bloc: {chemin_fichier.is_block_device()}")
```

### Fonction utilitaire pour analyser un chemin

```python
from pathlib import Path

def analyser_chemin(chemin_str):
    """Analyse un chemin et affiche ses propriétés"""
    chemin = Path(chemin_str)

    print(f"=== Analyse de: {chemin} ===")
    print(f"Existe: {chemin.exists()}")

    if chemin.exists():
        if chemin.is_file():
            print("Type: Fichier")
            try:
                stat = chemin.stat()
                print(f"Taille: {stat.st_size} bytes")
                print(f"Dernière modification: {stat.st_mtime}")
            except Exception as e:
                print(f"Erreur stat: {e}")
        elif chemin.is_dir():
            print("Type: Dossier")
            try:
                # Compter les éléments dans le dossier
                elements = list(chemin.iterdir())
                print(f"Contient: {len(elements)} éléments")
            except PermissionError:
                print("Accès refusé")
        else:
            print("Type: Autre (lien, device, etc.)")
    else:
        print("N'existe pas")

    print(f"Nom: {chemin.name}")
    if chemin.suffix:
        print(f"Extension: {chemin.suffix}")
    print(f"Parent: {chemin.parent}")
    print()

# Tests
analyser_chemin('test_dossier')
analyser_chemin('test_dossier/fichier_test.txt')
analyser_chemin('nexiste_pas.txt')
```

## Création et suppression

### Création de dossiers

```python
from pathlib import Path

# Création d'un dossier simple
nouveau_dossier = Path('mon_nouveau_dossier')
nouveau_dossier.mkdir()
print(f"Dossier créé: {nouveau_dossier}")

# Création avec exist_ok=True (pas d'erreur si existe déjà)
nouveau_dossier.mkdir(exist_ok=True)
print("Pas d'erreur si le dossier existe déjà")

# Création de dossiers imbriqués
dossiers_imbrique = Path('niveau1/niveau2/niveau3')
dossiers_imbrique.mkdir(parents=True, exist_ok=True)
print(f"Dossiers imbriqués créés: {dossiers_imbrique}")

# Création avec permissions spécifiques (Linux/Mac)
try:
    dossier_permissions = Path('dossier_prive')
    dossier_permissions.mkdir(mode=0o700, exist_ok=True)  # rwx------
    print("Dossier avec permissions restrictives créé")
except Exception as e:
    print(f"Erreur permissions: {e}")
```

### Création de fichiers

```python
from pathlib import Path

# Création d'un fichier vide
fichier_vide = Path('fichier_vide.txt')
fichier_vide.touch()
print(f"Fichier vide créé: {fichier_vide}")

# Création avec contenu texte
fichier_texte = Path('mon_fichier.txt')
fichier_texte.write_text('Bonjour le monde!\nCeci est un test.', encoding='utf-8')
print(f"Fichier texte créé: {fichier_texte}")

# Création avec contenu binaire
fichier_binaire = Path('donnees.bin')
donnees = b'\x00\x01\x02\x03\xFF'
fichier_binaire.write_bytes(donnees)
print(f"Fichier binaire créé: {fichier_binaire}")

# Création dans un sous-dossier
sous_dossier = Path('documents/projets')
sous_dossier.mkdir(parents=True, exist_ok=True)
fichier_projet = sous_dossier / 'readme.md'
fichier_projet.write_text('# Mon Projet\n\nDescription du projet...', encoding='utf-8')
print(f"Fichier dans sous-dossier créé: {fichier_projet}")
```

### Suppression

```python
from pathlib import Path
import shutil

def supprimer_securise(chemin_str):
    """Supprime un fichier ou dossier de manière sécurisée"""
    chemin = Path(chemin_str)

    if not chemin.exists():
        print(f"❌ {chemin} n'existe pas")
        return False

    try:
        if chemin.is_file():
            chemin.unlink()  # Supprime le fichier
            print(f"✅ Fichier supprimé: {chemin}")
        elif chemin.is_dir():
            # Pour supprimer un dossier et tout son contenu
            shutil.rmtree(chemin)
            print(f"✅ Dossier supprimé: {chemin}")
        return True
    except PermissionError:
        print(f"❌ Permission refusée pour: {chemin}")
        return False
    except Exception as e:
        print(f"❌ Erreur lors de la suppression: {e}")
        return False

# Exemples d'utilisation
supprimer_securise('fichier_vide.txt')
supprimer_securise('mon_nouveau_dossier')

# Suppression d'un dossier vide uniquement
dossier_vide = Path('dossier_test_vide')
dossier_vide.mkdir(exist_ok=True)
try:
    dossier_vide.rmdir()  # Fonctionne seulement si vide
    print("Dossier vide supprimé")
except OSError:
    print("Le dossier n'est pas vide")
```

## Navigation et listage

### Parcours de dossiers

```python
from pathlib import Path

def explorer_dossier(chemin_str, profondeur_max=2, profondeur_actuelle=0):
    """Explore un dossier de manière récursive"""
    chemin = Path(chemin_str)

    if not chemin.is_dir():
        print(f"❌ {chemin} n'est pas un dossier")
        return

    indent = "  " * profondeur_actuelle
    print(f"{indent}📁 {chemin.name}/")

    if profondeur_actuelle >= profondeur_max:
        return

    try:
        # Lister le contenu
        for element in sorted(chemin.iterdir()):
            if element.is_dir():
                explorer_dossier(element, profondeur_max, profondeur_actuelle + 1)
            else:
                taille = element.stat().st_size
                print(f"{indent}  📄 {element.name} ({taille} bytes)")
    except PermissionError:
        print(f"{indent}  ❌ Accès refusé")

# Création d'une structure de test
structure_test = Path('test_structure')
structure_test.mkdir(exist_ok=True)
(structure_test / 'dossier1').mkdir(exist_ok=True)
(structure_test / 'dossier1' / 'fichier1.txt').write_text('Contenu 1')
(structure_test / 'dossier1' / 'fichier2.py').write_text('print("Hello")')
(structure_test / 'dossier2').mkdir(exist_ok=True)
(structure_test / 'dossier2' / 'sous_dossier').mkdir(exist_ok=True)
(structure_test / 'dossier2' / 'sous_dossier' / 'profond.txt').write_text('Fichier profond')
(structure_test / 'fichier_racine.md').write_text('# Documentation')

print("=== Exploration de la structure ===")
explorer_dossier('test_structure')
```

### Recherche de fichiers

```python
from pathlib import Path

def rechercher_fichiers(dossier, pattern="*", recursif=True):
    """Recherche des fichiers selon un pattern"""
    chemin = Path(dossier)

    if not chemin.is_dir():
        print(f"❌ {dossier} n'est pas un dossier valide")
        return []

    try:
        if recursif:
            # Recherche récursive avec **
            fichiers = list(chemin.rglob(pattern))
        else:
            # Recherche dans le dossier courant seulement
            fichiers = list(chemin.glob(pattern))

        return fichiers
    except Exception as e:
        print(f"❌ Erreur lors de la recherche: {e}")
        return []

# Exemples de recherche
print("=== Recherche de fichiers ===")

# Tous les fichiers .txt
fichiers_txt = rechercher_fichiers('test_structure', '*.txt')
print(f"Fichiers .txt trouvés: {len(fichiers_txt)}")
for fichier in fichiers_txt:
    print(f"  - {fichier}")

# Tous les fichiers Python
fichiers_py = rechercher_fichiers('test_structure', '*.py')
print(f"\nFichiers .py trouvés: {len(fichiers_py)}")
for fichier in fichiers_py:
    print(f"  - {fichier}")

# Recherche par nom partiel
fichiers_avec_fichier = rechercher_fichiers('test_structure', '*fichier*')
print(f"\nFichiers contenant 'fichier': {len(fichiers_avec_fichier)}")
for fichier in fichiers_avec_fichier:
    print(f"  - {fichier}")

# Tous les fichiers (pas les dossiers)
tous_fichiers = rechercher_fichiers('test_structure')
fichiers_seulement = [f for f in tous_fichiers if f.is_file()]
print(f"\nTous les fichiers: {len(fichiers_seulement)}")
```

### Filtrage avancé

```python
from pathlib import Path
from datetime import datetime, timedelta

def filtrer_fichiers_par_criteres(dossier, **criteres):
    """
    Filtre les fichiers selon différents critères

    Critères supportés:
    - extension: str (ex: '.py')
    - taille_min: int (en bytes)
    - taille_max: int (en bytes)
    - modifie_depuis: int (jours)
    - nom_contient: str
    """
    chemin = Path(dossier)
    resultats = []

    for fichier in chemin.rglob('*'):
        if not fichier.is_file():
            continue

        # Filtre par extension
        if 'extension' in criteres:
            if fichier.suffix.lower() != criteres['extension'].lower():
                continue

        # Filtre par taille
        try:
            taille = fichier.stat().st_size
            if 'taille_min' in criteres and taille < criteres['taille_min']:
                continue
            if 'taille_max' in criteres and taille > criteres['taille_max']:
                continue
        except:
            continue

        # Filtre par date de modification
        if 'modifie_depuis' in criteres:
            try:
                mtime = datetime.fromtimestamp(fichier.stat().st_mtime)
                limite = datetime.now() - timedelta(days=criteres['modifie_depuis'])
                if mtime < limite:
                    continue
            except:
                continue

        # Filtre par nom
        if 'nom_contient' in criteres:
            if criteres['nom_contient'].lower() not in fichier.name.lower():
                continue

        resultats.append(fichier)

    return resultats

# Exemples de filtrage
print("\n=== Filtrage avancé ===")

# Fichiers Python modifiés récemment
fichiers_py_recents = filtrer_fichiers_par_criteres(
    'test_structure',
    extension='.py',
    modifie_depuis=1  # Dernières 24h
)
print(f"Fichiers Python récents: {len(fichiers_py_recents)}")

# Fichiers de plus de 10 bytes
gros_fichiers = filtrer_fichiers_par_criteres(
    'test_structure',
    taille_min=10
)
print(f"Fichiers > 10 bytes: {len(gros_fichiers)}")

# Fichiers contenant "fichier" dans le nom
fichiers_nom = filtrer_fichiers_par_criteres(
    'test_structure',
    nom_contient='fichier'
)
print(f"Fichiers avec 'fichier' dans le nom: {len(fichiers_nom)}")
```

## Opérations sur les fichiers

### Lecture et écriture avec pathlib

```python
from pathlib import Path
import json

# Préparation de fichiers de test
test_dir = Path('test_operations')
test_dir.mkdir(exist_ok=True)

print("=== Lecture et écriture avec pathlib ===")

# 1. Fichiers texte
fichier_texte = test_dir / 'exemple.txt'
contenu = """Ligne 1: Bonjour le monde!
Ligne 2: Ceci est un test de pathlib.
Ligne 3: Très pratique pour gérer les fichiers."""

# Écriture
fichier_texte.write_text(contenu, encoding='utf-8')
print(f"✅ Fichier texte écrit: {fichier_texte}")

# Lecture
contenu_lu = fichier_texte.read_text(encoding='utf-8')
print(f"📖 Contenu lu ({len(contenu_lu)} caractères)")
print(f"Première ligne: {contenu_lu.split()[0]}")

# 2. Fichiers binaires
fichier_binaire = test_dir / 'donnees.bin'
donnees_binaires = bytes(range(256))  # 0 à 255

# Écriture binaire
fichier_binaire.write_bytes(donnees_binaires)
print(f"✅ Fichier binaire écrit: {fichier_binaire} ({len(donnees_binaires)} bytes)")

# Lecture binaire
donnees_lues = fichier_binaire.read_bytes()
print(f"📖 Données binaires lues: {len(donnees_lues)} bytes")
print(f"Premiers bytes: {list(donnees_lues[:10])}")

# 3. Fichiers JSON avec pathlib
fichier_json = test_dir / 'config.json'
config = {
    "version": "1.0",
    "debug": True,
    "utilisateurs": ["alice", "bob", "charlie"],
    "parametres": {
        "timeout": 30,
        "retries": 3
    }
}

# Écriture JSON
fichier_json.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"✅ Configuration JSON sauvegardée: {fichier_json}")

# Lecture JSON
config_chargee = json.loads(fichier_json.read_text(encoding='utf-8'))
print(f"📖 Configuration chargée: {config_chargee['version']}")
```

### Copie et déplacement

```python
from pathlib import Path
import shutil

def copier_fichier(source, destination):
    """Copie un fichier avec gestion d'erreurs"""
    source_path = Path(source)
    dest_path = Path(destination)

    if not source_path.exists():
        print(f"❌ Source n'existe pas: {source_path}")
        return False

    if not source_path.is_file():
        print(f"❌ Source n'est pas un fichier: {source_path}")
        return False

    try:
        # Créer le dossier de destination si nécessaire
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        # Copier le fichier
        shutil.copy2(source_path, dest_path)
        print(f"✅ Fichier copié: {source_path} → {dest_path}")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la copie: {e}")
        return False

def deplacer_fichier(source, destination):
    """Déplace un fichier"""
    source_path = Path(source)
    dest_path = Path(destination)

    if not source_path.exists():
        print(f"❌ Source n'existe pas: {source_path}")
        return False

    try:
        # Créer le dossier de destination si nécessaire
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        # Déplacer le fichier
        shutil.move(str(source_path), str(dest_path))
        print(f"✅ Fichier déplacé: {source_path} → {dest_path}")
        return True
    except Exception as e:
        print(f"❌ Erreur lors du déplacement: {e}")
        return False

# Tests des opérations
print("\n=== Copie et déplacement ===")

# Créer des fichiers de test
dossier_test = Path('test_copie')
dossier_test.mkdir(exist_ok=True)

fichier_original = dossier_test / 'original.txt'
fichier_original.write_text('Contenu du fichier original', encoding='utf-8')

# Test de copie
copier_fichier(fichier_original, dossier_test / 'copie' / 'fichier_copie.txt')

# Test de déplacement
fichier_temp = dossier_test / 'temporaire.txt'
fichier_temp.write_text('Fichier temporaire', encoding='utf-8')
deplacer_fichier(fichier_temp, dossier_test / 'archive' / 'ancien_temp.txt')

# Vérification
print(f"Original existe toujours: {fichier_original.exists()}")
print(f"Temporaire existe encore: {fichier_temp.exists()}")
```

## Chemins absolus et relatifs

### Conversion et résolution

```python
from pathlib import Path

print("=== Chemins absolus et relatifs ===")

# Chemin de travail actuel
cwd = Path.cwd()
print(f"Répertoire de travail: {cwd}")

# Différents types de chemins
chemin_relatif = Path('documents/mon_fichier.txt')
chemin_absolu = Path('/home/user/documents/mon_fichier.txt')

print(f"\nChemin relatif: {chemin_relatif}")
print(f"Est absolu: {chemin_relatif.is_absolute()}")
print(f"Converti en absolu: {chemin_relatif.absolute()}")

print(f"\nChemin absolu: {chemin_absolu}")
print(f"Est absolu: {chemin_absolu.is_absolute()}")

# Résolution des chemins (gère les .. et .)
chemin_complexe = Path('documents/../photos/./vacances/../famille/photo.jpg')
print(f"\nChemin complexe: {chemin_complexe}")
print(f"Résolu: {chemin_complexe.resolve()}")

# Calcul de chemins relatifs
base = Path('/home/user/documents')
cible = Path('/home/user/photos/vacances/plage.jpg')

try:
    relatif = cible.relative_to(base)
    print(f"\nDe {base} vers {cible}:")
    print(f"Chemin relatif: {relatif}")
except ValueError as e:
    print(f"Impossible de calculer le chemin relatif: {e}")

# relative_to avec un parent commun
cible2 = Path('/home/user/documents/projets/app.py')
relatif2 = cible2.relative_to(base)
print(f"Relatif dans documents: {relatif2}")
```

### Navigation dans l'arborescence

```python
from pathlib import Path

def naviguer_arborescence():
    """Démonstration de navigation dans l'arborescence"""
    print("=== Navigation dans l'arborescence ===")

    # Point de départ
    fichier = Path('projets/python/mon_app/src/main.py')
    print(f"Fichier de départ: {fichier}")

    # Remonter dans l'arborescence
    print(f"\nNavigation vers le haut:")
    print(f"Dossier parent: {fichier.parent}")  # src
    print(f"Grand-parent: {fichier.parent.parent}")  # mon_app
    print(f"Arrière-grand-parent: {fichier.parent.parent.parent}")  # python

    # Tous les parents
    print(f"\nTous les parents:")
    for i, parent in enumerate(fichier.parents):
        print(f"  Niveau {i}: {parent}")

    # Navigation latérale (vers un dossier frère)
    dossier_src = fichier.parent
    dossier_tests = dossier_src.parent / 'tests'
    fichier_test = dossier_tests / 'test_main.py'

    print(f"\nNavigation latérale:")
    print(f"Depuis: {fichier}")
    print(f"Vers tests: {fichier_test}")

    # Remonter à la racine du projet
    racine_projet = fichier.parents[2]  # python/mon_app -> racine
    readme = racine_projet / 'README.md'
    config = racine_projet / 'config' / 'settings.json'

    print(f"\nFichiers à la racine du projet:")
    print(f"README: {readme}")
    print(f"Config: {config}")

naviguer_arborescence()
```

## Informations et métadonnées

### Statistiques de fichiers

```python
from pathlib import Path
from datetime import datetime
import stat

def analyser_fichier_complet(chemin_str):
    """Analyse complète d'un fichier ou dossier"""
    chemin = Path(chemin_str)

    print(f"=== Analyse de: {chemin} ===")

    if not chemin.exists():
        print("❌ N'existe pas")
        return

    try:
        # Statistiques de base
        stats = chemin.stat()

        print(f"Type: {'Fichier' if chemin.is_file() else 'Dossier' if chemin.is_dir() else 'Autre'}")
        print(f"Taille: {stats.st_size:,} bytes ({stats.st_size / 1024:.2f} KB)")

        # Dates
        print(f"Créé: {datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Modifié: {datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Accédé: {datetime.fromtimestamp(stats.st_atime).strftime('%Y-%m-%d %H:%M:%S')}")

        # Permissions (Unix/Linux/Mac)
        mode = stats.st_mode
        permissions = stat.filemode(mode)
        print(f"Permissions: {permissions}")

        # Propriétaire (Unix/Linux/Mac)
        try:
            print(f"UID: {stats.st_uid}")
            print(f"GID: {stats.st_gid}")
        except AttributeError:
            print("Infos propriétaire non disponibles (Windows)")

        # Informations spécifiques aux fichiers
        if chemin.is_file():
            if chemin.suffix:
                print(f"Extension: {chemin.suffix}")

            # Essayer de détecter le type de contenu
            try:
                # Test si c'est du texte
                contenu_debut = chemin.read_bytes()[:100]
                try:
                    contenu_debut.decode('utf-8')
                    print("Type de contenu: Probablement texte (UTF-8)")
                except UnicodeDecodeError:
                    print("Type de contenu: Probablement binaire")
            except:
                print("Impossible de lire le contenu")

        # Informations spécifiques aux dossiers
        elif chemin.is_dir():
            try:
                elements = list(chemin.iterdir())
                nb_fichiers = sum(1 for e in elements if e.is_file())
                nb_dossiers = sum(1 for e in elements if e.is_dir())
                print(f"Contenu: {nb_fichiers} fichiers, {nb_dossiers} dossiers")

                # Taille totale du dossier
                taille_totale = sum(f.stat().st_size for f in chemin.rglob('*') if f.is_file())
                print(f"Taille totale: {taille_totale:,} bytes ({taille_totale / 1024 / 1024:.2f} MB)")

            except PermissionError:
                print("❌ Accès refusé au contenu du dossier")

    except Exception as e:
        print(f"❌ Erreur lors de l'analyse: {e}")

    print()

# Tests avec nos fichiers existants
if Path('test_operations').exists():
    analyser_fichier_complet('test_operations')
    analyser_fichier_complet('test_operations/exemple.txt')
```

### Surveillance des modifications

```python
from pathlib import Path
import time
from datetime import datetime

class SurveillerFichier:
    """Classe pour surveiller les modifications d'un fichier"""

    def __init__(self, chemin_fichier):
        self.chemin = Path(chemin_fichier)
        self.derniere_modification = None
        self.derniere_taille = None
        self._initialiser()

    def _initialiser(self):
        """Initialise les valeurs de référence"""
        if self.chemin.exists():
            stats = self.chemin.stat()
            self.derniere_modification = stats.st_mtime
            self.derniere_taille = stats.st_size
            print(f"📊 Surveillance initialisée pour: {self.chemin}")
        else:
            print(f"⚠️ Fichier non trouvé: {self.chemin}")

    def verifier_modifications(self):
        """Vérifie si le fichier a été modifié"""
        if not self.chemin.exists():
            if self.derniere_modification is not None:
                print(f"🗑️ Fichier supprimé: {self.chemin}")
                self.derniere_modification = None
                self.derniere_taille = None
                return True
            return False

        stats = self.chemin.stat()
        modification_actuelle = stats.st_mtime
        taille_actuelle = stats.st_size

        # Vérifier les changements
        if (self.derniere_modification != modification_actuelle or
            self.derniere_taille != taille_actuelle):

            print(f"📝 Modification détectée: {self.chemin}")
            print(f"   Ancienne taille: {self.derniere_taille} bytes")
            print(f"   Nouvelle taille: {taille_actuelle} bytes")
            print(f"   Modifié le: {datetime.fromtimestamp(modification_actuelle)}")

            self.derniere_modification = modification_actuelle
            self.derniere_taille = taille_actuelle
            return True

        return False

def demo_surveillance():
    """Démonstration de surveillance de fichier"""
    print("=== Démonstration - Surveillance de fichier ===\n")

    # Créer un fichier de test
    fichier_test = Path('fichier_surveille.txt')
    fichier_test.write_text('Contenu initial\n', encoding='utf-8')

    # Initialiser la surveillance
    surveillant = SurveillerFichier(fichier_test)

    print("Modifiez le fichier 'fichier_surveille.txt' pour voir la surveillance en action.")
    print("Appuyez sur Ctrl+C pour arrêter.\n")

    try:
        compteur = 0
        while compteur < 10:  # Limité pour la démo
            if surveillant.verifier_modifications():
                print("  → Changement détecté!")
            else:
                print("  . Aucun changement")

            time.sleep(2)  # Vérifier toutes les 2 secondes
            compteur += 1

    except KeyboardInterrupt:
        print("\n🛑 Surveillance arrêtée")

    # Nettoyage
    if fichier_test.exists():
        fichier_test.unlink()
        print(f"🧹 Fichier de test supprimé: {fichier_test}")

# Exécuter la démo (commenté pour éviter l'attente)
# demo_surveillance()
```

## Cas d'usage pratiques

### Exemple 1 : Organisateur de fichiers

```python
from pathlib import Path
import shutil
from collections import defaultdict

class OrganisateurFichiers:
    """Organise les fichiers par extension dans des dossiers séparés"""

    def __init__(self, dossier_source):
        self.dossier_source = Path(dossier_source)
        self.regles_organisation = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c'],
            'tableurs': ['.xls', '.xlsx', '.csv', '.ods']
        }

    def analyser_dossier(self):
        """Analyse le contenu du dossier source"""
        if not self.dossier_source.exists():
            print(f"❌ Dossier source non trouvé: {self.dossier_source}")
            return {}

        stats = defaultdict(list)

        for fichier in self.dossier_source.iterdir():
            if fichier.is_file():
                extension = fichier.suffix.lower()
                categorie = self._obtenir_categorie(extension)
                stats[categorie].append(fichier)

        return dict(stats)

    def _obtenir_categorie(self, extension):
        """Détermine la catégorie d'un fichier selon son extension"""
        for categorie, extensions in self.regles_organisation.items():
            if extension in extensions:
                return categorie
        return 'autres'

    def afficher_statistiques(self):
        """Affiche les statistiques du dossier"""
        stats = self.analyser_dossier()

        print(f"=== Analyse de {self.dossier_source} ===")
        total_fichiers = sum(len(fichiers) for fichiers in stats.values())
        print(f"Total: {total_fichiers} fichiers\n")

        for categorie, fichiers in sorted(stats.items()):
            print(f"{categorie.upper()}: {len(fichiers)} fichiers")
            for fichier in fichiers[:3]:  # Afficher 3 premiers exemples
                taille = fichier.stat().st_size
                print(f"  - {fichier.name} ({taille} bytes)")
            if len(fichiers) > 3:
                print(f"  ... et {len(fichiers) - 3} autres")
            print()

    def organiser(self, mode_simulation=True):
        """Organise les fichiers (simulation par défaut)"""
        stats = self.analyser_dossier()

        if mode_simulation:
            print("=== MODE SIMULATION ===")
            print("Aucun fichier ne sera réellement déplacé.\n")
        else:
            print("=== ORGANISATION RÉELLE ===")
            print("Les fichiers vont être déplacés!\n")

        for categorie, fichiers in stats.items():
            if not fichiers:
                continue

            dossier_destination = self.dossier_source / categorie

            if not mode_simulation:
                dossier_destination.mkdir(exist_ok=True)

            print(f"📁 Catégorie '{categorie}': {len(fichiers)} fichiers")

            for fichier in fichiers:
                destination = dossier_destination / fichier.name

                if mode_simulation:
                    print(f"  → {fichier.name} → {categorie}/")
                else:
                    try:
                        shutil.move(str(fichier), str(destination))
                        print(f"  ✅ {fichier.name} → {categorie}/")
                    except Exception as e:
                        print(f"  ❌ Erreur avec {fichier.name}: {e}")
            print()

        if mode_simulation:
            print("Pour organiser réellement, utilisez organiser(mode_simulation=False)")

def demo_organisateur():
    """Démonstration de l'organisateur de fichiers"""
    print("=== Démonstration - Organisateur de fichiers ===\n")

    # Créer un dossier de test avec différents types de fichiers
    dossier_test = Path('test_organisation')
    dossier_test.mkdir(exist_ok=True)

    # Créer des fichiers de test
    fichiers_test = [
        ('photo1.jpg', 'Photo de vacances'),
        ('document.pdf', 'Document important'),
        ('musique.mp3', 'Fichier audio'),
        ('script.py', 'print("Hello World")'),
        ('presentation.pptx', 'Présentation PowerPoint'),
        ('donnees.csv', 'nom,age\nAlice,30\nBob,25'),
        ('video.mp4', 'Vidéo de démonstration'),
        ('readme.txt', 'Instructions d\'utilisation'),
        ('fichier_inconnu.xyz', 'Contenu mystérieux')
    ]

    for nom, contenu in fichiers_test:
        fichier = dossier_test / nom
        fichier.write_text(contenu, encoding='utf-8')

    print(f"✅ Dossier de test créé avec {len(fichiers_test)} fichiers")

    # Utiliser l'organisateur
    organisateur = OrganisateurFichiers(dossier_test)

    print("\n--- Analyse initiale ---")
    organisateur.afficher_statistiques()

    print("--- Simulation d'organisation ---")
    organisateur.organiser(mode_simulation=True)

    # Uncomment pour vraiment organiser:
    # print("--- Organisation réelle ---")
    # organisateur.organiser(mode_simulation=False)

# Lancer la démo
demo_organisateur()
```

### Exemple 2 : Gestionnaire de sauvegardes

```python
from pathlib import Path
import shutil
import time
from datetime import datetime
import zipfile

class GestionnaireSauvegardes:
    """Gestionnaire de sauvegardes avec horodatage"""

    def __init__(self, dossier_sauvegardes='sauvegardes'):
        self.dossier_sauvegardes = Path(dossier_sauvegardes)
        self.dossier_sauvegardes.mkdir(exist_ok=True)

    def creer_nom_sauvegarde(self, nom_base):
        """Crée un nom de sauvegarde avec timestamp"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f"{nom_base}_{timestamp}"

    def sauvegarder_fichier(self, fichier_source, nom_sauvegarde=None):
        """Sauvegarde un fichier unique"""
        source = Path(fichier_source)

        if not source.exists():
            print(f"❌ Fichier source non trouvé: {source}")
            return None

        if not source.is_file():
            print(f"❌ La source n'est pas un fichier: {source}")
            return None

        # Nom de sauvegarde
        if nom_sauvegarde is None:
            nom_sauvegarde = self.creer_nom_sauvegarde(source.stem)

        destination = self.dossier_sauvegardes / f"{nom_sauvegarde}{source.suffix}"

        try:
            shutil.copy2(source, destination)
            print(f"✅ Fichier sauvegardé: {source.name} → {destination.name}")
            return destination
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return None

    def sauvegarder_dossier(self, dossier_source, nom_sauvegarde=None, comprimer=True):
        """Sauvegarde un dossier entier"""
        source = Path(dossier_source)

        if not source.exists():
            print(f"❌ Dossier source non trouvé: {source}")
            return None

        if not source.is_dir():
            print(f"❌ La source n'est pas un dossier: {source}")
            return None

        # Nom de sauvegarde
        if nom_sauvegarde is None:
            nom_sauvegarde = self.creer_nom_sauvegarde(source.name)

        if comprimer:
            # Sauvegarde compressée
            destination = self.dossier_sauvegardes / f"{nom_sauvegarde}.zip"

            try:
                with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for fichier in source.rglob('*'):
                        if fichier.is_file():
                            # Chemin relatif dans l'archive
                            chemin_relatif = fichier.relative_to(source)
                            zip_file.write(fichier, chemin_relatif)

                print(f"✅ Dossier sauvegardé (compressé): {source.name} → {destination.name}")
                return destination
            except Exception as e:
                print(f"❌ Erreur lors de la compression: {e}")
                return None
        else:
            # Sauvegarde non compressée
            destination = self.dossier_sauvegardes / nom_sauvegarde

            try:
                shutil.copytree(source, destination)
                print(f"✅ Dossier sauvegardé: {source.name} → {destination.name}")
                return destination
            except Exception as e:
                print(f"❌ Erreur lors de la copie: {e}")
                return None

    def lister_sauvegardes(self):
        """Liste toutes les sauvegardes disponibles"""
        sauvegardes = list(self.dossier_sauvegardes.iterdir())

        if not sauvegardes:
            print("Aucune sauvegarde trouvée")
            return []

        print(f"=== Sauvegardes disponibles ({len(sauvegardes)}) ===")

        # Trier par date de modification
        sauvegardes.sort(key=lambda x: x.stat().st_mtime, reverse=True)

        for sauvegarde in sauvegardes:
            stats = sauvegarde.stat()
            taille = stats.st_size
            date_modif = datetime.fromtimestamp(stats.st_mtime)

            if sauvegarde.is_file():
                type_sauvegarde = "Fichier"
                if sauvegarde.suffix == '.zip':
                    type_sauvegarde = "Archive"
            else:
                type_sauvegarde = "Dossier"

            print(f"📦 {sauvegarde.name}")
            print(f"   Type: {type_sauvegarde}")
            print(f"   Taille: {taille:,} bytes ({taille / 1024 / 1024:.2f} MB)")
            print(f"   Créé: {date_modif.strftime('%Y-%m-%d %H:%M:%S')}")
            print()

        return sauvegardes

    def restaurer_sauvegarde(self, nom_sauvegarde, destination):
        """Restaure une sauvegarde"""
        sauvegarde = self.dossier_sauvegardes / nom_sauvegarde
        destination = Path(destination)

        if not sauvegarde.exists():
            print(f"❌ Sauvegarde non trouvée: {nom_sauvegarde}")
            return False

        try:
            if sauvegarde.suffix == '.zip':
                # Restaurer depuis une archive
                destination.mkdir(parents=True, exist_ok=True)

                with zipfile.ZipFile(sauvegarde, 'r') as zip_file:
                    zip_file.extractall(destination)

                print(f"✅ Archive restaurée: {nom_sauvegarde} → {destination}")
            elif sauvegarde.is_file():
                # Restaurer un fichier unique
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(sauvegarde, destination)
                print(f"✅ Fichier restauré: {nom_sauvegarde} → {destination}")
            else:
                # Restaurer un dossier
                if destination.exists():
                    shutil.rmtree(destination)
                shutil.copytree(sauvegarde, destination)
                print(f"✅ Dossier restauré: {nom_sauvegarde} → {destination}")

            return True
        except Exception as e:
            print(f"❌ Erreur lors de la restauration: {e}")
            return False

    def nettoyer_anciennes_sauvegardes(self, garder_nombre=5):
        """Supprime les anciennes sauvegardes en gardant les N plus récentes"""
        sauvegardes = list(self.dossier_sauvegardes.iterdir())

        if len(sauvegardes) <= garder_nombre:
            print(f"Seulement {len(sauvegardes)} sauvegardes, aucune suppression nécessaire")
            return

        # Trier par date (plus ancien en premier)
        sauvegardes.sort(key=lambda x: x.stat().st_mtime)

        # Supprimer les plus anciennes
        a_supprimer = sauvegardes[:-garder_nombre]

        print(f"🧹 Suppression de {len(a_supprimer)} anciennes sauvegardes:")

        for sauvegarde in a_supprimer:
            try:
                if sauvegarde.is_file():
                    sauvegarde.unlink()
                else:
                    shutil.rmtree(sauvegarde)
                print(f"  ✅ Supprimé: {sauvegarde.name}")
            except Exception as e:
                print(f"  ❌ Erreur suppression {sauvegarde.name}: {e}")

def demo_sauvegardes():
    """Démonstration du gestionnaire de sauvegardes"""
    print("=== Démonstration - Gestionnaire de sauvegardes ===\n")

    # Créer des fichiers et dossiers de test
    projet_test = Path('projet_test')
    projet_test.mkdir(exist_ok=True)

    (projet_test / 'main.py').write_text('print("Hello World")', encoding='utf-8')
    (projet_test / 'config.json').write_text('{"version": "1.0"}', encoding='utf-8')

    sous_dossier = projet_test / 'modules'
    sous_dossier.mkdir(exist_ok=True)
    (sous_dossier / 'utils.py').write_text('def helper(): pass', encoding='utf-8')

    # Initialiser le gestionnaire
    gestionnaire = GestionnaireSauvegardes('demo_sauvegardes')

    print("--- Sauvegarde d'un fichier ---")
    gestionnaire.sauvegarder_fichier(projet_test / 'main.py')

    print("\n--- Sauvegarde d'un dossier (compressé) ---")
    gestionnaire.sauvegarder_dossier(projet_test)

    print("\n--- Sauvegarde d'un dossier (non compressé) ---")
    gestionnaire.sauvegarder_dossier(projet_test, comprimer=False)

    print("\n--- Liste des sauvegardes ---")
    gestionnaire.lister_sauvegardes()

    print("--- Nettoyage (garder 2 sauvegardes) ---")
    gestionnaire.nettoyer_anciennes_sauvegardes(garder_nombre=2)

    print("\n--- Liste après nettoyage ---")
    gestionnaire.lister_sauvegardes()

# Lancer la démo
demo_sauvegardes()
```

### Exemple 3 : Analyseur de structure de projet

```python
from pathlib import Path
from collections import defaultdict
import mimetypes

class AnalyseurProjet:
    """Analyse la structure et les statistiques d'un projet"""

    def __init__(self, dossier_projet):
        self.dossier_projet = Path(dossier_projet)
        self.extensions_ignorees = {'.pyc', '.pyo', '.pyd', '__pycache__'}
        self.dossiers_ignores = {'.git', '.svn', 'node_modules', '__pycache__', '.vscode'}

    def analyser_structure(self):
        """Analyse la structure complète du projet"""
        if not self.dossier_projet.exists():
            print(f"❌ Projet non trouvé: {self.dossier_projet}")
            return {}

        stats = {
            'fichiers_par_extension': defaultdict(int),
            'taille_par_extension': defaultdict(int),
            'profondeur_max': 0,
            'total_fichiers': 0,
            'total_dossiers': 0,
            'taille_totale': 0,
            'fichiers_gros': [],  # > 1MB
            'dossiers_volumineux': [],  # > 100 fichiers
            'extensions_rares': [],  # < 3 occurrences
        }

        for chemin in self.dossier_projet.rglob('*'):
            # Ignorer certains dossiers
            if any(partie in self.dossiers_ignores for partie in chemin.parts):
                continue

            try:
                # Calculer la profondeur
                profondeur = len(chemin.relative_to(self.dossier_projet).parts)
                stats['profondeur_max'] = max(stats['profondeur_max'], profondeur)

                if chemin.is_file():
                    # Ignorer certaines extensions
                    if chemin.suffix in self.extensions_ignorees:
                        continue

                    stats['total_fichiers'] += 1

                    # Statistiques par extension
                    ext = chemin.suffix.lower() or '(sans extension)'
                    stats['fichiers_par_extension'][ext] += 1

                    # Taille du fichier
                    taille = chemin.stat().st_size
                    stats['taille_totale'] += taille
                    stats['taille_par_extension'][ext] += taille

                    # Fichiers volumineux (> 1MB)
                    if taille > 1024 * 1024:
                        stats['fichiers_gros'].append((chemin, taille))

                elif chemin.is_dir():
                    stats['total_dossiers'] += 1

                    # Compter les fichiers dans ce dossier
                    try:
                        nb_fichiers = len([f for f in chemin.iterdir() if f.is_file()])
                        if nb_fichiers > 100:
                            stats['dossiers_volumineux'].append((chemin, nb_fichiers))
                    except PermissionError:
                        pass

            except (PermissionError, OSError):
                continue

        # Identifier les extensions rares
        for ext, count in stats['fichiers_par_extension'].items():
            if count < 3:
                stats['extensions_rares'].append((ext, count))

        return stats

    def generer_rapport(self):
        """Génère un rapport complet d'analyse"""
        stats = self.analyser_structure()

        if not stats:
            return

        print(f"=== RAPPORT D'ANALYSE - {self.dossier_projet.name} ===\n")

        # Statistiques générales
        print("📊 STATISTIQUES GÉNÉRALES")
        print(f"Total fichiers: {stats['total_fichiers']:,}")
        print(f"Total dossiers: {stats['total_dossiers']:,}")
        print(f"Taille totale: {stats['taille_totale']:,} bytes ({stats['taille_totale'] / 1024 / 1024:.2f} MB)")
        print(f"Profondeur maximale: {stats['profondeur_max']} niveaux")
        print()

        # Répartition par extension
        print("📁 RÉPARTITION PAR TYPE DE FICHIER")
        extensions_triees = sorted(stats['fichiers_par_extension'].items(),
                                 key=lambda x: x[1], reverse=True)

        for ext, count in extensions_triees[:10]:  # Top 10
            taille_ext = stats['taille_par_extension'][ext]
            pourcentage = (count / stats['total_fichiers']) * 100
            print(f"{ext:15} {count:4d} fichiers ({pourcentage:5.1f}%) - {taille_ext / 1024:.1f} KB")

        if len(extensions_triees) > 10:
            print(f"... et {len(extensions_triees) - 10} autres types")
        print()

        # Fichiers volumineux
        if stats['fichiers_gros']:
            print("📏 FICHIERS VOLUMINEUX (> 1MB)")
            fichiers_gros_tries = sorted(stats['fichiers_gros'],
                                       key=lambda x: x[1], reverse=True)
            for fichier, taille in fichiers_gros_tries[:5]:
                nom_relatif = fichier.relative_to(self.dossier_projet)
                print(f"{nom_relatif} - {taille / 1024 / 1024:.2f} MB")

            if len(fichiers_gros_tries) > 5:
                print(f"... et {len(fichiers_gros_tries) - 5} autres")
            print()

        # Dossiers volumineux
        if stats['dossiers_volumineux']:
            print("📦 DOSSIERS VOLUMINEUX (> 100 fichiers)")
            for dossier, nb_fichiers in stats['dossiers_volumineux']:
                nom_relatif = dossier.relative_to(self.dossier_projet)
                print(f"{nom_relatif} - {nb_fichiers} fichiers")
            print()

        # Extensions rares
        if stats['extensions_rares']:
            print("🔍 TYPES DE FICHIERS RARES")
            for ext, count in sorted(stats['extensions_rares']):
                print(f"{ext} - {count} fichier(s)")
            print()

        return stats

    def generer_arbre_simplifie(self, profondeur_max=3):
        """Génère un arbre simplifié de la structure"""
        print(f"🌳 STRUCTURE DU PROJET (profondeur {profondeur_max})")
        print(f"📁 {self.dossier_projet.name}/")

        self._afficher_arbre_recursif(self.dossier_projet, "", profondeur_max, 0)
        print()

    def _afficher_arbre_recursif(self, dossier, prefix, profondeur_max, profondeur_actuelle):
        """Affiche récursivement l'arbre du projet"""
        if profondeur_actuelle >= profondeur_max:
            return

        try:
            elements = sorted(dossier.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))

            # Filtrer les éléments ignorés
            elements = [e for e in elements if e.name not in self.dossiers_ignores]

            dossiers = [e for e in elements if e.is_dir()]
            fichiers = [e for e in elements if e.is_file()]

            # Afficher les dossiers
            for i, sous_dossier in enumerate(dossiers):
                is_last_dir = (i == len(dossiers) - 1) and not fichiers

                connector = "└── " if is_last_dir else "├── "
                print(f"{prefix}{connector}📁 {sous_dossier.name}/")

                extension = "    " if is_last_dir else "│   "
                self._afficher_arbre_recursif(
                    sous_dossier,
                    prefix + extension,
                    profondeur_max,
                    profondeur_actuelle + 1
                )
            # Afficher quelques fichiers représentatifs
            if fichiers:
                fichiers_a_afficher = fichiers[:3]  # Montrer seulement 3 fichiers

                for i, fichier in enumerate(fichiers_a_afficher):
                    is_last = i == len(fichiers_a_afficher) - 1 and len(fichiers) <= 3
                    connector = "└── " if is_last else "├── "

                    # Icône selon l'extension
                    if fichier.suffix in ['.py', '.js', '.java', '.cpp', '.c']:
                        icone = "🐍" if fichier.suffix == '.py' else "💻"
                    elif fichier.suffix in ['.jpg', '.png', '.gif', '.svg']:
                        icone = "🖼️"
                    elif fichier.suffix in ['.txt', '.md', '.rst']:
                        icone = "📝"
                    elif fichier.suffix in ['.json', '.xml', '.yaml', '.yml']:
                        icone = "⚙️"
                    else:
                        icone = "📄"

                    print(f"{prefix}{connector}{icone} {fichier.name}")

                if len(fichiers) > 3:
                    print(f"{prefix}    ... et {len(fichiers) - 3} autres fichiers")

        except PermissionError:
            print(f"{prefix}├── ❌ Accès refusé")

def demo_analyseur_projet():
    """Démonstration de l'analyseur de projet"""
    print("=== Démonstration - Analyseur de projet ===\n")

    # Créer une structure de projet complexe pour la démo
    projet = Path('demo_projet')
    projet.mkdir(exist_ok=True)

    # Structure principale
    (projet / 'src').mkdir(exist_ok=True)
    (projet / 'src' / 'main.py').write_text('# Application principale\nprint("Hello")', encoding='utf-8')
    (projet / 'src' / 'utils.py').write_text('# Utilitaires\ndef helper(): pass', encoding='utf-8')

    # Modules
    (projet / 'src' / 'modules').mkdir(exist_ok=True)
    (projet / 'src' / 'modules' / '__init__.py').write_text('', encoding='utf-8')
    (projet / 'src' / 'modules' / 'auth.py').write_text('# Module authentification', encoding='utf-8')
    (projet / 'src' / 'modules' / 'database.py').write_text('# Module base de données', encoding='utf-8')

    # Tests
    (projet / 'tests').mkdir(exist_ok=True)
    (projet / 'tests' / 'test_main.py').write_text('# Tests unitaires', encoding='utf-8')
    (projet / 'tests' / 'test_utils.py').write_text('# Tests utilitaires', encoding='utf-8')

    # Documentation
    (projet / 'docs').mkdir(exist_ok=True)
    (projet / 'docs' / 'README.md').write_text('# Documentation\n\nGuide d\'utilisation', encoding='utf-8')
    (projet / 'docs' / 'api.md').write_text('# API Reference', encoding='utf-8')

    # Configuration
    (projet / 'config').mkdir(exist_ok=True)
    (projet / 'config' / 'settings.json').write_text('{"debug": true, "port": 8000}', encoding='utf-8')
    (projet / 'config' / 'database.yaml').write_text('host: localhost\nport: 5432', encoding='utf-8')

    # Fichiers racine
    (projet / 'requirements.txt').write_text('flask==2.0.1\nrequests==2.25.1', encoding='utf-8')
    (projet / 'setup.py').write_text('from setuptools import setup\nsetup(name="demo")', encoding='utf-8')
    (projet / '.gitignore').write_text('__pycache__/\n*.pyc\n.env', encoding='utf-8')

    # Créer un gros fichier pour les tests
    gros_contenu = "x" * (2 * 1024 * 1024)  # 2MB
    (projet / 'data' / 'large_file.txt').parent.mkdir(exist_ok=True)
    (projet / 'data' / 'large_file.txt').write_text(gros_contenu, encoding='utf-8')

    print(f"✅ Projet de démonstration créé: {projet}")

    # Analyser le projet
    analyseur = AnalyseurProjet(projet)

    print("\n--- Structure simplifiée ---")
    analyseur.generer_arbre_simplifie(profondeur_max=3)

    print("--- Rapport d'analyse ---")
    analyseur.generer_rapport()

# Lancer la démo
demo_analyseur_projet()

## Bonnes pratiques avec pathlib

### 1. Gestion d'erreurs robuste

```python
from pathlib import Path

def operation_fichier_securisee(chemin_str, operation):
    """Template pour opérations de fichiers sécurisées"""
    chemin = Path(chemin_str)

    try:
        # Vérifications préalables
        if operation in ['read', 'write', 'delete']:
            if not chemin.exists():
                raise FileNotFoundError(f"Chemin non trouvé: {chemin}")

        if operation == 'read':
            if not chemin.is_file():
                raise ValueError(f"N'est pas un fichier: {chemin}")
            return chemin.read_text(encoding='utf-8')

        elif operation == 'write':
            # Créer le dossier parent si nécessaire
            chemin.parent.mkdir(parents=True, exist_ok=True)
            return chemin.write_text("Contenu", encoding='utf-8')

        elif operation == 'delete':
            if chemin.is_file():
                chemin.unlink()
            elif chemin.is_dir():
                import shutil
                shutil.rmtree(chemin)
            return True

    except PermissionError:
        print(f"❌ Permission refusée: {chemin}")
        return None
    except FileNotFoundError as e:
        print(f"❌ Fichier non trouvé: {e}")
        return None
    except ValueError as e:
        print(f"❌ Erreur de valeur: {e}")
        return None
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return None

# Tests
print("=== Tests de gestion d'erreurs ===")
operation_fichier_securisee('fichier_inexistant.txt', 'read')
operation_fichier_securisee('nouveau_fichier.txt', 'write')
operation_fichier_securisee('nouveau_fichier.txt', 'read')
```

### 2. Patterns utiles

```python
from pathlib import Path
import tempfile
import contextlib

# Pattern 1: Répertoire de travail temporaire
@contextlib.contextmanager
def repertoire_temporaire():
    """Context manager pour travailler dans un répertoire temporaire"""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        ancien_cwd = Path.cwd()
        try:
            import os
            os.chdir(temp_path)
            yield temp_path
        finally:
            os.chdir(ancien_cwd)

# Pattern 2: Sauvegarde automatique
@contextlib.contextmanager
def sauvegarde_automatique(fichier):
    """Context manager pour sauvegarde automatique"""
    fichier_path = Path(fichier)
    sauvegarde = None

    if fichier_path.exists():
        # Créer une sauvegarde
        sauvegarde = fichier_path.with_suffix(fichier_path.suffix + '.backup')
        import shutil
        shutil.copy2(fichier_path, sauvegarde)

    try:
        yield fichier_path
    except Exception:
        # Restaurer en cas d'erreur
        if sauvegarde and sauvegarde.exists():
            shutil.copy2(sauvegarde, fichier_path)
        raise
    finally:
        # Nettoyer la sauvegarde
        if sauvegarde and sauvegarde.exists():
            sauvegarde.unlink()

# Pattern 3: Recherche avec cache
class ChercheurFichiers:
    def __init__(self):
        self._cache = {}

    def rechercher_avec_cache(self, dossier, pattern):
        """Recherche avec mise en cache des résultats"""
        cle_cache = f"{dossier}:{pattern}"

        if cle_cache in self._cache:
            print(f"📋 Résultat depuis le cache: {pattern}")
            return self._cache[cle_cache]

        print(f"🔍 Recherche en cours: {pattern}")
        resultats = list(Path(dossier).rglob(pattern))
        self._cache[cle_cache] = resultats

        return resultats

# Démonstrations des patterns
print("\n=== Démonstration des patterns ===")

# Pattern 1: Répertoire temporaire
print("1. Répertoire temporaire:")
with repertoire_temporaire() as temp_dir:
    print(f"   Travail dans: {temp_dir}")
    (temp_dir / 'test.txt').write_text('Fichier temporaire')
    print(f"   Fichier créé: {list(temp_dir.iterdir())}")
print("   Répertoire temporaire nettoyé automatiquement")

# Pattern 3: Cache de recherche
print("\n3. Recherche avec cache:")
chercheur = ChercheurFichiers()
if Path('demo_projet').exists():
    # Première recherche
    resultats1 = chercheur.rechercher_avec_cache('demo_projet', '*.py')
    print(f"   Trouvé: {len(resultats1)} fichiers Python")

    # Deuxième recherche (depuis le cache)
    resultats2 = chercheur.rechercher_avec_cache('demo_projet', '*.py')
    print(f"   Trouvé: {len(resultats2)} fichiers Python")
```

### 3. Performance et optimisation

```python
from pathlib import Path
import time
from concurrent.futures import ThreadPoolExecutor

def comparer_performances():
    """Compare les performances de différentes approches"""

    # Créer des fichiers de test
    test_dir = Path('test_performance')
    test_dir.mkdir(exist_ok=True)

    # Créer beaucoup de fichiers
    for i in range(1000):
        (test_dir / f'file_{i:04d}.txt').write_text(f'Contenu {i}')

    print("=== Comparaison de performances ===")

    # Test 1: iterdir() vs rglob()
    start = time.time()
    files1 = list(test_dir.iterdir())
    time1 = time.time() - start

    start = time.time()
    files2 = list(test_dir.rglob('*'))
    time2 = time.time() - start

    print(f"iterdir(): {time1:.4f}s ({len(files1)} éléments)")
    print(f"rglob():   {time2:.4f}s ({len(files2)} éléments)")

    # Test 2: Lecture séquentielle vs parallèle
    fichiers = [f for f in test_dir.iterdir() if f.is_file()][:100]  # Premier 100

    # Séquentiel
    start = time.time()
    contenus_seq = []
    for fichier in fichiers:
        try:
            contenus_seq.append(fichier.read_text())
        except:
            pass
    time_seq = time.time() - start

    # Parallèle
    def lire_fichier(fichier):
        try:
            return fichier.read_text()
        except:
            return ""

    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        contenus_par = list(executor.map(lire_fichier, fichiers))
    time_par = time.time() - start

    print(f"\nLecture de {len(fichiers)} fichiers:")
    print(f"Séquentiel: {time_seq:.4f}s")
    print(f"Parallèle:  {time_par:.4f}s (amélioration: {time_seq/time_par:.1f}x)")

    # Nettoyage
    import shutil
    shutil.rmtree(test_dir)
    print("\nFichiers de test supprimés")

# Exécuter le test de performance
comparer_performances()
```

## Migration depuis os.path

### Guide de migration

```python
import os
from pathlib import Path

def guide_migration():
    """Guide pour migrer depuis os.path vers pathlib"""

    print("=== Guide de migration os.path → pathlib ===\n")

    exemples = [
        # (description, ancien_code, nouveau_code)
        (
            "Joindre des chemins",
            "os.path.join('dossier', 'fichier.txt')",
            "Path('dossier') / 'fichier.txt'"
        ),
        (
            "Obtenir le nom du fichier",
            "os.path.basename('/path/to/file.txt')",
            "Path('/path/to/file.txt').name"
        ),
        (
            "Obtenir le dossier parent",
            "os.path.dirname('/path/to/file.txt')",
            "Path('/path/to/file.txt').parent"
        ),
        (
            "Obtenir l'extension",
            "os.path.splitext('file.txt')[1]",
            "Path('file.txt').suffix"
        ),
        (
            "Vérifier l'existence",
            "os.path.exists('file.txt')",
            "Path('file.txt').exists()"
        ),
        (
            "Vérifier si c'est un fichier",
            "os.path.isfile('file.txt')",
            "Path('file.txt').is_file()"
        ),
        (
            "Vérifier si c'est un dossier",
            "os.path.isdir('dossier')",
            "Path('dossier').is_dir()"
        ),
        (
            "Chemin absolu",
            "os.path.abspath('file.txt')",
            "Path('file.txt').absolute()"
        ),
        (
            "Répertoire courant",
            "os.getcwd()",
            "Path.cwd()"
        ),
        (
            "Lister un dossier",
            "os.listdir('dossier')",
            "list(Path('dossier').iterdir())"
        ),
        (
            "Créer un dossier",
            "os.makedirs('path/to/dir', exist_ok=True)",
            "Path('path/to/dir').mkdir(parents=True, exist_ok=True)"
        ),
        (
            "Supprimer un fichier",
            "os.remove('file.txt')",
            "Path('file.txt').unlink()"
        ),
        (
            "Renommer un fichier",
            "os.rename('old.txt', 'new.txt')",
            "Path('old.txt').rename('new.txt')"
        ),
        (
            "Statistiques de fichier",
            "os.stat('file.txt').st_size",
            "Path('file.txt').stat().st_size"
        ),
        (
            "Recherche récursive",
            "# Complexe avec os.walk",
            "list(Path('.').rglob('*.py'))"
        )
    ]

    for description, ancien, nouveau in exemples:
        print(f"🔄 {description}")
        print(f"   ❌ Ancien: {ancien}")
        print(f"   ✅ Nouveau: {nouveau}")
        print()

guide_migration()
```

### Exemple de refactoring

```python
# AVANT: Code utilisant os.path
import os
import shutil

def analyser_projet_ancien(dossier_projet):
    """Version ancienne avec os.path"""
    if not os.path.exists(dossier_projet):
        return None

    stats = {}

    for root, dirs, files in os.walk(dossier_projet):
        # Ignorer certains dossiers
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__']]

        for file in files:
            chemin_complet = os.path.join(root, file)
            _, ext = os.path.splitext(file)

            if ext not in stats:
                stats[ext] = []

            try:
                taille = os.path.getsize(chemin_complet)
                stats[ext].append((chemin_complet, taille))
            except OSError:
                pass

    return stats

# APRÈS: Code utilisant pathlib
from pathlib import Path

def analyser_projet_moderne(dossier_projet):
    """Version moderne avec pathlib"""
    projet = Path(dossier_projet)

    if not projet.exists():
        return None

    stats = {}
    dossiers_ignores = {'.git', '__pycache__', 'node_modules'}

    for fichier in projet.rglob('*'):
        # Ignorer les dossiers spécifiés
        if any(partie in dossiers_ignores for partie in fichier.parts):
            continue

        if fichier.is_file():
            ext = fichier.suffix or '(sans extension)'

            if ext not in stats:
                stats[ext] = []

            try:
                taille = fichier.stat().st_size
                stats[ext].append((fichier, taille))
            except OSError:
                pass

    return stats

# Comparaison
print("=== Comparaison refactoring ===")
if Path('demo_projet').exists():
    print("Analyse avec pathlib:")
    stats_moderne = analyser_projet_moderne('demo_projet')
    for ext, fichiers in sorted(stats_moderne.items()):
        print(f"  {ext}: {len(fichiers)} fichiers")
```

## Résumé du module

### Concepts clés appris

1. **Approche orientée objet** : Chemins comme objets avec méthodes
2. **Opérateur `/`** : Jointure intuitive des chemins
3. **Méthodes de vérification** : `exists()`, `is_file()`, `is_dir()`
4. **Navigation** : `parent`, `parents`, `iterdir()`, `rglob()`
5. **Opérations** : `mkdir()`, `write_text()`, `read_text()`, `unlink()`
6. **Propriétés** : `name`, `stem`, `suffix`, `absolute()`

### Avantages de pathlib

**✅ Points forts :**
- Code plus lisible et expressif
- Gestion automatique des différences de plateformes
- Méthodes intégrées pour opérations courantes
- Meilleure intégration avec les IDE
- Gestion d'erreurs plus cohérente

**🔄 Migration :**
- Remplacement progressif de `os.path`
- Compatibilité avec le code existant
- Performances équivalentes ou meilleures

### Cas d'usage couverts

1. **Organisation de fichiers** : Tri automatique par extension
2. **Sauvegardes** : Système de versioning avec compression
3. **Analyse de projets** : Statistiques et structure
4. **Surveillance** : Détection de modifications
5. **Templates** : Patterns réutilisables

### Bonnes pratiques retenues

1. **Toujours valider l'existence** avant les opérations
2. **Gérer les erreurs** (permissions, fichiers manquants)
3. **Utiliser `mkdir(parents=True, exist_ok=True)`** pour la création
4. **Préférer `rglob()`** pour les recherches récursives
5. **Spécifier l'encodage** pour les fichiers texte
6. **Utiliser des context managers** pour les opérations temporaires

### Intégration avec les autres modules

Pathlib s'intègre parfaitement avec :
- **Module 4.1** : Lecture/écriture de fichiers
- **Module 4.2** : Formats de données (JSON, CSV, XML)
- **Module 4.3** : Sérialisation pickle

Cette approche moderne unifie la gestion des chemins et facilite la maintenance du code, rendant les opérations sur fichiers plus intuitives et moins sujettes aux erreurs.

## Conclusion du Module 4

Félicitations ! Vous avez maintenant maîtrisé les quatre aspects essentiels de la gestion des données et fichiers en Python :

1. **Fichiers texte et binaires** : Lecture/écriture, encodage, gestion d'erreurs
2. **Formats structurés** : JSON, CSV, XML avec validation et bonnes pratiques
3. **Sérialisation** : Pickle pour objets Python complexes
4. **Gestion moderne des chemins** : Pathlib pour une approche orientée objet

Ces compétences forment une base solide pour tous vos projets Python impliquant des données externes, des configurations, ou des systèmes de fichiers.

⏭️
