# ============================================================================
#   Section 3.5 : Enregistrement automatique des classes
#   Description : Métaclasse RegistryMeta qui enregistre toutes les sous-classes
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

class RegistryMeta(type):
    """Métaclasse qui enregistre toutes les classes créées"""
    registry = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)

        # Enregistrer la classe (sauf la classe de base)
        if name != 'Plugin':
            mcs.registry[name] = cls

        return cls

class Plugin(metaclass=RegistryMeta):
    pass

class PDFPlugin(Plugin):
    pass

class ExcelPlugin(Plugin):
    pass

class ImagePlugin(Plugin):
    pass

# Voir toutes les classes enregistrées
print("Plugins disponibles :")
for nom, classe in RegistryMeta.registry.items():
    print(f"  - {nom}")
