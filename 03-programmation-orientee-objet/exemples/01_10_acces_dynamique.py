# ============================================================================
#   Section 3.1 : Accès dynamique aux attributs (getattr, setattr, hasattr)
#   Description : Lire/écrire/tester un attribut par son nom (chaîne) ;
#                 valeur par défaut, delattr, remplir un objet depuis un dict
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


p = Personne("Alice", 30)

# Accès classique et accès dynamique donnent le même résultat
print(p.nom)              # Alice
print(getattr(p, "nom"))  # Alice (mais ici le nom est une chaîne)

# Le nom de l'attribut peut venir d'une variable
champ = "age"
print(getattr(p, champ))  # 30

# getattr accepte une valeur par défaut si l'attribut n'existe pas
print(getattr(p, "ville", "Inconnue"))  # Inconnue

# Sans valeur par défaut, accéder à un attribut absent lève une erreur
try:
    print(p.ville)
except AttributeError as e:
    print(f"AttributeError : {e}")

# setattr crée ou modifie un attribut dynamiquement
setattr(p, "ville", "Paris")
print(p.ville)              # Paris

# hasattr teste l'existence ; delattr supprime
print(hasattr(p, "email"))  # False
delattr(p, "ville")
print(hasattr(p, "ville"))  # False

# Cas d'usage : remplir un objet à partir d'un dictionnaire {champ: valeur}
class Config:
    pass

donnees = {"hote": "localhost", "port": 8000, "debug": True}
config = Config()
for cle, valeur in donnees.items():
    setattr(config, cle, valeur)
print(f"{config.hote}:{config.port} (debug={config.debug})")  # localhost:8000 (debug=True)
