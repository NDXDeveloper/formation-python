# ============================================================================
#   Section 7.2 : Les modules datetime et time
#   Description : Classes date, time et timedelta - dates seules, heures
#                 seules, durées, opérations arithmétiques, comparaisons
#   Fichier source : 02-datetime-et-time.md
# ============================================================================

from datetime import date, time, datetime, timedelta

# --- Classe date (sans heure) ---
print("=== Classe date ===")

aujourd_hui = date.today()
print(f"Aujourd'hui : {aujourd_hui}")

noel = date(2025, 12, 25)
print(f"Noël : {noel}")

print(f"Année : {aujourd_hui.year}")
print(f"Mois : {aujourd_hui.month}")
print(f"Jour : {aujourd_hui.day}")
print(f"Formatage : {aujourd_hui.strftime('%d/%m/%Y')}")
print(f"Weekday : {aujourd_hui.weekday()} (0=lundi)")

# --- Classe time (sans date) ---
print("\n=== Classe time ===")

heure_reunion = time(14, 30, 0)
print(f"Heure réunion : {heure_reunion}")

heure_precise = time(14, 30, 45, 123456)
print(f"Heure précise : {heure_precise}")

print(f"Heure : {heure_reunion.hour}")
print(f"Minute : {heure_reunion.minute}")
print(f"Seconde : {heure_reunion.second}")
print(f"Format %H:%M : {heure_reunion.strftime('%H:%M')}")
print(f"Format 12h : {heure_reunion.strftime('%I:%M %p')}")

# --- Classe timedelta (durées) ---
print("\n=== Classe timedelta ===")

un_jour = timedelta(days=1)
une_semaine = timedelta(weeks=1)
deux_heures = timedelta(hours=2)
trente_minutes = timedelta(minutes=30)
dix_secondes = timedelta(seconds=10)

print(f"1 jour : {un_jour}")
print(f"1 semaine : {une_semaine}")
print(f"2 heures : {deux_heures}")
print(f"30 minutes : {trente_minutes}")

duree = timedelta(days=2, hours=3, minutes=30)
print(f"\n2j 3h 30min : {duree}")
print(f"Jours : {duree.days}")
print(f"Secondes totales : {duree.total_seconds()}")

# --- Opérations arithmétiques ---
print("\n=== Opérations arithmétiques ===")

# Utiliser une date fixe pour des résultats prévisibles
base = datetime(2025, 10, 27, 14, 30, 0)
print(f"Date de base : {base}")

demain = base + timedelta(days=1)
print(f"Demain : {demain}")

dans_une_semaine = base + timedelta(weeks=1)
print(f"Dans une semaine : {dans_une_semaine}")

dans_trois_heures = base + timedelta(hours=3)
print(f"Dans 3 heures : {dans_trois_heures}")

hier = base - timedelta(days=1)
print(f"Hier : {hier}")

il_y_a_un_mois = base - timedelta(days=30)
print(f"Il y a un mois : {il_y_a_un_mois}")

# --- Différence entre deux dates ---
print("\n=== Différence entre dates ===")

debut = datetime(2025, 1, 1)
fin = datetime(2025, 12, 31)
difference = fin - debut
print(f"Du 01/01 au 31/12/2025 : {difference}")
print(f"Nombre de jours : {difference.days}")
print(f"Nombre de secondes : {difference.total_seconds()}")

naissance = date(1990, 5, 15)
jours_vecus = aujourd_hui - naissance
print(f"\nJours vécus depuis le 15/05/1990 : {jours_vecus.days}")
print(f"Années approximatives : {jours_vecus.days / 365.25:.1f}")

# --- Temps restant ---
print("\n=== Temps restant ===")

def temps_restant(date_cible):
    """Calcule le temps restant jusqu'à une date cible"""
    maintenant = datetime.now()
    difference = date_cible - maintenant

    if difference.total_seconds() < 0:
        return "Cette date est deja passee!"

    jours = difference.days
    heures, reste = divmod(difference.seconds, 3600)
    minutes, secondes = divmod(reste, 60)
    return f"{jours} jours, {heures} heures, {minutes} minutes"

nouvel_an = datetime(2027, 1, 1, 0, 0, 0)
print(f"Temps restant jusqu'au Nouvel An 2027 : {temps_restant(nouvel_an)}")

passe = datetime(2020, 1, 1)
print(f"Date passée (01/01/2020) : {temps_restant(passe)}")

# --- Comparaison de dates ---
print("\n=== Comparaison de dates ===")

date1 = datetime(2025, 10, 27)
date2 = datetime(2025, 12, 25)

print(f"date1 = {date1.strftime('%d/%m/%Y')}")
print(f"date2 = {date2.strftime('%d/%m/%Y')}")
print(f"date1 < date2 : {date1 < date2}")
print(f"date1 > date2 : {date1 > date2}")
print(f"date1 == date2 : {date1 == date2}")
print(f"date1 != date2 : {date1 != date2}")

# Trouver min/max
dates = [
    datetime(2025, 1, 15),
    datetime(2025, 6, 20),
    datetime(2025, 3, 10)
]

date_la_plus_recente = max(dates)
date_la_plus_ancienne = min(dates)

print(f"\nDate la plus récente : {date_la_plus_recente.strftime('%d/%m/%Y')}")
print(f"Date la plus ancienne : {date_la_plus_ancienne.strftime('%d/%m/%Y')}")
