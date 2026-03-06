# ============================================================================
#   Section 3.5 : Valeurs par défaut et field()
#   Description : default_factory pour mutables, champs exclus de repr/compare
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

from dataclasses import dataclass, field

@dataclass
class Configuration:
    nom: str
    debug: bool = False
    # Utiliser field(default_factory=...) pour les mutables
    options: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)

    # Champ exclu de __repr__ et __eq__
    _cache: dict = field(default_factory=dict, repr=False, compare=False)

config = Configuration("prod", options=["verbose"])
print(config)  # Configuration(nom='prod', debug=False, options=['verbose'], metadata={})
