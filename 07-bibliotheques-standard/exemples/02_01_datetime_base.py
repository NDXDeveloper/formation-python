# ============================================================================
#   Section 7.2 : Les modules datetime et time
#   Description : Classe datetime - création, composants, formatage strftime,
#                 parsing strptime, calcul d'âge
#   Fichier source : 02-datetime-et-time.md
# ============================================================================

from datetime import datetime, timezone

# --- Date et heure actuelles ---
print("=== Date et heure actuelles ===")

maintenant = datetime.now()
print(f"Maintenant : {maintenant}")

maintenant_utc = datetime.now(timezone.utc)
print(f"UTC : {maintenant_utc}")

# --- Créer une date/heure spécifique ---
print("\n=== Créer des dates spécifiques ===")

noel = datetime(2025, 12, 25, 18, 0, 0)
print(f"Noël : {noel}")

anniversaire = datetime(1990, 5, 15)
print(f"Anniversaire : {anniversaire}")

# --- Accéder aux composants ---
print("\n=== Composants d'une date ===")

print(f"Année : {maintenant.year}")
print(f"Mois : {maintenant.month}")
print(f"Jour : {maintenant.day}")
print(f"Heure : {maintenant.hour}")
print(f"Minute : {maintenant.minute}")
print(f"Seconde : {maintenant.second}")
print(f"Jour de la semaine : {maintenant.weekday()} (0=lundi)")
print(f"ISO weekday : {maintenant.isoweekday()} (1=lundi)")

# --- Formatage avec strftime ---
print("\n=== Formatage (strftime) ===")

# Utiliser une date fixe pour des résultats prévisibles
date_fixe = datetime(2025, 10, 27, 14, 30, 45)

print(f"Par défaut         : {date_fixe}")
print(f"%d/%m/%Y           : {date_fixe.strftime('%d/%m/%Y')}")
print(f"%d-%m-%Y %H:%M:%S  : {date_fixe.strftime('%d-%m-%Y %H:%M:%S')}")
print(f"%Y-%m-%d           : {date_fixe.strftime('%Y-%m-%d')}")
print(f"%d/%m/%y            : {date_fixe.strftime('%d/%m/%y')}")
print(f"%H:%M              : {date_fixe.strftime('%H:%M')}")
print(f"%I:%M %p           : {date_fixe.strftime('%I:%M %p')}")

# --- Parsing avec strptime ---
print("\n=== Parsing (strptime) ===")

date_str = "27/10/2025 14:30:45"
date_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
print(f"'{date_str}' -> {date_obj}")

date1 = datetime.strptime("2025-10-27", "%Y-%m-%d")
date3 = datetime.strptime("10/27/25", "%m/%d/%y")

print(f"'2025-10-27' -> {date1}")
print(f"'10/27/25'   -> {date3}")

# --- Calculer l'âge ---
print("\n=== Calculer l'âge ===")

def calculer_age(date_naissance):
    """Calcule l'âge d'une personne à partir de sa date de naissance"""
    aujourd_hui = datetime.now()
    age = aujourd_hui.year - date_naissance.year
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1
    return age

date_naissance = datetime(1990, 5, 15)
age = calculer_age(date_naissance)
print(f"Né le 15/05/1990 -> Age : {age} ans")

date_naissance_str = "15/05/1990"
date_naissance = datetime.strptime(date_naissance_str, "%d/%m/%Y")
age = calculer_age(date_naissance)
print(f"Parsing '{date_naissance_str}' -> Age : {age} ans")

# --- Parsing sécurisé ---
print("\n=== Parsing sécurisé ===")

def parser_date_securise(date_str, format_str):
    """Parse une date avec gestion d'erreur"""
    try:
        return datetime.strptime(date_str, format_str)
    except ValueError as e:
        print(f"  Erreur de parsing : {e}")
        return None

date = parser_date_securise("2025-13-01", "%Y-%m-%d")  # Mois invalide
if date:
    print(f"  Date : {date}")
else:
    print("  Date invalide")

date = parser_date_securise("2025-06-15", "%Y-%m-%d")  # Valide
if date:
    print(f"  Date : {date}")
