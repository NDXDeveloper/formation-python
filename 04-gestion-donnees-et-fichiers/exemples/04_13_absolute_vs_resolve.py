# ============================================================================
#   Section 4.4 : absolute() vs resolve() - normalisation des chemins
#   Description : absolute() préfixe le répertoire courant mais garde les '..' ;
#                 resolve() normalise (supprime les '..') et suit les liens
#   Fichier source : 04-gestion-chemins-pathlib.md
# ============================================================================

from pathlib import Path

chemin = Path('dossier/sousdossier/../fichier.txt')

absolu = chemin.absolute()    # préfixe le répertoire courant, sans simplifier
resolu = chemin.resolve()     # normalise : supprime les '..' (et suit les liens)

print("absolute() garde le '..' ?", '..' in absolu.parts)    # True
print("resolve()  garde le '..' ?", '..' in resolu.parts)    # False
print("Même nom de fichier final ?", absolu.name == resolu.name == 'fichier.txt')  # True
