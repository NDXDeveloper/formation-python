# ============================================================================
#   Section 4.3 : Pickle - Gestion des erreurs et sécurité
#   Description : Fonctions de sauvegarde/chargement sécurisées,
#                 protocoles, versioning
#   Fichier source : 03-serialisation-pickle.md
# ============================================================================

import pickle
import os

# --- Fonctions sécurisées ---
print("=== Sauvegarde/chargement sécurisés ===")

def sauvegarder_securise(objet, fichier):
    """Sauvegarde avec gestion d'erreurs"""
    try:
        with open(fichier, 'wb') as f:
            pickle.dump(objet, f)
        print(f"Sauvegarde réussie : {fichier}")
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")
        return False

def charger_securise(fichier, defaut=None):
    """Chargement avec gestion d'erreurs"""
    try:
        with open(fichier, 'rb') as f:
            objet = pickle.load(f)
        print(f"Chargement réussi : {fichier}")
        return objet
    except FileNotFoundError:
        print(f"Fichier non trouvé : {fichier}")
        return defaut
    except pickle.UnpicklingError:
        print(f"Fichier pickle corrompu : {fichier}")
        return defaut
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return defaut

donnees = {'clé': 'valeur'}
sauvegarder_securise(donnees, 'donnees.pkl')

resultat = charger_securise('donnees.pkl', defaut={})
print(f"Données : {resultat}")

# Fichier inexistant
resultat = charger_securise('inexistant.pkl', defaut={})
print(f"Données par défaut : {resultat}")

# --- Protocoles ---
print("\n=== Protocoles pickle ===")

donnees = {'nom': 'Python', 'version': 3.12}

# Protocole 0 : ASCII
with open('proto0.pkl', 'wb') as f:
    pickle.dump(donnees, f, protocol=0)

# Protocole le plus récent
with open('proto_recent.pkl', 'wb') as f:
    pickle.dump(donnees, f, protocol=pickle.HIGHEST_PROTOCOL)

print(f"Protocole le plus récent : {pickle.HIGHEST_PROTOCOL}")

# Comparer les tailles
taille_0 = os.path.getsize('proto0.pkl')
taille_recent = os.path.getsize('proto_recent.pkl')
print(f"Taille protocole 0 : {taille_0} octets")
print(f"Taille protocole {pickle.HIGHEST_PROTOCOL} : {taille_recent} octets")

# --- Versioning ---
print("\n=== Versioning ===")

donnees = {
    'version': 1,
    'utilisateur': 'Alice',
    'score': 100
}

with open('save.pkl', 'wb') as f:
    pickle.dump(donnees, f)

with open('save.pkl', 'rb') as f:
    donnees = pickle.load(f)
    if donnees.get('version') != 1:
        print("Version incompatible !")
    else:
        print(f"Version {donnees['version']} - {donnees['utilisateur']} : {donnees['score']} pts")

# Nettoyage
for f in ['donnees.pkl', 'proto0.pkl', 'proto_recent.pkl', 'save.pkl']:
    os.remove(f)
