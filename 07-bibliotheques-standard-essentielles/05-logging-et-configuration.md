🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 7.5 : logging et configuration

## Introduction

Le logging (journalisation) est essentiel pour surveiller, déboguer et maintenir des applications. Le module `logging` de Python offre un système flexible et puissant pour enregistrer les événements de votre programme.

### Analogie simple
Imaginez le logging comme le **journal de bord** d'un navire :
- **Différents niveaux** : météo calme, tempête, urgence
- **Horodatage** : quand chaque événement s'est produit
- **Destinations multiples** : carnet de bord, radio, signaux lumineux
- **Filtrage** : ne noter que les événements importants selon la situation

## Pourquoi utiliser le logging ?

### Problèmes avec print()
```python
# ❌ Problématique avec print()
def calculer_division(a, b):
    print(f"Calcul de {a} / {b}")  # Toujours affiché
    if b == 0:
        print("ERREUR: Division par zéro!")  # Mélangé avec les résultats
        return None
    result = a / b
    print(f"Résultat: {result}")  # Difficile à filtrer
    return result

# ✅ Solution avec logging
import logging

def calculer_division_log(a, b):
    logging.info(f"Calcul de {a} / {b}")
    if b == 0:
        logging.error("Division par zéro!")
        return None
    result = a / b
    logging.debug(f"Résultat: {result}")
    return result
```

## Niveaux de logging

```python
import logging

# Configuration basique
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def demo_niveaux():
    """Démonstration des différents niveaux de logging."""

    print("📊 NIVEAUX DE LOGGING")
    print("-" * 25)

    # Du moins important au plus important
    logging.debug("Message de débogage - détails techniques")
    logging.info("Information générale - flux normal")
    logging.warning("Avertissement - quelque chose d'inhabituel")
    logging.error("Erreur - le programme continue mais avec un problème")
    logging.critical("Critique - erreur grave, arrêt possible")

demo_niveaux()
```

### Hiérarchie des niveaux
```
CRITICAL (50) - Erreurs critiques
ERROR    (40) - Erreurs
WARNING  (30) - Avertissements (niveau par défaut)
INFO     (20) - Informations générales
DEBUG    (10) - Informations de débogage
```

## Configuration de base

### Configuration simple
```python
import logging

# Configuration en une ligne
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def test_configuration():
    """Test de la configuration basique."""

    logging.debug("Ceci ne s'affichera pas (niveau trop bas)")
    logging.info("Application démarrée")
    logging.warning("Attention: configuration par défaut")
    logging.error("Erreur simulée")

test_configuration()
```

### Configuration avec fichier
```python
import logging

# Configuration pour écrire dans un fichier
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='application.log',
    filemode='w'  # 'w' pour écraser, 'a' pour ajouter
)

def test_fichier_log():
    """Test de logging dans un fichier."""

    logging.info("Début de l'application")

    try:
        result = 10 / 2
        logging.info(f"Calcul réussi: {result}")
    except Exception as e:
        logging.error(f"Erreur de calcul: {e}")

    logging.info("Fin de l'application")
    print("📁 Vérifiez le fichier 'application.log'")

test_fichier_log()
```

## Loggers, Handlers et Formatters

### Système de logging avancé
```python
import logging
import sys

def configurer_logging_avance():
    """Configuration avancée avec plusieurs handlers."""

    # Créer un logger principal
    logger = logging.getLogger('mon_app')
    logger.setLevel(logging.DEBUG)

    # Éviter la duplication des logs
    logger.handlers.clear()

    # Formatter pour les messages
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Handler pour la console (INFO et plus)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler pour fichier d'erreurs (ERROR et plus)
    error_handler = logging.FileHandler('errors.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)

    # Handler pour fichier complet (DEBUG et plus)
    debug_handler = logging.FileHandler('debug.log')
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    logger.addHandler(debug_handler)

    return logger

# Test de la configuration avancée
logger = configurer_logging_avance()

logger.debug("Message de débogage")
logger.info("Information générale")
logger.warning("Avertissement")
logger.error("Erreur test")

print("📁 Vérifiez les fichiers 'errors.log' et 'debug.log'")
```

## Logging dans des applications réelles

### Exemple 1 : Calculatrice avec logging
```python
import logging

class Calculatrice:
    """Calculatrice avec logging intégré."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.historique = []

    def addition(self, a, b):
        """Addition avec logging."""
        self.logger.info(f"Addition: {a} + {b}")
        result = a + b
        self._enregistrer_operation("addition", a, b, result)
        return result

    def division(self, a, b):
        """Division avec gestion d'erreur et logging."""
        self.logger.info(f"Division: {a} / {b}")

        if b == 0:
            self.logger.error("Tentative de division par zéro")
            raise ValueError("Division par zéro impossible")

        result = a / b
        self._enregistrer_operation("division", a, b, result)
        return result

    def _enregistrer_operation(self, operation, a, b, result):
        """Enregistre l'opération dans l'historique."""
        entry = {
            'operation': operation,
            'operandes': (a, b),
            'resultat': result
        }
        self.historique.append(entry)
        self.logger.debug(f"Opération enregistrée: {entry}")

    def afficher_historique(self):
        """Affiche l'historique des opérations."""
        self.logger.info("Affichage de l'historique")

        if not self.historique:
            print("Aucune opération dans l'historique")
            return

        print("📊 Historique des calculs:")
        for i, entry in enumerate(self.historique, 1):
            op = entry['operation']
            a, b = entry['operandes']
            result = entry['resultat']
            print(f"  {i}. {op}({a}, {b}) = {result}")

# Configuration et test
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

calc = Calculatrice()
calc.addition(5, 3)
calc.division(10, 2)

try:
    calc.division(5, 0)
except ValueError as e:
    print(f"Erreur capturée: {e}")

calc.afficher_historique()
```

### Exemple 2 : Processeur de fichiers
```python
import logging
import os
from datetime import datetime

class ProcesseurFichiers:
    """Processeur de fichiers avec logging détaillé."""

    def __init__(self, repertoire_source):
        self.repertoire_source = repertoire_source
        self.logger = logging.getLogger(self.__class__.__name__)
        self.statistiques = {
            'fichiers_traites': 0,
            'erreurs': 0,
            'taille_totale': 0
        }

    def traiter_tous_fichiers(self):
        """Traite tous les fichiers du répertoire."""
        self.logger.info(f"Début du traitement du répertoire: {self.repertoire_source}")

        if not os.path.exists(self.repertoire_source):
            self.logger.error(f"Répertoire inexistant: {self.repertoire_source}")
            return False

        try:
            fichiers = os.listdir(self.repertoire_source)
            self.logger.info(f"{len(fichiers)} fichier(s) trouvé(s)")

            for fichier in fichiers:
                self.traiter_fichier(fichier)

            self.afficher_statistiques()
            return True

        except Exception as e:
            self.logger.critical(f"Erreur critique lors du traitement: {e}")
            return False

    def traiter_fichier(self, nom_fichier):
        """Traite un fichier individuel."""
        chemin_complet = os.path.join(self.repertoire_source, nom_fichier)

        try:
            if os.path.isfile(chemin_complet):
                taille = os.path.getsize(chemin_complet)
                self.logger.debug(f"Traitement de {nom_fichier} ({taille} octets)")

                # Simulation du traitement
                self.statistiques['fichiers_traites'] += 1
                self.statistiques['taille_totale'] += taille

                self.logger.info(f"✅ {nom_fichier} traité avec succès")
            else:
                self.logger.warning(f"⚠️ {nom_fichier} n'est pas un fichier")

        except Exception as e:
            self.statistiques['erreurs'] += 1
            self.logger.error(f"❌ Erreur avec {nom_fichier}: {e}")

    def afficher_statistiques(self):
        """Affiche les statistiques finales."""
        stats = self.statistiques
        self.logger.info("📊 Statistiques finales:")
        self.logger.info(f"  Fichiers traités: {stats['fichiers_traites']}")
        self.logger.info(f"  Erreurs: {stats['erreurs']}")
        self.logger.info(f"  Taille totale: {stats['taille_totale']:,} octets")

# Configuration et test
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Console
        logging.FileHandler('processeur.log')  # Fichier
    ]
)

# Test avec le répertoire courant
processeur = ProcesseurFichiers('.')
processeur.traiter_tous_fichiers()
```

## Configuration via fichier

### Fichier de configuration JSON
```python
import logging
import logging.config
import json

# Configuration via dictionnaire
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'detailed'
        }
    },
    'loggers': {
        '': {  # Root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

def configurer_logging_avance():
    """Configure le logging via dictionnaire."""
    logging.config.dictConfig(LOGGING_CONFIG)

    # Sauvegarder la configuration dans un fichier
    with open('logging_config.json', 'w') as f:
        json.dump(LOGGING_CONFIG, f, indent=2)

    print("📄 Configuration sauvegardée dans 'logging_config.json'")

# Application de la configuration
configurer_logging_avance()

# Test
logger = logging.getLogger(__name__)
logger.debug("Message de debug")
logger.info("Application configurée")
logger.warning("Test d'avertissement")
```

## Exercices pratiques

### Exercice 1 : Système de monitoring simple
```python
import logging
import time
import psutil  # pip install psutil

class MonitorSysteme:
    """Monitor système avec logging."""

    def __init__(self):
        self.logger = logging.getLogger('Monitor')
        self.seuils = {
            'cpu': 80.0,      # %
            'memoire': 85.0,  # %
            'disque': 90.0    # %
        }

    def verifier_ressources(self):
        """Vérifie l'utilisation des ressources."""
        cpu = psutil.cpu_percent(interval=1)
        memoire = psutil.virtual_memory().percent
        disque = psutil.disk_usage('/').percent

        self.logger.info(f"CPU: {cpu}%, RAM: {memoire}%, Disque: {disque}%")

        # Alertes basées sur les seuils
        if cpu > self.seuils['cpu']:
            self.logger.warning(f"⚠️ CPU élevé: {cpu}%")

        if memoire > self.seuils['memoire']:
            self.logger.error(f"❌ Mémoire critique: {memoire}%")

        if disque > self.seuils['disque']:
            self.logger.critical(f"🚨 Disque plein: {disque}%")

    def monitorer(self, duree=30, intervalle=5):
        """Lance le monitoring pendant une durée donnée."""
        self.logger.info(f"Début monitoring ({duree}s, intervalle {intervalle}s)")

        fin = time.time() + duree
        while time.time() < fin:
            self.verifier_ressources()
            time.sleep(intervalle)

        self.logger.info("Fin du monitoring")

# Configuration et test
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Décommenter pour tester (nécessite psutil)
# monitor = MonitorSysteme()
# monitor.verifier_ressources()
```

### Exercice 2 : Logger pour API web
```python
import logging
from datetime import datetime
import json

class APILogger:
    """Logger spécialisé pour API web."""

    def __init__(self):
        # Logger pour les requêtes
        self.request_logger = logging.getLogger('api.requests')

        # Logger pour les erreurs
        self.error_logger = logging.getLogger('api.errors')

        # Logger pour les performances
        self.perf_logger = logging.getLogger('api.performance')

    def log_request(self, method, endpoint, user_id=None, ip=None):
        """Log une requête API."""
        self.request_logger.info(
            f"{method} {endpoint} - User: {user_id} - IP: {ip}"
        )

    def log_response(self, endpoint, status_code, response_time):
        """Log une réponse API."""
        level = logging.INFO if status_code < 400 else logging.ERROR

        self.request_logger.log(
            level,
            f"{endpoint} → {status_code} ({response_time:.3f}s)"
        )

        # Log performance si lent
        if response_time > 1.0:
            self.perf_logger.warning(
                f"Réponse lente: {endpoint} ({response_time:.3f}s)"
            )

    def log_error(self, endpoint, error, user_id=None):
        """Log une erreur API."""
        self.error_logger.error(
            f"Erreur sur {endpoint} - User: {user_id} - Error: {error}"
        )

# Configuration multi-logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Test
api_logger = APILogger()
api_logger.log_request('GET', '/api/users', user_id=123, ip='192.168.1.1')
api_logger.log_response('/api/users', 200, 0.145)
api_logger.log_response('/api/slow-endpoint', 200, 2.5)  # Lent
api_logger.log_error('/api/broken', 'Database connection failed', user_id=123)
```

### Exercice 3 : Configurateur automatique
```python
import logging
import os
from datetime import datetime

class ConfigurateurLogging:
    """Configurateur automatique de logging selon l'environnement."""

    @staticmethod
    def detecter_environnement():
        """Détecte l'environnement d'exécution."""
        if os.getenv('ENV') == 'production':
            return 'production'
        elif os.getenv('ENV') == 'test':
            return 'test'
        else:
            return 'development'

    @classmethod
    def configurer(cls, app_name='app'):
        """Configure le logging selon l'environnement."""
        env = cls.detecter_environnement()
        timestamp = datetime.now().strftime('%Y%m%d')

        config = {
            'development': {
                'level': logging.DEBUG,
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'handlers': [logging.StreamHandler()]
            },
            'test': {
                'level': logging.WARNING,
                'format': '%(levelname)s: %(message)s',
                'handlers': [logging.FileHandler(f'test_{timestamp}.log')]
            },
            'production': {
                'level': logging.INFO,
                'format': '%(asctime)s - %(levelname)s - %(message)s',
                'handlers': [
                    logging.FileHandler(f'{app_name}_{timestamp}.log'),
                    logging.StreamHandler()
                ]
            }
        }

        current_config = config[env]

        logging.basicConfig(
            level=current_config['level'],
            format=current_config['format'],
            handlers=current_config['handlers']
        )

        logger = logging.getLogger(app_name)
        logger.info(f"Configuration {env} appliquée pour {app_name}")

        return logger

# Test avec différents environnements
print("🔧 Test de configuration automatique")

# Environnement de développement (par défaut)
logger_dev = ConfigurateurLogging.configurer('mon_app')
logger_dev.debug("Message de debug")
logger_dev.info("Application démarrée")

# Simulation environnement de production
os.environ['ENV'] = 'production'
logger_prod = ConfigurateurLogging.configurer('mon_app')
logger_prod.info("Application en production")
```

## Bonnes pratiques

### **1. Niveaux appropriés**
```python
# ✅ Bon usage des niveaux
logging.debug("Variables: x={}, y={}".format(x, y))    # Détails techniques
logging.info("Utilisateur connecté: {}".format(user))  # Flux normal
logging.warning("Tentative de connexion échouée")      # Inhabituel
logging.error("Impossible de se connecter à la DB")    # Erreur récupérable
logging.critical("Mémoire insuffisante, arrêt")        # Erreur fatale
```

### **2. Messages informatifs**
```python
# ✅ Messages clairs et contextuels
logging.error(f"Échec connexion DB: {db_url} - Erreur: {str(e)}")

# ❌ Messages vagues
logging.error("Erreur")
```

### **3. Éviter les informations sensibles**
```python
# ✅ Sécurisé
logging.info(f"Connexion utilisateur: {username}")

# ❌ Dangereux
logging.info(f"Connexion: {username}:{password}")
```

### **4. Performance**
```python
# ✅ Évaluation paresseuse pour debug
logging.debug("Données: %s", donnees_complexes)  # Formatage seulement si nécessaire

# ❌ Toujours évalué
logging.debug(f"Données: {donnees_complexes}")   # Formatage même si debug désactivé
```

## Cas d'usage courants

### **Applications web**
- Requêtes et réponses HTTP
- Erreurs d'authentification
- Performance des endpoints

### **Applications de traitement**
- Progression des tâches
- Erreurs de données
- Statistiques de traitement

### **Services système**
- Monitoring de ressources
- Alertes de sécurité
- Événements de maintenance

### **Debugging et développement**
- Traçage d'exécution
- Valeurs de variables
- Flux de contrôle

## Résumé

Le module `logging` est essentiel pour :

1. **Surveiller** le comportement des applications
2. **Déboguer** efficacement les problèmes
3. **Auditer** les événements importants
4. **Alerter** sur les conditions anormales

### Configuration recommandée
- **Développement** : DEBUG en console
- **Test** : WARNING dans fichiers
- **Production** : INFO dans fichiers + erreurs critiques en console

Le logging bien configuré transforme une application "boîte noire" en système transparent et maintenable.

Ceci conclut le Module 7 sur les bibliothèques standard essentielles de Python !

⏭️
