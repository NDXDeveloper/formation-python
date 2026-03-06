# ============================================================================
#   Section 4.1 : Gestion des erreurs avec les fichiers
#   Description : try/except pour FileNotFoundError, PermissionError
#   Fichier source : 01-lecture-ecriture-fichiers.md
# ============================================================================

try:
    with open('fichier_inexistant.txt', 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
except FileNotFoundError:
    print("Erreur : Le fichier n'existe pas !")
except PermissionError:
    print("Erreur : Pas les permissions pour accéder au fichier")
except Exception as e:
    print(f"Erreur inattendue : {e}")
