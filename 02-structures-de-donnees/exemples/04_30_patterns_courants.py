# ============================================================================
#   Section 2.4 : Regex - Patterns courants
#   Description : Collection de patterns regex utiles : email, URL, téléphone,
#                 date, code postal, IPv4, heure, carte bancaire, couleur hex
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# Email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# URL
url_pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'

# Numéro de téléphone français
tel_fr_pattern = r'^(?:0|\+33)[1-9](?:[0-9]{2}){4}$'

# Date (format DD/MM/YYYY)
date_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'

# Code postal français
code_postal_pattern = r'^\d{5}$'

# IPv4
ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

# Heure (format HH:MM)
heure_pattern = r'^([01][0-9]|2[0-3]):[0-5][0-9]$'

# Numéro de carte bancaire (espaces optionnels)
carte_pattern = r'^\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}$'

# Couleur hexadécimale
hex_color_pattern = r'^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'

# --- Tests de démonstration ---
tests = {
    "Email": (email_pattern, ["test@example.com", "invalide"]),
    "URL": (url_pattern, ["https://example.com", "pas-une-url"]),
    "Tél FR": (tel_fr_pattern, ["0612345678", "123"]),
    "Date": (date_pattern, ["27/10/2024", "32/13/2024"]),
    "Code postal": (code_postal_pattern, ["75001", "7500"]),
    "IPv4": (ipv4_pattern, ["192.168.1.1", "999.999.999.999"]),
    "Heure": (heure_pattern, ["14:30", "25:00"]),
    "Couleur hex": (hex_color_pattern, ["#FF5733", "ZZZZZZ"]),
}

for nom, (pattern, exemples) in tests.items():
    resultats = [f"{e}: {'OK' if re.match(pattern, e) else 'KO'}" for e in exemples]
    print(f"{nom}: {', '.join(resultats)}")
