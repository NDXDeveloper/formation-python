# ============================================================================
#   Section 7.2 : Les modules datetime et time
#   Description : Fuseaux horaires avec zoneinfo et timezone,
#                 conversion entre fuseaux, UTC
#   Fichier source : 02-datetime-et-time.md
# ============================================================================

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# --- Fuseaux horaires avec zoneinfo ---
print("=== Fuseaux horaires ===")

maintenant_paris = datetime.now(ZoneInfo("Europe/Paris"))
maintenant_tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))
maintenant_ny = datetime.now(ZoneInfo("America/New_York"))

print(f"Paris    : {maintenant_paris.strftime('%Y-%m-%d %H:%M:%S %Z')}")
print(f"Tokyo    : {maintenant_tokyo.strftime('%Y-%m-%d %H:%M:%S %Z')}")
print(f"New York : {maintenant_ny.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# --- Conversion entre fuseaux ---
print("\n=== Conversion entre fuseaux ===")

date_paris = datetime(2025, 10, 27, 14, 30, tzinfo=ZoneInfo("Europe/Paris"))
date_tokyo = date_paris.astimezone(ZoneInfo("Asia/Tokyo"))
date_ny = date_paris.astimezone(ZoneInfo("America/New_York"))

print(f"14h30 à Paris :")
print(f"  -> Tokyo    : {date_tokyo.strftime('%H:%M %Z')}")
print(f"  -> New York : {date_ny.strftime('%H:%M %Z')}")

# --- UTC ---
print("\n=== UTC ===")

maintenant_utc = datetime.now(timezone.utc)
print(f"UTC actuel : {maintenant_utc.strftime('%Y-%m-%d %H:%M:%S %Z')}")

date_utc = datetime(2025, 10, 27, 12, 0, 0, tzinfo=timezone.utc)
print(f"Date UTC : {date_utc}")

# Conversion UTC -> local
date_locale = date_utc.astimezone()
print(f"UTC -> Local : {date_locale.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# --- Bonnes pratiques ---
print("\n=== Bonnes pratiques ===")

# Stocker en UTC
date_stockage = datetime.now(timezone.utc)
print(f"Stockage (UTC) : {date_stockage.strftime('%Y-%m-%d %H:%M:%S')}")

# Afficher en local
date_affichage = date_stockage.astimezone(ZoneInfo("Europe/Paris"))
print(f"Affichage (Paris) : {date_affichage.strftime('%d/%m/%Y à %H:%M')}")

# Format ISO pour stockage
date_iso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Format ISO : {date_iso}")

# Format localisé pour affichage
date_aff = datetime.now().strftime("%d/%m/%Y à %H:%M")
print(f"Format localisé : {date_aff}")
