🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.1 : os, sys, subprocess

## Introduction

Dans cette section, nous allons découvrir trois modules fondamentaux pour interagir avec le système d'exploitation et l'environnement Python. Ces modules forment le trio essentiel pour créer des scripts robustes et des applications qui s'intègrent parfaitement dans leur environnement.

### Analogie simple
Imaginez votre programme Python comme un **habitant dans une maison** (votre ordinateur) :
- **os** : vous permet d'explorer les pièces, ouvrir les portes, allumer les lumières
- **sys** : vous donne accès aux réglages de la maison (thermostat, alarme, etc.)
- **subprocess** : vous permet d'appeler des services externes (plombier, électricien)

## Module os : Interface avec le système d'exploitation

Le module `os` (operating system) fournit une interface portable pour utiliser les fonctionnalités du système d'exploitation.

### Gestion des répertoires et fichiers

#### Navigation dans l'arborescence

```python
import os

# Connaître le répertoire de travail actuel
repertoire_actuel = os.getcwd()
print(f"Répertoire actuel : {repertoire_actuel}")

# Changer de répertoire
os.chdir('/home/user/Documents')  # Linux/Mac
# os.chdir('C:\\Users\\user\\Documents')  # Windows

# Lister le contenu d'un répertoire
contenu = os.listdir('.')
print("Contenu du répertoire :")
for element in contenu:
    print(f"  {element}")

# Lister avec plus d'informations
print("\nContenu détaillé :")
for element in os.listdir('.'):
    chemin_complet = os.path.join('.', element)
    if os.path.isdir(chemin_complet):
        print(f"📁 {element}/")
    else:
        taille = os.path.getsize(chemin_complet)
        print(f"📄 {element} ({taille} octets)")
```

#### Création et suppression

```python
import os

# Créer un répertoire
nouveau_dossier = "mon_projet"
if not os.path.exists(nouveau_dossier):
    os.mkdir(nouveau_dossier)
    print(f"Dossier '{nouveau_dossier}' créé")

# Créer plusieurs niveaux de répertoires
os.makedirs("projets/python/scripts", exist_ok=True)
print("Arborescence créée")

# Supprimer un fichier
fichier_test = "test.txt"
if os.path.exists(fichier_test):
    os.remove(fichier_test)
    print(f"Fichier '{fichier_test}' supprimé")

# Supprimer un répertoire vide
try:
    os.rmdir("dossier_vide")
    print("Répertoire vide supprimé")
except OSError as e:
    print(f"Erreur : {e}")

# Supprimer un répertoire et son contenu
import shutil
if os.path.exists("dossier_avec_contenu"):
    shutil.rmtree("dossier_avec_contenu")
    print("Répertoire et contenu supprimés")
```

#### Manipulation des chemins

```python
import os

# Construire des chemins portables
chemin = os.path.join("projets", "python", "main.py")
print(f"Chemin construit : {chemin}")

# Séparer un chemin
repertoire, fichier = os.path.split(chemin)
print(f"Répertoire : {repertoire}")
print(f"Fichier : {fichier}")

# Extraire l'extension
nom, extension = os.path.splitext(fichier)
print(f"Nom : {nom}, Extension : {extension}")

# Chemin absolu
chemin_absolu = os.path.abspath(".")
print(f"Chemin absolu : {chemin_absolu}")

# Vérifier l'existence
print(f"Le fichier existe : {os.path.exists('main.py')}")
print(f"C'est un fichier : {os.path.isfile('main.py')}")
print(f"C'est un dossier : {os.path.isdir('.')}")
```

### Variables d'environnement

```python
import os

# Lire une variable d'environnement
utilisateur = os.environ.get('USER', 'utilisateur_inconnu')  # Linux/Mac
# utilisateur = os.environ.get('USERNAME', 'utilisateur_inconnu')  # Windows
print(f"Utilisateur : {utilisateur}")

# Lire avec valeur par défaut
chemin_home = os.environ.get('HOME', '/tmp')
print(f"Répertoire home : {chemin_home}")

# Définir une variable d'environnement
os.environ['MON_PROJET'] = 'super_application'
print(f"Variable définie : {os.environ['MON_PROJET']}")

# Lister toutes les variables d'environnement
print("Variables d'environnement importantes :")
variables_importantes = ['PATH', 'HOME', 'USER', 'LANG']
for var in variables_importantes:
    valeur = os.environ.get(var, 'Non définie')
    print(f"  {var}: {valeur}")
```

### Exemple pratique : Gestionnaire de fichiers simple

```python
import os
import shutil
from datetime import datetime

class GestionnaireFichiers:
    """Gestionnaire simple pour organiser les fichiers."""

    def __init__(self, repertoire_base="."):
        self.repertoire_base = os.path.abspath(repertoire_base)

    def creer_structure_projet(self, nom_projet):
        """Crée une structure de projet standard."""
        dossiers = [
            nom_projet,
            os.path.join(nom_projet, "src"),
            os.path.join(nom_projet, "tests"),
            os.path.join(nom_projet, "docs"),
            os.path.join(nom_projet, "data")
        ]

        for dossier in dossiers:
            chemin_complet = os.path.join(self.repertoire_base, dossier)
            os.makedirs(chemin_complet, exist_ok=True)
            print(f"✅ Créé : {dossier}")

        # Créer des fichiers de base
        fichiers = {
            os.path.join(nom_projet, "README.md"): f"# {nom_projet}\n\nDescription du projet",
            os.path.join(nom_projet, "requirements.txt"): "# Dépendances du projet\n",
            os.path.join(nom_projet, "src", "main.py"): "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\ndef main():\n    print('Hello World!')\n\nif __name__ == '__main__':\n    main()\n"
        }

        for fichier, contenu in fichiers.items():
            chemin_complet = os.path.join(self.repertoire_base, fichier)
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                f.write(contenu)
            print(f"📄 Créé : {fichier}")

    def organiser_par_type(self, repertoire_source):
        """Organise les fichiers par type d'extension."""
        if not os.path.exists(repertoire_source):
            print(f"Le répertoire {repertoire_source} n'existe pas")
            return

        # Créer des dossiers par type
        types_fichiers = {
            '.txt': 'documents',
            '.pdf': 'documents',
            '.doc': 'documents',
            '.docx': 'documents',
            '.jpg': 'images',
            '.jpeg': 'images',
            '.png': 'images',
            '.gif': 'images',
            '.mp3': 'audio',
            '.wav': 'audio',
            '.mp4': 'videos',
            '.avi': 'videos',
            '.py': 'scripts',
            '.js': 'scripts'
        }

        for fichier in os.listdir(repertoire_source):
            chemin_source = os.path.join(repertoire_source, fichier)

            # Ignorer les dossiers
            if os.path.isdir(chemin_source):
                continue

            # Déterminer le type
            _, extension = os.path.splitext(fichier)
            type_dossier = types_fichiers.get(extension.lower(), 'autres')

            # Créer le dossier de destination
            dossier_dest = os.path.join(repertoire_source, type_dossier)
            os.makedirs(dossier_dest, exist_ok=True)

            # Déplacer le fichier
            chemin_dest = os.path.join(dossier_dest, fichier)
            shutil.move(chemin_source, chemin_dest)
            print(f"📁 {fichier} → {type_dossier}/")

    def nettoyer_fichiers_anciens(self, repertoire, jours=30):
        """Supprime les fichiers plus anciens que X jours."""
        if not os.path.exists(repertoire):
            print(f"Le répertoire {repertoire} n'existe pas")
            return

        limite_temps = datetime.now().timestamp() - (jours * 24 * 3600)
        fichiers_supprimes = 0

        for fichier in os.listdir(repertoire):
            chemin_complet = os.path.join(repertoire, fichier)

            if os.path.isfile(chemin_complet):
                derniere_modification = os.path.getmtime(chemin_complet)

                if derniere_modification < limite_temps:
                    os.remove(chemin_complet)
                    print(f"🗑️ Supprimé : {fichier}")
                    fichiers_supprimes += 1

        print(f"Total supprimé : {fichiers_supprimes} fichiers")

# Utilisation
gestionnaire = GestionnaireFichiers()
gestionnaire.creer_structure_projet("mon_super_projet")
```

## Module sys : Interface avec l'interpréteur Python

Le module `sys` donne accès aux variables et fonctions qui interagissent fortement avec l'interpréteur Python.

### Arguments de ligne de commande

```python
import sys

def afficher_arguments():
    """Affiche les arguments passés au script."""
    print(f"Nom du script : {sys.argv[0]}")
    print(f"Nombre d'arguments : {len(sys.argv) - 1}")

    if len(sys.argv) > 1:
        print("Arguments :")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"  {i}: {arg}")
    else:
        print("Aucun argument fourni")

# Utilisation : python script.py arg1 arg2 arg3
afficher_arguments()
```

### Exemple : Calculatrice en ligne de commande

```python
#!/usr/bin/env python3
import sys

def calculatrice():
    """Calculatrice simple en ligne de commande."""
    if len(sys.argv) != 4:
        print("Usage: python calculatrice.py <nombre1> <opérateur> <nombre2>")
        print("Opérateurs supportés: +, -, *, /")
        sys.exit(1)  # Quitter avec code d'erreur

    try:
        nombre1 = float(sys.argv[1])
        operateur = sys.argv[2]
        nombre2 = float(sys.argv[3])

        if operateur == '+':
            resultat = nombre1 + nombre2
        elif operateur == '-':
            resultat = nombre1 - nombre2
        elif operateur == '*':
            resultat = nombre1 * nombre2
        elif operateur == '/':
            if nombre2 == 0:
                print("Erreur : Division par zéro")
                sys.exit(1)
            resultat = nombre1 / nombre2
        else:
            print(f"Opérateur non supporté : {operateur}")
            sys.exit(1)

        print(f"{nombre1} {operateur} {nombre2} = {resultat}")

    except ValueError:
        print("Erreur : Les nombres doivent être numériques")
        sys.exit(1)

if __name__ == "__main__":
    calculatrice()
```

### Informations système

```python
import sys
import platform

def afficher_info_systeme():
    """Affiche des informations sur le système et Python."""
    print("=== INFORMATIONS SYSTÈME ===")

    # Version de Python
    print(f"Version Python : {sys.version}")
    print(f"Version courte : {sys.version_info}")

    # Plateforme
    print(f"Plateforme : {sys.platform}")
    print(f"Architecture : {platform.architecture()}")
    print(f"Machine : {platform.machine()}")
    print(f"OS : {platform.system()} {platform.release()}")

    # Chemins Python
    print(f"Exécutable Python : {sys.executable}")
    print(f"Préfixe : {sys.prefix}")

    # Modules
    print(f"Modules chargés : {len(sys.modules)}")

    # Chemin de recherche des modules
    print("Chemins de recherche des modules :")
    for i, chemin in enumerate(sys.path):
        print(f"  {i}: {chemin}")

afficher_info_systeme()
```

### Gestion de la sortie et des erreurs

```python
import sys

def logger_simple(message, niveau="INFO"):
    """Logger simple utilisant sys.stdout et sys.stderr."""

    if niveau == "ERROR":
        print(f"❌ ERREUR: {message}", file=sys.stderr)
    elif niveau == "WARNING":
        print(f"⚠️ ATTENTION: {message}", file=sys.stderr)
    else:
        print(f"ℹ️ INFO: {message}", file=sys.stdout)

# Test du logger
logger_simple("Application démarrée")
logger_simple("Fichier non trouvé", "WARNING")
logger_simple("Erreur critique", "ERROR")

# Redirection de sortie vers un fichier
with open("log.txt", "w") as f:
    # Sauvegarder les sorties originales
    stdout_original = sys.stdout
    stderr_original = sys.stderr

    # Rediriger vers le fichier
    sys.stdout = f
    sys.stderr = f

    print("Ce message va dans le fichier")
    logger_simple("Message de log", "ERROR")

    # Restaurer les sorties originales
    sys.stdout = stdout_original
    sys.stderr = stderr_original

print("Ce message s'affiche normalement")
```

## Module subprocess : Exécution de processus externes

Le module `subprocess` permet d'exécuter d'autres programmes et de communiquer avec eux.

### Exécution simple de commandes

```python
import subprocess
import sys

def executer_commande(commande):
    """Exécute une commande système et retourne le résultat."""
    try:
        # Exécuter la commande
        resultat = subprocess.run(
            commande,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30  # Timeout de 30 secondes
        )

        print(f"Commande : {commande}")
        print(f"Code de retour : {resultat.returncode}")

        if resultat.stdout:
            print("Sortie standard :")
            print(resultat.stdout)

        if resultat.stderr:
            print("Erreurs :")
            print(resultat.stderr)

        return resultat.returncode == 0

    except subprocess.TimeoutExpired:
        print(f"Timeout : la commande '{commande}' a pris trop de temps")
        return False
    except Exception as e:
        print(f"Erreur : {e}")
        return False

# Exemples d'utilisation
if sys.platform.startswith('win'):
    # Commandes Windows
    executer_commande("dir")
    executer_commande("echo Hello World")
else:
    # Commandes Linux/Mac
    executer_commande("ls -la")
    executer_commande("echo 'Hello World'")
    executer_commande("date")
```

### Gestion avancée des processus

```python
import subprocess
import threading
import time

def executer_avec_monitoring(commande, timeout=60):
    """Exécute une commande avec monitoring en temps réel."""

    def lire_sortie(pipe, nom):
        """Lit la sortie d'un pipe en temps réel."""
        for ligne in iter(pipe.readline, ''):
            print(f"[{nom}] {ligne.strip()}")
        pipe.close()

    try:
        # Démarrer le processus
        processus = subprocess.Popen(
            commande,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        # Créer des threads pour lire stdout et stderr
        thread_stdout = threading.Thread(
            target=lire_sortie,
            args=(processus.stdout, "OUT")
        )
        thread_stderr = threading.Thread(
            target=lire_sortie,
            args=(processus.stderr, "ERR")
        )

        # Démarrer les threads
        thread_stdout.start()
        thread_stderr.start()

        # Attendre la fin du processus avec timeout
        try:
            code_retour = processus.wait(timeout=timeout)
            print(f"Processus terminé avec le code : {code_retour}")
        except subprocess.TimeoutExpired:
            print("Timeout dépassé, arrêt du processus...")
            processus.kill()
            code_retour = -1

        # Attendre que les threads finissent
        thread_stdout.join()
        thread_stderr.join()

        return code_retour

    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")
        return -1

# Test avec une commande qui prend du temps
if not sys.platform.startswith('win'):
    executer_avec_monitoring("ping -c 3 google.com")
```

### Exemple pratique : Gestionnaire de tâches système

```python
import subprocess
import sys
import json
from datetime import datetime

class GestionnaireTaches:
    """Gestionnaire pour automatiser des tâches système."""

    def __init__(self):
        self.historique = []

    def executer_tache(self, nom, commande, capture_output=True):
        """Exécute une tâche et enregistre le résultat."""
        debut = datetime.now()

        print(f"🚀 Démarrage de la tâche : {nom}")

        try:
            resultat = subprocess.run(
                commande,
                shell=True,
                capture_output=capture_output,
                text=True,
                timeout=300  # 5 minutes max
            )

            fin = datetime.now()
            duree = (fin - debut).total_seconds()

            # Enregistrer dans l'historique
            entry = {
                'nom': nom,
                'commande': commande,
                'debut': debut.isoformat(),
                'fin': fin.isoformat(),
                'duree': duree,
                'code_retour': resultat.returncode,
                'succes': resultat.returncode == 0
            }

            if capture_output:
                entry['stdout'] = resultat.stdout
                entry['stderr'] = resultat.stderr

            self.historique.append(entry)

            # Afficher le résultat
            if resultat.returncode == 0:
                print(f"✅ Tâche '{nom}' terminée avec succès ({duree:.2f}s)")
            else:
                print(f"❌ Tâche '{nom}' échouée (code {resultat.returncode})")
                if resultat.stderr:
                    print(f"Erreur : {resultat.stderr}")

            return resultat.returncode == 0

        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout : la tâche '{nom}' a pris trop de temps")
            return False
        except Exception as e:
            print(f"💥 Erreur lors de l'exécution de '{nom}' : {e}")
            return False

    def sauvegarder_historique(self, fichier="historique_taches.json"):
        """Sauvegarde l'historique des tâches."""
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(self.historique, f, indent=2, ensure_ascii=False)
        print(f"📄 Historique sauvegardé dans {fichier}")

    def rapport_execution(self):
        """Génère un rapport d'exécution."""
        if not self.historique:
            print("Aucune tâche exécutée")
            return

        total = len(self.historique)
        succes = sum(1 for t in self.historique if t['succes'])
        echecs = total - succes

        print("\n" + "="*50)
        print("📊 RAPPORT D'EXÉCUTION")
        print("="*50)
        print(f"Total de tâches : {total}")
        print(f"Succès : {succes} ({succes/total*100:.1f}%)")
        print(f"Échecs : {echecs} ({echecs/total*100:.1f}%)")

        if self.historique:
            duree_totale = sum(t['duree'] for t in self.historique)
            print(f"Durée totale : {duree_totale:.2f}s")

        print("\nDétail des tâches :")
        for tache in self.historique:
            statut = "✅" if tache['succes'] else "❌"
            print(f"  {statut} {tache['nom']} ({tache['duree']:.2f}s)")

# Exemple d'utilisation
gestionnaire = GestionnaireTaches()

# Définir des tâches selon l'OS
if sys.platform.startswith('win'):
    taches = [
        ("Afficher la date", "date /t"),
        ("Lister les fichiers", "dir"),
        ("Info système", "systeminfo | findstr /C:\"OS Name\"")
    ]
else:
    taches = [
        ("Afficher la date", "date"),
        ("Lister les fichiers", "ls -la"),
        ("Espace disque", "df -h"),
        ("Charge système", "uptime")
    ]

# Exécuter toutes les tâches
for nom, commande in taches:
    gestionnaire.executer_tache(nom, commande)
    time.sleep(1)  # Petite pause entre les tâches

# Générer le rapport
gestionnaire.rapport_execution()
gestionnaire.sauvegarder_historique()
```

## Projet intégré : Outil de maintenance système

Créons un outil complet qui utilise les trois modules :

```python
#!/usr/bin/env python3
"""
Outil de maintenance système
Utilise os, sys, et subprocess pour automatiser la maintenance
"""

import os
import sys
import subprocess
import shutil
import json
from datetime import datetime, timedelta
import argparse

class OutilMaintenance:
    """Outil complet de maintenance système."""

    def __init__(self, config_file="maintenance_config.json"):
        self.config_file = config_file
        self.config = self.charger_configuration()
        self.log = []

    def charger_configuration(self):
        """Charge la configuration depuis un fichier JSON."""
        config_defaut = {
            "repertoires_nettoyage": ["~/Downloads", "~/Desktop"],
            "extensions_temporaires": [".tmp", ".cache", ".log"],
            "jours_retention": 30,
            "sauvegarde_repertoire": "~/Backups",
            "commandes_maintenance": {
                "linux": [
                    "sudo apt update",
                    "sudo apt autoremove -y",
                    "sudo apt autoclean"
                ],
                "darwin": [  # macOS
                    "brew update",
                    "brew cleanup"
                ],
                "win32": [
                    "sfc /scannow",
                    "dism /online /cleanup-image /restorehealth"
                ]
            }
        }

        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                print(f"✅ Configuration chargée depuis {self.config_file}")
                return config
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement de la config : {e}")
                print("Utilisation de la configuration par défaut")

        # Sauvegarder la configuration par défaut
        with open(self.config_file, 'w') as f:
            json.dump(config_defaut, f, indent=2)
        print(f"📄 Configuration par défaut créée : {self.config_file}")

        return config_defaut

    def log_action(self, action, status, details=""):
        """Enregistre une action dans le log."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "status": status,
            "details": details
        }
        self.log.append(entry)

        # Affichage avec emoji
        emoji = "✅" if status == "succes" else "❌" if status == "erreur" else "ℹ️"
        print(f"{emoji} {action}: {details}")

    def nettoyer_fichiers_temporaires(self):
        """Nettoie les fichiers temporaires dans les répertoires configurés."""
        self.log_action("nettoyage", "info", "Début du nettoyage")

        fichiers_supprimes = 0
        espace_libere = 0

        for repertoire in self.config["repertoires_nettoyage"]:
            repertoire_expanse = os.path.expanduser(repertoire)

            if not os.path.exists(repertoire_expanse):
                self.log_action("nettoyage", "erreur", f"Répertoire non trouvé: {repertoire}")
                continue

            self.log_action("nettoyage", "info", f"Nettoyage de {repertoire_expanse}")

            for racine, dirs, fichiers in os.walk(repertoire_expanse):
                for fichier in fichiers:
                    chemin_complet = os.path.join(racine, fichier)

                    # Vérifier l'âge du fichier
                    try:
                        age_fichier = datetime.fromtimestamp(os.path.getmtime(chemin_complet))
                        limite = datetime.now() - timedelta(days=self.config["jours_retention"])

                        if age_fichier < limite:
                            # Vérifier l'extension
                            _, extension = os.path.splitext(fichier)
                            if extension.lower() in self.config["extensions_temporaires"]:
                                taille = os.path.getsize(chemin_complet)
                                os.remove(chemin_complet)
                                fichiers_supprimes += 1
                                espace_libere += taille

                    except Exception as e:
                        self.log_action("nettoyage", "erreur", f"Erreur avec {fichier}: {e}")

        self.log_action("nettoyage", "succes",
                       f"{fichiers_supprimes} fichiers supprimés, {espace_libere/1024/1024:.2f} MB libérés")

    def executer_maintenance_systeme(self):
        """Exécute les commandes de maintenance système."""
        plateforme = sys.platform
        commandes = self.config["commandes_maintenance"].get(plateforme, [])

        if not commandes:
            self.log_action("maintenance", "erreur", f"Aucune commande définie pour {plateforme}")
            return

        self.log_action("maintenance", "info", f"Maintenance système pour {plateforme}")

        for commande in commandes:
            try:
                self.log_action("commande", "info", f"Exécution: {commande}")

                resultat = subprocess.run(
                    commande,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=300
                )

                if resultat.returncode == 0:
                    self.log_action("commande", "succes", f"'{commande}' terminée")
                else:
                    self.log_action("commande", "erreur",
                                   f"'{commande}' échouée (code {resultat.returncode})")
                    if resultat.stderr:
                        print(f"Erreur détaillée: {resultat.stderr}")

            except subprocess.TimeoutExpired:
                self.log_action("commande", "erreur", f"Timeout pour '{commande}'")
            except Exception as e:
                self.log_action("commande", "erreur", f"Erreur avec '{commande}': {e}")

    def creer_sauvegarde(self, repertoire_source):
        """Crée une sauvegarde d'un répertoire."""
        repertoire_source = os.path.expanduser(repertoire_source)
        repertoire_sauvegarde = os.path.expanduser(self.config["sauvegarde_repertoire"])

        if not os.path.exists(repertoire_source):
            self.log_action("sauvegarde", "erreur", f"Source non trouvée: {repertoire_source}")
            return

        # Créer le répertoire de sauvegarde
        os.makedirs(repertoire_sauvegarde, exist_ok=True)

        # Nom de la sauvegarde avec timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_source = os.path.basename(repertoire_source.rstrip('/\\'))
        nom_sauvegarde = f"{nom_source}_backup_{timestamp}"
        chemin_sauvegarde = os.path.join(repertoire_sauvegarde, nom_sauvegarde)

        try:
            self.log_action("sauvegarde", "info", f"Sauvegarde de {repertoire_source}")

            # Utiliser shutil pour copier récursivement
            shutil.copytree(repertoire_source, chemin_sauvegarde)

            # Calculer la taille de la sauvegarde
            taille = self.calculer_taille_repertoire(chemin_sauvegarde)

            self.log_action("sauvegarde", "succes",
                           f"Sauvegarde créée: {nom_sauvegarde} ({taille/1024/1024:.2f} MB)")

        except Exception as e:
            self.log_action("sauvegarde", "erreur", f"Erreur lors de la sauvegarde: {e}")

    def calculer_taille_repertoire(self, repertoire):
        """Calcule la taille totale d'un répertoire."""
        taille_totale = 0

        for racine, dirs, fichiers in os.walk(repertoire):
            for fichier in fichiers:
                chemin_fichier = os.path.join(racine, fichier)
                try:
                    taille_totale += os.path.getsize(chemin_fichier)
                except OSError:
                    pass  # Ignorer les fichiers inaccessibles

        return taille_totale

    def analyser_espace_disque(self):
        """Analyse l'utilisation de l'espace disque."""
        self.log_action("analyse", "info", "Analyse de l'espace disque")

        try:
            if sys.platform.startswith('win'):
                # Windows
                resultat = subprocess.run(
                    'wmic logicaldisk get size,freespace,caption',
                    shell=True,
                    capture_output=True,
                    text=True
                )
                self.log_action("analyse", "info", "Espace disque Windows analysé")

            else:
                # Linux/Mac
                resultat = subprocess.run(
                    'df -h',
                    shell=True,
                    capture_output=True,
                    text=True
                )

                if resultat.returncode == 0:
                    lignes = resultat.stdout.strip().split('\n')
                    self.log_action("analyse", "info", "Espace disque Unix analysé")

                    # Parser et afficher les informations importantes
                    for ligne in lignes[1:]:  # Ignorer l'en-tête
                        elements = ligne.split()
                        if len(elements) >= 6:
                            systeme_fichiers = elements[0]
                            utilise = elements[2] if len(elements[2]) > 1 else "N/A"
                            disponible = elements[3] if len(elements[3]) > 1 else "N/A"
                            pourcentage = elements[4] if len(elements[4]) > 1 else "N/A"
                            point_montage = elements[5]

                            print(f"📁 {point_montage}: {utilise} utilisé, {disponible} libre ({pourcentage})")

        except Exception as e:
            self.log_action("analyse", "erreur", f"Erreur analyse disque: {e}")

    def generer_rapport(self):
        """Génère un rapport complet de maintenance."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_rapport = f"rapport_maintenance_{timestamp}.txt"

        try:
            with open(nom_rapport, 'w', encoding='utf-8') as f:
                f.write("RAPPORT DE MAINTENANCE SYSTÈME\n")
                f.write("=" * 50 + "\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Système: {sys.platform}\n")
                f.write(f"Python: {sys.version}\n\n")

                # Statistiques générales
                total_actions = len(self.log)
                succes = sum(1 for entry in self.log if entry['status'] == 'succes')
                erreurs = sum(1 for entry in self.log if entry['status'] == 'erreur')

                f.write("RÉSUMÉ\n")
                f.write("-" * 20 + "\n")
                f.write(f"Total d'actions: {total_actions}\n")
                f.write(f"Succès: {succes}\n")
                f.write(f"Erreurs: {erreurs}\n")
                f.write(f"Taux de réussite: {succes/total_actions*100:.1f}%\n\n")

                # Détail des actions
                f.write("DÉTAIL DES ACTIONS\n")
                f.write("-" * 30 + "\n")

                for entry in self.log:
                    f.write(f"[{entry['timestamp']}] {entry['action'].upper()}\n")
                    f.write(f"Status: {entry['status']}\n")
                    f.write(f"Détails: {entry['details']}\n")
                    f.write("-" * 50 + "\n")

            self.log_action("rapport", "succes", f"Rapport généré: {nom_rapport}")

        except Exception as e:
            self.log_action("rapport", "erreur", f"Erreur génération rapport: {e}")

    def maintenance_complete(self, inclure_sauvegarde=False, repertoire_sauvegarde=None):
        """Exécute une maintenance complète du système."""
        print("\n" + "="*60)
        print("🔧 DÉBUT DE LA MAINTENANCE SYSTÈME")
        print("="*60)

        # 1. Analyse de l'espace disque
        self.analyser_espace_disque()

        # 2. Nettoyage des fichiers temporaires
        self.nettoyer_fichiers_temporaires()

        # 3. Sauvegarde si demandée
        if inclure_sauvegarde and repertoire_sauvegarde:
            self.creer_sauvegarde(repertoire_sauvegarde)

        # 4. Maintenance système
        self.executer_maintenance_systeme()

        # 5. Rapport final
        self.generer_rapport()

        print("\n" + "="*60)
        print("✅ MAINTENANCE TERMINÉE")
        print("="*60)

def main():
    """Fonction principale avec interface en ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Outil de maintenance système utilisant os, sys, subprocess"
    )

    parser.add_argument(
        '--action',
        choices=['nettoyage', 'maintenance', 'sauvegarde', 'analyse', 'complet'],
        default='complet',
        help='Type d\'action à effectuer'
    )

    parser.add_argument(
        '--repertoire-sauvegarde',
        help='Répertoire à sauvegarder'
    )

    parser.add_argument(
        '--config',
        default='maintenance_config.json',
        help='Fichier de configuration'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simulation sans modification'
    )

    args = parser.parse_args()

    # Vérification des privilèges si nécessaire
    if args.action == 'maintenance' and not args.dry_run:
        if sys.platform.startswith('win'):
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    print("⚠️  Attention: Privilèges administrateur recommandés pour la maintenance")
            except:
                pass
        else:
            if os.geteuid() != 0:
                print("⚠️  Attention: Privilèges root recommandés pour certaines opérations")

    # Créer l'outil de maintenance
    outil = OutilMaintenance(args.config)

    if args.dry_run:
        print("🔍 MODE SIMULATION ACTIVÉ - Aucune modification ne sera effectuée")
        outil.config["dry_run"] = True

    # Exécuter l'action demandée
    try:
        if args.action == 'nettoyage':
            outil.nettoyer_fichiers_temporaires()

        elif args.action == 'maintenance':
            outil.executer_maintenance_systeme()

        elif args.action == 'sauvegarde':
            if not args.repertoire_sauvegarde:
                print("❌ Erreur: --repertoire-sauvegarde requis pour l'action sauvegarde")
                sys.exit(1)
            outil.creer_sauvegarde(args.repertoire_sauvegarde)

        elif args.action == 'analyse':
            outil.analyser_espace_disque()

        elif args.action == 'complet':
            outil.maintenance_complete(
                inclure_sauvegarde=bool(args.repertoire_sauvegarde),
                repertoire_sauvegarde=args.repertoire_sauvegarde
            )

        # Générer le rapport final
        outil.generer_rapport()

    except KeyboardInterrupt:
        print("\n🛑 Opération interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"💥 Erreur inattendue: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Exercices pratiques

### Exercice 1 : Moniteur de système simple

Créez un moniteur qui surveille les ressources système :

```python
import os
import sys
import subprocess
import time
import psutil  # Installer avec: pip install psutil

class MoniteurSysteme:
    """Moniteur simple des ressources système."""

    def __init__(self, intervalle=5):
        self.intervalle = intervalle
        self.en_cours = False

    def obtenir_info_cpu(self):
        """Récupère l'utilisation du CPU."""
        return psutil.cpu_percent(interval=1)

    def obtenir_info_memoire(self):
        """Récupère l'utilisation de la mémoire."""
        memoire = psutil.virtual_memory()
        return {
            'total': memoire.total,
            'disponible': memoire.available,
            'utilise': memoire.used,
            'pourcentage': memoire.percent
        }

    def obtenir_info_disque(self):
        """Récupère l'utilisation du disque."""
        disque = psutil.disk_usage('/')
        return {
            'total': disque.total,
            'libre': disque.free,
            'utilise': disque.used,
            'pourcentage': (disque.used / disque.total) * 100
        }

    def afficher_rapport(self):
        """Affiche un rapport des ressources."""
        print("\n" + "="*50)
        print(f"📊 RAPPORT SYSTÈME - {time.strftime('%H:%M:%S')}")
        print("="*50)

        # CPU
        cpu = self.obtenir_info_cpu()
        print(f"🖥️  CPU: {cpu:.1f}%")

        # Mémoire
        mem = self.obtenir_info_memoire()
        print(f"🧠 Mémoire: {mem['pourcentage']:.1f}% "
              f"({mem['utilise']/1024**3:.1f}GB / {mem['total']/1024**3:.1f}GB)")

        # Disque
        disque = self.obtenir_info_disque()
        print(f"💾 Disque: {disque['pourcentage']:.1f}% "
              f"({disque['utilise']/1024**3:.1f}GB / {disque['total']/1024**3:.1f}GB)")

        # Processus top
        processus = psutil.process_iter(['pid', 'name', 'cpu_percent'])
        top_processus = sorted(processus, key=lambda p: p.info['cpu_percent'], reverse=True)[:5]

        print("\n🔥 Top 5 processus (CPU):")
        for proc in top_processus:
            print(f"  {proc.info['name']}: {proc.info['cpu_percent']:.1f}%")

    def monitorer(self, duree=None):
        """Lance le monitoring en continu."""
        self.en_cours = True
        cycles = 0

        try:
            while self.en_cours:
                self.afficher_rapport()
                cycles += 1

                if duree and cycles >= duree:
                    break

                time.sleep(self.intervalle)

        except KeyboardInterrupt:
            print("\n🛑 Monitoring arrêté")
        finally:
            self.en_cours = False

# Utilisation
if __name__ == "__main__":
    moniteur = MoniteurSysteme(intervalle=3)
    moniteur.monitorer(duree=10)  # 10 cycles de monitoring
```

### Exercice 2 : Gestionnaire de processus

Créez un gestionnaire pour lancer et surveiller des processus :

```python
import subprocess
import threading
import time
import signal
import sys
import os

class GestionnaireProcessus:
    """Gestionnaire pour lancer et surveiller des processus."""

    def __init__(self):
        self.processus = {}
        self.en_cours = True

        # Gérer l'arrêt propre
        signal.signal(signal.SIGINT, self.arreter_tous)
        if hasattr(signal, 'SIGTERM'):
            signal.signal(signal.SIGTERM, self.arreter_tous)

    def lancer_processus(self, nom, commande, repertoire=None):
        """Lance un nouveau processus."""
        try:
            print(f"🚀 Lancement de '{nom}': {commande}")

            processus = subprocess.Popen(
                commande,
                shell=True,
                cwd=repertoire,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            self.processus[nom] = {
                'processus': processus,
                'commande': commande,
                'debut': time.time(),
                'actif': True
            }

            # Lancer un thread de surveillance
            thread = threading.Thread(
                target=self.surveiller_processus,
                args=(nom,)
            )
            thread.daemon = True
            thread.start()

            print(f"✅ Processus '{nom}' lancé (PID: {processus.pid})")
            return True

        except Exception as e:
            print(f"❌ Erreur lors du lancement de '{nom}': {e}")
            return False

    def surveiller_processus(self, nom):
        """Surveille un processus spécifique."""
        processus_info = self.processus[nom]
        processus = processus_info['processus']

        # Attendre la fin du processus
        code_retour = processus.wait()
        duree = time.time() - processus_info['debut']

        # Lire les sorties
        stdout, stderr = processus.communicate()

        # Mettre à jour le statut
        processus_info['actif'] = False
        processus_info['code_retour'] = code_retour
        processus_info['duree'] = duree
        processus_info['stdout'] = stdout
        processus_info['stderr'] = stderr

        # Afficher le résultat
        if code_retour == 0:
            print(f"✅ Processus '{nom}' terminé avec succès ({duree:.2f}s)")
        else:
            print(f"❌ Processus '{nom}' échoué (code {code_retour}, {duree:.2f}s)")
            if stderr:
                print(f"Erreur: {stderr[:200]}...")

    def arreter_processus(self, nom):
        """Arrête un processus spécifique."""
        if nom not in self.processus:
            print(f"❌ Processus '{nom}' non trouvé")
            return False

        processus_info = self.processus[nom]
        if not processus_info['actif']:
            print(f"ℹ️ Processus '{nom}' déjà terminé")
            return True

        processus = processus_info['processus']

        try:
            print(f"🛑 Arrêt du processus '{nom}'...")
            processus.terminate()

            # Attendre un peu pour un arrêt propre
            try:
                processus.wait(timeout=5)
                print(f"✅ Processus '{nom}' arrêté proprement")
            except subprocess.TimeoutExpired:
                print(f"⚠️ Arrêt forcé du processus '{nom}'")
                processus.kill()
                processus.wait()

            processus_info['actif'] = False
            return True

        except Exception as e:
            print(f"❌ Erreur lors de l'arrêt de '{nom}': {e}")
            return False

    def lister_processus(self):
        """Liste tous les processus gérés."""
        if not self.processus:
            print("Aucun processus géré")
            return

        print("\n📋 PROCESSUS GÉRÉS")
        print("-" * 50)

        for nom, info in self.processus.items():
            statut = "🟢 Actif" if info['actif'] else "🔴 Terminé"
            duree = time.time() - info['debut'] if info['actif'] else info.get('duree', 0)

            print(f"{statut} {nom}")
            print(f"  Commande: {info['commande']}")
            print(f"  Durée: {duree:.2f}s")
            print(f"  PID: {info['processus'].pid}")

            if not info['actif'] and 'code_retour' in info:
                print(f"  Code retour: {info['code_retour']}")

            print()

    def arreter_tous(self, signal_num=None, frame=None):
        """Arrête tous les processus."""
        print("\n🛑 Arrêt de tous les processus...")

        for nom in list(self.processus.keys()):
            if self.processus[nom]['actif']:
                self.arreter_processus(nom)

        self.en_cours = False
        print("✅ Tous les processus arrêtés")

    def executer_batch(self, commandes):
        """Exécute un lot de commandes."""
        print(f"📦 Exécution de {len(commandes)} commandes")

        for i, (nom, commande) in enumerate(commandes, 1):
            print(f"\n[{i}/{len(commandes)}] {nom}")
            self.lancer_processus(f"{nom}_{i}", commande)
            time.sleep(1)  # Petite pause entre les lancements

        # Attendre que tous se terminent
        while any(info['actif'] for info in self.processus.values()):
            time.sleep(1)

        print("\n✅ Toutes les commandes terminées")
        self.lister_processus()

# Exemple d'utilisation
if __name__ == "__main__":
    gestionnaire = GestionnaireProcessus()

    # Définir des commandes selon l'OS
    if sys.platform.startswith('win'):
        commandes = [
            ("ping_google", "ping -n 3 google.com"),
            ("liste_fichiers", "dir"),
            ("info_systeme", "systeminfo")
        ]
    else:
        commandes = [
            ("ping_google", "ping -c 3 google.com"),
            ("liste_fichiers", "ls -la"),
            ("espace_disque", "df -h"),
            ("charge_systeme", "uptime")
        ]

    try:
        gestionnaire.executer_batch(commandes)
    except KeyboardInterrupt:
        print("\n🛑 Interruption utilisateur")
        gestionnaire.arreter_tous()
```

### Exercice 3 : Installateur de logiciels multi-plateforme

Créez un installateur qui s'adapte au système d'exploitation :

```python
import os
import sys
import subprocess
import json
import platform

class InstallateurMultiPlateforme:
    """Installateur de logiciels multi-plateforme."""

    def __init__(self):
        self.systeme = self.detecter_systeme()
        self.gestionnaires = self.obtenir_gestionnaires_paquets()
        self.log_installation = []

    def detecter_systeme(self):
        """Détecte le système d'exploitation et la distribution."""
        info = {
            'os': platform.system(),
            'version': platform.release(),
            'architecture': platform.machine(),
            'distribution': None
        }

        if info['os'] == 'Linux':
            try:
                # Essayer de lire /etc/os-release
                with open('/etc/os-release', 'r') as f:
                    for ligne in f:
                        if ligne.startswith('ID='):
                            info['distribution'] = ligne.split('=')[1].strip().strip('"')
                            break
            except:
                # Fallback vers lsb_release
                try:
                    result = subprocess.run(
                        ['lsb_release', '-si'],
                        capture_output=True,
                        text=True
                    )
                    info['distribution'] = result.stdout.strip().lower()
                except:
                    info['distribution'] = 'unknown'

        return info

    def obtenir_gestionnaires_paquets(self):
        """Obtient les gestionnaires de paquets disponibles selon l'OS."""
        gestionnaires = {}

        if self.systeme['os'] == 'Windows':
            # Vérifier si Chocolatey est installé
            try:
                subprocess.run(['choco', '--version'],
                             capture_output=True, check=True)
                gestionnaires['chocolatey'] = True
            except:
                gestionnaires['chocolatey'] = False

            # Vérifier si winget est disponible
            try:
                subprocess.run(['winget', '--version'],
                             capture_output=True, check=True)
                gestionnaires['winget'] = True
            except:
                gestionnaires['winget'] = False

        elif self.systeme['os'] == 'Darwin':  # macOS
            # Vérifier si Homebrew est installé
            try:
                subprocess.run(['brew', '--version'],
                             capture_output=True, check=True)
                gestionnaires['homebrew'] = True
            except:
                gestionnaires['homebrew'] = False

        elif self.systeme['os'] == 'Linux':
            # Vérifier les gestionnaires Linux courants
            gestionnaires_linux = {
                'apt': ['apt', '--version'],
                'yum': ['yum', '--version'],
                'dnf': ['dnf', '--version'],
                'pacman': ['pacman', '--version'],
                'zypper': ['zypper', '--version']
            }

            for nom, commande in gestionnaires_linux.items():
                try:
                    subprocess.run(commande, capture_output=True, check=True)
                    gestionnaires[nom] = True
                except:
                    gestionnaires[nom] = False

        return gestionnaires

    def installer_paquet(self, nom_paquet, gestionnaire=None):
        """Installe un paquet avec le gestionnaire approprié."""
        if gestionnaire is None:
            gestionnaire = self.choisir_gestionnaire()

        if not gestionnaire:
            print("❌ Aucun gestionnaire de paquets disponible")
            return False

        commandes = self.obtenir_commandes_installation(gestionnaire, nom_paquet)

        for commande in commandes:
            print(f"🚀 Exécution: {' '.join(commande)}")

            try:
                resultat = subprocess.run(
                    commande,
                    capture_output=True,
                    text=True,
                    timeout=300
                )

                if resultat.returncode == 0:
                    print(f"✅ Installation réussie: {nom_paquet}")
                    self.log_installation.append({
                        'paquet': nom_paquet,
                        'gestionnaire': gestionnaire,
                        'statut': 'succes',
                        'commande': ' '.join(commande)
                    })
                    return True
                else:
                    print(f"❌ Erreur d'installation: {resultat.stderr}")
                    self.log_installation.append({
                        'paquet': nom_paquet,
                        'gestionnaire': gestionnaire,
                        'statut': 'erreur',
                        'erreur': resultat.stderr
                    })
                    return False

            except subprocess.TimeoutExpired:
                print(f"⏰ Timeout lors de l'installation de {nom_paquet}")
                return False
            except Exception as e:
                print(f"💥 Erreur inattendue: {e}")
                return False

    def choisir_gestionnaire(self):
        """Choisit le meilleur gestionnaire disponible."""
        if self.systeme['os'] == 'Windows':
            if self.gestionnaires.get('winget'):
                return 'winget'
            elif self.gestionnaires.get('chocolatey'):
                return 'chocolatey'

        elif self.systeme['os'] == 'Darwin':
            if self.gestionnaires.get('homebrew'):
                return 'homebrew'

        elif self.systeme['os'] == 'Linux':
            # Priorité selon la distribution
            if self.gestionnaires.get('apt'):
                return 'apt'
            elif self.gestionnaires.get('dnf'):
                return 'dnf'
            elif self.gestionnaires.get('yum'):
                return 'yum'
            elif self.gestionnaires.get('pacman'):
                return 'pacman'
            elif self.gestionnaires.get('zypper'):
                return 'zypper'

        return None

    def obtenir_commandes_installation(self, gestionnaire, paquet):
        """Retourne les commandes d'installation selon le gestionnaire."""
        commandes_map = {
            'apt': [
                ['sudo', 'apt', 'update'],
                ['sudo', 'apt', 'install', '-y', paquet]
            ],
            'dnf': [
                ['sudo', 'dnf', 'install', '-y', paquet]
            ],
            'yum': [
                ['sudo', 'yum', 'install', '-y', paquet]
            ],
            'pacman': [
                ['sudo', 'pacman', '-Sy', '--noconfirm', paquet]
            ],
            'zypper': [
                ['sudo', 'zypper', 'install', '-y', paquet]
            ],
            'homebrew': [
                ['brew', 'install', paquet]
            ],
            'chocolatey': [
                ['choco', 'install', paquet, '-y']
            ],
            'winget': [
                ['winget', 'install', paquet]
            ]
        }

        return commandes_map.get(gestionnaire, [])

    def installer_liste_paquets(self, fichier_config):
        """Installe une liste de paquets depuis un fichier de configuration."""
        try:
            with open(fichier_config, 'r') as f:
                config = json.load(f)
        except Exception as e:
            print(f"❌ Erreur lecture config: {e}")
            return False

        paquets = config.get('paquets', [])
        gestionnaire = config.get('gestionnaire')

        print(f"📦 Installation de {len(paquets)} paquets")

        succes = 0
        for paquet in paquets:
            if self.installer_paquet(paquet, gestionnaire):
                succes += 1

        print(f"\n📊 Résultat: {succes}/{len(paquets)} paquets installés")
        return succes == len(paquets)

    def afficher_rapport(self):
        """Affiche un rapport d'installation."""
        print("\n" + "="*50)
        print("📋 RAPPORT D'INSTALLATION")
        print("="*50)

        print(f"Système: {self.systeme['os']} {self.systeme['version']}")
        print(f"Architecture: {self.systeme['architecture']}")

        if self.systeme['distribution']:
            print(f"Distribution: {self.systeme['distribution']}")

        print(f"\nGestionnaires disponibles:")
        for gestionnaire, disponible in self.gestionnaires.items():
            statut = "✅" if disponible else "❌"
            print(f"  {statut} {gestionnaire}")

        if self.log_installation:
            print(f"\nInstallations tentées: {len(self.log_installation)}")

            succes = sum(1 for log in self.log_installation if log['statut'] == 'succes')
            echecs = len(self.log_installation) - succes

            print(f"Succès: {succes}")
            print(f"Échecs: {echecs}")

            if echecs > 0:
                print("\nÉchecs détaillés:")
                for log in self.log_installation:
                    if log['statut'] == 'erreur':
                        print(f"  ❌ {log['paquet']}: {log.get('erreur', 'Erreur inconnue')}")
        else:
            print("\nAucune installation tentée")

    def creer_config_exemple(self, nom_fichier="paquets_exemple.json"):
        """Crée un fichier de configuration d'exemple."""
        config_exemple = {
            "description": "Configuration d'installation de paquets",
            "gestionnaire": None,  # Auto-détection
            "paquets": []
        }

        # Adapter selon l'OS
        if self.systeme['os'] == 'Windows':
            config_exemple['paquets'] = [
                "git",
                "python3",
                "vscode",
                "firefox",
                "7zip"
            ]
        elif self.systeme['os'] == 'Darwin':
            config_exemple['paquets'] = [
                "git",
                "python3",
                "visual-studio-code",
                "firefox",
                "wget"
            ]
        elif self.systeme['os'] == 'Linux':
            config_exemple['paquets'] = [
                "git",
                "python3",
                "curl",
                "wget",
                "vim",
                "htop"
            ]

        with open(nom_fichier, 'w') as f:
            json.dump(config_exemple, f, indent=2)

        print(f"📄 Configuration d'exemple créée: {nom_fichier}")

# Exemple d'utilisation complète
def main():
    installateur = InstallateurMultiPlateforme()

    print("🔍 Détection du système...")
    installateur.afficher_rapport()

    # Créer une configuration d'exemple
    installateur.creer_config_exemple()

    # Menu interactif
    while True:
        print("\n" + "="*40)
        print("INSTALLATEUR MULTI-PLATEFORME")
        print("="*40)
        print("1. Installer un paquet")
        print("2. Installer depuis un fichier")
        print("3. Afficher le rapport")
        print("4. Créer config exemple")
        print("5. Quitter")

        choix = input("\nVotre choix (1-5): ").strip()

        if choix == '1':
            paquet = input("Nom du paquet à installer: ").strip()
            if paquet:
                installateur.installer_paquet(paquet)

        elif choix == '2':
            fichier = input("Chemin du fichier de configuration: ").strip()
            if not fichier:
                fichier = "paquets_exemple.json"

            if os.path.exists(fichier):
                installateur.installer_liste_paquets(fichier)
            else:
                print(f"❌ Fichier non trouvé: {fichier}")

        elif choix == '3':
            installateur.afficher_rapport()

        elif choix == '4':
            nom = input("Nom du fichier (défaut: paquets_exemple.json): ").strip()
            if not nom:
                nom = "paquets_exemple.json"
            installateur.creer_config_exemple(nom)

        elif choix == '5':
            print("👋 Au revoir!")
            break

        else:
            print("❌ Choix invalide")

if __name__ == "__main__":
    main()
```

## Récapitulatif des modules os, sys, subprocess

### Module `os` - Points clés

#### **Gestion des fichiers et répertoires**
```python
import os

# Navigation
os.getcwd()                    # Répertoire actuel
os.chdir(path)                # Changer de répertoire
os.listdir(path)              # Lister le contenu

# Création/suppression
os.mkdir(path)                # Créer un répertoire
os.makedirs(path, exist_ok=True)  # Créer récursivement
os.remove(file)               # Supprimer un fichier
os.rmdir(dir)                 # Supprimer un répertoire vide

# Tests
os.path.exists(path)          # Vérifier l'existence
os.path.isfile(path)          # C'est un fichier ?
os.path.isdir(path)           # C'est un répertoire ?
```

#### **Manipulation des chemins**
```python
import os

# Construction portable
os.path.join('dossier', 'fichier.txt')

# Décomposition
os.path.split(path)           # (répertoire, fichier)
os.path.splitext(path)        # (nom, extension)
os.path.dirname(path)         # Répertoire parent
os.path.basename(path)        # Nom du fichier

# Transformations
os.path.abspath(path)         # Chemin absolu
os.path.expanduser('~/docs')  # Expansion du ~
```

#### **Variables d'environnement**
```python
import os

# Lecture
os.environ.get('HOME', '/tmp')    # Avec valeur par défaut
os.environ['USER']                # Direct (peut lever une exception)

# Écriture
os.environ['MA_VARIABLE'] = 'valeur'
```

### Module `sys` - Points clés

#### **Arguments de ligne de commande**
```python
import sys

# sys.argv[0] = nom du script
# sys.argv[1:] = arguments

if len(sys.argv) > 1:
    print(f"Premier argument: {sys.argv[1]}")
```

#### **Informations système**
```python
import sys

sys.version               # Version Python complète
sys.version_info          # Version structurée
sys.platform              # Plateforme (win32, linux, darwin)
sys.executable            # Chemin de l'exécutable Python
sys.path                  # Chemins de recherche des modules
```

#### **Sortie et erreurs**
```python
import sys

print("Message normal", file=sys.stdout)
print("Message d'erreur", file=sys.stderr)

sys.exit(0)               # Quitter avec code de retour
```

### Module `subprocess` - Points clés

#### **Exécution simple**
```python
import subprocess

# Méthode recommandée
result = subprocess.run(
    ['ls', '-la'],            # Commande en liste
    capture_output=True,      # Capturer stdout/stderr
    text=True,                # Mode texte
    timeout=30                # Timeout en secondes
)

# Vérifier le résultat
if result.returncode == 0:
    print(result.stdout)
else:
    print(f"Erreur: {result.stderr}")
```

#### **Exécution avec shell**
```python
import subprocess

# Avec shell (attention à la sécurité)
result = subprocess.run(
    "ls -la | grep python",
    shell=True,
    capture_output=True,
    text=True
)
```

#### **Processus en arrière-plan**
```python
import subprocess

# Lancer sans attendre
process = subprocess.Popen(
    ['ping', 'google.com'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Continuer d'autres tâches...

# Récupérer le résultat plus tard
stdout, stderr = process.communicate()
```

## Bonnes pratiques

### **Sécurité**
```python
# ✅ Bon: utiliser une liste pour les arguments
subprocess.run(['ls', user_input])

# ❌ Dangereux: concaténation avec shell=True
subprocess.run(f"ls {user_input}", shell=True)
```

### **Portabilité**
```python
import os
import sys

# ✅ Portable
chemin = os.path.join('dossier', 'fichier.txt')

# ❌ Spécifique à un OS
chemin = 'dossier\\fichier.txt'  # Windows seulement

# ✅ Adaptation selon l'OS
if sys.platform.startswith('win'):
    commande = ['dir']
else:
    commande = ['ls', '-la']
```

### **Gestion d'erreurs**
```python
import subprocess
import os

try:
    # Opération système
    result = subprocess.run(['command'],
                          capture_output=True,
                          check=True,  # Lève une exception si échec
                          timeout=30)
except subprocess.CalledProcessError as e:
    print(f"Commande échouée: {e}")
except subprocess.TimeoutExpired:
    print("Timeout dépassé")
except FileNotFoundError:
    print("Commande non trouvée")
```

### **Utilisation des chemins modernes**
```python
# Alternative moderne: pathlib (Python 3.4+)
from pathlib import Path

# Plus lisible et orienté objet
chemin = Path.home() / 'Documents' / 'projet'
chemin.mkdir(parents=True, exist_ok=True)

for fichier in chemin.glob('*.py'):
    print(fichier.name)
```

## Cas d'usage courants

### **Scripts d'administration**
- Nettoyage automatique de fichiers
- Sauvegarde de répertoires
- Monitoring de ressources
- Installation de logiciels

### **Outils de développement**
- Build automatique de projets
- Tests d'intégration
- Déploiement automatisé
- Gestion d'environnements

### **Applications système**
- Gestionnaires de fichiers
- Moniteurs de performance
- Outils de maintenance
- Interfaces de ligne de commande

## Exercice final : Outil de diagnostic système

Créez un outil complet qui combine tous les concepts appris :

```python
#!/usr/bin/env python3
"""
Outil de diagnostic système complet
Utilise os, sys, subprocess pour analyser le système
"""

import os
import sys
import subprocess
import platform
import time
import json
from datetime import datetime

def diagnostic_complet():
    """Effectue un diagnostic complet du système."""

    diagnostic = {
        'timestamp': datetime.now().isoformat(),
        'systeme': {},
        'python': {},
        'stockage': {},
        'processus': {},
        'reseau': {}
    }

    print("🔍 DIAGNOSTIC SYSTÈME COMPLET")
    print("=" * 50)

    # 1. Informations système
    print("📋 Collecte des informations système...")
    diagnostic['systeme'] = {
        'os': platform.system(),
        'version': platform.release(),
        'architecture': platform.machine(),
        'processeur': platform.processor(),
        'hostname': platform.node()
    }

    # 2. Informations Python
    print("🐍 Informations Python...")
    diagnostic['python'] = {
        'version': sys.version,
        'executable': sys.executable,
        'path': sys.path[:5],  # Premiers 5 chemins
        'modules_charges': len(sys.modules)
    }

    # 3. Analyse du stockage
    print("💾 Analyse du stockage...")
    try:
        if sys.platform.startswith('win'):
            result = subprocess.run(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'],
                                  capture_output=True, text=True)
        else:
            result = subprocess.run(['df', '-h'], capture_output=True, text=True)

        diagnostic['stockage']['commande'] = result.stdout if result.returncode == 0 else "Erreur"
    except:
        diagnostic['stockage']['erreur'] = "Impossible d'obtenir les informations de stockage"

    # 4. Processus en cours
    print("⚙️ Analyse des processus...")
    try:
        if sys.platform.startswith('win'):
            result = subprocess.run(['tasklist', '/FO', 'CSV'], capture_output=True, text=True)
        else:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)

        if result.returncode == 0:
            lignes = result.stdout.split('\n')
            diagnostic['processus']['total'] = len(lignes) - 1
            diagnostic['processus']['echantillon'] = lignes[:5]
    except:
        diagnostic['processus']['erreur'] = "Impossible d'obtenir la liste des processus"

    # 5. Test réseau
    print("🌐 Test de connectivité réseau...")
    try:
        if sys.platform.startswith('win'):
            result = subprocess.run(['ping', '-n', '3', 'google.com'],
                                  capture_output=True, text=True, timeout=10)
        else:
            result = subprocess.run(['ping', '-c', '3', 'google.com'],
                                  capture_output=True, text=True, timeout=10)

        diagnostic['reseau']['ping_google'] = result.returncode == 0
    except:
        diagnostic['reseau']['ping_google'] = False

    # 6. Variables d'environnement importantes
    print("🔧 Variables d'environnement...")
    variables_importantes = ['PATH', 'HOME', 'USER', 'USERNAME', 'LANG', 'SHELL']
    diagnostic['environnement'] = {}

    for var in variables_importantes:
        valeur = os.environ.get(var)
        if valeur:
            # Tronquer les valeurs très longues
            diagnostic['environnement'][var] = valeur[:100] + "..." if len(valeur) > 100 else valeur

    # 7. Sauvegarde du diagnostic
    nom_fichier = f"diagnostic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        json.dump(diagnostic, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Diagnostic terminé")
    print(f"📄 Rapport sauvegardé: {nom_fichier}")

    # 8. Résumé à l'écran
    print("\n📊 RÉSUMÉ")
    print("-" * 30)
    print(f"Système: {diagnostic['systeme']['os']} {diagnostic['systeme']['version']}")
    print(f"Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"Architecture: {diagnostic['systeme']['architecture']}")
    print(f"Connectivité: {'✅' if diagnostic['reseau']['ping_google'] else '❌'}")

    return diagnostic

if __name__ == "__main__":
    try:
        diagnostic_complet()
    except KeyboardInterrupt:
        print("\n🛑 Diagnostic interrompu")
        sys.exit(1)
    except Exception as e:
        print(f"💥 Erreur inattendue: {e}")
        sys.exit(1)
```

## Conclusion

Les modules `os`, `sys`, et `subprocess` forment la base de tout script Python qui interagit avec le système. Ils permettent de :

- **Naviguer** dans le système de fichiers de manière portable
- **Obtenir des informations** sur l'environnement d'exécution
- **Exécuter des commandes** externes et intégrer Python avec d'autres outils
- **Créer des applications** robustes et multiplateformes

Maîtriser ces modules vous permet de créer des outils d'administration, des scripts d'automatisation, et des applications qui s'intègrent parfaitement dans leur environnement système.

Dans la prochaine section, nous explorerons les modules `datetime` et `time` pour la gestion du temps dans vos applications.

⏭️
