# ============================================================================
#   Section 2.4 : Regex - Parsing de logs
#   Description : Extraire les entrées d'erreur d'un fichier de log
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

log = """
2024-10-27 14:30:15 ERROR Connection timeout
2024-10-27 14:31:22 INFO User login successful
2024-10-27 14:32:05 WARNING Low memory
2024-10-27 14:33:18 ERROR Database connection failed
"""

# Extraire les entrées d'erreur
pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR) (.+)'

erreurs = re.findall(pattern, log)

print("Erreurs trouvées :")
for date, niveau, message in erreurs:
    print(f"  [{date}] {message}")
