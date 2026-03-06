# ============================================================================
#   Section 3.5 : __init_subclass__ - Alternative aux métaclasses
#   Description : Enregistrement automatique de plugins et validation de
#                 méthodes requises avec __init_subclass__
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# --- Enregistrement automatique ---
class Plugin:
    """Classe de base pour les plugins"""
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)
        print(f"Plugin enregistré : {cls.__name__}")

class PDFPlugin(Plugin):
    pass

class ExcelPlugin(Plugin):
    pass

class ImagePlugin(Plugin):
    pass

print(f"\nNombre de plugins : {len(Plugin.plugins)}")
for plugin in Plugin.plugins:
    print(f"  - {plugin.__name__}")

# --- Validation avec __init_subclass__ ---
print()

class RequiredMethods:
    """Classe qui impose des méthodes obligatoires"""
    required_methods = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Ne pas vérifier les classes qui redéfinissent required_methods
        if 'required_methods' in cls.__dict__:
            return

        # Vérifier que toutes les méthodes requises sont présentes
        for method in cls.required_methods:
            if not hasattr(cls, method):
                raise TypeError(
                    f"La classe {cls.__name__} doit implémenter la méthode '{method}'"
                )

class DataProcessor(RequiredMethods):
    required_methods = ['process', 'validate']

class CSVProcessor(DataProcessor):
    def process(self, data):
        return f"Processing CSV: {data}"

    def validate(self, data):
        return True

# Ceci fonctionne
processor = CSVProcessor()
print(processor.process("data.csv"))

# Ceci échouerait :
try:
    class BadProcessor(DataProcessor):
        def process(self, data):
            return data
        # Manque validate()
except TypeError as e:
    print(f"Erreur : {e}")
