# ============================================================================
#   Section 3.1 : Lire vs écrire un attribut de classe via une instance
#   Description : affecter un attribut de classe via l'instance crée un attribut
#                 d'instance qui MASQUE celui de la classe (shadowing)
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Chien:
    espece = "Canis familiaris"   # attribut de classe


chien1 = Chien()
chien2 = Chien()

# Affecter via l'instance crée un attribut d'INSTANCE (la classe n'est pas touchée)
chien1.espece = "Loup"
print(chien1.espece)   # Loup              (attribut d'instance, masque la classe)
print(chien2.espece)   # Canis familiaris  (inchangé)
print(Chien.espece)    # Canis familiaris  (la classe est intacte)

# Pour modifier la valeur partagée, il faut passer par la CLASSE :
Chien.espece = "Canis lupus"
print(chien2.espece)   # Canis lupus  (chien2 voit la classe)
print(chien1.espece)   # Loup         (chien1 garde son attribut d'instance)

# instance.__dict__ ne contient QUE les attributs d'instance
print(chien1.__dict__)   # {'espece': 'Loup'}
print(chien2.__dict__)   # {}
