🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 4.3 : Sérialisation avec pickle

## Introduction

La sérialisation est le processus de conversion d'un objet Python en une séquence de bytes qui peut être stockée dans un fichier ou transmise sur un réseau. Le module `pickle` de Python permet de sérialiser et désérialiser presque tous les objets Python, préservant leur structure et leurs types de données exacts.

## Qu'est-ce que pickle ?

### Définition
**Pickle** est le protocole de sérialisation natif de Python. Il peut convertir des objets Python complexes (listes imbriquées, dictionnaires, classes personnalisées, etc.) en format binaire et les restaurer exactement comme ils étaient.

### Avantages de pickle
- **Fidélité** : Préserve exactement les types Python
- **Simplicité** : Interface très facile à utiliser
- **Completude** : Supporte presque tous les objets Python
- **Rapidité** : Performance optimisée pour Python

### Inconvénients de pickle
- **Spécifique à Python** : Non lisible par d'autres langages
- **Sécurité** : Peut exécuter du code arbitraire
- **Portabilité** : Dépendant de la version Python

## Utilisation de base

### Sérialisation (pickle.dump et pickle.dumps)

```python
import pickle

# Données à sérialiser
donnees = {
    'nom': 'Alice',
    'age': 30,
    'hobbies': ['lecture', 'natation', 'cuisine'],
    'informations': {
        'ville': 'Paris',
        'travail': 'Développeuse'
    }
}

# Méthode 1: Sauvegarder dans un fichier (dump)
with open('donnees.pkl', 'wb') as f:
    pickle.dump(donnees, f)

print("Données sauvegardées dans donnees.pkl")

# Méthode 2: Convertir en bytes (dumps)
donnees_bytes = pickle.dumps(donnees)
print(f"Taille des données sérialisées: {len(donnees_bytes)} bytes")
```

### Désérialisation (pickle.load et pickle.loads)

```python
import pickle

# Méthode 1: Charger depuis un fichier (load)
with open('donnees.pkl', 'rb') as f:
    donnees_restaurees = pickle.load(f)

print("Données restaurées:", donnees_restaurees)

# Méthode 2: Depuis des bytes (loads)
donnees_depuis_bytes = pickle.loads(donnees_bytes)
print("Données depuis bytes:", donnees_depuis_bytes)

# Vérification que les données sont identiques
print("Identiques?", donnees == donnees_restaurees)
```

## Types de données supportés

### Types simples et collections

```python
import pickle

# Démonstration avec différents types
exemples = {
    'entier': 42,
    'flottant': 3.14159,
    'chaine': "Bonjour le monde!",
    'booleen': True,
    'none': None,
    'liste': [1, 2, 3, 'quatre', 5.0],
    'tuple': (10, 20, 30),
    'ensemble': {1, 2, 3, 4, 5},
    'dictionnaire': {'a': 1, 'b': 2, 'c': 3}
}

# Sérialisation
with open('types_varies.pkl', 'wb') as f:
    pickle.dump(exemples, f)

# Désérialisation et vérification
with open('types_varies.pkl', 'rb') as f:
    exemples_restaures = pickle.load(f)

# Vérification type par type
for cle, valeur in exemples.items():
    valeur_restauree = exemples_restaures[cle]
    print(f"{cle}: {type(valeur)} → {type(valeur_restauree)} | Identique: {valeur == valeur_restauree}")
```

### Objets plus complexes

```python
import pickle
from datetime import datetime, date
import re

# Objets complexes
objets_complexes = {
    'date_actuelle': datetime.now(),
    'date_naissance': date(1990, 5, 15),
    'pattern_regex': re.compile(r'\d+'),
    'fonction': lambda x: x * 2,  # Attention: les lambdas ne sont pas toujours sérialisables
    'liste_imbriquee': [[1, 2], [3, 4], {'nested': True}]
}

try:
    # Sérialisation
    with open('objets_complexes.pkl', 'wb') as f:
        # Les lambdas peuvent poser problème selon le contexte
        objets_sans_lambda = {k: v for k, v in objets_complexes.items() if k != 'fonction'}
        pickle.dump(objets_sans_lambda, f)

    # Désérialisation
    with open('objets_complexes.pkl', 'rb') as f:
        objets_restaures = pickle.load(f)

    print("Objets complexes restaurés avec succès!")
    for cle, valeur in objets_restaures.items():
        print(f"{cle}: {type(valeur)} = {valeur}")

except Exception as e:
    print(f"Erreur lors de la sérialisation: {e}")
```

## Sérialisation d'objets personnalisés

### Classes simples

```python
import pickle

class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
        self.date_creation = datetime.now()

    def __str__(self):
        return f"Personne(nom='{self.nom}', age={self.age})"

    def __repr__(self):
        return self.__str__()

    def saluer(self):
        return f"Bonjour, je suis {self.nom} et j'ai {self.age} ans"

# Création d'objets
alice = Personne("Alice Dupont", 30, "alice@email.com")
bob = Personne("Bob Martin", 25, "bob@email.com")

# Liste d'objets
equipe = [alice, bob]

print("Avant sérialisation:")
for personne in equipe:
    print(f"- {personne.saluer()}")

# Sérialisation
with open('equipe.pkl', 'wb') as f:
    pickle.dump(equipe, f)

# Désérialisation
with open('equipe.pkl', 'rb') as f:
    equipe_restauree = pickle.load(f)

print("\nAprès désérialisation:")
for personne in equipe_restauree:
    print(f"- {personne.saluer()}")
    print(f"  Créé le: {personne.date_creation}")
```

### Classes avec méthodes personnalisées de sérialisation

```python
import pickle
from datetime import datetime

class CompteBancaire:
    def __init__(self, numero, titulaire, solde=0):
        self.numero = numero
        self.titulaire = titulaire
        self.solde = solde
        self.historique = []
        self.derniere_connexion = datetime.now()

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            self.historique.append(f"Dépôt: +{montant}€")
            print(f"Dépôt de {montant}€. Nouveau solde: {self.solde}€")

    def retirer(self, montant):
        if 0 < montant <= self.solde:
            self.solde -= montant
            self.historique.append(f"Retrait: -{montant}€")
            print(f"Retrait de {montant}€. Nouveau solde: {self.solde}€")
        else:
            print("Fonds insuffisants ou montant invalide")

    def __getstate__(self):
        """Personnalise ce qui est sérialisé"""
        # On peut choisir de ne pas sérialiser certains attributs
        state = self.__dict__.copy()
        # Par exemple, on reset la dernière connexion
        state['derniere_connexion'] = None
        return state

    def __setstate__(self, state):
        """Personnalise la restauration"""
        # Restaure l'état
        self.__dict__.update(state)
        # Définit une nouvelle date de connexion
        self.derniere_connexion = datetime.now()
        print(f"Compte {self.numero} restauré pour {self.titulaire}")

    def __str__(self):
        return f"Compte {self.numero}: {self.titulaire} - {self.solde}€"

# Utilisation
compte = CompteBancaire("12345", "Alice Dupont", 1000)
compte.deposer(500)
compte.retirer(200)

print(f"\nAvant sérialisation: {compte}")
print(f"Dernière connexion: {compte.derniere_connexion}")

# Sérialisation
with open('compte.pkl', 'wb') as f:
    pickle.dump(compte, f)

print("\n--- Sérialisation effectuée ---")

# Simulation d'un redémarrage (attendre un peu)
import time
time.sleep(1)

# Désérialisation
with open('compte.pkl', 'rb') as f:
    compte_restaure = pickle.load(f)

print(f"\nAprès désérialisation: {compte_restaure}")
print(f"Nouvelle connexion: {compte_restaure.derniere_connexion}")
print(f"Historique conservé: {compte_restaure.historique}")
```

## Protocoles pickle

### Choix du protocole

```python
import pickle

# Données d'exemple
donnees = {'nom': 'Test', 'valeurs': list(range(1000))}

# Test des différents protocoles
for protocole in range(pickle.HIGHEST_PROTOCOL + 1):
    # Sérialisation avec protocole spécifique
    donnees_serialisees = pickle.dumps(donnees, protocol=protocole)

    print(f"Protocole {protocole}: {len(donnees_serialisees)} bytes")

    # Vérification de la désérialisation
    donnees_restaurees = pickle.loads(donnees_serialisees)
    print(f"  Restauration réussie: {donnees == donnees_restaurees}")

# Utilisation du protocole le plus récent (recommandé)
with open('donnees_moderne.pkl', 'wb') as f:
    pickle.dump(donnees, f, protocol=pickle.HIGHEST_PROTOCOL)

print(f"\nProtocole le plus élevé disponible: {pickle.HIGHEST_PROTOCOL}")
```

### Compatibilité des protocoles

```python
import pickle

# Table de compatibilité des protocoles
compatibilite = {
    0: "Version 0.9.2 et plus (lisible par l'homme)",
    1: "Ancien format binaire",
    2: "Python 2.3+ (nouvelles classes)",
    3: "Python 3.0+ (bytes explicites)",
    4: "Python 3.4+ (gros objets)",
    5: "Python 3.8+ (optimisations)"
}

print("Protocoles pickle et leur compatibilité:")
for protocole, description in compatibilite.items():
    if protocole <= pickle.HIGHEST_PROTOCOL:
        print(f"  {protocole}: {description}")
```

## Gestion des erreurs et sécurité

### Erreurs courantes

```python
import pickle
import io

def demo_erreurs_pickle():
    print("=== Démonstration des erreurs courantes ===\n")

    # 1. Tentative de pickle d'un objet non-sérialisable
    print("1. Objet non-sérialisable (fonction lambda):")
    try:
        fonction_lambda = lambda x: x * 2
        pickle.dumps(fonction_lambda)
    except Exception as e:
        print(f"   Erreur: {type(e).__name__}: {e}\n")

    # 2. Fichier corrompu
    print("2. Fichier pickle corrompu:")
    try:
        # Création d'un fichier "corrompu"
        with open('corrompu.pkl', 'wb') as f:
            f.write(b'ceci n\'est pas du pickle valide')

        # Tentative de lecture
        with open('corrompu.pkl', 'rb') as f:
            pickle.load(f)
    except Exception as e:
        print(f"   Erreur: {type(e).__name__}: {e}\n")

    # 3. Problème de module manquant
    print("3. Classe non trouvée:")
    # Simulons une classe qui n'existe plus
    class ClasseTemporaire:
        def __init__(self, valeur):
            self.valeur = valeur

    # Sérialisation
    obj = ClasseTemporaire(42)
    donnees_bytes = pickle.dumps(obj)

    # Suppression de la classe du namespace
    del ClasseTemporaire

    try:
        # Tentative de désérialisation
        pickle.loads(donnees_bytes)
    except Exception as e:
        print(f"   Erreur: {type(e).__name__}: {e}\n")

def lecture_pickle_securisee(fichier):
    """Fonction pour lire un fichier pickle de manière sécurisée"""
    try:
        with open(fichier, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"Fichier {fichier} non trouvé")
        return None
    except pickle.UnpicklingError as e:
        print(f"Erreur de désérialisation: {e}")
        return None
    except EOFError:
        print(f"Fichier {fichier} vide ou tronqué")
        return None
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return None

# Démonstration
demo_erreurs_pickle()
```

### Sécurité avec pickle

```python
import pickle
import types

class SecureUnpickler(pickle.Unpickler):
    """Unpickler sécurisé qui restreint les types autorisés"""

    # Types autorisés pour la désérialisation
    TYPES_AUTORISES = {
        'builtins.list',
        'builtins.dict',
        'builtins.tuple',
        'builtins.set',
        'builtins.str',
        'builtins.int',
        'builtins.float',
        'builtins.bool',
        'builtins.NoneType',
        'datetime.datetime',
        'datetime.date',
    }

    def find_class(self, module, name):
        """Vérifie si la classe est autorisée"""
        classe_complete = f"{module}.{name}"

        if classe_complete in self.TYPES_AUTORISES:
            return super().find_class(module, name)

        # Permet les classes définies dans le module principal
        if module == "__main__":
            return super().find_class(module, name)

        raise pickle.UnpicklingError(f"Classe non autorisée: {classe_complete}")

def charger_pickle_securise(fichier, types_supplementaires=None):
    """Charge un fichier pickle avec restrictions de sécurité"""
    try:
        with open(fichier, 'rb') as f:
            unpickler = SecureUnpickler(f)

            # Ajouter des types supplémentaires si nécessaire
            if types_supplementaires:
                unpickler.TYPES_AUTORISES.update(types_supplementaires)

            return unpickler.load()
    except Exception as e:
        print(f"Erreur lors du chargement sécurisé: {e}")
        return None

# Exemple d'utilisation
donnees_sures = {
    'nom': 'Alice',
    'age': 30,
    'date_naissance': date(1993, 5, 15)
}

# Sauvegarde
with open('donnees_sures.pkl', 'wb') as f:
    pickle.dump(donnees_sures, f)

# Chargement sécurisé
donnees_restaurees = charger_pickle_securise('donnees_sures.pkl')
print("Données chargées de manière sécurisée:", donnees_restaurees)
```

## Comparaison avec d'autres formats

### Benchmark pickle vs JSON

```python
import pickle
import json
import time
from datetime import datetime

def benchmark_serialisation():
    # Données de test
    donnees_test = {
        'utilisateurs': [
            {
                'id': i,
                'nom': f'Utilisateur{i}',
                'email': f'user{i}@email.com',
                'scores': list(range(100)),
                'actif': i % 2 == 0
            }
            for i in range(1000)
        ],
        'metadata': {
            'version': '1.0',
            'date_creation': datetime.now().isoformat(),
            'total': 1000
        }
    }

    print("=== Benchmark Pickle vs JSON ===\n")

    # Test Pickle
    start_time = time.time()
    donnees_pickle = pickle.dumps(donnees_test, protocol=pickle.HIGHEST_PROTOCOL)
    temps_pickle_serialisation = time.time() - start_time

    start_time = time.time()
    donnees_pickle_restaurees = pickle.loads(donnees_pickle)
    temps_pickle_deserialisation = time.time() - start_time

    # Test JSON
    start_time = time.time()
    donnees_json = json.dumps(donnees_test, ensure_ascii=False)
    temps_json_serialisation = time.time() - start_time

    start_time = time.time()
    donnees_json_restaurees = json.loads(donnees_json)
    temps_json_deserialisation = time.time() - start_time

    # Résultats
    print(f"Taille des données:")
    print(f"  Pickle: {len(donnees_pickle):,} bytes")
    print(f"  JSON:   {len(donnees_json.encode('utf-8')):,} bytes")
    print(f"  Rapport: {len(donnees_json.encode('utf-8')) / len(donnees_pickle):.2f}x\n")

    print(f"Temps de sérialisation:")
    print(f"  Pickle: {temps_pickle_serialisation:.6f}s")
    print(f"  JSON:   {temps_json_serialisation:.6f}s")
    print(f"  Rapport: {temps_json_serialisation / temps_pickle_serialisation:.2f}x\n")

    print(f"Temps de désérialisation:")
    print(f"  Pickle: {temps_pickle_deserialisation:.6f}s")
    print(f"  JSON:   {temps_json_deserialisation:.6f}s")
    print(f"  Rapport: {temps_json_deserialisation / temps_pickle_deserialisation:.2f}x\n")

    # Vérification de l'intégrité
    print(f"Intégrité des données:")
    print(f"  Pickle: {'✅' if donnees_test == donnees_pickle_restaurees else '❌'}")
    # JSON ne peut pas restaurer exactement (datetime devient string)
    print(f"  JSON:   {'⚠️' if isinstance(donnees_json_restaurees['metadata']['date_creation'], str) else '❌'}")

# Exécution du benchmark
benchmark_serialisation()
```

## Cas d'usage pratiques

### Exemple 1 : Cache d'application

```python
import pickle
import os
import time
from datetime import datetime, timedelta
from pathlib import Path

class CacheManager:
    """Gestionnaire de cache utilisant pickle"""

    def __init__(self, dossier_cache="cache", duree_cache_heures=24):
        self.dossier_cache = Path(dossier_cache)
        self.dossier_cache.mkdir(exist_ok=True)
        self.duree_cache = timedelta(hours=duree_cache_heures)

    def _chemin_cache(self, cle):
        """Génère le chemin du fichier cache pour une clé"""
        nom_fichier = f"{cle}.pkl"
        return self.dossier_cache / nom_fichier

    def mettre_en_cache(self, cle, donnees):
        """Met des données en cache"""
        cache_data = {
            'donnees': donnees,
            'timestamp': datetime.now(),
            'cle': cle
        }

        chemin = self._chemin_cache(cle)
        try:
            with open(chemin, 'wb') as f:
                pickle.dump(cache_data, f, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"✅ Données mises en cache: {cle}")
        except Exception as e:
            print(f"❌ Erreur mise en cache: {e}")

    def obtenir_du_cache(self, cle):
        """Récupère des données du cache si elles sont valides"""
        chemin = self._chemin_cache(cle)

        if not chemin.exists():
            print(f"🔍 Cache manqué: {cle}")
            return None

        try:
            with open(chemin, 'rb') as f:
                cache_data = pickle.load(f)

            # Vérifier si le cache est encore valide
            age_cache = datetime.now() - cache_data['timestamp']
            if age_cache > self.duree_cache:
                print(f"⏰ Cache expiré: {cle} (âge: {age_cache})")
                self.supprimer_cache(cle)
                return None

            print(f"✅ Cache trouvé: {cle} (âge: {age_cache})")
            return cache_data['donnees']

        except Exception as e:
            print(f"❌ Erreur lecture cache: {e}")
            self.supprimer_cache(cle)
            return None

    def supprimer_cache(self, cle):
        """Supprime une entrée du cache"""
        chemin = self._chemin_cache(cle)
        if chemin.exists():
            chemin.unlink()
            print(f"🗑️ Cache supprimé: {cle}")

    def nettoyer_cache_expire(self):
        """Nettoie tous les caches expirés"""
        print("🧹 Nettoyage du cache...")
        compteur = 0

        for fichier_cache in self.dossier_cache.glob("*.pkl"):
            try:
                with open(fichier_cache, 'rb') as f:
                    cache_data = pickle.load(f)

                age_cache = datetime.now() - cache_data['timestamp']
                if age_cache > self.duree_cache:
                    fichier_cache.unlink()
                    compteur += 1
                    print(f"  Supprimé: {cache_data['cle']}")

            except Exception as e:
                print(f"  Erreur avec {fichier_cache}: {e}")
                fichier_cache.unlink()  # Supprime les fichiers corrompus
                compteur += 1

        print(f"✅ Nettoyage terminé: {compteur} fichiers supprimés")

    def lister_cache(self):
        """Liste toutes les entrées du cache"""
        print("📋 Contenu du cache:")

        for fichier_cache in self.dossier_cache.glob("*.pkl"):
            try:
                with open(fichier_cache, 'rb') as f:
                    cache_data = pickle.load(f)

                age_cache = datetime.now() - cache_data['timestamp']
                statut = "✅ Valide" if age_cache <= self.duree_cache else "⏰ Expiré"

                print(f"  {cache_data['cle']}: {statut} (âge: {age_cache})")

            except Exception as e:
                print(f"  {fichier_cache.name}: ❌ Erreur ({e})")

# Fonction simulant un calcul coûteux
def calcul_complexe(n):
    """Simule un calcul qui prend du temps"""
    print(f"⚙️ Exécution du calcul complexe pour n={n}...")
    time.sleep(2)  # Simule le temps de calcul
    resultat = sum(i**2 for i in range(n))
    return {'resultat': resultat, 'n': n, 'calcule_le': datetime.now()}

# Fonction avec cache
def calcul_avec_cache(n, cache_manager):
    """Calcul avec mise en cache automatique"""
    cle_cache = f"calcul_{n}"

    # Essaie d'abord de récupérer du cache
    resultat = cache_manager.obtenir_du_cache(cle_cache)

    if resultat is None:
        # Calcul et mise en cache
        resultat = calcul_complexe(n)
        cache_manager.mettre_en_cache(cle_cache, resultat)

    return resultat

# Démonstration
def demo_cache():
    print("=== Démonstration du système de cache ===\n")

    # Initialisation du cache (expire après 30 secondes pour la démo)
    cache = CacheManager(duree_cache_heures=1/120)  # 30 secondes

    # Premier appel (calcul)
    print("1. Premier appel:")
    result1 = calcul_avec_cache(1000, cache)
    print(f"   Résultat: {result1['resultat']}\n")

    # Deuxième appel (cache)
    print("2. Deuxième appel (devrait utiliser le cache):")
    result2 = calcul_avec_cache(1000, cache)
    print(f"   Résultat: {result2['resultat']}\n")

    # Autre calcul
    print("3. Calcul différent:")
    result3 = calcul_avec_cache(500, cache)
    print(f"   Résultat: {result3['resultat']}\n")

    # État du cache
    cache.lister_cache()

    print("\n4. Attente expiration...")
    time.sleep(31)  # Attendre que le cache expire

    print("5. Appel après expiration:")
    result4 = calcul_avec_cache(1000, cache)
    print(f"   Résultat: {result4['resultat']}\n")

    # Nettoyage
    cache.nettoyer_cache_expire()

# Lancement de la démo
demo_cache()
```

### Exemple 2 : Sauvegarde d'état de jeu

```python
import pickle
from datetime import datetime
import random

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.niveau = 1
        self.experience = 0
        self.vie = 100
        self.inventaire = []
        self.position = (0, 0)
        self.argent = 50

    def gagner_experience(self, points):
        self.experience += points
        # Niveau up tous les 100 points
        while self.experience >= self.niveau * 100:
            self.experience -= self.niveau * 100
            self.niveau += 1
            self.vie = 100  # Restore la vie au niveau up
            print(f"{self.nom} atteint le niveau {self.niveau}!")

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        print(f"{self.nom} a trouvé: {objet}")

    def deplacer(self, x, y):
        self.position = (x, y)
        print(f"{self.nom} se déplace en ({x}, {y})")

    def __str__(self):
        return f"{self.nom} (Niv.{self.niveau}) - Vie:{self.vie} - Pos:{self.position} - Argent:{self.argent}€"

class Jeu:
    def __init__(self):
        self.joueur = None
        self.temps_jeu = 0
        self.date_creation = datetime.now()
        self.derniere_sauvegarde = None

    def nouveau_joueur(self, nom):
        self.joueur = Joueur(nom)
        print(f"Nouveau joueur créé: {self.joueur}")

    def jouer_tour(self):
        """Simule un tour de jeu"""
        if not self.joueur:
            print("Aucun joueur chargé!")
            return

        self.temps_jeu += 1

        # Actions aléatoires
        actions = [
            lambda: self.joueur.gagner_experience(random.randint(10, 50)),
            lambda: self.joueur.ajouter_objet(random.choice([
                "Épée", "Potion", "Bouclier", "Gemme", "Parchemin"
            ])),
            lambda: self.joueur.deplacer(
                random.randint(-10, 10),
                random.randint(-10, 10)
            ),
            lambda: setattr(self.joueur, 'argent',
                          self.joueur.argent + random.randint(5, 25))
        ]

        # Exécute 1-3 actions aléatoires
        for _ in range(random.randint(1, 3)):
            random.choice(actions)()

        print(f"Tour {self.temps_jeu} terminé")
        print(f"État: {self.joueur}")
        print(f"Inventaire: {', '.join(self.joueur.inventaire[-3:])}")  # 3 derniers objets
        print("-" * 50)

    def sauvegarder(self, nom_fichier="sauvegarde.pkl"):
        """Sauvegarde l'état du jeu"""
        if not self.joueur:
            print("Aucun joueur à sauvegarder!")
            return False

        donnees_sauvegarde = {
            'joueur': self.joueur,
            'temps_jeu': self.temps_jeu,
            'date_creation': self.date_creation,
            'date_sauvegarde': datetime.now(),
            'version': '1.0'
        }

        try:
            with open(nom_fichier, 'wb') as f:
                pickle.dump(donnees_sauvegarde, f, protocol=pickle.HIGHEST_PROTOCOL)

            self.derniere_sauvegarde = datetime.now()
            print(f"✅ Jeu sauvegardé dans {nom_fichier}")
            return True

        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            return False

    def charger(self, nom_fichier="sauvegarde.pkl"):
        """Charge l'état du jeu"""
        try:
            with open(nom_fichier, 'rb') as f:
                donnees_sauvegarde = pickle.load(f)

            # Vérification de la version (simple)
            if donnees_sauvegarde.get('version') != '1.0':
                print(f"⚠️ Version de sauvegarde différente: {donnees_sauvegarde.get('version')}")

            # Restoration des données
            self.joueur = donnees_sauvegarde['joueur']
            self.temps_jeu = donnees_sauvegarde['temps_jeu']
            self.date_creation = donnees_sauvegarde['date_creation']

            print(f"✅ Jeu chargé depuis {nom_fichier}")
            print(f"   Joueur: {self.joueur.nom} (Niveau {self.joueur.niveau})")
            print(f"   Temps de jeu: {self.temps_jeu} tours")
            print(f"   Créé le: {self.date_creation}")
            print(f"   Sauvegardé le: {donnees_sauvegarde['date_sauvegarde']}")
            return True

        except FileNotFoundError:
            print(f"❌ Fichier de sauvegarde {nom_fichier} non trouvé")
            return False
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")
            return False

    def afficher_stats(self):
        """Affiche les statistiques du jeu"""
        if not self.joueur:
            print("Aucun joueur chargé!")
            return

        print("=== STATISTIQUES DU JEU ===")
        print(f"Joueur: {self.joueur.nom}")
        print(f"Niveau: {self.joueur.niveau}")
        print(f"Expérience: {self.joueur.experience}")
        print(f"Vie: {self.joueur.vie}")
        print(f"Position: {self.joueur.position}")
        print(f"Argent: {self.joueur.argent}€")
        print(f"Objets dans l'inventaire: {len(self.joueur.inventaire)}")
        if self.joueur.inventaire:
            print(f"Inventaire: {', '.join(self.joueur.inventaire)}")
        print(f"Temps de jeu: {self.temps_jeu} tours")
        print(f"Dernière sauvegarde: {self.derniere_sauvegarde or 'Jamais'}")

# Démonstration du système de sauvegarde
def demo_sauvegarde_jeu():
    print("=== Démonstration - Sauvegarde de jeu ===\n")

    # Nouveau jeu
    jeu = Jeu()
    jeu.nouveau_joueur("Alice")

    # Jouer quelques tours
    print("\n--- Session de jeu ---")
    for i in range(5):
        jeu.jouer_tour()

    # Afficher les stats
    print("\n--- Stats avant sauvegarde ---")
    jeu.afficher_stats()

    # Sauvegarder
    print("\n--- Sauvegarde ---")
    jeu.sauvegarder("ma_partie.pkl")

    # Simuler la fermeture du jeu
    print("\n--- Fermeture du jeu (simulation) ---")
    del jeu

    # Nouveau jeu et chargement
    print("\n--- Nouveau jeu et chargement ---")
    nouveau_jeu = Jeu()
    if nouveau_jeu.charger("ma_partie.pkl"):
        print("\n--- Stats après chargement ---")
        nouveau_jeu.afficher_stats()

        # Continuer à jouer
        print("\n--- Continuation de la partie ---")
        for i in range(3):
            nouveau_jeu.jouer_tour()

        # Sauvegarde finale
        nouveau_jeu.sauvegarder("ma_partie_suite.pkl")

# Lancement de la démo
demo_sauvegarde_jeu()
```

## Optimisation et bonnes pratiques

### Optimisation de la taille

```python
import pickle
import sys
import gzip
import bz2

def comparer_tailles_compression():
    """Compare les tailles avec différentes méthodes de compression"""

    # Données d'exemple (répétitives pour montrer l'effet de la compression)
    donnees = {
        'messages': ['Bonjour le monde!'] * 1000,
        'nombres': list(range(10000)),
        'utilisateurs': [
            {'nom': f'User{i}', 'email': f'user{i}@email.com', 'actif': True}
            for i in range(1000)
        ]
    }

    print("=== Comparaison des tailles avec compression ===\n")

    # Pickle standard
    donnees_pickle = pickle.dumps(donnees, protocol=pickle.HIGHEST_PROTOCOL)
    taille_pickle = len(donnees_pickle)

    # Pickle + gzip
    donnees_gzip = gzip.compress(donnees_pickle)
    taille_gzip = len(donnees_gzip)

    # Pickle + bz2
    donnees_bz2 = bz2.compress(donnees_pickle)
    taille_bz2 = len(donnees_bz2)

    # Affichage des résultats
    print(f"Taille des données en mémoire: ~{sys.getsizeof(donnees):,} bytes")
    print(f"Pickle standard:    {taille_pickle:,} bytes")
    print(f"Pickle + gzip:      {taille_gzip:,} bytes (ratio: {taille_gzip/taille_pickle:.2%})")
    print(f"Pickle + bz2:       {taille_bz2:,} bytes (ratio: {taille_bz2/taille_pickle:.2%})")

    # Test de décompression
    donnees_gzip_restaurees = pickle.loads(gzip.decompress(donnees_gzip))
    donnees_bz2_restaurees = pickle.loads(bz2.decompress(donnees_bz2))

    print(f"\nIntégrité après décompression:")
    print(f"Gzip: {'✅' if donnees == donnees_gzip_restaurees else '❌'}")
    print(f"Bz2:  {'✅' if donnees == donnees_bz2_restaurees else '❌'}")

def sauvegarder_avec_compression(donnees, fichier, methode='gzip'):
    """Sauvegarde avec compression"""
    donnees_pickle = pickle.dumps(donnees, protocol=pickle.HIGHEST_PROTOCOL)

    if methode == 'gzip':
        with gzip.open(f"{fichier}.gz", 'wb') as f:
            f.write(donnees_pickle)
        print(f"✅ Sauvegardé avec gzip: {fichier}.gz")
    elif methode == 'bz2':
        with bz2.open(f"{fichier}.bz2", 'wb') as f:
            f.write(donnees_pickle)
        print(f"✅ Sauvegardé avec bz2: {fichier}.bz2")
    else:
        with open(fichier, 'wb') as f:
            f.write(donnees_pickle)
        print(f"✅ Sauvegardé sans compression: {fichier}")

def charger_avec_compression(fichier, methode='gzip'):
    """Charge avec décompression"""
    try:
        if methode == 'gzip':
            with gzip.open(f"{fichier}.gz", 'rb') as f:
                return pickle.load(f)
        elif methode == 'bz2':
            with bz2.open(f"{fichier}.bz2", 'rb') as f:
                return pickle.load(f)
        else:
            with open(fichier, 'rb') as f:
                return pickle.load(f)
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")
        return None

# Démonstration
comparer_tailles_compression()
```

### Gestion de versions et migration

```python
import pickle
from datetime import datetime

class MigrateurDonnees:
    """Gestionnaire de migration pour les différentes versions de données"""

    VERSION_ACTUELLE = "2.0"

    @classmethod
    def migrer_donnees(cls, donnees):
        """Migre les données vers la version actuelle"""
        version = donnees.get('version', '1.0')

        if version == cls.VERSION_ACTUELLE:
            return donnees

        print(f"🔄 Migration depuis la version {version} vers {cls.VERSION_ACTUELLE}")

        # Migration 1.0 → 1.5
        if version == '1.0':
            donnees = cls._migrer_1_0_vers_1_5(donnees)
            version = '1.5'

        # Migration 1.5 → 2.0
        if version == '1.5':
            donnees = cls._migrer_1_5_vers_2_0(donnees)
            version = '2.0'

        donnees['version'] = version
        print(f"✅ Migration terminée vers la version {version}")
        return donnees

    @staticmethod
    def _migrer_1_0_vers_1_5(donnees):
        """Migration spécifique 1.0 → 1.5"""
        print("  Ajout du champ 'derniere_connexion'")

        if 'joueur' in donnees:
            # Ajouter un champ manquant
            if not hasattr(donnees['joueur'], 'derniere_connexion'):
                donnees['joueur'].derniere_connexion = datetime.now()

            # Convertir l'ancien format d'inventaire
            if hasattr(donnees['joueur'], 'objets'):
                donnees['joueur'].inventaire = donnees['joueur'].objets
                delattr(donnees['joueur'], 'objets')

        donnees['version'] = '1.5'
        return donnees

    @staticmethod
    def _migrer_1_5_vers_2_0(donnees):
        """Migration spécifique 1.5 → 2.0"""
        print("  Restructuration des statistiques")

        if 'joueur' in donnees:
            # Ajouter nouvelles statistiques
            if not hasattr(donnees['joueur'], 'statistiques'):
                donnees['joueur'].statistiques = {
                    'ennemis_vaincus': 0,
                    'quetes_terminees': 0,
                    'distance_parcourue': 0
                }

        donnees['version'] = '2.0'
        return donnees

class JoueurV2:
    """Version 2.0 de la classe Joueur avec nouvelles fonctionnalités"""

    def __init__(self, nom):
        self.nom = nom
        self.niveau = 1
        self.experience = 0
        self.vie = 100
        self.inventaire = []
        self.position = (0, 0)
        self.argent = 50
        self.derniere_connexion = datetime.now()
        self.statistiques = {
            'ennemis_vaincus': 0,
            'quetes_terminees': 0,
            'distance_parcourue': 0
        }

    def __str__(self):
        return f"{self.nom} v2.0 (Niv.{self.niveau}) - Ennemis vaincus: {self.statistiques['ennemis_vaincus']}"

def sauvegarder_avec_version(donnees, fichier, version=None):
    """Sauvegarde avec information de version"""
    if version is None:
        version = MigrateurDonnees.VERSION_ACTUELLE

    donnees_versionnees = {
        **donnees,
        'version': version,
        'date_sauvegarde': datetime.now(),
        'python_version': sys.version
    }

    with open(fichier, 'wb') as f:
        pickle.dump(donnees_versionnees, f, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"✅ Sauvegardé avec version {version}")

def charger_avec_migration(fichier):
    """Charge et migre automatiquement si nécessaire"""
    try:
        with open(fichier, 'rb') as f:
            donnees = pickle.load(f)

        # Migration automatique
        donnees = MigrateurDonnees.migrer_donnees(donnees)

        return donnees

    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")
        return None

# Démonstration de migration
def demo_migration():
    print("=== Démonstration - Migration de versions ===\n")

    # Simulation d'une ancienne sauvegarde (version 1.0)
    ancien_joueur = Joueur("Bob")  # Utilise l'ancienne classe
    ancien_joueur.objets = ["Épée", "Bouclier"]  # Ancien format

    anciennes_donnees = {
        'joueur': ancien_joueur,
        'temps_jeu': 50,
        'version': '1.0',
        'date_creation': datetime.now()
    }

    # Sauvegarde ancienne version
    with open('ancienne_version.pkl', 'wb') as f:
        pickle.dump(anciennes_donnees, f)

    print("Ancienne sauvegarde créée (version 1.0)")

    # Chargement avec migration
    print("\n--- Chargement avec migration ---")
    donnees_migrees = charger_avec_migration('ancienne_version.pkl')

    if donnees_migrees:
        print(f"Version finale: {donnees_migrees['version']}")
        joueur_migre = donnees_migrees['joueur']
        print(f"Joueur migré: {joueur_migre}")
        if hasattr(joueur_migre, 'inventaire'):
            print(f"Inventaire migré: {joueur_migre.inventaire}")
        if hasattr(joueur_migre, 'statistiques'):
            print(f"Nouvelles stats: {joueur_migre.statistiques}")

# Démonstration
demo_migration()
```

## Alternatives à pickle

### Comparaison avec d'autres formats

```python
import pickle
import json
import csv
import io
from datetime import datetime

class ComparateurFormats:
    """Compare pickle avec d'autres formats de sérialisation"""

    def __init__(self):
        self.donnees_test = {
            'nom': 'Alice',
            'age': 30,
            'scores': [85, 92, 78, 96],
            'preferences': {
                'couleur': 'bleu',
                'sport': 'natation'
            },
            'actif': True,
            'date_inscription': datetime.now()
        }

    def test_pickle(self):
        """Test avec pickle"""
        try:
            # Sérialisation
            donnees_serialisees = pickle.dumps(self.donnees_test)

            # Désérialisation
            donnees_restaurees = pickle.loads(donnees_serialisees)

            return {
                'format': 'Pickle',
                'taille': len(donnees_serialisees),
                'lisible': False,
                'types_preserves': self.donnees_test == donnees_restaurees,
                'portable': False,
                'securise': False,
                'donnees_restaurees': donnees_restaurees
            }
        except Exception as e:
            return {'format': 'Pickle', 'erreur': str(e)}

    def test_json(self):
        """Test avec JSON"""
        try:
            # Préparation des données (JSON ne supporte pas datetime)
            donnees_json = self.donnees_test.copy()
            donnees_json['date_inscription'] = donnees_json['date_inscription'].isoformat()

            # Sérialisation
            donnees_serialisees = json.dumps(donnees_json, ensure_ascii=False)

            # Désérialisation
            donnees_restaurees = json.loads(donnees_serialisees)

            return {
                'format': 'JSON',
                'taille': len(donnees_serialisees.encode('utf-8')),
                'lisible': True,
                'types_preserves': False,  # datetime devient string
                'portable': True,
                'securise': True,
                'donnees_restaurees': donnees_restaurees
            }
        except Exception as e:
            return {'format': 'JSON', 'erreur': str(e)}

    def test_csv(self):
        """Test avec CSV (structure aplatie)"""
        try:
            # Aplatissement des données pour CSV
            donnees_aplaties = {
                'nom': self.donnees_test['nom'],
                'age': self.donnees_test['age'],
                'score_1': self.donnees_test['scores'][0],
                'score_2': self.donnees_test['scores'][1],
                'score_3': self.donnees_test['scores'][2],
                'score_4': self.donnees_test['scores'][3],
                'couleur_pref': self.donnees_test['preferences']['couleur'],
                'sport_pref': self.donnees_test['preferences']['sport'],
                'actif': self.donnees_test['actif'],
                'date_inscription': self.donnees_test['date_inscription'].isoformat()
            }

            # Sérialisation en CSV
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=donnees_aplaties.keys())
            writer.writeheader()
            writer.writerow(donnees_aplaties)
            csv_content = output.getvalue()

            # Désérialisation
            input_stream = io.StringIO(csv_content)
            reader = csv.DictReader(input_stream)
            donnees_restaurees = next(reader)

            return {
                'format': 'CSV',
                'taille': len(csv_content.encode('utf-8')),
                'lisible': True,
                'types_preserves': False,  # Tout devient string
                'portable': True,
                'securise': True,
                'structure_preservee': False,  # Perte de la hiérarchie
                'donnees_restaurees': donnees_restaurees
            }
        except Exception as e:
            return {'format': 'CSV', 'erreur': str(e)}

    def comparer_tout(self):
        """Compare tous les formats"""
        print("=== Comparaison des formats de sérialisation ===\n")
        print("Données d'origine:")
        for cle, valeur in self.donnees_test.items():
            print(f"  {cle}: {valeur} ({type(valeur).__name__})")
        print()

        # Tests
        resultats = [
            self.test_pickle(),
            self.test_json(),
            self.test_csv()
        ]

        # Tableau comparatif
        print("| Format | Taille | Lisible | Types | Portable | Sécurisé |")
        print("|--------|--------|---------|-------|----------|----------|")

        for resultat in resultats:
            if 'erreur' not in resultat:
                format_nom = resultat['format']
                taille = f"{resultat['taille']} bytes"
                lisible = "✅" if resultat['lisible'] else "❌"
                types = "✅" if resultat['types_preserves'] else "❌"
                portable = "✅" if resultat['portable'] else "❌"
                securise = "✅" if resultat['securise'] else "❌"

                print(f"| {format_nom} | {taille} | {lisible} | {types} | {portable} | {securise} |")

        print("\n=== Recommandations d'usage ===")
        print("🥇 Pickle: Sérialisation Python native, objets complexes")
        print("🥈 JSON: Échange de données, APIs, configuration")
        print("🥉 CSV: Données tabulaires, export Excel, simplicité")

# Démonstration
comparateur = ComparateurFormats()
comparateur.comparer_tout()
```

## Exercices pratiques

### Exercice 1 : Gestionnaire de favoris

```python
import pickle
from datetime import datetime
from pathlib import Path

class GestionnaireFavoris:
    """Gestionnaire de favoris avec sérialisation pickle"""

    def __init__(self, fichier_favoris="favoris.pkl"):
        self.fichier_favoris = fichier_favoris
        self.favoris = self.charger_favoris()

    def charger_favoris(self):
        """Charge les favoris depuis le fichier"""
        if Path(self.fichier_favoris).exists():
            try:
                with open(self.fichier_favoris, 'rb') as f:
                    data = pickle.load(f)
                    # Migration si nécessaire (ancienne version = liste simple)
                    if isinstance(data, list):
                        return {
                            'sites': data,
                            'categories': {},
                            'version': '1.0'
                        }
                    return data
            except Exception as e:
                print(f"Erreur chargement favoris: {e}")
                return {'sites': [], 'categories': {}, 'version': '2.0'}
        return {'sites': [], 'categories': {}, 'version': '2.0'}

    def sauvegarder_favoris(self):
        """Sauvegarde les favoris"""
        try:
            with open(self.fichier_favoris, 'wb') as f:
                pickle.dump(self.favoris, f)
            print("✅ Favoris sauvegardés")
        except Exception as e:
            print(f"❌ Erreur sauvegarde: {e}")

    def ajouter_favori(self, nom, url, categorie="Général"):
        """Ajoute un favori"""
        favori = {
            'nom': nom,
            'url': url,
            'categorie': categorie,
            'date_ajout': datetime.now(),
            'visites': 0
        }

        self.favoris['sites'].append(favori)

        # Mettre à jour les catégories
        if categorie not in self.favoris['categories']:
            self.favoris['categories'][categorie] = []
        self.favoris['categories'][categorie].append(len(self.favoris['sites']) - 1)

        self.sauvegarder_favoris()
        print(f"✅ Favori ajouté: {nom}")

    def lister_favoris(self, categorie=None):
        """Liste les favoris"""
        if not self.favoris['sites']:
            print("Aucun favori enregistré")
            return

        sites_a_afficher = self.favoris['sites']

        if categorie:
            indices = self.favoris['categories'].get(categorie, [])
            sites_a_afficher = [self.favoris['sites'][i] for i in indices]
            print(f"=== Favoris - Catégorie: {categorie} ===")
        else:
            print("=== Tous les favoris ===")

        for i, site in enumerate(sites_a_afficher):
            print(f"{i+1}. {site['nom']}")
            print(f"   URL: {site['url']}")
            print(f"   Catégorie: {site['categorie']}")
            print(f"   Ajouté le: {site['date_ajout'].strftime('%Y-%m-%d %H:%M')}")
            print(f"   Visites: {site['visites']}")
            print()

    def rechercher_favori(self, terme):
        """Recherche dans les favoris"""
        resultats = []
        for site in self.favoris['sites']:
            if (terme.lower() in site['nom'].lower() or
                terme.lower() in site['url'].lower()):
                resultats.append(site)

        if resultats:
            print(f"=== Résultats pour '{terme}' ===")
            for site in resultats:
                print(f"- {site['nom']} ({site['url']})")
        else:
            print(f"Aucun résultat pour '{terme}'")

    def obtenir_statistiques(self):
        """Affiche les statistiques"""
        if not self.favoris['sites']:
            print("Aucune statistique disponible")
            return

        total_sites = len(self.favoris['sites'])
        total_visites = sum(site['visites'] for site in self.favoris['sites'])

        # Site le plus visité
        site_populaire = max(self.favoris['sites'], key=lambda x: x['visites'])

        # Catégories
        nb_categories = len(self.favoris['categories'])

        print("=== Statistiques des favoris ===")
        print(f"Total de sites: {total_sites}")
        print(f"Total de visites: {total_visites}")
        print(f"Nombre de catégories: {nb_categories}")
        print(f"Site le plus visité: {site_populaire['nom']} ({site_populaire['visites']} visites)")

        # Répartition par catégorie
        print("\nRépartition par catégorie:")
        for categorie, indices in self.favoris['categories'].items():
            print(f"  {categorie}: {len(indices)} sites")

# Interface simple pour tester
def demo_gestionnaire_favoris():
    print("=== Démonstration - Gestionnaire de favoris ===\n")

    gestionnaire = GestionnaireFavoris("demo_favoris.pkl")

    # Ajouter quelques favoris
    gestionnaire.ajouter_favori("Python.org", "https://python.org", "Programmation")
    gestionnaire.ajouter_favori("GitHub", "https://github.com", "Développement")
    gestionnaire.ajouter_favori("Stack Overflow", "https://stackoverflow.com", "Programmation")
    gestionnaire.ajouter_favori("Netflix", "https://netflix.com", "Divertissement")

    # Simuler quelques visites
    gestionnaire.favoris['sites'][0]['visites'] = 15
    gestionnaire.favoris['sites'][1]['visites'] = 8
    gestionnaire.favoris['sites'][2]['visites'] = 23
    gestionnaire.favoris['sites'][3]['visites'] = 5

    # Tests
    print("\n--- Liste complète ---")
    gestionnaire.lister_favoris()

    print("--- Catégorie Programmation ---")
    gestionnaire.lister_favoris("Programmation")

    print("--- Recherche 'python' ---")
    gestionnaire.rechercher_favori("python")

    print("--- Statistiques ---")
    gestionnaire.obtenir_statistiques()

# Lancement de la démo
demo_gestionnaire_favoris()
```

### Exercice 2 : Journal de bord avec pickle

```python
import pickle
from datetime import datetime, date
from enum import Enum

class TypeEntree(Enum):
    PERSONNEL = "personnel"
    TRAVAIL = "travail"
    PROJET = "projet"
    IDEE = "idée"

class EntreeJournal:
    def __init__(self, titre, contenu, type_entree=TypeEntree.PERSONNEL):
        self.id = None  # Sera défini par le journal
        self.titre = titre
        self.contenu = contenu
        self.type = type_entree
        self.date_creation = datetime.now()
        self.date_modification = datetime.now()
        self.tags = []
        self.favoris = False

    def modifier(self, nouveau_titre=None, nouveau_contenu=None):
        if nouveau_titre:
            self.titre = nouveau_titre
        if nouveau_contenu:
            self.contenu = nouveau_contenu
        self.date_modification = datetime.now()

    def ajouter_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
            self.date_modification = datetime.now()

    def __str__(self):
        return f"[{self.type.value.upper()}] {self.titre} ({self.date_creation.strftime('%Y-%m-%d')})"

class JournalBord:
    def __init__(self, fichier_journal="journal.pkl"):
        self.fichier_journal = fichier_journal
        self.entrees = []
        self.compteur_id = 1
        self.charger_journal()
    def charger_journal(self):
        """Charge le journal depuis le fichier"""
        try:
            with open(self.fichier_journal, 'rb') as f:
                data = pickle.load(f)
                self.entrees = data.get('entrees', [])
                self.compteur_id = data.get('compteur_id', 1)
                print(f"✅ Journal chargé: {len(self.entrees)} entrées")
        except FileNotFoundError:
            print("📖 Nouveau journal créé")
            self.entrees = []
            self.compteur_id = 1
        except Exception as e:
            print(f"❌ Erreur chargement journal: {e}")
            self.entrees = []
            self.compteur_id = 1

    def sauvegarder_journal(self):
        """Sauvegarde le journal"""
        try:
            data = {
                'entrees': self.entrees,
                'compteur_id': self.compteur_id,
                'date_sauvegarde': datetime.now(),
                'version': '1.0'
            }
            with open(self.fichier_journal, 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
            print("✅ Journal sauvegardé")
        except Exception as e:
            print(f"❌ Erreur sauvegarde: {e}")

    def ajouter_entree(self, titre, contenu, type_entree=TypeEntree.PERSONNEL, tags=None):
        """Ajoute une entrée au journal"""
        entree = EntreeJournal(titre, contenu, type_entree)
        entree.id = self.compteur_id
        self.compteur_id += 1

        if tags:
            entree.tags = tags.copy()

        self.entrees.append(entree)
        self.sauvegarder_journal()
        print(f"✅ Entrée ajoutée: '{titre}' (ID: {entree.id})")
        return entree.id

    def modifier_entree(self, id_entree, nouveau_titre=None, nouveau_contenu=None):
        """Modifie une entrée existante"""
        entree = self.trouver_entree(id_entree)
        if entree:
            entree.modifier(nouveau_titre, nouveau_contenu)
            self.sauvegarder_journal()
            print(f"✅ Entrée {id_entree} modifiée")
            return True
        return False

    def supprimer_entree(self, id_entree):
        """Supprime une entrée"""
        entree = self.trouver_entree(id_entree)
        if entree:
            self.entrees.remove(entree)
            self.sauvegarder_journal()
            print(f"✅ Entrée {id_entree} supprimée")
            return True
        print(f"❌ Entrée {id_entree} non trouvée")
        return False

    def trouver_entree(self, id_entree):
        """Trouve une entrée par son ID"""
        for entree in self.entrees:
            if entree.id == id_entree:
                return entree
        return None

    def lister_entrees(self, type_filtre=None, date_debut=None, date_fin=None):
        """Liste les entrées avec filtres optionnels"""
        entrees_filtrees = self.entrees.copy()

        # Filtre par type
        if type_filtre:
            entrees_filtrees = [e for e in entrees_filtrees if e.type == type_filtre]

        # Filtre par date
        if date_debut:
            entrees_filtrees = [e for e in entrees_filtrees if e.date_creation.date() >= date_debut]
        if date_fin:
            entrees_filtrees = [e for e in entrees_filtrees if e.date_creation.date() <= date_fin]

        # Tri par date (plus récent en premier)
        entrees_filtrees.sort(key=lambda x: x.date_creation, reverse=True)

        if not entrees_filtrees:
            print("Aucune entrée trouvée avec ces critères")
            return

        print(f"=== Journal ({len(entrees_filtrees)} entrées) ===")
        for entree in entrees_filtrees:
            etoile = "⭐" if entree.favoris else "  "
            tags_str = f" #{' #'.join(entree.tags)}" if entree.tags else ""
            print(f"{etoile} [{entree.id:2d}] {entree}{tags_str}")

            # Aperçu du contenu (50 premiers caractères)
            apercu = entree.contenu[:50] + "..." if len(entree.contenu) > 50 else entree.contenu
            print(f"      {apercu}")
            print()

    def rechercher(self, terme):
        """Recherche dans le titre, contenu et tags"""
        resultats = []
        terme_lower = terme.lower()

        for entree in self.entrees:
            if (terme_lower in entree.titre.lower() or
                terme_lower in entree.contenu.lower() or
                any(terme_lower in tag.lower() for tag in entree.tags)):
                resultats.append(entree)

        if resultats:
            print(f"=== Résultats pour '{terme}' ({len(resultats)} trouvé(s)) ===")
            for entree in resultats:
                print(f"[{entree.id}] {entree}")
                # Surbrillance du terme dans le contenu
                contenu_apercu = entree.contenu[:100]
                if terme_lower in contenu_apercu.lower():
                    print(f"    ...{contenu_apercu}...")
                print()
        else:
            print(f"Aucun résultat pour '{terme}'")

    def afficher_entree(self, id_entree):
        """Affiche une entrée complète"""
        entree = self.trouver_entree(id_entree)
        if not entree:
            print(f"❌ Entrée {id_entree} non trouvée")
            return

        print("=" * 60)
        print(f"ID: {entree.id} | Type: {entree.type.value.upper()}")
        print(f"Titre: {entree.titre}")
        print(f"Créé le: {entree.date_creation.strftime('%Y-%m-%d %H:%M:%S')}")
        if entree.date_modification != entree.date_creation:
            print(f"Modifié le: {entree.date_modification.strftime('%Y-%m-%d %H:%M:%S')}")
        if entree.tags:
            print(f"Tags: {', '.join(entree.tags)}")
        if entree.favoris:
            print("⭐ FAVORI")
        print("-" * 60)
        print(entree.contenu)
        print("=" * 60)

    def obtenir_statistiques(self):
        """Affiche les statistiques du journal"""
        if not self.entrees:
            print("Aucune statistique disponible")
            return

        # Statistiques générales
        total_entrees = len(self.entrees)
        total_mots = sum(len(e.contenu.split()) for e in self.entrees)
        favoris = sum(1 for e in self.entrees if e.favoris)

        # Par type
        stats_types = {}
        for entree in self.entrees:
            type_nom = entree.type.value
            if type_nom not in stats_types:
                stats_types[type_nom] = 0
            stats_types[type_nom] += 1

        # Tags les plus utilisés
        tous_tags = []
        for entree in self.entrees:
            tous_tags.extend(entree.tags)

        stats_tags = {}
        for tag in tous_tags:
            stats_tags[tag] = stats_tags.get(tag, 0) + 1

        # Activité par mois
        activite_mois = {}
        for entree in self.entrees:
            mois = entree.date_creation.strftime('%Y-%m')
            activite_mois[mois] = activite_mois.get(mois, 0) + 1

        # Affichage
        print("=== Statistiques du journal ===")
        print(f"Total d'entrées: {total_entrees}")
        print(f"Total de mots: {total_mots:,}")
        print(f"Moyenne mots/entrée: {total_mots/total_entrees:.1f}")
        print(f"Entrées favorites: {favoris}")

        print(f"\nRépartition par type:")
        for type_nom, count in sorted(stats_types.items()):
            pourcentage = (count / total_entrees) * 100
            print(f"  {type_nom.capitalize()}: {count} ({pourcentage:.1f}%)")

        if stats_tags:
            print(f"\nTags les plus utilisés:")
            tags_tries = sorted(stats_tags.items(), key=lambda x: x[1], reverse=True)
            for tag, count in tags_tries[:5]:
                print(f"  #{tag}: {count}")

        if len(activite_mois) > 1:
            print(f"\nActivité par mois:")
            for mois in sorted(activite_mois.keys()):
                print(f"  {mois}: {activite_mois[mois]} entrées")

    def exporter_texte(self, fichier_export="journal_export.txt"):
        """Exporte le journal en format texte"""
        try:
            with open(fichier_export, 'w', encoding='utf-8') as f:
                f.write("JOURNAL PERSONNEL\n")
                f.write("=" * 50 + "\n")
                f.write(f"Exporté le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total d'entrées: {len(self.entrees)}\n\n")

                # Tri par date
                entrees_triees = sorted(self.entrees, key=lambda x: x.date_creation)

                for entree in entrees_triees:
                    f.write(f"[{entree.id}] {entree.titre}\n")
                    f.write(f"Type: {entree.type.value} | Date: {entree.date_creation.strftime('%Y-%m-%d %H:%M')}\n")
                    if entree.tags:
                        f.write(f"Tags: {', '.join(entree.tags)}\n")
                    f.write("-" * 40 + "\n")
                    f.write(entree.contenu + "\n")
                    f.write("\n" + "=" * 50 + "\n\n")

            print(f"✅ Journal exporté vers {fichier_export}")
        except Exception as e:
            print(f"❌ Erreur lors de l'export: {e}")

# Interface de démonstration
def demo_journal():
    print("=== Démonstration - Journal de bord ===\n")

    journal = JournalBord("demo_journal.pkl")

    # Ajouter quelques entrées
    print("--- Ajout d'entrées ---")
    id1 = journal.ajouter_entree(
        "Première journée de formation Python",
        "Aujourd'hui j'ai commencé ma formation Python. J'ai appris les bases de la syntaxe et les types de données. C'est passionnant !",
        TypeEntree.PERSONNEL,
        ["python", "formation", "apprentissage"]
    )

    id2 = journal.ajouter_entree(
        "Réunion projet X",
        "Réunion avec l'équipe pour définir les spécifications du projet X. Nous avons décidé d'utiliser Python et PostgreSQL.",
        TypeEntree.TRAVAIL,
        ["projet", "reunion", "specifications"]
    )

    id3 = journal.ajouter_entree(
        "Idée d'application mobile",
        "Idée: créer une app pour suivre ses habitudes quotidiennes avec des graphiques et des statistiques motivantes.",
        TypeEntree.IDEE,
        ["app", "mobile", "habitudes"]
    )

    # Marquer une entrée comme favorie
    entree1 = journal.trouver_entree(id1)
    entree1.favoris = True
    journal.sauvegarder_journal()

    print("\n--- Liste complète ---")
    journal.lister_entrees()

    print("--- Entrées de type TRAVAIL ---")
    journal.lister_entrees(type_filtre=TypeEntree.TRAVAIL)

    print("--- Recherche 'python' ---")
    journal.rechercher("python")

    print("--- Affichage détaillé de l'entrée 1 ---")
    journal.afficher_entree(id1)

    print("--- Modification d'une entrée ---")
    journal.modifier_entree(id2, nouveau_contenu="Réunion très productive! Nous avons validé l'architecture technique.")

    print("--- Statistiques ---")
    journal.obtenir_statistiques()

    print("--- Export en texte ---")
    journal.exporter_texte("mon_journal.txt")

# Lancement de la démo
demo_journal()

## Résumé du module

Dans cette section sur la sérialisation avec pickle, vous avez appris :

### Concepts fondamentaux
- **Sérialisation** : Conversion d'objets Python en bytes
- **Désérialisation** : Restauration d'objets depuis les bytes
- **Protocoles pickle** : Différentes versions du format

### Fonctions principales
- `pickle.dump()` et `pickle.load()` : Fichiers
- `pickle.dumps()` et `pickle.loads()` : Bytes en mémoire
- Gestion des protocoles pour l'optimisation

### Types supportés
- Types simples (int, str, float, bool)
- Collections (list, dict, tuple, set)
- Objets datetime et regex
- Classes personnalisées
- Structures imbriquées complexes

### Avantages et limitations

**✅ Avantages :**
- Préservation exacte des types Python
- Support des objets complexes
- Performance optimisée
- Interface simple

**❌ Limitations :**
- Spécifique à Python
- Problèmes de sécurité potentiels
- Non lisible par l'homme
- Dépendance aux versions

### Cas d'usage typiques
- **Cache d'applications** : Stockage temporaire de résultats
- **Sauvegarde d'état** : Jeux, applications complexes
- **Sérialisation d'objets** : Classes personnalisées
- **Transfer entre processus** : Multiprocessing Python

### Bonnes pratiques apprises
1. **Toujours gérer les erreurs** lors de la désérialisation
2. **Utiliser le protocole le plus récent** pour les performances
3. **Implémenter `__getstate__` et `__setstate__`** pour contrôler la sérialisation
4. **Valider les données** avant utilisation
5. **Prévoir la migration** entre versions
6. **Ne jamais désérialiser** des données non fiables
7. **Compresser les gros fichiers** (gzip, bz2)

### Sécurité
- Pickle peut exécuter du code arbitraire
- Utiliser uniquement avec des sources fiables
- Implémenter un `SecureUnpickler` si nécessaire
- Préférer JSON pour l'échange de données

### Alternatives selon le contexte
- **JSON** : Échange web, configuration, lisibilité
- **CSV** : Données tabulaires, Excel
- **XML** : Documents structurés, standards
- **SQLite** : Données relationnelles persistantes

La prochaine section abordera la gestion moderne des chemins avec le module `pathlib`, complétant ainsi vos compétences en manipulation de fichiers et données.

⏭️
