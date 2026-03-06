# ============================================================================
#   Section 4.3 : Pickle - Sérialisation en bytes
#   Description : pickle.dumps() et pickle.loads() pour sérialiser sans fichier
#   Fichier source : 03-serialisation-pickle.md
# ============================================================================

import pickle

# Objet à sérialiser
donnees = {'nom': 'Python', 'version': 3.12, 'tags': ['simple', 'puissant']}

# Sérialiser en bytes
donnees_bytes = pickle.dumps(donnees)

print("Type :", type(donnees_bytes))  # <class 'bytes'>
print("Taille :", len(donnees_bytes), "octets")

# Désérialiser
donnees_restaurees = pickle.loads(donnees_bytes)
print("Données restaurées :", donnees_restaurees)
