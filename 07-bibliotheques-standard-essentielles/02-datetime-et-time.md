🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.2 : datetime et time

## Introduction

La gestion du temps est cruciale dans presque toutes les applications. Python fournit deux modules principaux pour travailler avec le temps : `datetime` pour la manipulation des dates et heures, et `time` pour les opérations temporelles de base et la mesure de performance.

### Analogie simple
Imaginez que vous organisez un événement :
- **time** : c'est votre **chronomètre** (mesurer des durées, faire des pauses)
- **datetime** : c'est votre **agenda** (dates, heures, rendez-vous, fuseaux horaires)

## Module time : Les bases temporelles

Le module `time` fournit des fonctions de base pour travailler avec le temps système.

### Temps Unix et timestamps

```python
import time

# Obtenir le timestamp actuel (secondes depuis le 1er janvier 1970)
maintenant = time.time()
print(f"Timestamp actuel : {maintenant}")
print(f"Timestamp arrondi : {int(maintenant)}")

# Convertir un timestamp en temps lisible
temps_lisible = time.ctime(maintenant)
print(f"Temps lisible : {temps_lisible}")

# Temps UTC vs temps local
temps_utc = time.gmtime(maintenant)
temps_local = time.localtime(maintenant)

print(f"UTC : {time.asctime(temps_utc)}")
print(f"Local : {time.asctime(temps_local)}")
```

### Pauses et temporisation

```python
import time

def demo_pauses():
    """Démonstration des différentes façons de faire des pauses."""

    print("Début de la démonstration...")

    # Pause simple
    print("Pause de 2 secondes...")
    time.sleep(2)
    print("Réveil !")

    # Pause avec feedback
    print("Compte à rebours de 5 secondes :")
    for i in range(5, 0, -1):
        print(f"  {i}...")
        time.sleep(1)
    print("  🚀 Décollage !")

# Exécuter la démo
demo_pauses()
```

### Mesure de performance

```python
import time

def mesurer_performance(fonction, *args, **kwargs):
    """Mesure le temps d'exécution d'une fonction."""

    # time.perf_counter() est plus précis pour mesurer des durées
    debut = time.perf_counter()

    # Exécuter la fonction
    resultat = fonction(*args, **kwargs)

    fin = time.perf_counter()
    duree = fin - debut

    print(f"⏱️  Fonction '{fonction.__name__}' exécutée en {duree:.4f} secondes")
    return resultat, duree

# Exemple d'utilisation
def calcul_lent(n):
    """Simule un calcul qui prend du temps."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Mesurer le calcul
resultat, duree = mesurer_performance(calcul_lent, 100000)
print(f"Résultat : {resultat}")

# Comparer différentes approches
def calcul_rapide(n):
    """Version optimisée du calcul."""
    return sum(i ** 2 for i in range(n))

print("\nComparaison de performance :")
mesurer_performance(calcul_lent, 50000)
mesurer_performance(calcul_rapide, 50000)
```

### Formatage du temps

```python
import time

def afficher_formats_temps():
    """Montre différents formats de temps."""

    maintenant = time.time()
    temps_struct = time.localtime(maintenant)

    print("🕐 FORMATS DE TEMPS")
    print("-" * 30)

    # Formats prédéfinis
    print(f"ctime()     : {time.ctime(maintenant)}")
    print(f"asctime()   : {time.asctime(temps_struct)}")

    # Formatage personnalisé avec strftime
    formats = {
        "Date simple": "%Y-%m-%d",
        "Heure simple": "%H:%M:%S",
        "DateTime complet": "%Y-%m-%d %H:%M:%S",
        "Format français": "%d/%m/%Y à %H:%M",
        "Format long": "%A %d %B %Y à %H:%M:%S",
        "ISO 8601": "%Y-%m-%dT%H:%M:%S",
        "Timestamp": "%s"
    }

    print("\nFormats personnalisés :")
    for nom, format_str in formats.items():
        try:
            resultat = time.strftime(format_str, temps_struct)
            print(f"{nom:15} : {resultat}")
        except:
            print(f"{nom:15} : (non supporté sur ce système)")

afficher_formats_temps()
```

## Module datetime : Manipulation avancée des dates

Le module `datetime` offre des classes pour manipuler les dates et heures de manière plus intuitive.

### Classes principales

```python
from datetime import datetime, date, time, timedelta

# Classe date : juste la date
aujourd_hui = date.today()
print(f"Aujourd'hui : {aujourd_hui}")
print(f"Année : {aujourd_hui.year}")
print(f"Mois : {aujourd_hui.month}")
print(f"Jour : {aujourd_hui.day}")

# Classe time : juste l'heure
maintenant_heure = datetime.now().time()
print(f"Heure actuelle : {maintenant_heure}")
print(f"Heure : {maintenant_heure.hour}")
print(f"Minute : {maintenant_heure.minute}")
print(f"Seconde : {maintenant_heure.second}")

# Classe datetime : date + heure
maintenant = datetime.now()
print(f"Maintenant : {maintenant}")
print(f"Weekday : {maintenant.weekday()}")  # 0=lundi, 6=dimanche
print(f"Isoweekday : {maintenant.isoweekday()}")  # 1=lundi, 7=dimanche
```

### Création de dates et heures

```python
from datetime import datetime, date, time

def exemples_creation_datetime():
    """Exemples de création d'objets datetime."""

    print("📅 CRÉATION DE DATES ET HEURES")
    print("-" * 40)

    # Maintenant
    maintenant = datetime.now()
    print(f"Maintenant : {maintenant}")

    # Date spécifique
    noel_2024 = datetime(2024, 12, 25)
    print(f"Noël 2024 : {noel_2024}")

    # Date et heure spécifiques
    rendez_vous = datetime(2024, 6, 15, 14, 30, 0)
    print(f"Rendez-vous : {rendez_vous}")

    # Depuis une chaîne de caractères
    date_string = "2024-03-15 09:30:00"
    date_parsee = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print(f"Date parsée : {date_parsee}")

    # Depuis un timestamp
    timestamp = 1672531200  # 1er janvier 2023
    date_timestamp = datetime.fromtimestamp(timestamp)
    print(f"Depuis timestamp : {date_timestamp}")

    # Date aujourd'hui à minuit
    aujourd_hui_minuit = datetime.combine(date.today(), time.min)
    print(f"Aujourd'hui minuit : {aujourd_hui_minuit}")

exemples_creation_datetime()
```

### Calculs avec les dates (timedelta)

```python
from datetime import datetime, timedelta

def demo_calculs_dates():
    """Démonstration des calculs avec les dates."""

    print("🧮 CALCULS AVEC LES DATES")
    print("-" * 35)

    # Date de référence
    maintenant = datetime.now()
    print(f"Maintenant : {maintenant.strftime('%Y-%m-%d %H:%M:%S')}")

    # Ajouter du temps
    dans_une_semaine = maintenant + timedelta(weeks=1)
    dans_30_jours = maintenant + timedelta(days=30)
    dans_2_heures = maintenant + timedelta(hours=2)
    dans_45_minutes = maintenant + timedelta(minutes=45)

    print(f"Dans 1 semaine : {dans_une_semaine.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Dans 30 jours : {dans_30_jours.strftime('%Y-%m-%d')}")
    print(f"Dans 2 heures : {dans_2_heures.strftime('%H:%M:%S')}")
    print(f"Dans 45 minutes : {dans_45_minutes.strftime('%H:%M:%S')}")

    # Soustraire du temps
    il_y_a_une_semaine = maintenant - timedelta(weeks=1)
    il_y_a_un_mois = maintenant - timedelta(days=30)

    print(f"Il y a 1 semaine : {il_y_a_une_semaine.strftime('%Y-%m-%d')}")
    print(f"Il y a 1 mois : {il_y_a_un_mois.strftime('%Y-%m-%d')}")

    # Calculer la différence entre deux dates
    naissance = datetime(1990, 5, 15)
    age = maintenant - naissance

    print(f"\nCalcul d'âge :")
    print(f"Né le : {naissance.strftime('%d/%m/%Y')}")
    print(f"Âge en jours : {age.days}")
    print(f"Âge en années : {age.days // 365}")

    # Durées complexes
    duree_complexe = timedelta(
        days=7,
        hours=3,
        minutes=30,
        seconds=45,
        microseconds=123456
    )

    print(f"\nDurée complexe : {duree_complexe}")
    print(f"Total en secondes : {duree_complexe.total_seconds()}")

demo_calculs_dates()
```

### Formatage et parsing

```python
from datetime import datetime
import locale

def demo_formatage():
    """Démonstration du formatage des dates."""

    print("🎨 FORMATAGE DES DATES")
    print("-" * 30)

    maintenant = datetime.now()

    # Formats courants
    formats = [
        ("%Y-%m-%d", "Format ISO (YYYY-MM-DD)"),
        ("%d/%m/%Y", "Format français (DD/MM/YYYY)"),
        ("%m/%d/%Y", "Format américain (MM/DD/YYYY)"),
        ("%Y-%m-%d %H:%M:%S", "DateTime complet"),
        ("%d %B %Y", "Date avec nom du mois"),
        ("%A %d %B %Y", "Date complète avec jour"),
        ("%d %b %Y à %H:%M", "Format court français"),
        ("%c", "Format local par défaut"),
        ("%x", "Date locale"),
        ("%X", "Heure locale")
    ]

    for format_code, description in formats:
        try:
            resultat = maintenant.strftime(format_code)
            print(f"{description:25} : {resultat}")
        except:
            print(f"{description:25} : (erreur)")

    print("\n📖 PARSING DE CHAÎNES")
    print("-" * 25)

    # Exemples de parsing
    exemples_parsing = [
        ("2024-03-15", "%Y-%m-%d"),
        ("15/03/2024", "%d/%m/%Y"),
        ("March 15, 2024", "%B %d, %Y"),
        ("2024-03-15 14:30:00", "%Y-%m-%d %H:%M:%S"),
        ("15 mars 2024", "%d %B %Y")  # Nécessite locale français
    ]

    for date_str, format_str in exemples_parsing:
        try:
            date_parsee = datetime.strptime(date_str, format_str)
            print(f"'{date_str}' → {date_parsee}")
        except ValueError as e:
            print(f"'{date_str}' → Erreur: {e}")

demo_formatage()
```

### Gestion des fuseaux horaires

```python
from datetime import datetime, timezone, timedelta

def demo_fuseaux_horaires():
    """Démonstration de la gestion des fuseaux horaires."""

    print("🌍 FUSEAUX HORAIRES")
    print("-" * 25)

    # Heure UTC
    utc_maintenant = datetime.now(timezone.utc)
    print(f"UTC maintenant : {utc_maintenant}")

    # Heure locale (sans info de fuseau)
    local_maintenant = datetime.now()
    print(f"Local (naïf) : {local_maintenant}")

    # Créer des fuseaux horaires personnalisés
    paris_tz = timezone(timedelta(hours=1))  # UTC+1 (hiver)
    tokyo_tz = timezone(timedelta(hours=9))  # UTC+9
    new_york_tz = timezone(timedelta(hours=-5))  # UTC-5 (hiver)

    # Convertir l'heure UTC vers différents fuseaux
    paris_time = utc_maintenant.astimezone(paris_tz)
    tokyo_time = utc_maintenant.astimezone(tokyo_tz)
    ny_time = utc_maintenant.astimezone(new_york_tz)

    print(f"\nMême moment dans différents fuseaux :")
    print(f"Paris : {paris_time.strftime('%H:%M:%S')}")
    print(f"Tokyo : {tokyo_time.strftime('%H:%M:%S')}")
    print(f"New York : {ny_time.strftime('%H:%M:%S')}")

    # Créer une date avec fuseau horaire
    reunion = datetime(2024, 6, 15, 14, 0, 0, tzinfo=paris_tz)
    print(f"\nRéunion planifiée : {reunion}")
    print(f"En UTC : {reunion.astimezone(timezone.utc)}")

demo_fuseaux_horaires()
```

## Projet pratique : Gestionnaire de temps et productivité

Créons un outil complet pour gérer le temps et mesurer la productivité :

```python
from datetime import datetime, timedelta
import time
import json
import os

class GestionnaireTemps:
    """Gestionnaire de temps et suivi de productivité."""

    def __init__(self, fichier_donnees="temps_productivite.json"):
        self.fichier_donnees = fichier_donnees
        self.donnees = self.charger_donnees()
        self.session_actuelle = None

    def charger_donnees(self):
        """Charge les données depuis le fichier JSON."""
        if os.path.exists(self.fichier_donnees):
            try:
                with open(self.fichier_donnees, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                print("⚠️ Erreur de chargement, création de nouvelles données")

        return {
            'sessions': [],
            'objectifs': [],
            'statistiques': {}
        }

    def sauvegarder_donnees(self):
        """Sauvegarde les données dans le fichier JSON."""
        try:
            with open(self.fichier_donnees, 'w', encoding='utf-8') as f:
                json.dump(self.donnees, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ Erreur de sauvegarde : {e}")
            return False

    def demarrer_session(self, nom_tache, categorie="Général"):
        """Démarre une nouvelle session de travail."""
        if self.session_actuelle:
            print("⚠️ Une session est déjà en cours. Arrêtez-la d'abord.")
            return False

        self.session_actuelle = {
            'nom': nom_tache,
            'categorie': categorie,
            'debut': datetime.now().isoformat(),
            'fin': None,
            'duree_secondes': 0,
            'pauses': [],
            'notes': ""
        }

        print(f"🚀 Session démarrée : {nom_tache}")
        print(f"   Catégorie : {categorie}")
        print(f"   Début : {datetime.now().strftime('%H:%M:%S')}")
        return True

    def arreter_session(self, notes=""):
        """Arrête la session en cours."""
        if not self.session_actuelle:
            print("❌ Aucune session en cours")
            return False

        fin = datetime.now()
        debut = datetime.fromisoformat(self.session_actuelle['debut'])
        duree = fin - debut

        self.session_actuelle['fin'] = fin.isoformat()
        self.session_actuelle['duree_secondes'] = duree.total_seconds()
        self.session_actuelle['notes'] = notes

        # Ajouter aux données
        self.donnees['sessions'].append(self.session_actuelle.copy())

        print(f"⏹️ Session terminée : {self.session_actuelle['nom']}")
        print(f"   Durée : {self.formater_duree(duree.total_seconds())}")

        if notes:
            print(f"   Notes : {notes}")

        self.session_actuelle = None
        self.sauvegarder_donnees()
        return True

    def pause_session(self):
        """Met en pause la session actuelle."""
        if not self.session_actuelle:
            print("❌ Aucune session en cours")
            return False

        pause = {
            'debut': datetime.now().isoformat(),
            'fin': None
        }

        self.session_actuelle['pauses'].append(pause)
        print("⏸️ Session mise en pause")
        return True

    def reprendre_session(self):
        """Reprend la session après une pause."""
        if not self.session_actuelle or not self.session_actuelle['pauses']:
            print("❌ Aucune pause en cours")
            return False

        derniere_pause = self.session_actuelle['pauses'][-1]
        if derniere_pause['fin'] is not None:
            print("❌ Aucune pause en cours")
            return False

        derniere_pause['fin'] = datetime.now().isoformat()
        print("▶️ Session reprise")
        return True

    def formater_duree(self, secondes):
        """Formate une durée en secondes vers un format lisible."""
        heures = int(secondes // 3600)
        minutes = int((secondes % 3600) // 60)
        secondes = int(secondes % 60)

        if heures > 0:
            return f"{heures}h {minutes}m {secondes}s"
        elif minutes > 0:
            return f"{minutes}m {secondes}s"
        else:
            return f"{secondes}s"

    def afficher_session_actuelle(self):
        """Affiche l'état de la session actuelle."""
        if not self.session_actuelle:
            print("ℹ️ Aucune session en cours")
            return

        debut = datetime.fromisoformat(self.session_actuelle['debut'])
        maintenant = datetime.now()

        # Calculer le temps total moins les pauses
        temps_total = (maintenant - debut).total_seconds()
        temps_pause = 0

        for pause in self.session_actuelle['pauses']:
            debut_pause = datetime.fromisoformat(pause['debut'])
            if pause['fin']:
                fin_pause = datetime.fromisoformat(pause['fin'])
                temps_pause += (fin_pause - debut_pause).total_seconds()
            else:
                # Pause en cours
                temps_pause += (maintenant - debut_pause).total_seconds()

        temps_effectif = temps_total - temps_pause

        print(f"⏱️ SESSION ACTUELLE")
        print(f"   Tâche : {self.session_actuelle['nom']}")
        print(f"   Catégorie : {self.session_actuelle['categorie']}")
        print(f"   Début : {debut.strftime('%H:%M:%S')}")
        print(f"   Temps total : {self.formater_duree(temps_total)}")
        print(f"   Temps de pause : {self.formater_duree(temps_pause)}")
        print(f"   Temps effectif : {self.formater_duree(temps_effectif)}")

        # Vérifier si en pause
        if self.session_actuelle['pauses']:
            derniere_pause = self.session_actuelle['pauses'][-1]
            if derniere_pause['fin'] is None:
                print(f"   ⏸️ EN PAUSE depuis {datetime.fromisoformat(derniere_pause['debut']).strftime('%H:%M:%S')}")

    def statistiques_journalieres(self, date=None):
        """Affiche les statistiques pour une journée donnée."""
        if date is None:
            date = datetime.now().date()
        elif isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d").date()

        sessions_jour = []
        for session in self.donnees['sessions']:
            debut_session = datetime.fromisoformat(session['debut']).date()
            if debut_session == date:
                sessions_jour.append(session)

        if not sessions_jour:
            print(f"📊 Aucune session le {date.strftime('%d/%m/%Y')}")
            return

        print(f"📊 STATISTIQUES DU {date.strftime('%d/%m/%Y')}")
        print("-" * 40)

        # Temps total et par catégorie
        temps_total = 0
        temps_par_categorie = {}

        for session in sessions_jour:
            duree = session['duree_secondes']
            temps_total += duree

            categorie = session['categorie']
            temps_par_categorie[categorie] = temps_par_categorie.get(categorie, 0) + duree

        print(f"Temps total travaillé : {self.formater_duree(temps_total)}")
        print(f"Nombre de sessions : {len(sessions_jour)}")

        print("\nRépartition par catégorie :")
        for categorie, duree in sorted(temps_par_categorie.items()):
            pourcentage = (duree / temps_total) * 100 if temps_total > 0 else 0
            print(f"  {categorie} : {self.formater_duree(duree)} ({pourcentage:.1f}%)")

        print("\nDétail des sessions :")
        for session in sessions_jour:
            debut = datetime.fromisoformat(session['debut'])
            duree = session['duree_secondes']
            print(f"  {debut.strftime('%H:%M')} - {session['nom']} ({self.formater_duree(duree)})")

    def statistiques_hebdomadaires(self):
        """Affiche les statistiques de la semaine."""
        aujourd_hui = datetime.now().date()
        debut_semaine = aujourd_hui - timedelta(days=aujourd_hui.weekday())

        print(f"📊 STATISTIQUES DE LA SEMAINE")
        print(f"Du {debut_semaine.strftime('%d/%m')} au {(debut_semaine + timedelta(days=6)).strftime('%d/%m/%Y')}")
        print("-" * 50)

        temps_par_jour = {}
        jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

        for i in range(7):
            jour = debut_semaine + timedelta(days=i)
            temps_jour = 0

            for session in self.donnees['sessions']:
                debut_session = datetime.fromisoformat(session['debut']).date()
                if debut_session == jour:
                    temps_jour += session['duree_secondes']

            temps_par_jour[jour] = temps_jour

        temps_total_semaine = sum(temps_par_jour.values())
        moyenne_jour = temps_total_semaine / 7

        print(f"Temps total : {self.formater_duree(temps_total_semaine)}")
        print(f"Moyenne par jour : {self.formater_duree(moyenne_jour)}")

        print("\nDétail par jour :")
        for i, (jour, temps) in enumerate(temps_par_jour.items()):
            nom_jour = jours_semaine[i]
            if temps > 0:
                print(f"  {nom_jour:9} {jour.strftime('%d/%m')} : {self.formater_duree(temps)}")
            else:
                print(f"  {nom_jour:9} {jour.strftime('%d/%m')} : ---")

    def definir_objectif(self, nom, duree_minutes, categorie="Général"):
        """Définit un objectif de temps quotidien."""
        objectif = {
            'nom': nom,
            'duree_minutes': duree_minutes,
            'categorie': categorie,
            'cree_le': datetime.now().isoformat()
        }

        self.donnees['objectifs'].append(objectif)
        self.sauvegarder_donnees()

        print(f"🎯 Objectif défini : {nom}")
        print(f"   Durée : {duree_minutes} minutes par jour")
        print(f"   Catégorie : {categorie}")

    def verifier_objectifs(self, date=None):
        """Vérifie l'atteinte des objectifs pour une date donnée."""
        if date is None:
            date = datetime.now().date()
        elif isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d").date()

        if not self.donnees['objectifs']:
            print("🎯 Aucun objectif défini")
            return

        print(f"🎯 OBJECTIFS DU {date.strftime('%d/%m/%Y')}")
        print("-" * 35)

        # Calculer le temps par catégorie pour la journée
        temps_par_categorie = {}
        for session in self.donnees['sessions']:
            debut_session = datetime.fromisoformat(session['debut']).date()
            if debut_session == date:
                categorie = session['categorie']
                temps_par_categorie[categorie] = temps_par_categorie.get(categorie, 0) + session['duree_secondes']

        # Vérifier chaque objectif
        for objectif in self.donnees['objectifs']:
            categorie = objectif['categorie']
            objectif_secondes = objectif['duree_minutes'] * 60
            temps_realise = temps_par_categorie.get(categorie, 0)

            pourcentage = (temps_realise / objectif_secondes) * 100 if objectif_secondes > 0 else 0

            if pourcentage >= 100:
                statut = "✅"
            elif pourcentage >= 80:
                statut = "🟡"
            else:
                statut = "❌"

            print(f"{statut} {objectif['nom']}")
            print(f"   Objectif : {objectif['duree_minutes']} min")
            print(f"   Réalisé : {self.formater_duree(temps_realise)}")
            print(f"   Progression : {pourcentage:.1f}%")
            print()

# Interface utilisateur simple
def main():
    """Interface principale du gestionnaire de temps."""
    gestionnaire = GestionnaireTemps()

    print("⏰ GESTIONNAIRE DE TEMPS ET PRODUCTIVITÉ")
    print("=" * 45)

    while True:
        print("\n" + "="*40)
        print("MENU PRINCIPAL")
        print("="*40)
        print("1. Démarrer une session")
        print("2. Arrêter la session")
        print("3. Pause / Reprendre")
        print("4. État actuel")
        print("5. Statistiques du jour")
        print("6. Statistiques de la semaine")
        print("7. Définir un objectif")
        print("8. Vérifier les objectifs")
        print("9. Quitter")

        choix = input("\nVotre choix (1-9) : ").strip()

        if choix == '1':
            nom = input("Nom de la tâche : ").strip()
            if nom:
                categorie = input("Catégorie (ou Entrée pour 'Général') : ").strip()
                if not categorie:
                    categorie = "Général"
                gestionnaire.demarrer_session(nom, categorie)

        elif choix == '2':
            notes = input("Notes (optionnel) : ").strip()
            gestionnaire.arreter_session(notes)

        elif choix == '3':
            if gestionnaire.session_actuelle:
                if gestionnaire.session_actuelle['pauses'] and \
                   gestionnaire.session_actuelle['pauses'][-1]['fin'] is None:
                    gestionnaire.reprendre_session()
                else:
                    gestionnaire.pause_session()
            else:
                print("❌ Aucune session en cours")

        elif choix == '4':
            gestionnaire.afficher_session_actuelle()
        elif choix == '5':
            date_str = input("Date (YYYY-MM-DD, ou Entrée pour aujourd'hui) : ").strip()
            try:
                if date_str:
                    gestionnaire.statistiques_journalieres(date_str)
                else:
                    gestionnaire.statistiques_journalieres()
            except ValueError:
                print("❌ Format de date invalide. Utilisez YYYY-MM-DD")

        elif choix == '6':
            gestionnaire.statistiques_hebdomadaires()

        elif choix == '7':
            nom = input("Nom de l'objectif : ").strip()
            if nom:
                try:
                    duree = int(input("Durée en minutes par jour : "))
                    categorie = input("Catégorie (ou Entrée pour 'Général') : ").strip()
                    if not categorie:
                        categorie = "Général"
                    gestionnaire.definir_objectif(nom, duree, categorie)
                except ValueError:
                    print("❌ La durée doit être un nombre entier")

        elif choix == '8':
            date_str = input("Date (YYYY-MM-DD, ou Entrée pour aujourd'hui) : ").strip()
            try:
                if date_str:
                    gestionnaire.verifier_objectifs(date_str)
                else:
                    gestionnaire.verifier_objectifs()
            except ValueError:
                print("❌ Format de date invalide. Utilisez YYYY-MM-DD")

        elif choix == '9':
            if gestionnaire.session_actuelle:
                reponse = input("Une session est en cours. L'arrêter ? (o/N) : ").strip().lower()
                if reponse == 'o':
                    gestionnaire.arreter_session("Session interrompue")
                else:
                    continue
            print("👋 Au revoir !")
            break

        else:
            print("❌ Choix invalide")

        # Petite pause avant le prochain menu
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Application interrompue")
    except Exception as e:
        print(f"\n💥 Erreur inattendue : {e}")
```

## Exercices pratiques

### Exercice 1 : Calculateur d'âge avancé

Créez un calculateur d'âge qui donne des informations détaillées :

```python
from datetime import datetime, date, timedelta

class CalculateurAge:
    """Calculateur d'âge avancé avec informations détaillées."""

    def __init__(self):
        self.aujourd_hui = date.today()

    def calculer_age_detaille(self, date_naissance):
        """Calcule l'âge avec des détails complets."""
        if isinstance(date_naissance, str):
            try:
                date_naissance = datetime.strptime(date_naissance, "%Y-%m-%d").date()
            except ValueError:
                try:
                    date_naissance = datetime.strptime(date_naissance, "%d/%m/%Y").date()
                except ValueError:
                    raise ValueError("Format de date invalide. Utilisez YYYY-MM-DD ou DD/MM/YYYY")

        if date_naissance > self.aujourd_hui:
            raise ValueError("La date de naissance ne peut pas être dans le futur")

        # Calcul de l'âge en années
        age_annees = self.aujourd_hui.year - date_naissance.year

        # Vérifier si l'anniversaire a eu lieu cette année
        if (self.aujourd_hui.month, self.aujourd_hui.day) < (date_naissance.month, date_naissance.day):
            age_annees -= 1

        # Calcul du prochain anniversaire
        prochain_anniversaire = date(self.aujourd_hui.year, date_naissance.month, date_naissance.day)
        if prochain_anniversaire <= self.aujourd_hui:
            prochain_anniversaire = date(self.aujourd_hui.year + 1, date_naissance.month, date_naissance.day)

        jours_jusqu_anniversaire = (prochain_anniversaire - self.aujourd_hui).days

        # Calculs supplémentaires
        jours_total = (self.aujourd_hui - date_naissance).days
        semaines_total = jours_total // 7
        mois_total = age_annees * 12 + (self.aujourd_hui.month - date_naissance.month)

        # Ajustement pour les mois si le jour n'est pas encore passé
        if self.aujourd_hui.day < date_naissance.day:
            mois_total -= 1

        return {
            'date_naissance': date_naissance,
            'aujourd_hui': self.aujourd_hui,
            'age_annees': age_annees,
            'age_mois': mois_total,
            'age_semaines': semaines_total,
            'age_jours': jours_total,
            'age_heures': jours_total * 24,
            'age_minutes': jours_total * 24 * 60,
            'prochain_anniversaire': prochain_anniversaire,
            'jours_jusqu_anniversaire': jours_jusqu_anniversaire,
            'signe_zodiaque': self.obtenir_signe_zodiaque(date_naissance),
            'jour_semaine_naissance': self.obtenir_jour_semaine(date_naissance)
        }

    def obtenir_signe_zodiaque(self, date_naissance):
        """Détermine le signe du zodiaque."""
        signes = [
            ((3, 21), (4, 19), "Bélier"),
            ((4, 20), (5, 20), "Taureau"),
            ((5, 21), (6, 20), "Gémeaux"),
            ((6, 21), (7, 22), "Cancer"),
            ((7, 23), (8, 22), "Lion"),
            ((8, 23), (9, 22), "Vierge"),
            ((9, 23), (10, 22), "Balance"),
            ((10, 23), (11, 21), "Scorpion"),
            ((11, 22), (12, 21), "Sagittaire"),
            ((12, 22), (12, 31), "Capricorne"),
            ((1, 1), (1, 19), "Capricorne"),
            ((1, 20), (2, 18), "Verseau"),
            ((2, 19), (3, 20), "Poissons")
        ]

        mois, jour = date_naissance.month, date_naissance.day

        for debut, fin, signe in signes:
            if (mois == debut[0] and jour >= debut[1]) or (mois == fin[0] and jour <= fin[1]):
                return signe

        return "Inconnu"

    def obtenir_jour_semaine(self, date_obj):
        """Obtient le jour de la semaine en français."""
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        return jours[date_obj.weekday()]

    def afficher_age_detaille(self, date_naissance):
        """Affiche un rapport d'âge détaillé."""
        try:
            infos = self.calculer_age_detaille(date_naissance)

            print("\n" + "="*50)
            print("🎂 CALCULATEUR D'ÂGE DÉTAILLÉ")
            print("="*50)

            print(f"📅 Date de naissance : {infos['date_naissance'].strftime('%d/%m/%Y')}")
            print(f"📅 Aujourd'hui : {infos['aujourd_hui'].strftime('%d/%m/%Y')}")
            print(f"👶 Né(e) un {infos['jour_semaine_naissance']}")
            print(f"♈ Signe du zodiaque : {infos['signe_zodiaque']}")

            print(f"\n🎯 ÂGE ACTUEL")
            print(f"   {infos['age_annees']} ans")
            print(f"   {infos['age_mois']} mois")
            print(f"   {infos['age_semaines']} semaines")
            print(f"   {infos['age_jours']} jours")
            print(f"   {infos['age_heures']:,} heures")
            print(f"   {infos['age_minutes']:,} minutes")

            print(f"\n🎉 PROCHAIN ANNIVERSAIRE")
            print(f"   Date : {infos['prochain_anniversaire'].strftime('%d/%m/%Y')}")
            print(f"   Dans {infos['jours_jusqu_anniversaire']} jours")

            if infos['jours_jusqu_anniversaire'] == 0:
                print("   🎉 C'est aujourd'hui ! Joyeux anniversaire ! 🎉")
            elif infos['jours_jusqu_anniversaire'] <= 7:
                print("   🎂 Anniversaire dans moins d'une semaine !")
            elif infos['jours_jusqu_anniversaire'] <= 30:
                print("   🗓️ Anniversaire ce mois-ci !")

        except ValueError as e:
            print(f"❌ Erreur : {e}")

    def comparer_ages(self, date1, date2):
        """Compare deux âges."""
        try:
            age1 = self.calculer_age_detaille(date1)
            age2 = self.calculer_age_detaille(date2)

            diff_jours = abs(age1['age_jours'] - age2['age_jours'])
            diff_annees = diff_jours // 365
            diff_mois = (diff_jours % 365) // 30
            diff_jours_restants = (diff_jours % 365) % 30

            plus_age = "Personne 1" if age1['age_jours'] > age2['age_jours'] else "Personne 2"

            print(f"\n👥 COMPARAISON D'ÂGES")
            print(f"Personne 1 : {age1['age_annees']} ans ({age1['date_naissance'].strftime('%d/%m/%Y')})")
            print(f"Personne 2 : {age2['age_annees']} ans ({age2['date_naissance'].strftime('%d/%m/%Y')})")
            print(f"Plus âgé(e) : {plus_age}")
            print(f"Différence : {diff_annees} ans, {diff_mois} mois, {diff_jours_restants} jours")

        except ValueError as e:
            print(f"❌ Erreur : {e}")

# Interface du calculateur d'âge
def interface_calculateur_age():
    """Interface utilisateur pour le calculateur d'âge."""
    calc = CalculateurAge()

    while True:
        print("\n" + "="*40)
        print("🎂 CALCULATEUR D'ÂGE")
        print("="*40)
        print("1. Calculer mon âge")
        print("2. Comparer deux âges")
        print("3. Retour au menu principal")

        choix = input("\nVotre choix (1-3) : ").strip()

        if choix == '1':
            date_naissance = input("Date de naissance (YYYY-MM-DD ou DD/MM/YYYY) : ").strip()
            calc.afficher_age_detaille(date_naissance)

        elif choix == '2':
            date1 = input("Date de naissance 1 (YYYY-MM-DD ou DD/MM/YYYY) : ").strip()
            date2 = input("Date de naissance 2 (YYYY-MM-DD ou DD/MM/YYYY) : ").strip()
            calc.comparer_ages(date1, date2)

        elif choix == '3':
            break

        else:
            print("❌ Choix invalide")

# Test du calculateur
if __name__ == "__main__":
    interface_calculateur_age()
```

### Exercice 2 : Planificateur d'événements

Créez un planificateur qui gère les événements avec rappels :

```python
from datetime import datetime, timedelta
import json
import os

class PlanificateurEvenements:
    """Planificateur d'événements avec rappels."""

    def __init__(self, fichier="evenements.json"):
        self.fichier = fichier
        self.evenements = self.charger_evenements()

    def charger_evenements(self):
        """Charge les événements depuis le fichier."""
        if os.path.exists(self.fichier):
            try:
                with open(self.fichier, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def sauvegarder_evenements(self):
        """Sauvegarde les événements dans le fichier."""
        try:
            with open(self.fichier, 'w', encoding='utf-8') as f:
                json.dump(self.evenements, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ Erreur de sauvegarde : {e}")
            return False

    def ajouter_evenement(self, titre, date_heure, lieu="", description="", rappel_minutes=0):
        """Ajoute un nouvel événement."""
        try:
            if isinstance(date_heure, str):
                # Essayer différents formats
                formats = [
                    "%Y-%m-%d %H:%M",
                    "%d/%m/%Y %H:%M",
                    "%Y-%m-%d",
                    "%d/%m/%Y"
                ]

                date_heure_obj = None
                for fmt in formats:
                    try:
                        date_heure_obj = datetime.strptime(date_heure, fmt)
                        break
                    except ValueError:
                        continue

                if not date_heure_obj:
                    raise ValueError("Format de date invalide")

                date_heure = date_heure_obj

            evenement = {
                'id': len(self.evenements) + 1,
                'titre': titre,
                'date_heure': date_heure.isoformat(),
                'lieu': lieu,
                'description': description,
                'rappel_minutes': rappel_minutes,
                'cree_le': datetime.now().isoformat(),
                'termine': False
            }

            self.evenements.append(evenement)
            self.sauvegarder_evenements()

            print(f"✅ Événement ajouté : {titre}")
            print(f"   Date : {date_heure.strftime('%d/%m/%Y à %H:%M')}")
            if rappel_minutes > 0:
                print(f"   Rappel : {rappel_minutes} minutes avant")

            return True

        except ValueError as e:
            print(f"❌ Erreur : {e}")
            return False

    def lister_evenements(self, filtre="tous", limite=None):
        """Liste les événements selon un filtre."""
        maintenant = datetime.now()
        evenements_filtres = []

        for evenement in self.evenements:
            date_event = datetime.fromisoformat(evenement['date_heure'])

            if filtre == "tous":
                evenements_filtres.append(evenement)
            elif filtre == "futurs" and date_event > maintenant and not evenement['termine']:
                evenements_filtres.append(evenement)
            elif filtre == "passes" and (date_event <= maintenant or evenement['termine']):
                evenements_filtres.append(evenement)
            elif filtre == "aujourd_hui" and date_event.date() == maintenant.date():
                evenements_filtres.append(evenement)
            elif filtre == "cette_semaine":
                debut_semaine = maintenant - timedelta(days=maintenant.weekday())
                fin_semaine = debut_semaine + timedelta(days=6)
                if debut_semaine.date() <= date_event.date() <= fin_semaine.date():
                    evenements_filtres.append(evenement)

        # Trier par date
        evenements_filtres.sort(key=lambda x: x['date_heure'])

        if limite:
            evenements_filtres = evenements_filtres[:limite]

        if not evenements_filtres:
            print(f"📅 Aucun événement ({filtre})")
            return

        print(f"\n📅 ÉVÉNEMENTS ({filtre.upper()})")
        print("-" * 50)

        for evenement in evenements_filtres:
            date_event = datetime.fromisoformat(evenement['date_heure'])
            statut = "✅" if evenement['termine'] else ("🔴" if date_event < maintenant else "🟢")

            print(f"{statut} {evenement['titre']}")
            print(f"   📅 {date_event.strftime('%d/%m/%Y à %H:%M')}")

            if evenement['lieu']:
                print(f"   📍 {evenement['lieu']}")

            if evenement['description']:
                description = evenement['description'][:60] + "..." if len(evenement['description']) > 60 else evenement['description']
                print(f"   📝 {description}")

            # Temps restant ou écoulé
            if not evenement['termine']:
                if date_event > maintenant:
                    delta = date_event - maintenant
                    if delta.days > 0:
                        print(f"   ⏰ Dans {delta.days} jours et {delta.seconds//3600} heures")
                    elif delta.seconds > 3600:
                        print(f"   ⏰ Dans {delta.seconds//3600} heures et {(delta.seconds%3600)//60} minutes")
                    else:
                        print(f"   ⏰ Dans {delta.seconds//60} minutes")
                else:
                    delta = maintenant - date_event
                    print(f"   ⏰ En retard de {delta.days} jours" if delta.days > 0 else f"   ⏰ En retard de {delta.seconds//3600} heures")

            print()

    def verifier_rappels(self):
        """Vérifie et affiche les rappels."""
        maintenant = datetime.now()
        rappels = []

        for evenement in self.evenements:
            if evenement['termine'] or evenement['rappel_minutes'] == 0:
                continue

            date_event = datetime.fromisoformat(evenement['date_heure'])
            temps_rappel = date_event - timedelta(minutes=evenement['rappel_minutes'])

            # Vérifier si le rappel doit être déclenché (dans les 5 prochaines minutes)
            if temps_rappel <= maintenant <= temps_rappel + timedelta(minutes=5):
                rappels.append(evenement)

        if rappels:
            print("\n🔔 RAPPELS D'ÉVÉNEMENTS")
            print("-" * 30)

            for evenement in rappels:
                date_event = datetime.fromisoformat(evenement['date_heure'])
                temps_restant = date_event - maintenant

                print(f"🚨 {evenement['titre']}")
                print(f"   📅 {date_event.strftime('%d/%m/%Y à %H:%M')}")

                if temps_restant.total_seconds() > 0:
                    if temps_restant.seconds > 3600:
                        print(f"   ⏰ Commence dans {temps_restant.seconds//3600}h {(temps_restant.seconds%3600)//60}min")
                    else:
                        print(f"   ⏰ Commence dans {temps_restant.seconds//60} minutes")
                else:
                    print(f"   ⏰ A commencé !")

                if evenement['lieu']:
                    print(f"   📍 {evenement['lieu']}")
                print()

        return len(rappels)

    def marquer_termine(self, id_evenement):
        """Marque un événement comme terminé."""
        for evenement in self.evenements:
            if evenement['id'] == id_evenement:
                evenement['termine'] = True
                self.sauvegarder_evenements()
                print(f"✅ Événement '{evenement['titre']}' marqué comme terminé")
                return True

        print(f"❌ Événement avec l'ID {id_evenement} non trouvé")
        return False

    def supprimer_evenement(self, id_evenement):
        """Supprime un événement."""
        for i, evenement in enumerate(self.evenements):
            if evenement['id'] == id_evenement:
                titre = evenement['titre']
                del self.evenements[i]
                self.sauvegarder_evenements()
                print(f"🗑️ Événement '{titre}' supprimé")
                return True

        print(f"❌ Événement avec l'ID {id_evenement} non trouvé")
        return False

    def modifier_evenement(self, id_evenement):
        """Interface pour modifier un événement."""
        evenement = None
        for e in self.evenements:
            if e['id'] == id_evenement:
                evenement = e
                break

        if not evenement:
            print(f"❌ Événement avec l'ID {id_evenement} non trouvé")
            return False

        print(f"\n✏️ MODIFICATION DE L'ÉVÉNEMENT")
        print(f"Titre actuel : {evenement['titre']}")

        nouveau_titre = input("Nouveau titre (ou Entrée pour garder) : ").strip()
        if nouveau_titre:
            evenement['titre'] = nouveau_titre

        date_actuelle = datetime.fromisoformat(evenement['date_heure'])
        print(f"Date actuelle : {date_actuelle.strftime('%d/%m/%Y %H:%M')}")

        nouvelle_date = input("Nouvelle date (DD/MM/YYYY HH:MM, ou Entrée pour garder) : ").strip()
        if nouvelle_date:
            try:
                evenement['date_heure'] = datetime.strptime(nouvelle_date, "%d/%m/%Y %H:%M").isoformat()
            except ValueError:
                print("⚠️ Format de date invalide, conservé l'ancien")

        print(f"Lieu actuel : {evenement['lieu']}")
        nouveau_lieu = input("Nouveau lieu (ou Entrée pour garder) : ").strip()
        if nouveau_lieu:
            evenement['lieu'] = nouveau_lieu

        self.sauvegarder_evenements()
        print("✅ Événement modifié avec succès")
        return True

    def statistiques(self):
        """Affiche des statistiques sur les événements."""
        if not self.evenements:
            print("📊 Aucun événement pour les statistiques")
            return

        maintenant = datetime.now()
        futurs = sum(1 for e in self.evenements if datetime.fromisoformat(e['date_heure']) > maintenant and not e['termine'])
        passes = len(self.evenements) - futurs
        termines = sum(1 for e in self.evenements if e['termine'])

        # Événements par mois
        evenements_par_mois = {}
        for evenement in self.evenements:
            date_event = datetime.fromisoformat(evenement['date_heure'])
            mois = date_event.strftime('%Y-%m')
            evenements_par_mois[mois] = evenements_par_mois.get(mois, 0) + 1

        print("\n📊 STATISTIQUES DES ÉVÉNEMENTS")
        print("-" * 40)
        print(f"Total d'événements : {len(self.evenements)}")
        print(f"Événements futurs : {futurs}")
        print(f"Événements passés : {passes}")
        print(f"Événements terminés : {termines}")

        if evenements_par_mois:
            print(f"\nRépartition par mois :")
            for mois, count in sorted(evenements_par_mois.items()):
                date_mois = datetime.strptime(mois, '%Y-%m')
                nom_mois = date_mois.strftime('%B %Y')
                print(f"  {nom_mois} : {count} événements")

# Interface du planificateur
def interface_planificateur():
    """Interface utilisateur pour le planificateur."""
    planificateur = PlanificateurEvenements()

    while True:
        # Vérifier les rappels à chaque itération
        rappels = planificateur.verifier_rappels()

        print("\n" + "="*40)
        print("📅 PLANIFICATEUR D'ÉVÉNEMENTS")
        print("="*40)
        print("1. Ajouter un événement")
        print("2. Lister les événements")
        print("3. Événements d'aujourd'hui")
        print("4. Événements de la semaine")
        print("5. Modifier un événement")
        print("6. Marquer comme terminé")
        print("7. Supprimer un événement")
        print("8. Statistiques")
        print("9. Retour au menu principal")

        if rappels > 0:
            print(f"\n🔔 {rappels} rappel(s) actif(s)")

        choix = input("\nVotre choix (1-9) : ").strip()

        if choix == '1':
            titre = input("Titre de l'événement : ").strip()
            if titre:
                date_str = input("Date et heure (DD/MM/YYYY HH:MM) : ").strip()
                lieu = input("Lieu (optionnel) : ").strip()
                description = input("Description (optionnel) : ").strip()

                try:
                    rappel = int(input("Rappel en minutes avant (0 = pas de rappel) : ") or "0")
                    planificateur.ajouter_evenement(titre, date_str, lieu, description, rappel)
                except ValueError:
                    print("⚠️ Rappel invalide, défini à 0")
                    planificateur.ajouter_evenement(titre, date_str, lieu, description, 0)

        elif choix == '2':
            print("\nType d'événements :")
            print("1. Tous")
            print("2. Futurs")
            print("3. Passés")

            filtre_choix = input("Votre choix (1-3) : ").strip()
            filtre_map = {'1': 'tous', '2': 'futurs', '3': 'passes'}
            filtre = filtre_map.get(filtre_choix, 'tous')

            planificateur.lister_evenements(filtre)

        elif choix == '3':
            planificateur.lister_evenements("aujourd_hui")

        elif choix == '4':
            planificateur.lister_evenements("cette_semaine")

        elif choix == '5':
            try:
                id_event = int(input("ID de l'événement à modifier : "))
                planificateur.modifier_evenement(id_event)
            except ValueError:
                print("❌ ID invalide")

        elif choix == '6':
            try:
                id_event = int(input("ID de l'événement à marquer terminé : "))
                planificateur.marquer_termine(id_event)
            except ValueError:
                print("❌ ID invalide")

        elif choix == '7':
            try:
                id_event = int(input("ID de l'événement à supprimer : "))
                confirmation = input(f"Confirmer la suppression ? (o/N) : ").strip().lower()
                if confirmation == 'o':
                    planificateur.supprimer_evenement(id_event)
            except ValueError:
                print("❌ ID invalide")

        elif choix == '8':
            planificateur.statistiques()

        elif choix == '9':
            break

        else:
            print("❌ Choix invalide")

# Test du planificateur
if __name__ == "__main__":
    interface_planificateur()
```

### Exercice 3 : Analyseur de performance temporelle

Créez un outil pour analyser les performances de fonctions dans le temps :

```python
import time
from datetime import datetime, timedelta
import statistics
import json
from functools import wraps

class AnalyseurPerformance:
    """Analyseur de performance temporelle pour fonctions."""

    def __init__(self):
        self.mesures = {}
        self.historique = []

    def chronometrer(self, nom_fonction=None):
        """Décorateur pour chronométrer une fonction."""
        def decorateur(func):
            fonction_nom = nom_fonction or func.__name__

            @wraps(func)
            def wrapper(*args, **kwargs):
                debut = time.perf_counter()
                debut_processeur = time.process_time()

                try:
                    resultat = func(*args, **kwargs)
                    succes = True
                    erreur = None
                except Exception as e:
                    resultat = None
                    succes = False
                    erreur = str(e)

                fin = time.perf_counter()
                fin_processeur = time.process_time()

                duree_reelle = fin - debut
                duree_processeur = fin_processeur - debut_processeur

                # Enregistrer la mesure
                mesure = {
                    'fonction': fonction_nom,
                    'timestamp': datetime.now().isoformat(),
                    'duree_reelle': duree_reelle,
                    'duree_processeur': duree_processeur,
                    'succes': succes,
                    'erreur': erreur,
                    'args_count': len(args),
                    'kwargs_count': len(kwargs)
                }

                self.enregistrer_mesure(mesure)

                if not succes:
                    raise Exception(erreur)

                return resultat

            return wrapper
        return decorateur

    def enregistrer_mesure(self, mesure):
        """Enregistre une mesure de performance."""
        fonction = mesure['fonction']

        if fonction not in self.mesures:
            self.mesures[fonction] = []

        self.mesures[fonction].append(mesure)
        self.historique.append(mesure)

    def mesurer_fonction(self, func, *args, iterations=1, **kwargs):
        """Mesure manuellement une fonction sur plusieurs itérations."""
        resultats = []

        print(f"🔬 Mesure de {func.__name__} sur {iterations} itération(s)...")

        for i in range(iterations):
            debut = time.perf_counter()
            debut_processeur = time.process_time()

            try:
                resultat = func(*args, **kwargs)
                succes = True
                erreur = None
            except Exception as e:
                resultat = None
                succes = False
                erreur = str(e)

            fin = time.perf_counter()
            fin_processeur = time.process_time()

            duree_reelle = fin - debut
            duree_processeur = fin_processeur - debut_processeur

            mesure = {
                'iteration': i + 1,
                'duree_reelle': duree_reelle,
                'duree_processeur': duree_processeur,
                'succes': succes,
                'erreur': erreur
            }

            resultats.append(mesure)

            # Affichage en temps réel
            if iterations <= 10 or (i + 1) % (iterations // 10) == 0:
                print(f"  Itération {i+1}/{iterations}: {duree_reelle:.6f}s")

        return resultats

    def analyser_fonction(self, nom_fonction):
        """Analyse les performances d'une fonction."""
        if nom_fonction not in self.mesures:
            print(f"❌ Aucune mesure pour la fonction '{nom_fonction}'")
            return

        mesures = self.mesures[nom_fonction]
        durees = [m['duree_reelle'] for m in mesures if m['succes']]

        if not durees:
            print(f"❌ Aucune mesure réussie pour '{nom_fonction}'")
            return

        # Statistiques
        stats = {
            'count': len(mesures),
            'succes': len(durees),
            'echecs': len(mesures) - len(durees),
            'min': min(durees),
            'max': max(durees),
            'moyenne': statistics.mean(durees),
            'mediane': statistics.median(durees),
            'ecart_type': statistics.stdev(durees) if len(durees) > 1 else 0
        }

        print(f"\n📊 ANALYSE DE PERFORMANCE : {nom_fonction}")
        print("-" * 50)
        print(f"Nombre d'exécutions : {stats['count']}")
        print(f"Succès / Échecs : {stats['succes']} / {stats['echecs']}")
        print(f"Temps minimum : {stats['min']:.6f}s")
        print(f"Temps maximum : {stats['max']:.6f}s")
        print(f"Temps moyen : {stats['moyenne']:.6f}s")
        print(f"Temps médian : {stats['mediane']:.6f}s")
        print(f"Écart-type : {stats['ecart_type']:.6f}s")

        # Classification des performances
        if stats['moyenne'] < 0.001:
            performance = "🚀 Excellente"
        elif stats['moyenne'] < 0.01:
            performance = "✅ Bonne"
        elif stats['moyenne'] < 0.1:
            performance = "⚠️ Moyenne"
        else:
            performance = "🐌 Lente"

        print(f"Performance globale : {performance}")

        # Évolution temporelle
        if len(durees) > 5:
            print(f"\n📈 ÉVOLUTION TEMPORELLE")
            premieres = durees[:len(durees)//3]
            dernieres = durees[-len(durees)//3:]

            moyenne_debut = statistics.mean(premieres)
            moyenne_fin = statistics.mean(dernieres)

            if moyenne_fin < moyenne_debut * 0.9:
                tendance = "📈 Amélioration"
            elif moyenne_fin > moyenne_debut * 1.1:
                tendance = "📉 Dégradation"
            else:
                tendance = "➡️ Stable"

            print(f"Tendance : {tendance}")
            print(f"Début : {moyenne_debut:.6f}s → Fin : {moyenne_fin:.6f}s")

    def comparer_fonctions(self, noms_fonctions):
        """Compare les performances de plusieurs fonctions."""
        if len(noms_fonctions) < 2:
            print("❌ Il faut au moins 2 fonctions pour comparer")
            return

        print(f"\n🆚 COMPARAISON DE FONCTIONS")
        print("-" * 40)

        resultats = []

        for nom in noms_fonctions:
            if nom not in self.mesures:
                print(f"⚠️ Aucune mesure pour '{nom}', ignoré")
                continue

            durees = [m['duree_reelle'] for m in self.mesures[nom] if m['succes']]
            if durees:
                resultats.append({
                    'nom': nom,
                    'moyenne': statistics.mean(durees),
                    'count': len(durees)
                })

        if len(resultats) < 2:
            print("❌ Pas assez de fonctions avec des mesures valides")
            return

        # Trier par performance (plus rapide en premier)
        resultats.sort(key=lambda x: x['moyenne'])

        print("Classement (du plus rapide au plus lent) :")
        for i, resultat in enumerate(resultats, 1):
            if i == 1:
                badge = "🥇"
            elif i == 2:
                badge = "🥈"
            elif i == 3:
                badge = "🥉"
            else:
                badge = f"{i}."

            print(f"{badge} {resultat['nom']}: {resultat['moyenne']:.6f}s ({resultat['count']} mesures)")

        # Ratio par rapport au plus rapide
        plus_rapide = resultats[0]['moyenne']
        print(f"\nRatio par rapport au plus rapide :")
        for resultat in resultats[1:]:
            ratio = resultat['moyenne'] / plus_rapide
            print(f"  {resultat['nom']}: {ratio:.2f}x plus lent")

    def rapport_global(self):
        """Génère un rapport global de toutes les mesures."""
        if not self.historique:
            print("📊 Aucune mesure disponible")
            return

        print(f"\n📊 RAPPORT GLOBAL DE PERFORMANCE")
        print("=" * 50)

        # Statistiques générales
        total_mesures = len(self.historique)
        fonctions_uniques = len(self.mesures)
        mesures_reussies = sum(1 for m in self.historique if m['succes'])

        print(f"Total de mesures : {total_mesures}")
        print(f"Fonctions mesurées : {fonctions_uniques}")
        print(f"Taux de réussite : {mesures_reussies/total_mesures*100:.1f}%")

        # Top des fonctions les plus mesurées
        compteurs = {}
        for mesure in self.historique:
            fonction = mesure['fonction']
            compteurs[fonction] = compteurs.get(fonction, 0) + 1

        print(f"\nTop 5 des fonctions les plus mesurées :")
        for fonction, count in sorted(compteurs.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {fonction}: {count} mesures")

        # Évolution temporelle globale
        if len(self.historique) > 10:
            print(f"\n📈 ÉVOLUTION TEMPORELLE GLOBALE")

            # Grouper par heure
            mesures_par_heure = {}
            for mesure in self.historique:
                if mesure['succes']:
                    heure = datetime.fromisoformat(mesure['timestamp']).strftime('%Y-%m-%d %H:00')
                    if heure not in mesures_par_heure:
                        mesures_par_heure[heure] = []
                    mesures_par_heure[heure].append(mesure['duree_reelle'])

            if len(mesures_par_heure) > 1:
                print("Moyenne par heure (dernières 5 heures) :")
                heures_triees = sorted(mesures_par_heure.keys())[-5:]

                for heure in heures_triees:
                    durees = mesures_par_heure[heure]
                    moyenne = statistics.mean(durees)
                    heure_affichage = datetime.strptime(heure, '%Y-%m-%d %H:00').strftime('%H:00')
                    print(f"  {heure_affichage}: {moyenne:.6f}s ({len(durees)} mesures)")

    def sauvegarder_rapport(self, fichier="rapport_performance.json"):
        """Sauvegarde un rapport détaillé en JSON."""
        rapport = {
            'timestamp': datetime.now().isoformat(),
            'resume': {
                'total_mesures': len(self.historique),
                'fonctions_uniques': len(self.mesures),
                'mesures_reussies': sum(1 for m in self.historique if m['succes'])
            },
            'fonctions': {},
            'historique': self.historique
        }

        # Statistiques par fonction
        for nom_fonction, mesures in self.mesures.items():
            durees = [m['duree_reelle'] for m in mesures if m['succes']]

            if durees:
                rapport['fonctions'][nom_fonction] = {
                    'count': len(mesures),
                    'succes': len(durees),
                    'min': min(durees),
                    'max': max(durees),
                    'moyenne': statistics.mean(durees),
                    'mediane': statistics.median(durees),
                    'ecart_type': statistics.stdev(durees) if len(durees) > 1 else 0
                }

        try:
            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(rapport, f, indent=2, ensure_ascii=False)
            print(f"📄 Rapport sauvegardé : {fichier}")
            return True
        except Exception as e:
            print(f"❌ Erreur de sauvegarde : {e}")
            return False

# Exemples d'utilisation de l'analyseur
def exemples_analyseur():
    """Exemples d'utilisation de l'analyseur de performance."""

    analyseur = AnalyseurPerformance()

    # Exemple 1 : Utilisation du décorateur
    @analyseur.chronometrer("tri_bulle")
    def tri_bulle(liste):
        """Implémentation du tri à bulles (inefficace)."""
        n = len(liste)
        for i in range(n):
            for j in range(0, n - i - 1):
                if liste[j] > liste[j + 1]:
                    liste[j], liste[j + 1] = liste[j + 1], liste[j]
        return liste

    @analyseur.chronometrer("tri_python")
    def tri_python(liste):
        """Tri Python natif (efficace)."""
        return sorted(liste)

    @analyseur.chronometrer("calcul_fibonacci")
    def fibonacci_recursif(n):
        """Calcul récursif de Fibonacci (inefficace pour grands n)."""
        if n <= 1:
            return n
        return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

    @analyseur.chronometrer("calcul_fibonacci_iteratif")
    def fibonacci_iteratif(n):
        """Calcul itératif de Fibonacci (efficace)."""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    # Tests de performance
    print("🧪 TESTS DE PERFORMANCE")
    print("=" * 40)

    # Test des tris
    print("\n1. Test des algorithmes de tri")
    for taille in [100, 500, 1000]:
        import random
        liste_test = [random.randint(1, 1000) for _ in range(taille)]

        print(f"\nTaille de liste : {taille}")
        tri_bulle(liste_test.copy())
        tri_python(liste_test.copy())

    # Test de Fibonacci
    print("\n2. Test de Fibonacci")
    for n in [10, 15, 20]:
        print(f"\nFibonacci({n})")
        fibonacci_recursif(n)
        fibonacci_iteratif(n)

    # Exemple 2 : Mesure manuelle
    print("\n3. Mesure manuelle d'une fonction")

    def calcul_complexe(n):
        """Simulation d'un calcul complexe."""
        time.sleep(0.01)  # Simulation
        return sum(i**2 for i in range(n))

    resultats = analyseur.mesurer_fonction(calcul_complexe, 1000, iterations=5)

    # Analyses
    print("\n" + "="*50)
    print("📊 ANALYSES DES RÉSULTATS")
    print("="*50)

    analyseur.analyser_fonction("tri_bulle")
    analyseur.analyser_fonction("tri_python")

    print("\n")
    analyseur.comparer_fonctions(["tri_bulle", "tri_python"])

    print("\n")
    analyseur.comparer_fonctions(["calcul_fibonacci", "calcul_fibonacci_iteratif"])

    analyseur.rapport_global()
    analyseur.sauvegarder_rapport()

# Interface de l'analyseur
def interface_analyseur():
    """Interface utilisateur pour l'analyseur de performance."""
    analyseur = AnalyseurPerformance()

    while True:
        print("\n" + "="*40)
        print("🔬 ANALYSEUR DE PERFORMANCE")
        print("="*40)
        print("1. Lancer les exemples de test")
        print("2. Analyser une fonction")
        print("3. Comparer des fonctions")
        print("4. Rapport global")
        print("5. Sauvegarder le rapport")
        print("6. Retour au menu principal")

        choix = input("\nVotre choix (1-6) : ").strip()

        if choix == '1':
            exemples_analyseur()

        elif choix == '2':
            nom = input("Nom de la fonction à analyser : ").strip()
            if nom:
                analyseur.analyser_fonction(nom)

        elif choix == '3':
            noms = input("Noms des fonctions (séparés par des virgules) : ").strip()
            if noms:
                liste_noms = [n.strip() for n in noms.split(',')]
                analyseur.comparer_fonctions(liste_noms)

        elif choix == '4':
            analyseur.rapport_global()

        elif choix == '5':
            fichier = input("Nom du fichier (ou Entrée pour défaut) : ").strip()
            if not fichier:
                fichier = "rapport_performance.json"
            analyseur.sauvegarder_rapport(fichier)

        elif choix == '6':
            break

        else:
            print("❌ Choix invalide")

# Test de l'analyseur
if __name__ == "__main__":
    interface_analyseur()
```

## Récapitulatif des modules datetime et time

### Module `time` - Points clés

#### **Fonctions essentielles**
```python
import time

# Timestamp Unix
time.time()                    # Timestamp actuel
time.ctime(timestamp)          # Conversion en chaîne lisible

# Formatage
time.strftime(format, time_struct)    # Formatage personnalisé
time.strptime(string, format)         # Parsing de chaîne

# Pauses et mesures
time.sleep(seconds)            # Pause
time.perf_counter()           # Mesure haute précision
time.process_time()           # Temps processeur

# Structures temporelles
time.localtime(timestamp)      # Temps local
time.gmtime(timestamp)         # Temps UTC
```

#### **Cas d'usage du module time**
- Mesure de performance (`perf_counter()`)
- Pauses dans les scripts (`sleep()`)
- Timestamps simples (`time()`)
- Formatage basique (`strftime()`)

### Module `datetime` - Points clés

#### **Classes principales**
```python
from datetime import datetime, date, time, timedelta, timezone

# Création d'objets datetime
datetime.now()                 # Maintenant
datetime(2024, 6, 15, 14, 30) # Date/heure spécifique
date.today()                  # Date d'aujourd'hui
time(14, 30, 0)               # Heure spécifique

# Calculs avec timedelta
timedelta(days=7, hours=2)    # Durée
datetime.now() + timedelta(days=1)  # Ajouter du temps
```

#### **Formatage et parsing**
```python
# Formatage
dt.strftime("%Y-%m-%d %H:%M:%S")    # Vers chaîne
dt.isoformat()                       # Format ISO

# Parsing
datetime.strptime(string, format)    # Depuis chaîne
datetime.fromisoformat(iso_string)   # Depuis ISO
```

#### **Fuseaux horaires**
```python
from datetime import timezone, timedelta

# UTC
datetime.now(timezone.utc)

# Fuseau personnalisé
paris_tz = timezone(timedelta(hours=1))
datetime.now(paris_tz)

# Conversion
utc_time.astimezone(local_tz)
```

## Bonnes pratiques

### **1. Choix du bon module**
```python
# ✅ Pour mesurer des performances
import time
debut = time.perf_counter()
# ... code à mesurer ...
duree = time.perf_counter() - debut

# ✅ Pour manipuler des dates
from datetime import datetime, timedelta
rendez_vous = datetime(2024, 6, 15, 14, 30)
dans_une_semaine = rendez_vous + timedelta(weeks=1)
```

### **2. Gestion des fuseaux horaires**
```python
# ✅ Toujours être explicite avec les fuseaux
from datetime import datetime, timezone

# Stocker en UTC
maintenant_utc = datetime.now(timezone.utc)

# Afficher en local
maintenant_local = maintenant_utc.astimezone()
```

### **3. Formatage cohérent**
```python
# ✅ Utiliser des formats standards
ISO_FORMAT = "%Y-%m-%d %H:%M:%S"
FRENCH_FORMAT = "%d/%m/%Y à %H:%M"

# ✅ Créer des fonctions utilitaires
def format_datetime_french(dt):
    return dt.strftime("%d/%m/%Y à %H:%M")
```

### **4. Gestion des erreurs**
```python
from datetime import datetime

def parse_date_safe(date_string, formats):
    """Parse une date avec plusieurs formats possibles."""
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError(f"Format de date non reconnu: {date_string}")

# Utilisation
formats = ["%Y-%m-%d", "%d/%m/%Y", "%Y-%m-%d %H:%M:%S"]
date = parse_date_safe("2024-06-15", formats)
```

## Cas d'usage courants

### **Applications de gestion du temps**
- Planificateurs et calendriers
- Systèmes de rappels
- Suivi d'activités

### **Analyse de performance**
- Profiling de code
- Benchmarking
- Monitoring d'applications

### **Logging et audit**
- Horodatage des événements
- Analyse de logs temporels
- Traçabilité des actions

### **Applications métier**
- Calculs d'âge et d'ancienneté
- Gestion des délais et échéances
- Facturation basée sur le temps

## Projet final : Application de gestion du temps complète

Voici une architecture pour une application complète combinant tous les concepts :

```python
from datetime import datetime, timedelta, timezone
import time
import json
import os
from typing import Dict, List, Optional

class ApplicationTemps:
    """Application complète de gestion du temps."""

    def __init__(self, fichier_donnees="app_temps.json"):
        self.fichier_donnees = fichier_donnees
        self.gestionnaire_sessions = GestionnaireTemps()
        self.planificateur = PlanificateurEvenements()
        self.calculateur_age = CalculateurAge()
        self.analyseur_perf = AnalyseurPerformance()

    def menu_principal(self):
        """Menu principal de l'application."""
        while True:
            print("\n" + "="*50)
            print("⏰ APPLICATION DE GESTION DU TEMPS")
            print("="*50)
            print("1. 📊 Gestionnaire de productivité")
            print("2. 📅 Planificateur d'événements")
            print("3. 🎂 Calculateur d'âge")
            print("4. 🔬 Analyseur de performance")
            print("5. 📈 Tableau de bord global")
            print("6. ⚙️  Paramètres")
            print("7. 🚪 Quitter")

            choix = input("\nVotre choix (1-7) : ").strip()

            if choix == '1':
                self.gestionnaire_sessions.interface()
            elif choix == '2':
                self.planificateur.interface()
            elif choix == '3':
                self.calculateur_age.interface()
            elif choix == '4':
                self.analyseur_perf.interface()
            elif choix == '5':
                self.tableau_de_bord()
            elif choix == '6':
                self.parametres()
            elif choix == '7':
                print("👋 À bientôt !")
                break
            else:
                print("❌ Choix invalide")

    def tableau_de_bord(self):
        """Affiche un tableau de bord global."""
        print("\n" + "="*50)
        print("📈 TABLEAU DE BORD GLOBAL")
        print("="*50)

        # Statistiques du jour
        print("📊 AUJOURD'HUI")
        print("-" * 20)
        self.gestionnaire_sessions.statistiques_journalieres()

        print("\n📅 ÉVÉNEMENTS PROCHES")
        print("-" * 25)
        self.planificateur.lister_evenements("cette_semaine", limite=3)

        print("\n🔔 RAPPELS ACTIFS")
        print("-" * 20)
        rappels = self.planificateur.verifier_rappels()
        if rappels == 0:
            print("Aucun rappel actif")

if __name__ == "__main__":
    app = ApplicationTemps()
    app.menu_principal()
```

## Conclusion

Les modules `datetime` et `time` sont essentiels pour :

1. **Gestion précise du temps** - timestamps, durées, calculs temporels
2. **Manipulation des dates** - création, formatage, parsing, fuseaux horaires
3. **Mesure de performance** - chronométrage précis, benchmarking
4. **Applications temporelles** - planification, suivi, analyse

### Recommandations d'utilisation

- **Utilisez `datetime`** pour la manipulation de dates et heures
- **Utilisez `time`** pour les mesures de performance et les pauses
- **Gérez toujours les fuseaux horaires** explicitement
- **Formatez de manière cohérente** selon votre contexte
- **Gérez les erreurs** de parsing et de calcul

Ces modules vous permettent de créer des applications robustes qui gèrent le temps de manière professionnelle, depuis les simples horodatages jusqu'aux systèmes complexes de planification et d'analyse temporelle.

Dans la prochaine section, nous explorerons les modules mathématiques : `math`, `random`, et `statistics`.

⏭️
