# ============================================================================
#   Section 9.2 : Creation d'exceptions personnalisees
#   Description : Hierarchie d'exceptions personnalisees a plusieurs niveaux
#                 (base -> categories -> specifiques) et capture a differents
#                 niveaux de la hierarchie
#   Fichier source : 02-exceptions-personnalisees.md
# ============================================================================

# Exception de base de l'application
class ErreurApplication(Exception):
    """Classe de base pour toutes les exceptions de l'application."""
    pass

# Categories
class ErreurBaseDeDonnees(ErreurApplication):
    """Erreurs liees a la base de donnees."""
    pass

class ErreurReseau(ErreurApplication):
    """Erreurs liees au reseau."""
    pass

class ErreurValidation(ErreurApplication):
    """Erreurs de validation des donnees."""
    pass

# Exceptions specifiques
class ConnexionBaseDeDonneesError(ErreurBaseDeDonnees):
    """Impossible de se connecter a la base de donnees."""
    pass

class RequeteEchoueeError(ErreurBaseDeDonnees):
    """La requete SQL a echoue."""
    pass

class TimeoutReseauError(ErreurReseau):
    """Le reseau a mis trop de temps a repondre."""
    pass

# ==========================================
# Capturer a differents niveaux de la hierarchie
# ==========================================
print("=== Hierarchie d'exceptions personnalisees ===\n")

def operation(scenario):
    if scenario == "db_connexion":
        raise ConnexionBaseDeDonneesError("Connexion refusee par le serveur")
    elif scenario == "db_requete":
        raise RequeteEchoueeError("Syntaxe SQL invalide")
    elif scenario == "reseau":
        raise TimeoutReseauError("Delai depasse apres 30s")

for scenario in ["db_connexion", "db_requete", "reseau"]:
    try:
        operation(scenario)
    except ConnexionBaseDeDonneesError as e:
        # Niveau le plus specifique
        print(f"  [specifique] Connexion BdD : {e}")
    except ErreurBaseDeDonnees as e:
        # Niveau categorie : capture les autres erreurs de base de donnees
        print(f"  [categorie]  Erreur BdD : {e}")
    except ErreurApplication as e:
        # Niveau global : capture toute erreur de l'application
        print(f"  [global]     {type(e).__name__} : {e}")

# ==========================================
# A retenir : toujours heriter d'Exception, jamais de BaseException
# ==========================================
print("\n=== Verification de la hierarchie ===\n")
print(f"  ConnexionBaseDeDonneesError sous ErreurBaseDeDonnees : "
      f"{issubclass(ConnexionBaseDeDonneesError, ErreurBaseDeDonnees)}")
print(f"  ErreurBaseDeDonnees sous ErreurApplication           : "
      f"{issubclass(ErreurBaseDeDonnees, ErreurApplication)}")
print(f"  ErreurApplication sous Exception (et non BaseException) : "
      f"{issubclass(ErreurApplication, Exception)}")
