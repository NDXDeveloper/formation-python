# ============================================================================
#   Section 4.4 : shutil.copy vs shutil.copy2 (préservation des métadonnées)
#   Description : copy ne préserve pas les dates ; copy2 préserve la date de
#                 dernière modification (utile pour une sauvegarde fidèle)
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

import os
import shutil
import time
from pathlib import Path

# Créer un fichier source avec une date de modification ANCIENNE (~28h avant)
source = Path('source.txt')
source.write_text("contenu important\n", encoding='utf-8')
ancienne_date = time.time() - 100000
os.utime(source, (ancienne_date, ancienne_date))

# copy : copie le contenu et les permissions, mais PAS la date de modification
copie_simple = Path('copie_simple.txt')
shutil.copy(source, copie_simple)

# copy2 : copie le contenu ET préserve la date de modification
copie_fidele = Path('copie_fidele.txt')
shutil.copy2(source, copie_fidele)

date_source = round(source.stat().st_mtime)
print("copy  préserve la date ?", round(copie_simple.stat().st_mtime) == date_source)   # False
print("copy2 préserve la date ?", round(copie_fidele.stat().st_mtime) == date_source)   # True

# Nettoyage
source.unlink()
copie_simple.unlink()
copie_fidele.unlink()
