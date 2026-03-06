# ============================================================================
#   Section 3.5 : Conversion automatique des noms d'attributs
#   Description : Métaclasse UpperAttrMeta qui convertit les noms en majuscules
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

class UpperAttrMeta(type):
    """Métaclasse qui convertit tous les noms d'attributs en majuscules"""

    def __new__(mcs, name, bases, attrs):
        uppercase_attrs = {}

        for attr_name, attr_value in attrs.items():
            # Ne pas modifier les méthodes spéciales (__init__, etc.)
            if not attr_name.startswith('__'):
                uppercase_attrs[attr_name.upper()] = attr_value
            else:
                uppercase_attrs[attr_name] = attr_value

        return super().__new__(mcs, name, bases, uppercase_attrs)

class MaClasse(metaclass=UpperAttrMeta):
    attribut = "valeur"
    autre_attribut = 42

    def methode(self):
        return "Bonjour"

# Les attributs sont maintenant en majuscules
print(MaClasse.ATTRIBUT)        # valeur
print(MaClasse.AUTRE_ATTRIBUT)  # 42
obj = MaClasse()
print(obj.METHODE())            # Bonjour
