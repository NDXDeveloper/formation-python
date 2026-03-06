# ============================================================================
#   Section 3.5 : Métaclasse personnalisée
#   Description : Métaclasse de base, avec timestamp, et avec validation
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# --- Métaclasse de base ---
class MaMetaclasse(type):
    def __new__(mcs, name, bases, attrs):
        print(f"Création de la classe {name}")
        return super().__new__(mcs, name, bases, attrs)

class MaClasse(metaclass=MaMetaclasse):
    pass

# Affiche : Création de la classe MaClasse

# --- Métaclasse qui ajoute un timestamp ---
print()

from datetime import datetime

class TimestampMeta(type):
    """Métaclasse qui ajoute un timestamp à chaque classe"""

    def __new__(mcs, name, bases, attrs):
        attrs['creation_time'] = datetime.now()
        return super().__new__(mcs, name, bases, attrs)

class Produit(metaclass=TimestampMeta):
    def __init__(self, nom):
        self.nom = nom

class Service(metaclass=TimestampMeta):
    def __init__(self, nom):
        self.nom = nom

# Chaque classe a maintenant un timestamp
print(f"Produit créé le : {Produit.creation_time}")
print(f"Service créé le : {Service.creation_time}")

# --- Métaclasse de validation ---
print()

class ValidationMeta(type):
    """Vérifie que certaines méthodes sont implémentées"""

    def __new__(mcs, name, bases, attrs):
        # Ignorer la classe de base
        if name != 'Animal':
            if 'faire_bruit' not in attrs:
                raise TypeError(f"La classe {name} doit implémenter 'faire_bruit'")

        return super().__new__(mcs, name, bases, attrs)

class Animal(metaclass=ValidationMeta):
    pass

class Chien(Animal):
    def faire_bruit(self):
        return "Wouf !"

rex = Chien()
print(rex.faire_bruit())  # Wouf !

# Ceci échouerait :
try:
    # Créer une classe sans faire_bruit
    Chat = ValidationMeta('Chat', (Animal,), {})
except TypeError as e:
    print(f"Erreur : {e}")
