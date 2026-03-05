🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.3 Patterns de conception courants

## Introduction

Imaginez que vous construisez une maison. Vous n'inventez pas la façon de faire une porte, une fenêtre ou un escalier à chaque fois. Vous utilisez des **modèles éprouvés** qui ont fait leurs preuves.

En programmation, c'est pareil ! Les **design patterns** (ou patterns de conception) sont des solutions réutilisables à des problèmes courants que rencontrent les développeurs. Ce sont des "recettes" ou des "modèles" qui ont été testés et améliorés au fil du temps.

### Pourquoi apprendre les patterns de conception ?

✅ **Résoudre des problèmes récurrents** : ne réinventez pas la roue

✅ **Code plus maintenable** : structure claire et prévisible

✅ **Communication efficace** : langage commun entre développeurs

✅ **Meilleures pratiques** : bénéficiez de l'expérience collective

✅ **Code flexible** : plus facile à modifier et étendre

### Les trois catégories de patterns

Les design patterns sont généralement classés en trois catégories :

1. **Patterns de création** : comment créer des objets de manière flexible
2. **Patterns structurels** : comment organiser et composer des objets
3. **Patterns comportementaux** : comment les objets communiquent entre eux

---

## Pattern 1 : Singleton (Création)

### Problème

Vous voulez qu'une classe n'ait **qu'une seule instance** dans toute votre application. Par exemple :
- Une connexion à la base de données
- Un gestionnaire de configuration
- Un système de logs

### Solution classique

```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialisation de la connexion
            cls._instance.connection = "Connexion à la base de données"
        return cls._instance

# Utilisation
db1 = DatabaseConnection()  
db2 = DatabaseConnection()  

print(db1 is db2)  # True - c'est la même instance !  
print(id(db1) == id(db2))  # True - même adresse mémoire  
```

### Solution Pythonique (avec décorateur)

```python
def singleton(cls):
    """Décorateur qui transforme une classe en Singleton"""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Configuration:
    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key)

# Utilisation
config1 = Configuration()  
config1.set("database", "postgresql")  

config2 = Configuration()  
print(config2.get("database"))  # "postgresql" - même instance !  
```

### Quand utiliser le Singleton ?

✅ **Gestionnaire de configuration** : une seule configuration pour toute l'app

✅ **Connexion à la base de données** : pool de connexions unique

✅ **Logger** : un seul système de logs

❌ **Évitez** : dans les tests (difficile à mocker) et si vous avez besoin de plusieurs instances

### Exemple pratique

```python
@singleton
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def get_logs(self):
        return self.logs

# Dans différentes parties de l'application
logger = Logger()  
logger.log("Application démarrée")  

# Plus tard, dans un autre fichier
logger = Logger()  # Même instance !  
logger.log("Traitement des données")  
print(logger.get_logs())  # Contient les deux logs  
```

---

## Pattern 2 : Factory (Création)

### Problème

Vous voulez créer des objets sans spécifier exactement leur classe. Utile quand :
- Vous avez plusieurs types d'objets similaires
- La création d'objets est complexe
- Vous voulez centraliser la logique de création

### Solution

```python
from abc import ABC, abstractmethod

# Classes de base
class Animal(ABC):
    @abstractmethod
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Wouf wouf!"

class Chat(Animal):
    def parler(self):
        return "Miaou!"

class Vache(Animal):
    def parler(self):
        return "Meuh!"

# Factory
class AnimalFactory:
    @staticmethod
    def creer_animal(type_animal: str) -> Animal:
        """Crée un animal en fonction du type demandé"""
        animaux = {
            "chien": Chien,
            "chat": Chat,
            "vache": Vache
        }

        classe_animal = animaux.get(type_animal.lower())
        if classe_animal is None:
            raise ValueError(f"Type d'animal inconnu : {type_animal}")

        return classe_animal()

# Utilisation
factory = AnimalFactory()

animal1 = factory.creer_animal("chien")  
print(animal1.parler())  # "Wouf wouf!"  

animal2 = factory.creer_animal("chat")  
print(animal2.parler())  # "Miaou!"  

# Facile d'ajouter de nouveaux types sans modifier le code existant
```

### Exemple pratique : Export de documents

```python
from abc import ABC, abstractmethod

class DocumentExporter(ABC):
    @abstractmethod
    def export(self, data: dict) -> str:
        pass

class PDFExporter(DocumentExporter):
    def export(self, data: dict) -> str:
        return f"Export PDF : {data}"

class ExcelExporter(DocumentExporter):
    def export(self, data: dict) -> str:
        return f"Export Excel : {data}"

class CSVExporter(DocumentExporter):
    def export(self, data: dict) -> str:
        return f"Export CSV : {data}"

class ExporterFactory:
    @staticmethod
    def get_exporter(format: str) -> DocumentExporter:
        exporters = {
            "pdf": PDFExporter,
            "excel": ExcelExporter,
            "csv": CSVExporter
        }

        exporter_class = exporters.get(format.lower())
        if not exporter_class:
            raise ValueError(f"Format non supporté : {format}")

        return exporter_class()

# Utilisation
data = {"nom": "Rapport", "date": "2024-01-15"}

# L'utilisateur choisit le format
format_choisi = "pdf"  # Pourrait venir d'une interface utilisateur

exporter = ExporterFactory.get_exporter(format_choisi)  
resultat = exporter.export(data)  
print(resultat)  
```

### Quand utiliser Factory ?

✅ **Multiples types similaires** : différents formats d'export, types de paiement, etc.

✅ **Logique de création complexe** : beaucoup de paramètres ou conditions

✅ **Extensibilité** : facile d'ajouter de nouveaux types

---

## Pattern 3 : Builder (Création)

### Problème

Vous voulez construire des objets complexes **étape par étape**, surtout quand il y a beaucoup de paramètres optionnels.

### Solution

```python
class Pizza:
    def __init__(self):
        self.taille = None
        self.fromage = False
        self.pepperoni = False
        self.champignons = False
        self.olives = False

    def __str__(self):
        ingredients = []
        if self.fromage:
            ingredients.append("fromage")
        if self.pepperoni:
            ingredients.append("pepperoni")
        if self.champignons:
            ingredients.append("champignons")
        if self.olives:
            ingredients.append("olives")

        return f"Pizza {self.taille} avec {', '.join(ingredients)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_taille(self, taille: str):
        self.pizza.taille = taille
        return self  # Retourne self pour chaîner les méthodes

    def ajouter_fromage(self):
        self.pizza.fromage = True
        return self

    def ajouter_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def ajouter_champignons(self):
        self.pizza.champignons = True
        return self

    def ajouter_olives(self):
        self.pizza.olives = True
        return self

    def build(self) -> Pizza:
        return self.pizza

# Utilisation - syntaxe fluide (method chaining)
pizza = (PizzaBuilder()
         .set_taille("grande")
         .ajouter_fromage()
         .ajouter_pepperoni()
         .ajouter_champignons()
         .build())

print(pizza)  # Pizza grande avec fromage, pepperoni, champignons
```

### Exemple pratique : Constructeur de requêtes SQL

```python
class SQLQuery:
    def __init__(self):
        self.select_fields = []
        self.from_table = None
        self.where_conditions = []
        self.order_by_field = None
        self.limit_value = None

    def to_sql(self) -> str:
        """Génère la requête SQL"""
        query_parts = []

        # SELECT
        fields = ", ".join(self.select_fields) if self.select_fields else "*"
        query_parts.append(f"SELECT {fields}")

        # FROM
        if self.from_table:
            query_parts.append(f"FROM {self.from_table}")

        # WHERE
        if self.where_conditions:
            conditions = " AND ".join(self.where_conditions)
            query_parts.append(f"WHERE {conditions}")

        # ORDER BY
        if self.order_by_field:
            query_parts.append(f"ORDER BY {self.order_by_field}")

        # LIMIT
        if self.limit_value:
            query_parts.append(f"LIMIT {self.limit_value}")

        return " ".join(query_parts)

class QueryBuilder:
    def __init__(self):
        self.query = SQLQuery()

    def select(self, *fields):
        self.query.select_fields = list(fields)
        return self

    def from_table(self, table: str):
        self.query.from_table = table
        return self

    def where(self, condition: str):
        self.query.where_conditions.append(condition)
        return self

    def order_by(self, field: str):
        self.query.order_by_field = field
        return self

    def limit(self, value: int):
        self.query.limit_value = value
        return self

    def build(self) -> str:
        return self.query.to_sql()

# Utilisation
query = (QueryBuilder()
         .select("nom", "email", "age")
         .from_table("users")
         .where("age > 18")
         .where("pays = 'France'")
         .order_by("nom")
         .limit(10)
         .build())

print(query)
# SELECT nom, email, age FROM users WHERE age > 18 AND pays = 'France' ORDER BY nom LIMIT 10
```

### Quand utiliser Builder ?

✅ **Objets avec beaucoup de paramètres** : évite les constructeurs avec 10+ paramètres

✅ **Construction étape par étape** : l'ordre de construction importe

✅ **Lisibilité** : le code est plus clair et auto-documenté

---

## Pattern 4 : Observer (Comportemental)

### Problème

Vous voulez qu'un objet **notifie automatiquement** d'autres objets quand son état change. C'est le pattern utilisé dans les systèmes d'événements.

### Solution

```python
from abc import ABC, abstractmethod

# Interface pour les observateurs
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Sujet observable
class Subject:
    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        """Ajoute un observateur"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """Retire un observateur"""
        self._observers.remove(observer)

    def notify(self, message: str):
        """Notifie tous les observateurs"""
        for observer in self._observers:
            observer.update(message)

# Observateurs concrets
class EmailNotifier(Observer):
    def update(self, message: str):
        print(f"📧 Email envoyé : {message}")

class SMSNotifier(Observer):
    def update(self, message: str):
        print(f"📱 SMS envoyé : {message}")

class PushNotifier(Observer):
    def update(self, message: str):
        print(f"🔔 Notification push : {message}")

# Utilisation
commande = Subject()

# Attacher des observateurs
commande.attach(EmailNotifier())  
commande.attach(SMSNotifier())  
commande.attach(PushNotifier())  

# Quand quelque chose se passe, tout le monde est notifié
commande.notify("Votre commande a été expédiée !")
# 📧 Email envoyé : Votre commande a été expédiée !
# 📱 SMS envoyé : Votre commande a été expédiée !
# 🔔 Notification push : Votre commande a été expédiée !
```

### Exemple pratique : Système de blog

```python
class BlogPost(Subject):
    def __init__(self, titre: str):
        super().__init__()
        self.titre = titre
        self.contenu = ""

    def publier(self, contenu: str):
        self.contenu = contenu
        self.notify(f"Nouvel article publié : {self.titre}")

    def modifier(self, nouveau_contenu: str):
        self.contenu = nouveau_contenu
        self.notify(f"Article modifié : {self.titre}")

class Abonne(Observer):
    def __init__(self, nom: str):
        self.nom = nom

    def update(self, message: str):
        print(f"{self.nom} a reçu : {message}")

# Utilisation
article = BlogPost("Introduction à Python")

# Des abonnés s'inscrivent
alice = Abonne("Alice")  
bob = Abonne("Bob")  
charlie = Abonne("Charlie")  

article.attach(alice)  
article.attach(bob)  
article.attach(charlie)  

# Publier l'article
article.publier("Python est un langage génial...")
# Alice a reçu : Nouvel article publié : Introduction à Python
# Bob a reçu : Nouvel article publié : Introduction à Python
# Charlie a reçu : Nouvel article publié : Introduction à Python

# Bob se désabonne
article.detach(bob)

# Modifier l'article
article.modifier("Python est vraiment génial!")
# Alice a reçu : Article modifié : Introduction à Python
# Charlie a reçu : Article modifié : Introduction à Python
```

### Quand utiliser Observer ?

✅ **Systèmes de notifications** : alertes, emails, push

✅ **Interface utilisateur** : mise à jour de l'affichage quand les données changent

✅ **Événements** : systèmes événementiels (event-driven)

---

## Pattern 5 : Strategy (Comportemental)

### Problème

Vous avez plusieurs façons de faire la même chose (algorithmes différents) et vous voulez pouvoir **changer facilement** entre ces méthodes.

### Solution

```python
from abc import ABC, abstractmethod

# Stratégies de paiement
class PaymentStrategy(ABC):
    @abstractmethod
    def payer(self, montant: float) -> str:
        pass

class CarteBancaire(PaymentStrategy):
    def __init__(self, numero: str):
        self.numero = numero

    def payer(self, montant: float) -> str:
        return f"Paiement de {montant}€ par carte {self.numero[-4:]}"

class PayPal(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def payer(self, montant: float) -> str:
        return f"Paiement de {montant}€ via PayPal ({self.email})"

class Crypto(PaymentStrategy):
    def __init__(self, wallet: str):
        self.wallet = wallet

    def payer(self, montant: float) -> str:
        return f"Paiement de {montant}€ en crypto (wallet: {self.wallet})"

# Contexte qui utilise une stratégie
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def ajouter_item(self, item: str, prix: float):
        self.items.append({"item": item, "prix": prix})

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def checkout(self):
        total = round(sum(item["prix"] for item in self.items), 2)

        if self.payment_strategy is None:
            return "Veuillez choisir un moyen de paiement"

        return self.payment_strategy.payer(total)

# Utilisation
cart = ShoppingCart()  
cart.ajouter_item("Livre Python", 29.99)  
cart.ajouter_item("Clavier", 79.99)  

# Choisir la stratégie de paiement
cart.set_payment_strategy(CarteBancaire("1234-5678-9012-3456"))  
print(cart.checkout())  # Paiement de 109.98€ par carte 3456  

# Changer de stratégie
cart.set_payment_strategy(PayPal("user@example.com"))  
print(cart.checkout())  # Paiement de 109.98€ via PayPal (user@example.com)  
```

### Exemple pratique : Compression de fichiers

```python
class CompressionStrategy(ABC):
    @abstractmethod
    def compresser(self, data: str) -> str:
        pass

class ZipCompression(CompressionStrategy):
    def compresser(self, data: str) -> str:
        return f"[ZIP] {data[:20]}... (compressé)"

class RarCompression(CompressionStrategy):
    def compresser(self, data: str) -> str:
        return f"[RAR] {data[:20]}... (compressé)"

class GzipCompression(CompressionStrategy):
    def compresser(self, data: str) -> str:
        return f"[GZIP] {data[:20]}... (compressé)"

class FileCompressor:
    def __init__(self, strategy: CompressionStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CompressionStrategy):
        self.strategy = strategy

    def compress_file(self, filename: str, data: str):
        compressed = self.strategy.compresser(data)
        print(f"Fichier {filename} : {compressed}")

# Utilisation
data = "Beaucoup de données à compresser..." * 100

compressor = FileCompressor(ZipCompression())  
compressor.compress_file("document.txt", data)  

# Changer de stratégie à la volée
compressor.set_strategy(GzipCompression())  
compressor.compress_file("image.jpg", data)  
```

### Quand utiliser Strategy ?

✅ **Algorithmes interchangeables** : tri, recherche, compression, etc.

✅ **Éviter les if/else multiples** : remplace les longues chaînes de conditions

✅ **Open/Closed Principle** : facile d'ajouter de nouvelles stratégies

---

## Pattern 6 : Decorator (Structurel)

### Problème

Vous voulez **ajouter des fonctionnalités** à un objet dynamiquement, sans modifier sa classe.

### Solution avec classe

```python
from abc import ABC, abstractmethod

# Interface de base
class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Café de base
class SimpleCoffee(Coffee):
    def get_description(self) -> str:
        return "Café simple"

    def get_cost(self) -> float:
        return 2.0

# Décorateur de base
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_description(self) -> str:
        return self._coffee.get_description()

    def get_cost(self) -> float:
        return self._coffee.get_cost()

# Décorateurs concrets
class MilkDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, lait"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.5

class SugarDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, sucre"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.2

class WhippedCreamDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, chantilly"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.7

# Utilisation - on peut empiler les décorateurs !
coffee = SimpleCoffee()  
print(f"{coffee.get_description()}: {coffee.get_cost()}€")  
# Café simple: 2.0€

coffee = MilkDecorator(coffee)  
print(f"{coffee.get_description()}: {coffee.get_cost()}€")  
# Café simple, lait: 2.5€

coffee = SugarDecorator(coffee)  
print(f"{coffee.get_description()}: {coffee.get_cost()}€")  
# Café simple, lait, sucre: 2.7€

coffee = WhippedCreamDecorator(coffee)  
print(f"{coffee.get_description()}: {coffee.get_cost()}€")  
# Café simple, lait, sucre, chantilly: 3.4€

# Ou en une seule ligne
coffee_deluxe = WhippedCreamDecorator(
    SugarDecorator(
        MilkDecorator(
            SimpleCoffee()
        )
    )
)
```

### Solution Pythonique avec décorateurs de fonctions

Python a un support natif pour les décorateurs, ce qui rend le pattern encore plus simple :

```python
import time  
from functools import wraps  

def timer(func):
    """Décorateur qui mesure le temps d'exécution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} a pris {end - start:.4f} secondes")
        return result
    return wrapper

def logger(func):
    """Décorateur qui log les appels de fonction"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} a retourné {result}")
        return result
    return wrapper

def validator(func):
    """Décorateur qui valide les paramètres"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("Tous les arguments doivent être des nombres")
        return func(*args, **kwargs)
    return wrapper

# Utilisation - on empile les décorateurs
@timer
@logger
@validator
def calculer_moyenne(a, b, c):
    """Calcule la moyenne de trois nombres"""
    return (a + b + c) / 3

# Test
resultat = calculer_moyenne(10, 20, 30)
# Appel de calculer_moyenne avec args=(10, 20, 30), kwargs={}
# calculer_moyenne a retourné 20.0
# calculer_moyenne a pris 0.0001 secondes
```

### Exemple pratique : Gestion des permissions

```python
from functools import wraps

def requires_authentication(func):
    """Vérifie que l'utilisateur est authentifié"""
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise PermissionError("Utilisateur non authentifié")
        return func(user, *args, **kwargs)
    return wrapper

def requires_admin(func):
    """Vérifie que l'utilisateur est admin"""
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            raise PermissionError("Droits admin requis")
        return func(user, *args, **kwargs)
    return wrapper

def log_action(func):
    """Log l'action effectuée"""
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        print(f"Action {func.__name__} par {user.get('name', 'Inconnu')}")
        return func(user, *args, **kwargs)
    return wrapper

# Application des décorateurs
@log_action
@requires_authentication
@requires_admin
def supprimer_utilisateur(user, user_id):
    print(f"Suppression de l'utilisateur {user_id}")
    return True

# Test avec utilisateur admin
admin_user = {
    "name": "Alice",
    "is_authenticated": True,
    "is_admin": True
}
supprimer_utilisateur(admin_user, 123)
# Action supprimer_utilisateur par Alice
# Suppression de l'utilisateur 123

# Test avec utilisateur normal (erreur)
normal_user = {
    "name": "Bob",
    "is_authenticated": True,
    "is_admin": False
}
try:
    supprimer_utilisateur(normal_user, 123)
except PermissionError as e:
    print(f"Erreur : {e}")
    # Erreur : Droits admin requis
```

### Quand utiliser Decorator ?

✅ **Ajouter des fonctionnalités** : logging, timing, caching, validation

✅ **Éviter la modification** : ajouter du comportement sans modifier le code original

✅ **Réutilisabilité** : mêmes décorateurs pour plusieurs fonctions/classes

---

## Pattern 7 : Iterator (Comportemental)

### Problème

Vous voulez parcourir une collection d'éléments sans exposer sa structure interne.

### Solution

Python a un support natif pour les itérateurs via le protocole d'itération :

```python
class Playlist:
    def __init__(self, nom: str):
        self.nom = nom
        self.chansons = []

    def ajouter_chanson(self, chanson: str):
        self.chansons.append(chanson)

    def __iter__(self):
        """Retourne un itérateur"""
        return iter(self.chansons)

# Utilisation
playlist = Playlist("Ma playlist")  
playlist.ajouter_chanson("Song 1")  
playlist.ajouter_chanson("Song 2")  
playlist.ajouter_chanson("Song 3")  

# On peut itérer directement !
for chanson in playlist:
    print(f"♪ {chanson}")
```

### Itérateur personnalisé

```python
class CountDown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        self.current -= 1
        return self.current + 1

# Utilisation
countdown = CountDown(5)  
for num in countdown:  
    print(num)
# 5
# 4
# 3
# 2
# 1
```

### Exemple pratique : Pagination

```python
class Paginator:
    def __init__(self, items: list, page_size: int = 10):
        self.items = items
        self.page_size = page_size
        self.num_pages = (len(items) + page_size - 1) // page_size

    def __iter__(self):
        self.current_page = 0
        return self

    def __next__(self):
        if self.current_page >= self.num_pages:
            raise StopIteration

        start = self.current_page * self.page_size
        end = start + self.page_size
        page = self.items[start:end]

        self.current_page += 1
        return page

# Utilisation
data = list(range(1, 26))  # 25 éléments  
paginator = Paginator(data, page_size=10)  

for page_num, page in enumerate(paginator, 1):
    print(f"Page {page_num}: {page}")
# Page 1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Page 2: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Page 3: [21, 22, 23, 24, 25]
```

### Générateurs : la façon Pythonique

Python offre les **générateurs** qui simplifient grandement la création d'itérateurs :

```python
def countdown(start: int):
    """Générateur de compte à rebours"""
    while start > 0:
        yield start
        start -= 1

# Utilisation identique
for num in countdown(5):
    print(num)

# Générateur avec pagination
def paginate(items: list, page_size: int = 10):
    """Génère des pages"""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

# Utilisation
for page in paginate(list(range(1, 26)), page_size=10):
    print(page)
```

### Quand utiliser Iterator ?

✅ **Collections personnalisées** : parcourir vos structures de données

✅ **Lazy loading** : générer des éléments à la demande (économie mémoire)

✅ **Flux infinis** : générer des données infinies (séquences mathématiques)

---

## Pattern 8 : Adapter (Structurel)

### Problème

Vous voulez utiliser une classe dont l'interface ne correspond pas à ce dont vous avez besoin. L'adapter permet de "traduire" une interface en une autre.

### Solution

```python
# Interface attendue par notre application
class MediaPlayer:
    def play(self, filename: str):
        pass

# Classe existante avec une interface différente
class MP3Player:
    def play_mp3(self, filename: str):
        print(f"Lecture MP3 : {filename}")

class MP4Player:
    def play_mp4(self, filename: str):
        print(f"Lecture MP4 : {filename}")

# Adapters pour rendre compatibles les interfaces
class MP3Adapter(MediaPlayer):
    def __init__(self):
        self.mp3_player = MP3Player()

    def play(self, filename: str):
        if filename.endswith('.mp3'):
            self.mp3_player.play_mp3(filename)

class MP4Adapter(MediaPlayer):
    def __init__(self):
        self.mp4_player = MP4Player()

    def play(self, filename: str):
        if filename.endswith('.mp4'):
            self.mp4_player.play_mp4(filename)

# Utilisation uniforme
def lire_media(player: MediaPlayer, filename: str):
    player.play(filename)

# Maintenant tout utilise la même interface
lire_media(MP3Adapter(), "musique.mp3")  
lire_media(MP4Adapter(), "video.mp4")  
```

### Exemple pratique : API externes

```python
# Notre interface standard pour la météo
class WeatherService:
    def get_temperature(self, city: str) -> float:
        pass

# API externe 1 (format différent)
class OpenWeatherAPI:
    def fetch_weather_data(self, location: str) -> dict:
        # Simule un appel API
        return {
            "location": location,
            "temp_kelvin": 293.15,  # Température en Kelvin
            "humidity": 65
        }

# API externe 2 (autre format)
class WeatherDotComAPI:
    def get_current_weather(self, place: str) -> dict:
        # Simule un autre appel API
        return {
            "place": place,
            "temperature_fahrenheit": 68,  # Température en Fahrenheit
            "conditions": "Sunny"
        }

# Adapters pour uniformiser
class OpenWeatherAdapter(WeatherService):
    def __init__(self):
        self.api = OpenWeatherAPI()

    def get_temperature(self, city: str) -> float:
        data = self.api.fetch_weather_data(city)
        # Convertir Kelvin en Celsius
        return round(data["temp_kelvin"] - 273.15, 1)

class WeatherDotComAdapter(WeatherService):
    def __init__(self):
        self.api = WeatherDotComAPI()

    def get_temperature(self, city: str) -> float:
        data = self.api.get_current_weather(city)
        # Convertir Fahrenheit en Celsius
        return round((data["temperature_fahrenheit"] - 32) * 5/9, 1)

# Utilisation uniforme dans notre application
def afficher_meteo(service: WeatherService, ville: str):
    temp = service.get_temperature(ville)
    print(f"Température à {ville} : {temp}°C")

# Peu importe l'API, l'interface est la même
afficher_meteo(OpenWeatherAdapter(), "Paris")  
afficher_meteo(WeatherDotComAdapter(), "Paris")  
```

### Quand utiliser Adapter ?

✅ **Intégration d'APIs externes** : uniformiser différentes APIs

✅ **Code legacy** : adapter ancien code sans le modifier

✅ **Bibliothèques tierces** : rendre compatible avec votre interface

---

## Pattern 9 : Repository (Structurel)

### Problème

Vous voulez **séparer la logique métier** de la logique d'accès aux données. Le Repository fait office d'intermédiaire entre votre application et la base de données.

### Solution

```python
from abc import ABC, abstractmethod

# Modèle de données
class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Interface du Repository
class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def find_all(self) -> list[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass

# Implémentation en mémoire (pour les tests)
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users = {}
        self._next_id = 1

    def find_by_id(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def find_all(self) -> list[User]:
        return list(self._users.values())

    def save(self, user: User) -> User:
        if user.id is None:
            user.id = self._next_id
            self._next_id += 1
        self._users[user.id] = user
        return user

    def delete(self, user_id: int) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False

# Implémentation avec base de données (simulée)
class DatabaseUserRepository(UserRepository):
    def __init__(self, connection):
        self.connection = connection

    def find_by_id(self, user_id: int) -> User | None:
        # Simuler une requête SQL
        query = f"SELECT * FROM users WHERE id = {user_id}"
        # result = self.connection.execute(query)
        print(f"SQL: {query}")
        return None  # Simulation

    def find_all(self) -> list[User]:
        query = "SELECT * FROM users"
        print(f"SQL: {query}")
        return []

    def save(self, user: User) -> User:
        if user.id:
            query = f"UPDATE users SET name='{user.name}', email='{user.email}' WHERE id={user.id}"
        else:
            query = f"INSERT INTO users (name, email) VALUES ('{user.name}', '{user.email}')"
        print(f"SQL: {query}")
        return user

    def delete(self, user_id: int) -> bool:
        query = f"DELETE FROM users WHERE id = {user_id}"
        print(f"SQL: {query}")
        return True

# Service métier (ne connaît pas les détails d'implémentation)
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register_user(self, name: str, email: str) -> User:
        user = User(id=None, name=name, email=email)
        return self.repository.save(user)

    def get_user(self, user_id: int) -> User | None:
        return self.repository.find_by_id(user_id)

    def list_users(self) -> list[User]:
        return self.repository.find_all()

# Utilisation - on peut changer facilement d'implémentation
repository = InMemoryUserRepository()
# repository = DatabaseUserRepository(connection)  # Même interface !

service = UserService(repository)

# Créer des utilisateurs
user1 = service.register_user("Alice", "alice@example.com")  
user2 = service.register_user("Bob", "bob@example.com")  

# Lister les utilisateurs
for user in service.list_users():
    print(user)
```

### Avantages du pattern Repository

✅ **Séparation des responsabilités** : logique métier ≠ accès aux données

✅ **Testabilité** : facile de mocker le repository pour les tests

✅ **Flexibilité** : changer de base de données sans modifier le code métier

✅ **Centralisation** : toutes les requêtes au même endroit

### Quand utiliser Repository ?

✅ **Applications avec base de données** : abstraire l'accès aux données

✅ **Tests unitaires** : faciliter le mocking

✅ **Architecture propre** : séparer les couches de l'application

---

## Pattern 10 : Context Manager (Pythonique)

### Problème

Vous voulez garantir qu'une ressource (fichier, connexion, etc.) est correctement **acquise et libérée**, même en cas d'erreur.

### Solution avec `__enter__` et `__exit__`

```python
class FileHandler:
    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Appelé au début du bloc with"""
        print(f"Ouverture de {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Appelé à la fin du bloc with (même en cas d'erreur)"""
        if self.file:
            print(f"Fermeture de {self.filename}")
            self.file.close()

        # Retourner False pour propager les exceptions
        # Retourner True pour supprimer les exceptions
        return False

# Utilisation
with FileHandler("test.txt", "w") as f:
    f.write("Hello World!")
# Ouverture de test.txt
# Fermeture de test.txt (automatique !)
```

### Solution avec `contextlib` (plus simple)

```python
from contextlib import contextmanager  
import time  

@contextmanager
def timer(name: str):
    """Context manager pour mesurer le temps d'exécution"""
    print(f"⏱️  Début de {name}")
    start = time.time()

    try:
        yield  # Le code du with s'exécute ici
    finally:
        end = time.time()
        print(f"⏱️  {name} terminé en {end - start:.4f}s")

# Utilisation
with timer("opération longue"):
    time.sleep(1)
    print("Traitement en cours...")
# ⏱️  Début de opération longue
# Traitement en cours...
# ⏱️  opération longue terminé en 1.0001s
```

### Exemple pratique : Gestion de connexion base de données

```python
from contextlib import contextmanager

class Database:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None

    def connect(self):
        print(f"Connexion à {self.connection_string}")
        # Simuler une connexion
        self.connection = f"Connection to {self.connection_string}"

    def disconnect(self):
        if self.connection:
            print("Déconnexion de la base de données")
            self.connection = None

    @contextmanager
    def transaction(self):
        """Context manager pour une transaction"""
        print("Début de la transaction")
        try:
            yield self.connection
            print("Commit de la transaction")
        except Exception as e:
            print(f"Rollback de la transaction : {e}")
            raise
        finally:
            print("Fin de la transaction")

# Utilisation
db = Database("postgresql://localhost/mydb")  
db.connect()  

with db.transaction() as conn:
    # Faire des opérations
    print("Insertion de données...")
    print("Mise à jour de données...")
    # Si une erreur survient, rollback automatique !

db.disconnect()
```

### Exemple pratique : Suppression temporaire de fichiers

```python
import os  
from contextlib import contextmanager  

@contextmanager
def temporary_file(filename: str):
    """Crée un fichier temporaire, puis le supprime"""
    print(f"Création du fichier temporaire {filename}")

    # Créer le fichier
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Contenu temporaire")

    try:
        yield filename  # Le fichier est disponible ici
    finally:
        # Nettoyage : supprimer le fichier
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Suppression du fichier {filename}")

# Utilisation
with temporary_file("temp.txt") as filename:
    print(f"Utilisation de {filename}")
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
# Le fichier est automatiquement supprimé après le with !
```

### Quand utiliser Context Manager ?

✅ **Gestion de ressources** : fichiers, connexions, verrous

✅ **Setup/Teardown** : actions avant/après (timing, logging)

✅ **Transactions** : garantir commit ou rollback

---

## Tableau récapitulatif des patterns

| Pattern | Catégorie | Utilité | Exemple d'usage |
|---------|-----------|---------|-----------------|
| **Singleton** | Création | Une seule instance | Configuration, Logger |
| **Factory** | Création | Créer objets sans spécifier classe | Export formats, Créer animaux |
| **Builder** | Création | Construction étape par étape | Requêtes SQL, Configuration complexe |
| **Observer** | Comportemental | Notification automatique | Système d'événements, Abonnements |
| **Strategy** | Comportemental | Algorithmes interchangeables | Paiement, Compression |
| **Decorator** | Structurel | Ajouter fonctionnalités dynamiquement | Logging, Validation, Permissions |
| **Iterator** | Comportemental | Parcourir collection | Pagination, Flux de données |
| **Adapter** | Structurel | Adapter interface | Intégration APIs externes |
| **Repository** | Structurel | Séparer logique métier/données | Accès base de données |
| **Context Manager** | Pythonique | Gestion ressources | Fichiers, Connexions, Transactions |

---

## Principes SOLID (bonus)

Les design patterns s'appuient souvent sur les principes SOLID :

### S - Single Responsibility Principle
**Une classe = une responsabilité**

```python
# ❌ Mauvais : trop de responsabilités
class User:
    def save_to_database(self):
        pass

    def send_email(self):
        pass

    def generate_report(self):
        pass

# ✅ Bon : séparation des responsabilités
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send(self, user, message):
        pass

class ReportGenerator:
    def generate(self, user):
        pass
```

### O - Open/Closed Principle
**Ouvert à l'extension, fermé à la modification**

```python
import math

# ✅ Bon : on peut ajouter de nouveaux types sans modifier le code existant
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Ajouter un nouveau type n'impacte pas le code existant
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```

### L - Liskov Substitution Principle
**Les sous-classes doivent être substituables à leurs classes parentes**

```python
# ✅ Bon : les sous-classes respectent le contrat de la classe parent
class Bird:
    def move(self):
        print("L'oiseau se déplace")

class Sparrow(Bird):
    def move(self):
        print("Le moineau vole")

class Penguin(Bird):
    def move(self):
        print("Le pingouin marche")  # Pas de vol, mais respecte le contrat "move"
```

### I - Interface Segregation Principle
**Beaucoup de petites interfaces plutôt qu'une grosse**

```python
# ✅ Bon : interfaces spécifiques
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Faxable(ABC):
    @abstractmethod
    def fax(self):
        pass

# Une imprimante simple n'implémente que ce dont elle a besoin
class SimplePrinter(Printable):
    def print(self):
        print("Impression...")

# Une imprimante multifonction implémente tout
class MultiFunctionPrinter(Printable, Scannable, Faxable):
    def print(self):
        print("Impression...")

    def scan(self):
        print("Scan...")

    def fax(self):
        print("Fax...")
```

### D - Dependency Inversion Principle
**Dépendre des abstractions, pas des implémentations concrètes**

```python
# ✅ Bon : dépend de l'abstraction
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class UserService:
    def __init__(self, database: Database):  # Dépend de l'abstraction
        self.database = database

    def create_user(self, user):
        self.database.save(user)

# Implémentations concrètes
class MySQLDatabase(Database):
    def save(self, data):
        print("Sauvegarde dans MySQL")

class MongoDBDatabase(Database):
    def save(self, data):
        print("Sauvegarde dans MongoDB")

# On peut facilement changer d'implémentation
service = UserService(MySQLDatabase())
# ou
service = UserService(MongoDBDatabase())
```

---

## Conseils pour bien utiliser les patterns

### 1. Ne sur-ingéniérisez pas

Les patterns sont des outils, pas des objectifs. N'utilisez un pattern que s'il résout réellement un problème.

```python
# ❌ Trop complexe pour un besoin simple
factory = AnimalFactory()  
builder = AnimalBuilder()  
animal = factory.create(builder.build("chat"))  

# ✅ Simple et suffisant
animal = Chat()
```

### 2. Commencez simple, refactorisez ensuite

Il vaut mieux commencer avec du code simple et ajouter des patterns quand le besoin apparaît.

### 3. Apprenez à reconnaître les problèmes

Avec l'expérience, vous reconnaîtrez les situations où un pattern est utile :
- Beaucoup de if/else → **Strategy** ou **Factory**
- Code dupliqué → **Decorator** ou **Template Method**
- Difficile à tester → **Repository** ou **Dependency Injection**

### 4. Privilégiez la clarté

Un pattern doit rendre le code **plus clair**, pas plus complexe. Si votre équipe ne comprend pas, c'est peut-être trop.

### 5. Python a ses propres patterns

Python offre des fonctionnalités natives qui remplacent certains patterns classiques :
- **Décorateurs** : pattern Decorator intégré
- **Context managers** : pattern Resource Management
- **Générateurs** : pattern Iterator simplifié
- **Duck typing** : moins besoin d'interfaces formelles

---

## Ressources pour aller plus loin

### Livres

- **"Design Patterns"** (Gang of Four) : le livre fondateur
- **"Head First Design Patterns"** : version illustrée et pédagogique
- **"Python Design Patterns"** : spécifique à Python

### Sites web

- **Refactoring Guru** : [refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)
  - Explications claires avec exemples
- **SourceMaking** : [sourcemaking.com/design_patterns](https://sourcemaking.com/design_patterns)
- **Python Patterns** : [python-patterns.guide](https://python-patterns.guide/)

### Vidéos

- Chaînes YouTube sur les design patterns en Python
- Cours sur Udemy, Coursera

---

## Résumé

Les design patterns sont des **solutions éprouvées** à des problèmes récurrents :

✅ **Patterns de création** : contrôlent comment les objets sont créés (Singleton, Factory, Builder)

✅ **Patterns structurels** : organisent les objets et leurs relations (Decorator, Adapter, Repository)

✅ **Patterns comportementaux** : gèrent la communication entre objets (Observer, Strategy, Iterator)

✅ **Pythoniques** : Python offre des fonctionnalités natives (décorateurs, context managers, générateurs)

### Pour bien débuter

1. **Comprenez le problème** avant d'appliquer un pattern
2. **Commencez par les plus courants** : Singleton, Factory, Strategy, Decorator
3. **Pratiquez** : essayez de les utiliser dans vos projets
4. **Lisez du code** : étudiez comment les bibliothèques populaires utilisent les patterns
5. **Refactorisez** : identifiez où les patterns amélioreraient votre code existant

Les design patterns ne sont pas de la magie, ce sont des **outils dans votre boîte à outils**. Plus vous coderez, plus leur utilisation deviendra naturelle. L'important est de savoir qu'ils existent et quand les utiliser ! 🚀

⏭️ [Optimisation des performances](/12-projets-et-bonnes-pratiques/04-optimisation-performances.md)
