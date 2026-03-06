# ============================================================================
#   Section 2.4 : Regex - Extraction d'URLs
#   Description : Pattern pour extraire des URLs http/https d'un texte
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

texte = """
Visitez notre site : https://example.com
Documentation : http://docs.example.com/guide
Ou contactez-nous via email
"""

# Pattern pour URLs
pattern = r'https?://[^\s]+'
urls = re.findall(pattern, texte)

for url in urls:
    print(f"URL trouvée : {url}")
# URL trouvée : https://example.com
# URL trouvée : http://docs.example.com/guide
