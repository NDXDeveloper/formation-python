# ============================================================================
#   Section 5.12 : Gestionnaire de configuration JSON
#   Description : Charger et valider une configuration depuis un fichier JSON
#   Fichier source : 05-gestion-des-erreurs.md
# ============================================================================

import json

class ConfigError(Exception):
    """Exception pour les erreurs de configuration."""
    pass

def charger_configuration(fichier_config):
    """Charge une configuration depuis un fichier JSON."""
    try:
        with open(fichier_config, 'r', encoding='utf-8') as f:
            config = json.load(f)

        champs_obligatoires = ['host', 'port', 'database']
        for champ in champs_obligatoires:
            if champ not in config:
                raise ConfigError(f"Champ obligatoire manquant : {champ}")

        if not isinstance(config['port'], int):
            raise ConfigError("Le port doit être un nombre entier")

        if config['port'] < 1 or config['port'] > 65535:
            raise ConfigError("Le port doit être entre 1 et 65535")

        print("Configuration chargée avec succès")
        return config

    except FileNotFoundError:
        raise ConfigError(f"Fichier de configuration introuvable : {fichier_config}")

    except json.JSONDecodeError as e:
        raise ConfigError(f"Fichier JSON invalide : {e}")

# Utilisation
try:
    config = charger_configuration("config.json")
    print(f"Connexion à {config['host']}:{config['port']}")
except ConfigError as e:
    print(f"Erreur de configuration : {e}")
    print("Utilisation de la configuration par défaut")
    config = {
        'host': 'localhost',
        'port': 5432,
        'database': 'mydb'
    }
    print(f"Connexion à {config['host']}:{config['port']}")
