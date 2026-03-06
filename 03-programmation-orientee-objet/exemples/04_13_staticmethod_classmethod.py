# ============================================================================
#   Section 3.4 : @staticmethod et @classmethod
#   Description : Méthode statique (Mathematiques), factory method (Personne),
#                 comparaison instance vs classe vs statique (Demo)
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

# --- @staticmethod ---
class Mathematiques:
    @staticmethod
    def additionner(a, b):
        """Méthode statique : pas besoin d'instance"""
        return a + b

    @staticmethod
    def multiplier(a, b):
        return a * b

# Appel sans créer d'instance
print(Mathematiques.additionner(5, 3))   # 8
print(Mathematiques.multiplier(4, 7))    # 28

# On peut aussi l'appeler depuis une instance
math = Mathematiques()
print(math.additionner(2, 3))  # 5

# --- @classmethod ---
print()

class Personne:
    nombre_personnes = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Personne.nombre_personnes += 1

    @classmethod
    def creer_depuis_naissance(cls, nom, annee_naissance):
        """Factory method : crée une personne à partir de l'année de naissance"""
        from datetime import datetime
        age = datetime.now().year - annee_naissance
        return cls(nom, age)

    @classmethod
    def nombre_total(cls):
        """Retourne le nombre total de personnes créées"""
        return cls.nombre_personnes

# Utilisation normale
p1 = Personne("Alice", 30)

# Utilisation avec classmethod
p2 = Personne.creer_depuis_naissance("Bob", 1990)

print(f"{p2.nom} a {p2.age} ans")
print(f"Nombre total de personnes : {Personne.nombre_total()}")

# --- Comparaison : Méthode d'Instance vs Statique vs Classe ---
print()

class Demo:
    attribut_classe = "Je suis un attribut de classe"

    def __init__(self, valeur):
        self.attribut_instance = valeur

    def methode_instance(self):
        """A accès à self et à la classe"""
        return f"Instance: {self.attribut_instance}, Classe: {self.attribut_classe}"

    @classmethod
    def methode_classe(cls):
        """A accès à la classe, pas à l'instance"""
        return f"Classe: {cls.attribut_classe}"

    @staticmethod
    def methode_statique():
        """N'a accès ni à self ni à cls"""
        return "Je suis une méthode statique"

# Créer une instance
obj = Demo("ma valeur")

# Méthode d'instance : besoin d'une instance
print(obj.methode_instance())

# Méthode de classe : peut être appelée sur la classe ou l'instance
print(Demo.methode_classe())
print(obj.methode_classe())

# Méthode statique : peut être appelée sur la classe ou l'instance
print(Demo.methode_statique())
print(obj.methode_statique())
