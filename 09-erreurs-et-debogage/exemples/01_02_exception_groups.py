# ============================================================================
#   Section 9.1 : Hierarchie des exceptions
#   Description : Groupes d'exceptions - regrouper plusieurs erreurs dans un
#                 ExceptionGroup et les traiter (Python 3.11+)
#   Fichier source : 01-hierarchie-des-exceptions.md
# ============================================================================

import sys

def valider_formulaire():
    """Leve plusieurs erreurs en meme temps, regroupees dans un ExceptionGroup."""
    raise ExceptionGroup("Le formulaire contient des erreurs", [  # noqa: F821 (builtin Python 3.11+)
        ValueError("L'age doit etre positif"),
        TypeError("Le nom doit etre une chaine"),
        ValueError("L'email est invalide"),
    ])

# ExceptionGroup (Python 3.11+) regroupe plusieurs exceptions levees ensemble.
# La syntaxe moderne pour les traiter est 'except*' (voir le .md) :
#
#     try:
#         valider_formulaire()
#     except* ValueError as eg:
#         ...
#     except* TypeError as eg:
#         ...
#
# Mais 'except*' est une SYNTAXE de Python 3.11+ : un fichier qui l'utilise ne
# se *parse* meme pas sur Python 3.10. Pour rester executable partout, on montre
# ici l'equivalent par inspection manuelle de l'attribut .exceptions.

if sys.version_info >= (3, 11):
    print("=== Groupes d'exceptions (ExceptionGroup, Python 3.11+) ===\n")
    try:
        valider_formulaire()
    except ExceptionGroup as groupe:  # noqa: F821 (builtin Python 3.11+)
        print(f"  Groupe : {groupe.message}")
        valeurs = [str(e) for e in groupe.exceptions if isinstance(e, ValueError)]
        types_ = [str(e) for e in groupe.exceptions if isinstance(e, TypeError)]
        print(f"  {len(valeurs)} ValueError : {valeurs}")
        print(f"  {len(types_)} TypeError  : {types_}")
else:
    print("Les groupes d'exceptions (ExceptionGroup / except*) necessitent Python 3.11+")
    print(f"Version actuelle : {sys.version_info.major}.{sys.version_info.minor} -> exemple ignore")
