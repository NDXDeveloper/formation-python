# ============================================================================
#   Section 3.5 : Attributs de classe calculés dynamiquement
#   Description : __getattribute__ dans une métaclasse pour des valeurs
#                 générées dynamiquement
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

class DynamicMeta(type):
    """Métaclasse qui calcule dynamiquement certains attributs"""

    def __getattribute__(cls, name):
        if name == 'dynamic_value':
            from datetime import datetime
            return f"Valeur générée à {datetime.now()}"

        return super().__getattribute__(name)

class MaClasse(metaclass=DynamicMeta):
    static_value = "valeur statique"

# Chaque accès génère une nouvelle valeur
print(MaClasse.dynamic_value)
print(MaClasse.dynamic_value)  # Temps différent

print(MaClasse.static_value)   # valeur statique
