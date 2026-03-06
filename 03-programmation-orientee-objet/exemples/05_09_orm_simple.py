# ============================================================================
#   Section 3.5 : Métaclasse pour un ORM simple
#   Description : Field, ModelMeta et Model pour un mini-ORM avec extraction
#                 automatique des champs
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

class Field:
    """Représente un champ de base de données"""
    def __init__(self, field_type):
        self.field_type = field_type

class ModelMeta(type):
    """Métaclasse pour créer des modèles ORM"""

    def __new__(mcs, name, bases, attrs):
        # Extraire les champs
        fields = {}

        for attr_name, attr_value in list(attrs.items()):
            if isinstance(attr_value, Field):
                fields[attr_name] = attr_value
                attrs.pop(attr_name)

        # Stocker les champs dans la classe
        attrs['_fields'] = fields

        return super().__new__(mcs, name, bases, attrs)

class Model(metaclass=ModelMeta):
    """Classe de base pour les modèles"""

    def __init__(self, **kwargs):
        for field_name in self._fields:
            setattr(self, field_name, kwargs.get(field_name))

    def __repr__(self):
        field_values = ', '.join(
            f"{name}={getattr(self, name, None)}"
            for name in self._fields
        )
        return f"{self.__class__.__name__}({field_values})"

# Utiliser le "mini-ORM"
class Utilisateur(Model):
    nom = Field('varchar')
    age = Field('int')
    email = Field('varchar')

class Produit(Model):
    nom = Field('varchar')
    prix = Field('decimal')

# Créer des instances
user = Utilisateur(nom="Alice", age=30, email="alice@example.com")
print(user)  # Utilisateur(nom=Alice, age=30, email=alice@example.com)

produit = Produit(nom="Livre", prix=15.99)
print(produit)  # Produit(nom=Livre, prix=15.99)

# Voir les champs définis
print(f"Champs de Utilisateur : {list(Utilisateur._fields.keys())}")
print(f"Champs de Produit : {list(Produit._fields.keys())}")
