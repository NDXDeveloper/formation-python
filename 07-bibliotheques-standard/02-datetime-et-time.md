🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.2 Les modules datetime et time

## Introduction

La gestion du temps est un aspect essentiel de la programmation. Que ce soit pour enregistrer quand un événement s'est produit, calculer des durées, programmer des tâches, ou simplement afficher la date et l'heure, Python offre deux modules puissants : `datetime` et `time`.

Dans cette section, nous allons explorer ces deux modules en détail, avec de nombreux exemples pratiques pour vous permettre de maîtriser la manipulation des dates et des heures en Python.

---

## Le module `datetime` - Manipulation de dates et heures

Le module `datetime` est le plus utilisé pour travailler avec des dates et des heures de manière intuitive et orientée objet.

### Import du module

```python
import datetime

# Ou importer des classes spécifiques
from datetime import datetime, date, time, timedelta
```

---

## La classe `datetime.datetime` - Date et heure combinées

### Obtenir la date et l'heure actuelles

```python
from datetime import datetime

# Date et heure actuelles
maintenant = datetime.now()
print(maintenant)  # 2025-10-27 14:30:45.123456

# Date et heure en UTC (temps universel coordonné)
maintenant_utc = datetime.utcnow()
print(maintenant_utc)
```

### Créer une date/heure spécifique

```python
from datetime import datetime

# Créer une date et heure précise
noel = datetime(2025, 12, 25, 18, 0, 0)
print(noel)  # 2025-12-25 18:00:00

# Avec seulement la date (heure à 00:00:00)
anniversaire = datetime(1990, 5, 15)
print(anniversaire)  # 1990-05-15 00:00:00
```

### Accéder aux composants d'une date/heure

```python
from datetime import datetime

maintenant = datetime.now()

# Accéder aux différents composants
print(f"Année : {maintenant.year}")
print(f"Mois : {maintenant.month}")
print(f"Jour : {maintenant.day}")
print(f"Heure : {maintenant.hour}")
print(f"Minute : {maintenant.minute}")
print(f"Seconde : {maintenant.second}")
print(f"Microseconde : {maintenant.microsecond}")

# Jour de la semaine (0 = lundi, 6 = dimanche)
print(f"Jour de la semaine : {maintenant.weekday()}")

# Jour de la semaine (1 = lundi, 7 = dimanche)
print(f"ISO weekday : {maintenant.isoweekday()}")
```

### Formatage de dates - Conversion en chaîne de caractères

Le formatage permet de convertir un objet `datetime` en une chaîne de caractères selon un format spécifique.

```python
from datetime import datetime

maintenant = datetime.now()

# Format par défaut
print(maintenant)  # 2025-10-27 14:30:45.123456

# Formats personnalisés avec strftime()
print(maintenant.strftime("%d/%m/%Y"))  # 27/10/2025
print(maintenant.strftime("%d-%m-%Y %H:%M:%S"))  # 27-10-2025 14:30:45
print(maintenant.strftime("%A %d %B %Y"))  # Monday 27 October 2025
print(maintenant.strftime("%H:%M"))  # 14:30

# Formats courants
print(maintenant.strftime("%Y-%m-%d"))  # Format ISO : 2025-10-27
print(maintenant.strftime("%d/%m/%y"))  # Format court : 27/10/25
print(maintenant.strftime("%I:%M %p"))  # Format 12h : 02:30 PM
```

**Principaux codes de formatage :**

| Code | Signification | Exemple |
|------|---------------|---------|
| `%Y` | Année (4 chiffres) | 2025 |
| `%y` | Année (2 chiffres) | 25 |
| `%m` | Mois (01-12) | 10 |
| `%B` | Nom du mois complet | October |
| `%b` | Nom du mois abrégé | Oct |
| `%d` | Jour du mois (01-31) | 27 |
| `%A` | Nom du jour complet | Monday |
| `%a` | Nom du jour abrégé | Mon |
| `%H` | Heure (00-23) | 14 |
| `%I` | Heure (01-12) | 02 |
| `%M` | Minutes (00-59) | 30 |
| `%S` | Secondes (00-59) | 45 |
| `%p` | AM/PM | PM |

### Parsing - Conversion depuis une chaîne de caractères

L'opération inverse du formatage : créer un objet `datetime` depuis une chaîne de caractères.

```python
from datetime import datetime

# Parser une date depuis une chaîne
date_str = "27/10/2025 14:30:45"
date_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
print(date_obj)  # 2025-10-27 14:30:45

# Autres exemples
date1 = datetime.strptime("2025-10-27", "%Y-%m-%d")
date2 = datetime.strptime("27 October 2025", "%d %B %Y")
date3 = datetime.strptime("10/27/25", "%m/%d/%y")

print(date1)  # 2025-10-27 00:00:00
print(date2)  # 2025-10-27 00:00:00
print(date3)  # 2025-10-27 00:00:00
```

### Exemple pratique : Calculer l'âge d'une personne

```python
from datetime import datetime

def calculer_age(date_naissance):
    """Calcule l'âge d'une personne à partir de sa date de naissance"""
    aujourd_hui = datetime.now()

    # Calculer l'âge
    age = aujourd_hui.year - date_naissance.year

    # Vérifier si l'anniversaire est passé cette année
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1

    return age

# Exemple d'utilisation
date_naissance = datetime(1990, 5, 15)
age = calculer_age(date_naissance)
print(f"Âge : {age} ans")

# Avec parsing depuis une chaîne
date_naissance_str = "15/05/1990"
date_naissance = datetime.strptime(date_naissance_str, "%d/%m/%Y")
age = calculer_age(date_naissance)
print(f"Âge : {age} ans")
```

---

## La classe `datetime.date` - Dates uniquement (sans heure)

Pour travailler uniquement avec des dates (sans l'heure), utilisez la classe `date`.

```python
from datetime import date

# Date d'aujourd'hui
aujourd_hui = date.today()
print(aujourd_hui)  # 2025-10-27

# Créer une date spécifique
noel = date(2025, 12, 25)
print(noel)  # 2025-12-25

# Accéder aux composants
print(f"Année : {aujourd_hui.year}")
print(f"Mois : {aujourd_hui.month}")
print(f"Jour : {aujourd_hui.day}")

# Formatage
print(aujourd_hui.strftime("%d/%m/%Y"))  # 27/10/2025
print(aujourd_hui.strftime("%A %d %B %Y"))  # Monday 27 October 2025

# Jour de la semaine
print(aujourd_hui.weekday())  # 0 (lundi)
print(aujourd_hui.isoweekday())  # 1 (lundi)
```

---

## La classe `datetime.time` - Heures uniquement (sans date)

Pour travailler uniquement avec des heures (sans la date), utilisez la classe `time`.

```python
from datetime import time

# Créer une heure spécifique
heure_reunion = time(14, 30, 0)  # 14h30m00s
print(heure_reunion)  # 14:30:00

# Avec microsecondes
heure_precise = time(14, 30, 45, 123456)
print(heure_precise)  # 14:30:45.123456

# Accéder aux composants
print(f"Heure : {heure_reunion.hour}")
print(f"Minute : {heure_reunion.minute}")
print(f"Seconde : {heure_reunion.second}")

# Formatage
print(heure_reunion.strftime("%H:%M"))  # 14:30
print(heure_reunion.strftime("%I:%M %p"))  # 02:30 PM
```

---

## La classe `timedelta` - Durées et différences de temps

`timedelta` représente une durée, c'est-à-dire la différence entre deux dates ou heures.

### Créer des durées

```python
from datetime import timedelta

# Créer des durées
un_jour = timedelta(days=1)
une_semaine = timedelta(weeks=1)
deux_heures = timedelta(hours=2)
trente_minutes = timedelta(minutes=30)
dix_secondes = timedelta(seconds=10)

# Combiner plusieurs unités
duree = timedelta(days=2, hours=3, minutes=30)
print(duree)  # 2 days, 3:30:00

# Convertir en différentes unités
print(f"Jours totaux : {duree.days}")
print(f"Secondes totales : {duree.total_seconds()}")
```

### Opérations arithmétiques avec les dates

```python
from datetime import datetime, timedelta

maintenant = datetime.now()
print(f"Maintenant : {maintenant}")

# Ajouter une durée
demain = maintenant + timedelta(days=1)
print(f"Demain : {demain}")

dans_une_semaine = maintenant + timedelta(weeks=1)
print(f"Dans une semaine : {dans_une_semaine}")

dans_trois_heures = maintenant + timedelta(hours=3)
print(f"Dans 3 heures : {dans_trois_heures}")

# Soustraire une durée
hier = maintenant - timedelta(days=1)
print(f"Hier : {hier}")

il_y_a_un_mois = maintenant - timedelta(days=30)
print(f"Il y a un mois : {il_y_a_un_mois}")
```

### Calculer la différence entre deux dates

```python
from datetime import datetime, date

# Avec datetime
debut = datetime(2025, 1, 1)
fin = datetime(2025, 12, 31)

difference = fin - debut
print(f"Différence : {difference}")  # 364 days, 0:00:00
print(f"Nombre de jours : {difference.days}")  # 364
print(f"Nombre de secondes : {difference.total_seconds()}")

# Avec date
naissance = date(1990, 5, 15)
aujourd_hui = date.today()

jours_vecus = aujourd_hui - naissance
print(f"Jours vécus : {jours_vecus.days}")
print(f"Années approximatives : {jours_vecus.days / 365.25:.1f}")
```

### Exemple pratique : Calculer le temps restant jusqu'à une date

```python
from datetime import datetime, timedelta

def temps_restant(date_cible):
    """Calcule le temps restant jusqu'à une date cible"""
    maintenant = datetime.now()
    difference = date_cible - maintenant

    if difference.total_seconds() < 0:
        return "Cette date est déjà passée!"

    jours = difference.days
    heures, reste = divmod(difference.seconds, 3600)
    minutes, secondes = divmod(reste, 60)

    return f"{jours} jours, {heures} heures, {minutes} minutes, {secondes} secondes"

# Exemple : Temps jusqu'à Noël
noel = datetime(2025, 12, 25, 0, 0, 0)
print(f"Temps restant jusqu'à Noël : {temps_restant(noel)}")

# Exemple : Temps jusqu'au Nouvel An
nouvel_an = datetime(2026, 1, 1, 0, 0, 0)
print(f"Temps restant jusqu'au Nouvel An : {temps_restant(nouvel_an)}")
```

---

## Comparaison de dates

Les objets `datetime` peuvent être comparés directement.

```python
from datetime import datetime, date

# Avec datetime
date1 = datetime(2025, 10, 27)
date2 = datetime(2025, 12, 25)

print(date1 < date2)   # True
print(date1 > date2)   # False
print(date1 == date2)  # False
print(date1 != date2)  # True

# Avec date
aujourd_hui = date.today()
noel = date(2025, 12, 25)

if aujourd_hui < noel:
    print("Noël n'est pas encore passé")
else:
    print("Noël est passé")

# Trouver la date la plus récente
dates = [
    datetime(2025, 1, 15),
    datetime(2025, 6, 20),
    datetime(2025, 3, 10)
]

date_la_plus_recente = max(dates)
date_la_plus_ancienne = min(dates)

print(f"Date la plus récente : {date_la_plus_recente}")
print(f"Date la plus ancienne : {date_la_plus_ancienne}")
```

---

## Le module `time` - Temps bas niveau

Le module `time` fournit des fonctions pour travailler avec le temps à un niveau plus bas, notamment pour mesurer des durées d'exécution et créer des délais.

### Import du module

```python
import time
```

### Obtenir le temps actuel (timestamp)

Un timestamp est le nombre de secondes écoulées depuis le 1er janvier 1970 (époque Unix).

```python
import time

# Timestamp actuel (secondes depuis l'époque Unix)
timestamp = time.time()
print(f"Timestamp : {timestamp}")  # Exemple : 1698415845.123456

# Convertir un timestamp en structure de temps lisible
temps_local = time.localtime(timestamp)
print(temps_local)

# Afficher de manière formatée
print(time.strftime("%Y-%m-%d %H:%M:%S", temps_local))
```

### Conversion entre datetime et timestamp

```python
import time
from datetime import datetime

# De datetime vers timestamp
maintenant = datetime.now()
timestamp = maintenant.timestamp()
print(f"Timestamp : {timestamp}")

# De timestamp vers datetime
timestamp = 1698415845
date_depuis_timestamp = datetime.fromtimestamp(timestamp)
print(f"Date : {date_depuis_timestamp}")
```

### Mettre en pause l'exécution avec `sleep()`

La fonction `sleep()` met le programme en pause pendant un nombre de secondes spécifié.

```python
import time

print("Début")
time.sleep(2)  # Pause de 2 secondes
print("2 secondes se sont écoulées")

# Avec des fractions de seconde
time.sleep(0.5)  # Pause de 0,5 seconde
print("0,5 seconde supplémentaire")
```

### Exemple pratique : Compte à rebours

```python
import time

def compte_a_rebours(secondes):
    """Affiche un compte à rebours"""
    while secondes > 0:
        print(f"{secondes}...", end=" ", flush=True)
        time.sleep(1)
        secondes -= 1
    print("C'est parti ! 🚀")

# Exemple d'utilisation
print("Début du compte à rebours :")
compte_a_rebours(5)
```

### Mesurer le temps d'exécution

```python
import time

# Méthode 1 : Avec time.time()
debut = time.time()

# Code à mesurer
total = 0
for i in range(1000000):
    total += i

fin = time.time()
duree = fin - debut
print(f"Temps d'exécution : {duree:.4f} secondes")

# Méthode 2 : Avec time.perf_counter() (plus précis)
debut = time.perf_counter()

# Code à mesurer
resultat = sum(range(1000000))

fin = time.perf_counter()
duree = fin - debut
print(f"Temps d'exécution : {duree:.6f} secondes")
```

### Exemple pratique : Chronomètre

```python
import time

class Chronometre:
    """Classe simple pour chronométrer des opérations"""

    def __init__(self):
        self.debut = None
        self.fin = None

    def demarrer(self):
        """Démarre le chronomètre"""
        self.debut = time.perf_counter()
        print("⏱️  Chronomètre démarré")

    def arreter(self):
        """Arrête le chronomètre et affiche le temps"""
        if self.debut is None:
            print("Le chronomètre n'a pas été démarré!")
            return

        self.fin = time.perf_counter()
        duree = self.fin - self.debut
        print(f"⏱️  Temps écoulé : {duree:.4f} secondes")
        return duree

    def __enter__(self):
        """Support du contexte manager (with)"""
        self.demarrer()
        return self

    def __exit__(self, *args):
        """Fin du contexte manager"""
        self.arreter()

# Utilisation classique
chrono = Chronometre()
chrono.demarrer()
time.sleep(2)
chrono.arreter()

# Utilisation avec context manager
print("\nAvec context manager :")
with Chronometre():
    # Code à chronométrer
    time.sleep(1.5)
    resultat = sum(range(1000000))
```

---

## Fuseaux horaires avec `datetime`

Pour travailler avec des fuseaux horaires, utilisez le module `zoneinfo` (Python 3.9+) ou `pytz` pour les versions antérieures.

### Avec zoneinfo (Python 3.9+)

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Heure actuelle dans différents fuseaux horaires
maintenant_paris = datetime.now(ZoneInfo("Europe/Paris"))
maintenant_tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))
maintenant_ny = datetime.now(ZoneInfo("America/New_York"))

print(f"Paris : {maintenant_paris}")
print(f"Tokyo : {maintenant_tokyo}")
print(f"New York : {maintenant_ny}")

# Convertir une date d'un fuseau à un autre
date_paris = datetime(2025, 10, 27, 14, 30, tzinfo=ZoneInfo("Europe/Paris"))
date_tokyo = date_paris.astimezone(ZoneInfo("Asia/Tokyo"))

print(f"14h30 à Paris correspond à {date_tokyo.strftime('%H:%M')} à Tokyo")
```

### Date et heure UTC

```python
from datetime import datetime, timezone

# Heure UTC actuelle
maintenant_utc = datetime.now(timezone.utc)
print(f"UTC : {maintenant_utc}")

# Créer une date en UTC
date_utc = datetime(2025, 10, 27, 12, 0, 0, tzinfo=timezone.utc)
print(date_utc)
```

---

## Exemples pratiques complets

### 1. Système de rappels

```python
from datetime import datetime, timedelta

class Rappel:
    """Système simple de rappels"""

    def __init__(self):
        self.rappels = []

    def ajouter(self, message, dans_combien_de_temps):
        """Ajoute un rappel

        Args:
            message: Message du rappel
            dans_combien_de_temps: timedelta indiquant quand le rappel doit sonner
        """
        moment = datetime.now() + dans_combien_de_temps
        self.rappels.append({
            'message': message,
            'moment': moment
        })
        print(f"✅ Rappel ajouté pour {moment.strftime('%d/%m/%Y à %H:%M')}")

    def verifier(self):
        """Vérifie si des rappels doivent sonner"""
        maintenant = datetime.now()
        rappels_a_supprimer = []

        for i, rappel in enumerate(self.rappels):
            if maintenant >= rappel['moment']:
                print(f"🔔 RAPPEL : {rappel['message']}")
                rappels_a_supprimer.append(i)

        # Supprimer les rappels qui ont sonné (en partant de la fin)
        for i in reversed(rappels_a_supprimer):
            del self.rappels[i]

    def lister(self):
        """Liste tous les rappels actifs"""
        if not self.rappels:
            print("Aucun rappel actif")
            return

        print("\n📋 Rappels actifs :")
        for rappel in sorted(self.rappels, key=lambda r: r['moment']):
            temps_restant = rappel['moment'] - datetime.now()
            jours = temps_restant.days
            heures = temps_restant.seconds // 3600
            minutes = (temps_restant.seconds % 3600) // 60

            print(f"  • {rappel['message']}")
            print(f"    Dans {jours}j {heures}h {minutes}min")

# Exemple d'utilisation
systeme = Rappel()

# Ajouter des rappels
systeme.ajouter("Réunion d'équipe", timedelta(hours=2))
systeme.ajouter("Appeler le dentiste", timedelta(days=1))
systeme.ajouter("Réviser Python", timedelta(hours=1, minutes=30))

# Lister les rappels
systeme.lister()

# Vérifier les rappels (à appeler régulièrement)
systeme.verifier()
```

### 2. Journal de logs avec horodatage

```python
from datetime import datetime

class Journal:
    """Système simple de journal avec horodatage"""

    def __init__(self, nom_fichier="journal.txt"):
        self.nom_fichier = nom_fichier

    def log(self, message, niveau="INFO"):
        """Ajoute une entrée au journal

        Args:
            message: Message à enregistrer
            niveau: Niveau du log (INFO, WARNING, ERROR)
        """
        maintenant = datetime.now()
        timestamp = maintenant.strftime("%Y-%m-%d %H:%M:%S")

        ligne = f"[{timestamp}] [{niveau}] {message}\n"

        # Écrire dans le fichier
        with open(self.nom_fichier, "a", encoding="utf-8") as f:
            f.write(ligne)

        # Afficher aussi dans la console
        print(ligne.strip())

    def info(self, message):
        """Log de niveau INFO"""
        self.log(message, "INFO")

    def warning(self, message):
        """Log de niveau WARNING"""
        self.log(message, "WARNING")

    def error(self, message):
        """Log de niveau ERROR"""
        self.log(message, "ERROR")

    def lire(self, dernieres_lignes=10):
        """Lit les dernières entrées du journal"""
        try:
            with open(self.nom_fichier, "r", encoding="utf-8") as f:
                lignes = f.readlines()
                print(f"\n📖 Dernières {dernieres_lignes} entrées :")
                for ligne in lignes[-dernieres_lignes:]:
                    print(ligne.strip())
        except FileNotFoundError:
            print("Le journal est vide")

# Exemple d'utilisation
journal = Journal()

journal.info("Application démarrée")
journal.info("Connexion à la base de données")
journal.warning("Mémoire utilisée : 80%")
journal.error("Échec de connexion au serveur")
journal.info("Application arrêtée")

# Lire le journal
journal.lire()
```

### 3. Calculateur de durées de travail

```python
from datetime import datetime, timedelta

class CalculateurTravail:
    """Calcule les heures de travail et les pauses"""

    def __init__(self):
        self.entrees = []

    def pointer_entree(self):
        """Enregistre une entrée (arrivée au travail)"""
        maintenant = datetime.now()
        self.entrees.append({
            'type': 'entree',
            'moment': maintenant
        })
        print(f"✅ Entrée enregistrée à {maintenant.strftime('%H:%M:%S')}")

    def pointer_sortie(self):
        """Enregistre une sortie (départ du travail)"""
        maintenant = datetime.now()
        self.entrees.append({
            'type': 'sortie',
            'moment': maintenant
        })
        print(f"✅ Sortie enregistrée à {maintenant.strftime('%H:%M:%S')}")

    def calculer_temps_travail(self):
        """Calcule le temps de travail total"""
        temps_total = timedelta()
        dernier_entree = None

        for entree in self.entrees:
            if entree['type'] == 'entree':
                dernier_entree = entree['moment']
            elif entree['type'] == 'sortie' and dernier_entree:
                duree = entree['moment'] - dernier_entree
                temps_total += duree
                dernier_entree = None

        heures = temps_total.total_seconds() / 3600
        return heures

    def afficher_resume(self):
        """Affiche un résumé de la journée"""
        if not self.entrees:
            print("Aucun pointage enregistré")
            return

        print("\n📊 Résumé de la journée :")
        print("-" * 40)

        for entree in self.entrees:
            type_emoji = "📥" if entree['type'] == 'entree' else "📤"
            type_texte = "Entrée" if entree['type'] == 'entree' else "Sortie"
            heure = entree['moment'].strftime('%H:%M:%S')
            print(f"{type_emoji} {type_texte} : {heure}")

        heures_travaillees = self.calculer_temps_travail()
        print("-" * 40)
        print(f"⏱️  Temps de travail total : {heures_travaillees:.2f} heures")

        # Calcul de la rémunération (exemple avec taux horaire)
        taux_horaire = 15.0  # euros par heure
        salaire = heures_travaillees * taux_horaire
        print(f"💰 Salaire estimé : {salaire:.2f} €")

# Exemple d'utilisation
calculateur = CalculateurTravail()

# Simuler une journée de travail
calculateur.pointer_entree()   # 08:00
import time
time.sleep(1)  # Simuler le passage du temps
calculateur.pointer_sortie()   # Pause déjeuner à 12:00
time.sleep(1)
calculateur.pointer_entree()   # Reprise à 13:00
time.sleep(1)
calculateur.pointer_sortie()   # Fin à 17:00

# Afficher le résumé
calculateur.afficher_resume()
```

### 4. Calculateur d'échéances

```python
from datetime import datetime, timedelta

def calculer_echeances(date_debut, montant_total, nombre_mensualites):
    """Calcule les échéances d'un prêt

    Args:
        date_debut: Date de début du prêt
        montant_total: Montant total à rembourser
        nombre_mensualites: Nombre de mensualités

    Returns:
        Liste des échéances
    """
    echeances = []
    montant_mensuel = montant_total / nombre_mensualites

    for i in range(nombre_mensualites):
        # Calculer la date (on ajoute i mois)
        mois_total = date_debut.month + i
        annee = date_debut.year + (mois_total - 1) // 12
        mois = ((mois_total - 1) % 12) + 1

        # Gérer les jours invalides (ex: 31 février)
        jour = min(date_debut.day, [31, 29 if annee % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][mois - 1])

        date_echeance = datetime(annee, mois, jour)

        echeances.append({
            'numero': i + 1,
            'date': date_echeance,
            'montant': montant_mensuel,
            'reste': montant_total - (montant_mensuel * (i + 1))
        })

    return echeances

# Exemple : Prêt de 10 000€ sur 12 mois
date_debut = datetime(2025, 1, 15)
montant = 10000
duree = 12

print("📋 Plan de remboursement")
print("=" * 60)

echeances = calculer_echeances(date_debut, montant, duree)

for ech in echeances:
    date_str = ech['date'].strftime('%d/%m/%Y')
    print(f"Mensualité {ech['numero']:2d} - {date_str} : "
          f"{ech['montant']:7.2f}€ (reste : {ech['reste']:7.2f}€)")

print("=" * 60)
print(f"Total : {montant:.2f}€")
```

---

## Bonnes pratiques

### 1. Toujours utiliser datetime pour les dates

```python
# ❌ Éviter les chaînes de caractères pour les calculs
date_str = "2025-10-27"
# Difficile de faire des calculs avec des chaînes

# ✅ Utiliser des objets datetime
from datetime import datetime
date_obj = datetime(2025, 10, 27)
# Facile de faire des calculs
```

### 2. Utiliser UTC pour stocker les dates

```python
from datetime import datetime, timezone

# ✅ Stocker en UTC
date_utc = datetime.now(timezone.utc)

# Convertir en temps local pour l'affichage
date_locale = date_utc.astimezone()
```

### 3. Préférer perf_counter() pour mesurer des performances

```python
import time

# ❌ Moins précis
debut = time.time()
# code...
fin = time.time()

# ✅ Plus précis
debut = time.perf_counter()
# code...
fin = time.perf_counter()
```

### 4. Formater les dates de manière cohérente

```python
from datetime import datetime

# ✅ Format ISO pour le stockage
date_iso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ✅ Format localisé pour l'affichage
date_affichage = datetime.now().strftime("%d/%m/%Y à %H:%M")
```

### 5. Gérer les erreurs de parsing

```python
from datetime import datetime

def parser_date_securise(date_str, format_str):
    """Parse une date avec gestion d'erreur"""
    try:
        return datetime.strptime(date_str, format_str)
    except ValueError as e:
        print(f"Erreur de parsing : {e}")
        return None

# Utilisation
date = parser_date_securise("2025-13-01", "%Y-%m-%d")  # Mois invalide
if date:
    print(date)
else:
    print("Date invalide")
```

---

## Résumé

### Module datetime

| Classe | Usage | Exemple |
|--------|-------|---------|
| `datetime` | Date et heure complètes | `datetime.now()` |
| `date` | Date uniquement | `date.today()` |
| `time` | Heure uniquement | `time(14, 30)` |
| `timedelta` | Durée/différence | `timedelta(days=7)` |

### Module time

| Fonction | Usage |
|----------|-------|
| `time()` | Timestamp actuel |
| `sleep()` | Mettre en pause |
| `perf_counter()` | Mesurer des performances |
| `strftime()` | Formater le temps |

### Opérations courantes

```python
from datetime import datetime, timedelta

# Obtenir la date/heure actuelle
maintenant = datetime.now()

# Créer une date spécifique
date = datetime(2025, 12, 25, 18, 0)

# Formater
texte = maintenant.strftime("%d/%m/%Y %H:%M")

# Parser
date = datetime.strptime("27/10/2025", "%d/%m/%Y")

# Calculer une différence
difference = date2 - date1

# Ajouter/Soustraire une durée
future = maintenant + timedelta(days=7)
passé = maintenant - timedelta(hours=3)
```

Les modules `datetime` et `time` sont essentiels pour toute application Python qui manipule des dates, des heures ou des durées. Avec la pratique, vous serez capable de gérer facilement tous vos besoins liés au temps !

⏭️ [math, random, statistics](/07-bibliotheques-standard/03-math-random-statistics.md)
