🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 12.3 : Patterns de conception courants

## Introduction

Imaginez que vous construisez une maison. Vous n'inventez pas de nouveaux plans à chaque fois : vous utilisez des modèles éprouvés (maison à étages, plain-pied, etc.). En programmation, c'est pareil ! Les **patterns de conception** (ou design patterns) sont des solutions toutes prêtes pour résoudre des problèmes récurrents.

Un pattern de conception, c'est comme une recette de cuisine : il décrit les ingrédients (classes, objets) et la méthode (interactions) pour obtenir un résultat spécifique.

## Pourquoi utiliser des patterns ?

### Les avantages

1. **Réutilisabilité** : Solutions testées et approuvées
2. **Communication** : Langage commun entre développeurs
3. **Maintenance** : Code plus facile à comprendre et modifier
4. **Éviter les pièges** : Solutions qui évitent les erreurs classiques

### Un exemple sans pattern

```python
# Code difficile à maintenir et comprendre
class GestionFichier:
    def __init__(self):
        self.config = {}
        self.load_config()

    def load_config(self):
        # Lecture de fichier compliquée...
        pass

    def save_data(self, data):
        # Logique mélangée...
        if self.config.get('format') == 'json':
            # Code JSON...
            pass
        elif self.config.get('format') == 'xml':
            # Code XML...
            pass
        # Difficile d'ajouter de nouveaux formats !
```

### Avec des patterns

```python
# Code clair et extensible
class SaverFactory:  # Pattern Factory
    @staticmethod
    def create_saver(format_type):
        if format_type == 'json':
            return JsonSaver()
        elif format_type == 'xml':
            return XmlSaver()

class FileManager:  # Pattern Strategy
    def __init__(self, saver):
        self.saver = saver

    def save(self, data):
        self.saver.save(data)
```

## Pattern 1 : Singleton

### Le problème

Parfois, vous voulez qu'une classe n'ait qu'une seule instance dans toute l'application. Par exemple :
- Configuration de l'application
- Connexion à une base de données
- Logger (système de journalisation)

### La solution : Singleton

Le pattern Singleton garantit qu'une classe n'a qu'une seule instance.

```python
class DatabaseConnection:
    """Connexion unique à la base de données."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.host = "localhost"
            self.port = 5432
            self.connected = False
            self.initialized = True

    def connect(self):
        """Se connecte à la base de données."""
        if not self.connected:
            print(f"Connexion à {self.host}:{self.port}")
            self.connected = True
        else:
            print("Déjà connecté!")

    def disconnect(self):
        """Se déconnecte de la base de données."""
        if self.connected:
            print("Déconnexion de la base de données")
            self.connected = False

# Utilisation
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # True - C'est la même instance !

db1.connect()
db2.connect()  # "Déjà connecté!" car c'est la même instance
```

### Version Python plus élégante

```python
class Config:
    """Configuration de l'application (Singleton)."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set_setting(self, key, value):
        """Définit une configuration."""
        self.settings[key] = value

    def get_setting(self, key, default=None):
        """Récupère une configuration."""
        return self.settings.get(key, default)

# Utilisation
config1 = Config()
config1.set_setting('debug', True)

config2 = Config()
print(config2.get_setting('debug'))  # True
```

### Quand utiliser Singleton ?

✅ **À utiliser pour :**
- Configuration globale de l'application
- Logger unique
- Cache partagé
- Connexion à une ressource coûteuse

❌ **À éviter pour :**
- Des objets qui pourraient avoir plusieurs instances
- Des situations où les tests deviennent difficiles

## Pattern 2 : Factory

### Le problème

Vous voulez créer des objets sans spécifier leur classe exacte. Par exemple, créer différents types de notifications selon le contexte.

### La solution : Factory

Le pattern Factory délègue la création d'objets à une classe spécialisée.

```python
from abc import ABC, abstractmethod

# Interface commune
class Notification(ABC):
    """Interface pour toutes les notifications."""

    @abstractmethod
    def send(self, message):
        pass

# Implémentations concrètes
class EmailNotification(Notification):
    """Notification par email."""

    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"📧 Email à {self.email}: {message}")

class SMSNotification(Notification):
    """Notification par SMS."""

    def __init__(self, phone):
        self.phone = phone

    def send(self, message):
        print(f"📱 SMS à {self.phone}: {message}")

class PushNotification(Notification):
    """Notification push."""

    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message):
        print(f"🔔 Push vers {self.device_id}: {message}")

# Factory
class NotificationFactory:
    """Factory pour créer des notifications."""

    @staticmethod
    def create_notification(type_notif, destination):
        """Crée une notification selon le type."""
        if type_notif == 'email':
            return EmailNotification(destination)
        elif type_notif == 'sms':
            return SMSNotification(destination)
        elif type_notif == 'push':
            return PushNotification(destination)
        else:
            raise ValueError(f"Type de notification inconnu: {type_notif}")

# Utilisation
def send_welcome_message(user_preference, destination):
    """Envoie un message de bienvenue selon la préférence."""
    notification = NotificationFactory.create_notification(
        user_preference, destination
    )
    notification.send("Bienvenue sur notre plateforme!")

# Tests
send_welcome_message('email', 'user@example.com')
send_welcome_message('sms', '+33123456789')
send_welcome_message('push', 'device_123')
```

### Factory avancée avec enregistrement

```python
class NotificationRegistry:
    """Factory avec système d'enregistrement."""

    def __init__(self):
        self._creators = {}

    def register(self, type_name, creator_class):
        """Enregistre un nouveau type de notification."""
        self._creators[type_name] = creator_class

    def create(self, type_name, *args, **kwargs):
        """Crée une notification du type demandé."""
        creator = self._creators.get(type_name)
        if not creator:
            raise ValueError(f"Type inconnu: {type_name}")
        return creator(*args, **kwargs)

# Utilisation
registry = NotificationRegistry()
registry.register('email', EmailNotification)
registry.register('sms', SMSNotification)
registry.register('push', PushNotification)

# Ajouter facilement de nouveaux types
class SlackNotification(Notification):
    def __init__(self, channel):
        self.channel = channel

    def send(self, message):
        print(f"💬 Slack #{self.channel}: {message}")

registry.register('slack', SlackNotification)

# Créer des notifications
email_notif = registry.create('email', 'test@example.com')
slack_notif = registry.create('slack', 'general')
```

## Pattern 3 : Observer

### Le problème

Vous voulez notifier plusieurs objets quand quelque chose change, sans que ces objets se connaissent entre eux.

### La solution : Observer

Le pattern Observer permet à un objet (sujet) de notifier automatiquement une liste d'objets (observateurs) des changements.

```python
from abc import ABC, abstractmethod

# Interface Observer
class Observer(ABC):
    """Interface pour les observateurs."""

    @abstractmethod
    def update(self, subject):
        pass

# Sujet observable
class Subject:
    """Classe de base pour les sujets observables."""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """Ajoute un observateur."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Retire un observateur."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        """Notifie tous les observateurs."""
        for observer in self._observers:
            observer.update(self)

# Exemple concret : Système météo
class WeatherStation(Subject):
    """Station météo qui notifie les changements."""

    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure

    def set_measurements(self, temperature, humidity, pressure):
        """Met à jour les mesures et notifie."""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()

# Observateurs concrets
class CurrentConditionsDisplay(Observer):
    """Affichage des conditions actuelles."""

    def __init__(self, name):
        self.name = name

    def update(self, weather_station):
        """Met à jour l'affichage."""
        print(f"[{self.name}] Conditions actuelles:")
        print(f"  Température: {weather_station.temperature}°C")
        print(f"  Humidité: {weather_station.humidity}%")
        print(f"  Pression: {weather_station.pressure} hPa")
        print()

class ForecastDisplay(Observer):
    """Affichage des prévisions."""

    def __init__(self):
        self.last_pressure = None

    def update(self, weather_station):
        """Met à jour les prévisions."""
        current_pressure = weather_station.pressure

        if self.last_pressure is not None:
            if current_pressure > self.last_pressure:
                forecast = "Temps s'améliore"
            elif current_pressure < self.last_pressure:
                forecast = "Temps se dégrade"
            else:
                forecast = "Temps stable"
        else:
            forecast = "Données insuffisantes"

        print(f"[Prévisions] {forecast}")
        self.last_pressure = current_pressure

class AlertSystem(Observer):
    """Système d'alerte."""

    def update(self, weather_station):
        """Vérifie s'il faut déclencher des alertes."""
        temp = weather_station.temperature

        if temp > 35:
            print("🚨 ALERTE: Canicule! Restez hydratés!")
        elif temp < -10:
            print("🚨 ALERTE: Gel intense! Attention sur les routes!")

        humidity = weather_station.humidity
        if humidity > 90:
            print("🚨 ALERTE: Humidité très élevée!")

# Utilisation
weather_station = WeatherStation()

# Créer les observateurs
current_display = CurrentConditionsDisplay("Écran Principal")
forecast_display = ForecastDisplay()
alert_system = AlertSystem()

# S'abonner aux notifications
weather_station.attach(current_display)
weather_station.attach(forecast_display)
weather_station.attach(alert_system)

# Simuler des changements météo
print("=== Mise à jour météo 1 ===")
weather_station.set_measurements(25, 65, 1013)

print("=== Mise à jour météo 2 ===")
weather_station.set_measurements(38, 70, 1005)

print("=== Mise à jour météo 3 ===")
weather_station.set_measurements(-15, 40, 1020)
```

### Observer avec événements nommés

```python
class EventObserver:
    """Observer générique avec événements nommés."""

    def __init__(self):
        self._observers = {}

    def subscribe(self, event_name, callback):
        """S'abonne à un événement."""
        if event_name not in self._observers:
            self._observers[event_name] = []
        self._observers[event_name].append(callback)

    def unsubscribe(self, event_name, callback):
        """Se désabonne d'un événement."""
        if event_name in self._observers:
            self._observers[event_name].remove(callback)

    def emit(self, event_name, *args, **kwargs):
        """Déclenche un événement."""
        if event_name in self._observers:
            for callback in self._observers[event_name]:
                callback(*args, **kwargs)

# Exemple : Système de commande e-commerce
class OrderSystem(EventObserver):
    """Système de commande avec événements."""

    def __init__(self):
        super().__init__()
        self.orders = []

    def create_order(self, order_data):
        """Crée une nouvelle commande."""
        order_id = len(self.orders) + 1
        order = {'id': order_id, **order_data}
        self.orders.append(order)

        # Déclencher l'événement
        self.emit('order_created', order)
        return order

    def ship_order(self, order_id):
        """Expédie une commande."""
        order = next((o for o in self.orders if o['id'] == order_id), None)
        if order:
            order['status'] = 'shipped'
            self.emit('order_shipped', order)

# Handlers d'événements
def send_confirmation_email(order):
    print(f"📧 Email de confirmation envoyé pour commande #{order['id']}")

def update_inventory(order):
    print(f"📦 Stock mis à jour pour commande #{order['id']}")

def send_shipping_notification(order):
    print(f"🚚 Notification d'expédition pour commande #{order['id']}")

def update_analytics(order):
    print(f"📊 Analytics mis à jour pour commande #{order['id']}")

# Configuration
order_system = OrderSystem()

# S'abonner aux événements
order_system.subscribe('order_created', send_confirmation_email)
order_system.subscribe('order_created', update_inventory)
order_system.subscribe('order_created', update_analytics)
order_system.subscribe('order_shipped', send_shipping_notification)
order_system.subscribe('order_shipped', update_analytics)

# Test
order = order_system.create_order({
    'customer': 'Jean Dupont',
    'items': ['Livre Python', 'Clavier'],
    'total': 45.99
})

order_system.ship_order(order['id'])
```

## Pattern 4 : Strategy

### Le problème

Vous avez plusieurs façons de faire la même chose et vous voulez pouvoir changer d'algorithme facilement.

### La solution : Strategy

Le pattern Strategy permet de définir une famille d'algorithmes et de les rendre interchangeables.

```python
from abc import ABC, abstractmethod

# Interface Strategy
class PaymentStrategy(ABC):
    """Interface pour les stratégies de paiement."""

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def is_valid(self):
        pass

# Stratégies concrètes
class CreditCardPayment(PaymentStrategy):
    """Paiement par carte de crédit."""

    def __init__(self, card_number, cvv, expiry_date):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date

    def is_valid(self):
        """Valide les informations de carte."""
        # Simulation de validation
        return (len(self.card_number) == 16 and
                len(self.cvv) == 3 and
                len(self.expiry_date) == 5)

    def pay(self, amount):
        """Effectue le paiement."""
        if not self.is_valid():
            raise ValueError("Informations de carte invalides")

        print(f"💳 Paiement de {amount}€ par carte ****{self.card_number[-4:]}")
        return True

class PayPalPayment(PaymentStrategy):
    """Paiement PayPal."""

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def is_valid(self):
        """Valide les informations PayPal."""
        return '@' in self.email and len(self.password) >= 6

    def pay(self, amount):
        """Effectue le paiement."""
        if not self.is_valid():
            raise ValueError("Informations PayPal invalides")

        print(f"🟦 Paiement de {amount}€ via PayPal ({self.email})")
        return True

class BankTransferPayment(PaymentStrategy):
    """Paiement par virement bancaire."""

    def __init__(self, account_number, bank_code):
        self.account_number = account_number
        self.bank_code = bank_code

    def is_valid(self):
        """Valide les informations bancaires."""
        return len(self.account_number) >= 10 and len(self.bank_code) == 5

    def pay(self, amount):
        """Effectue le paiement."""
        if not self.is_valid():
            raise ValueError("Informations bancaires invalides")

        print(f"🏦 Virement de {amount}€ depuis compte ****{self.account_number[-4:]}")
        return True

# Contexte qui utilise les stratégies
class ShoppingCart:
    """Panier d'achat avec système de paiement."""

    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, name, price):
        """Ajoute un article au panier."""
        self.items.append({'name': name, 'price': price})

    def remove_item(self, name):
        """Retire un article du panier."""
        self.items = [item for item in self.items if item['name'] != name]

    def get_total(self):
        """Calcule le total du panier."""
        return sum(item['price'] for item in self.items)

    def set_payment_strategy(self, strategy):
        """Définit la stratégie de paiement."""
        self.payment_strategy = strategy

    def checkout(self):
        """Finalise la commande."""
        if not self.payment_strategy:
            raise ValueError("Aucune méthode de paiement sélectionnée")

        if not self.items:
            raise ValueError("Panier vide")

        total = self.get_total()
        print(f"\n🛒 Commande:")
        for item in self.items:
            print(f"  - {item['name']}: {item['price']}€")
        print(f"💰 Total: {total}€")

        try:
            success = self.payment_strategy.pay(total)
            if success:
                print("✅ Paiement réussi!")
                self.items = []  # Vider le panier
                return True
        except ValueError as e:
            print(f"❌ Erreur de paiement: {e}")
            return False

# Utilisation
cart = ShoppingCart()

# Ajouter des articles
cart.add_item("Livre Python", 29.99)
cart.add_item("Clavier mécanique", 89.90)
cart.add_item("Souris gaming", 45.50)

# Test avec différentes stratégies de paiement
print("=== Test Carte de Crédit ===")
card_payment = CreditCardPayment("1234567890123456", "123", "12/25")
cart.set_payment_strategy(card_payment)
cart.checkout()

# Ajouter d'autres articles
cart.add_item("Écran 4K", 299.99)
cart.add_item("Webcam HD", 79.90)

print("\n=== Test PayPal ===")
paypal_payment = PayPalPayment("user@example.com", "password123")
cart.set_payment_strategy(paypal_payment)
cart.checkout()

# Test avec une carte invalide
cart.add_item("Casque audio", 149.99)

print("\n=== Test Carte Invalide ===")
invalid_card = CreditCardPayment("123", "12", "invalid")
cart.set_payment_strategy(invalid_card)
cart.checkout()
```

### Strategy pour algorithmes de tri

```python
class SortStrategy(ABC):
    """Interface pour les stratégies de tri."""

    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    """Tri à bulles (simple mais lent)."""

    def sort(self, data):
        """Tri à bulles."""
        arr = data.copy()
        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

class QuickSort(SortStrategy):
    """Tri rapide (efficace)."""

    def sort(self, data):
        """Tri rapide."""
        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]

        return self.sort(left) + middle + self.sort(right)

class PythonSort(SortStrategy):
    """Tri Python natif (Timsort)."""

    def sort(self, data):
        """Tri Python natif."""
        return sorted(data)

class DataSorter:
    """Classe qui utilise différentes stratégies de tri."""

    def __init__(self, strategy=None):
        self.strategy = strategy or PythonSort()

    def set_strategy(self, strategy):
        """Change la stratégie de tri."""
        self.strategy = strategy

    def sort_data(self, data):
        """Trie les données avec la stratégie actuelle."""
        print(f"Tri avec {self.strategy.__class__.__name__}")
        return self.strategy.sort(data)

# Test des stratégies
import random
import time

# Données de test
small_data = [random.randint(1, 100) for _ in range(10)]
large_data = [random.randint(1, 1000) for _ in range(100)]

sorter = DataSorter()

print("=== Tri de petites données ===")
print(f"Données originales: {small_data}")

for strategy in [BubbleSort(), QuickSort(), PythonSort()]:
    sorter.set_strategy(strategy)
    sorted_data = sorter.sort_data(small_data)
    print(f"Résultat: {sorted_data[:5]}...{sorted_data[-5:]}")
    print()
```

## Pattern 5 : Decorator

### Le problème

Vous voulez ajouter des fonctionnalités à un objet sans modifier sa classe, et de manière flexible.

### La solution : Decorator

Le pattern Decorator permet d'attacher dynamiquement de nouvelles responsabilités à un objet.

```python
from abc import ABC, abstractmethod

# Interface de base
class Coffee(ABC):
    """Interface pour les cafés."""

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

# Implémentation de base
class SimpleCoffee(Coffee):
    """Café simple de base."""

    def get_description(self):
        return "Café simple"

    def get_cost(self):
        return 2.00

# Décorateur de base
class CoffeeDecorator(Coffee):
    """Décorateur de base pour les cafés."""

    def __init__(self, coffee):
        self.coffee = coffee

    def get_description(self):
        return self.coffee.get_description()

    def get_cost(self):
        return self.coffee.get_cost()

# Décorateurs concrets
class MilkDecorator(CoffeeDecorator):
    """Ajoute du lait au café."""

    def get_description(self):
        return self.coffee.get_description() + ", Lait"

    def get_cost(self):
        return self.coffee.get_cost() + 0.50

class SugarDecorator(CoffeeDecorator):
    """Ajoute du sucre au café."""

    def get_description(self):
        return self.coffee.get_description() + ", Sucre"

    def get_cost(self):
        return self.coffee.get_cost() + 0.20

class WhipDecorator(CoffeeDecorator):
    """Ajoute de la chantilly au café."""

    def get_description(self):
        return self.coffee.get_description() + ", Chantilly"

    def get_cost(self):
        return self.coffee.get_cost() + 0.70

class VanillaDecorator(CoffeeDecorator):
    """Ajoute du sirop de vanille."""

    def get_description(self):
        return self.coffee.get_description() + ", Vanille"

    def get_cost(self):
        return self.coffee.get_cost() + 0.60

# Utilisation
def order_coffee():
    """Simule une commande de café."""
    # Café de base
    coffee = SimpleCoffee()
    print(f"☕ {coffee.get_description()}: {coffee.get_cost():.2f}€")

    # Ajouter du lait
    coffee = MilkDecorator(coffee)
    print(f"☕ {coffee.get_description()}: {coffee.get_cost():.2f}€")

    # Ajouter du sucre
    coffee = SugarDecorator(coffee)
    print(f"☕ {coffee.get_description()}: {coffee.get_cost():.2f}€")

    # Ajouter de la chantilly
    coffee = WhipDecorator(coffee)
    print(f"☕ {coffee.get_description()}: {coffee.get_cost():.2f}€")

    return coffee

print("=== Commande de café ===")
my_coffee = order_coffee()
print(f"\n🧾 Facture finale: {my_coffee.get_description()}")
print(f"💰 Prix total: {my_coffee.get_cost():.2f}€")

# Autre exemple : café complexe
print("\n=== Café gourmand ===")
gourmet_coffee = VanillaDecorator(
    WhipDecorator(
        MilkDecorator(
            SugarDecorator(
                SimpleCoffee()
            )
        )
    )
)

print(f"☕ {gourmet_coffee.get_description()}")
print(f"💰 Prix: {gourmet_coffee.get_cost():.2f}€")
```

### Decorator avec des fonctions Python

```python
import time
import functools

# Décorateur de timing
def timing_decorator(func):
    """Mesure le temps d'exécution d'une fonction."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"⏱️  {func.__name__} executée en {end_time - start_time:.4f} secondes")
        return result

    return wrapper

# Décorateur de logging
def logging_decorator(func):
    """Log les appels de fonction."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📝 Appel de {func.__name__} avec args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"📝 {func.__name__} retourne: {result}")
        return result

    return wrapper

# Décorateur de validation
def validate_positive(func):
    """Valide que les arguments sont positifs."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument négatif non autorisé: {arg}")

        return func(*args, **kwargs)

    return wrapper

# Utilisation avec des décorateurs empilés
@timing_decorator
@logging_decorator
@validate_positive
def calculate_fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci."""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

@timing_decorator
@logging_decorator
def factorial(n):
    """Calcule la factorielle de n."""
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Tests
print("=== Test Fibonacci ===")
try:
    result = calculate_fibonacci(8)
    print(f"Résultat final: {result}")
except ValueError as e:
    print(f"Erreur: {e}")

print("\n=== Test Factorielle ===")
result = factorial(5)
print(f"Résultat final: {result}")

print("\n=== Test avec valeur négative ===")
try:
    calculate_fibonacci(-3)
except ValueError as e:
    print(f"Erreur attendue: {e}")
```

### Décorateur de cache (memoization)

```python
def memoize(func):
    """Cache les résultats d'une fonction."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Créer une clé unique pour les arguments
        key = str(args) + str(sorted(kwargs.items()))

        if key in cache:
            print(f"💾 Cache hit pour {func.__name__}{args}")
            return cache[key]

        print(f"🔄 Calcul de {func.__name__}{args}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

@memoize
def fibonacci_optimized(n):
    """Fibonacci optimisé avec cache."""
    if n <= 1:
        return n
    return fibonacci_optimized(n-1) + fibonacci_optimized(n-2)

print("=== Fibonacci avec cache ===")
print(f"fibonacci_optimized(10) = {fibonacci_optimized(10)}")
print(f"fibonacci_optimized(10) = {fibonacci_optimized(10)}")  # Utilise le cache
```

## Pattern 6 : Command

### Le problème

Vous voulez encapsuler une requête comme un objet, permettant de paramétrer des clients avec différentes requêtes, mettre en file d'attente ou journaliser les requêtes.

### La solution : Command

Le pattern Command transforme une requête en objet autonome qui contient toute l'information sur la requête.

```python
from abc import ABC, abstractmethod

# Interface Command
class Command(ABC):
    """Interface pour toutes les commandes."""

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Récepteur - objet qui effectue le travail
class TextEditor:
    """Éditeur de texte simple."""

    def __init__(self):
        self.content = ""
        self.cursor_position = 0

    def insert_text(self, text, position=None):
        """Insère du texte à la position donnée."""
        if position is None:
            position = self.cursor_position

        self.content = (self.content[:position] +
                       text +
                       self.content[position:])
        self.cursor_position = position + len(text)

    def delete_text(self, start, length):
        """Supprime du texte."""
        deleted_text = self.content[start:start+length]
        self.content = self.content[:start] + self.content[start+length:]
        self.cursor_position = start
        return deleted_text

    def get_content(self):
        """Retourne le contenu actuel."""
        return self.content

    def set_cursor(self, position):
        """Définit la position du curseur."""
        self.cursor_position = max(0, min(position, len(self.content)))

# Commandes concrètes
class InsertCommand(Command):
    """Commande pour insérer du texte."""

    def __init__(self, editor, text, position=None):
        self.editor = editor
        self.text = text
        self.position = position
        self.executed_position = None

    def execute(self):
        """Exécute l'insertion."""
        self.executed_position = (self.position if self.position is not None
                                 else self.editor.cursor_position)
        self.editor.insert_text(self.text, self.executed_position)
        print(f"✏️  Texte inséré: '{self.text}' à la position {self.executed_position}")

    def undo(self):
        """Annule l'insertion."""
        if self.executed_position is not None:
            self.editor.delete_text(self.executed_position, len(self.text))
            print(f"↩️  Insertion annulée: '{self.text}'")

class DeleteCommand(Command):
    """Commande pour supprimer du texte."""

    def __init__(self, editor, start, length):
        self.editor = editor
        self.start = start
        self.length = length
        self.deleted_text = None

    def execute(self):
        """Exécute la suppression."""
        self.deleted_text = self.editor.delete_text(self.start, self.length)
        print(f"🗑️  Texte supprimé: '{self.deleted_text}' à partir de {self.start}")

    def undo(self):
        """Annule la suppression."""
        if self.deleted_text is not None:
            self.editor.insert_text(self.deleted_text, self.start)
            print(f"↩️  Suppression annulée: '{self.deleted_text}'")

class ReplaceCommand(Command):
    """Commande pour remplacer du texte."""

    def __init__(self, editor, start, length, new_text):
        self.editor = editor
        self.start = start
        self.length = length
        self.new_text = new_text
        self.old_text = None

    def execute(self):
        """Exécute le remplacement."""
        self.old_text = self.editor.delete_text(self.start, self.length)
        self.editor.insert_text(self.new_text, self.start)
        print(f"🔄 Texte remplacé: '{self.old_text}' → '{self.new_text}'")

    def undo(self):
        """Annule le remplacement."""
        if self.old_text is not None:
            self.editor.delete_text(self.start, len(self.new_text))
            self.editor.insert_text(self.old_text, self.start)
            print(f"↩️  Remplacement annulé: '{self.new_text}' → '{self.old_text}'")

# Invocateur - gère les commandes et l'historique
class EditorInvoker:
    """Invocateur qui gère les commandes et l'historique."""

    def __init__(self, editor):
        self.editor = editor
        self.history = []
        self.current_index = -1

    def execute_command(self, command):
        """Exécute une commande et l'ajoute à l'historique."""
        command.execute()

        # Supprimer les commandes "futures" si on était revenu en arrière
        self.history = self.history[:self.current_index + 1]

        # Ajouter la nouvelle commande
        self.history.append(command)
        self.current_index += 1

    def undo(self):
        """Annule la dernière commande."""
        if self.current_index >= 0:
            command = self.history[self.current_index]
            command.undo()
            self.current_index -= 1
            print(f"📋 État actuel: '{self.editor.get_content()}'")
        else:
            print("❌ Rien à annuler")

    def redo(self):
        """Refait la prochaine commande."""
        if self.current_index + 1 < len(self.history):
            self.current_index += 1
            command = self.history[self.current_index]
            command.execute()
            print(f"📋 État actuel: '{self.editor.get_content()}'")
        else:
            print("❌ Rien à refaire")

    def show_history(self):
        """Affiche l'historique des commandes."""
        print("\n📚 Historique des commandes:")
        for i, command in enumerate(self.history):
            marker = " → " if i == self.current_index else "   "
            print(f"{marker}{i}: {command.__class__.__name__}")

# Utilisation complète
def demo_text_editor():
    """Démonstration de l'éditeur de texte avec commandes."""

    # Créer l'éditeur et l'invocateur
    editor = TextEditor()
    invoker = EditorInvoker(editor)

    print("=== Démonstration de l'éditeur de texte ===")
    print(f"État initial: '{editor.get_content()}'")

    # Série de commandes
    commands = [
        InsertCommand(editor, "Bonjour "),
        InsertCommand(editor, "le monde!"),
        InsertCommand(editor, " magnifique", 8),  # Insérer au milieu
        ReplaceCommand(editor, 8, 10, "beau"),
        DeleteCommand(editor, 13, 5),  # Supprimer "monde"
    ]

    # Exécuter les commandes
    for i, command in enumerate(commands, 1):
        print(f"\n--- Commande {i} ---")
        invoker.execute_command(command)
        print(f"📋 Résultat: '{editor.get_content()}'")

    # Montrer l'historique
    invoker.show_history()

    # Tests d'annulation et de rétablissement
    print(f"\n=== Tests Undo/Redo ===")
    print(f"État avant undo: '{editor.get_content()}'")

    # Annuler quelques commandes
    for i in range(3):
        print(f"\n--- Undo {i+1} ---")
        invoker.undo()

    # Refaire quelques commandes
    for i in range(2):
        print(f"\n--- Redo {i+1} ---")
        invoker.redo()

    invoker.show_history()

demo_text_editor()
```

### Command avec macro-commandes

```python
class MacroCommand(Command):
    """Commande composée de plusieurs commandes."""

    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        """Exécute toutes les commandes."""
        print("🔄 Exécution de macro-commande")
        for command in self.commands:
            command.execute()

    def undo(self):
        """Annule toutes les commandes en ordre inverse."""
        print("↩️  Annulation de macro-commande")
        for command in reversed(self.commands):
            command.undo()

# Exemple d'utilisation
def demo_macro_command():
    """Démonstration des macro-commandes."""

    editor = TextEditor()
    invoker = EditorInvoker(editor)

    # Créer une macro qui ajoute une signature
    signature_macro = MacroCommand([
        InsertCommand(editor, "\n\n"),
        InsertCommand(editor, "Cordialement,\n"),
        InsertCommand(editor, "Jean Dupont")
    ])

    # Écrire un email
    invoker.execute_command(InsertCommand(editor, "Bonjour,\n\n"))
    invoker.execute_command(InsertCommand(editor, "Voici le rapport demandé.\n"))

    print(f"Email avant signature: '{editor.get_content()}'")

    # Ajouter la signature avec la macro
    invoker.execute_command(signature_macro)

    print(f"Email complet: '{editor.get_content()}'")

    # Annuler la signature entière
    invoker.undo()

    print(f"Après annulation de la signature: '{editor.get_content()}'")

print("\n" + "="*50)
demo_macro_command()
```

## Pattern 7 : Adapter

### Le problème

Vous voulez utiliser une classe existante dont l'interface n'est pas compatible avec ce dont vous avez besoin.

### La solution : Adapter

Le pattern Adapter permet à des classes avec des interfaces incompatibles de travailler ensemble.

```python
# Interface attendue par notre application
class MediaPlayer:
    """Interface standard pour les lecteurs média."""

    def play(self, filename):
        pass

# Classe existante avec une interface différente
class Mp3Player:
    """Lecteur MP3 existant."""

    def play_mp3(self, filename):
        print(f"🎵 Lecture MP3: {filename}")

class Mp4Player:
    """Lecteur MP4 existant."""

    def play_mp4(self, filename):
        print(f"🎬 Lecture MP4: {filename}")

class WavPlayer:
    """Lecteur WAV existant."""

    def play_wav(self, filename):
        print(f"🔊 Lecture WAV: {filename}")

# Adaptateurs pour rendre les classes compatibles
class Mp3Adapter(MediaPlayer):
    """Adaptateur pour Mp3Player."""

    def __init__(self):
        self.mp3_player = Mp3Player()

    def play(self, filename):
        self.mp3_player.play_mp3(filename)

class Mp4Adapter(MediaPlayer):
    """Adaptateur pour Mp4Player."""

    def __init__(self):
        self.mp4_player = Mp4Player()

    def play(self, filename):
        self.mp4_player.play_mp4(filename)

class WavAdapter(MediaPlayer):
    """Adaptateur pour WavPlayer."""

    def __init__(self):
        self.wav_player = WavPlayer()

    def play(self, filename):
        self.wav_player.play_wav(filename)

# Lecteur universel qui utilise les adaptateurs
class UniversalMediaPlayer(MediaPlayer):
    """Lecteur média universel."""

    def __init__(self):
        self.adapters = {
            'mp3': Mp3Adapter(),
            'mp4': Mp4Adapter(),
            'wav': WavAdapter()
        }

    def play(self, filename):
        """Joue un fichier selon son extension."""
        extension = filename.split('.')[-1].lower()

        if extension in self.adapters:
            print(f"📱 Lecture universelle de: {filename}")
            self.adapters[extension].play(filename)
        else:
            print(f"❌ Format non supporté: {extension}")

# Utilisation
def demo_adapter():
    """Démonstration du pattern Adapter."""

    player = UniversalMediaPlayer()

    # Test avec différents formats
    files = [
        "musique.mp3",
        "video.mp4",
        "son.wav",
        "document.pdf"  # Format non supporté
    ]

    for filename in files:
        player.play(filename)
        print()

demo_adapter()
```

### Adapter pour API externes

```python
# API externe existante (format différent)
class WeatherAPI:
    """API météo externe avec format spécifique."""

    def get_weather_data(self, city):
        """Retourne les données météo dans un format spécifique."""
        # Simulation d'appel API
        return {
            'city_name': city,
            'temp_celsius': 25.5,
            'humidity_percent': 65,
            'wind_speed_kmh': 15,
            'conditions': 'sunny'
        }

# Interface attendue par notre application
class StandardWeatherInterface:
    """Interface standard pour les données météo."""

    def get_temperature(self, location):
        pass

    def get_humidity(self, location):
        pass

    def get_conditions(self, location):
        pass

# Adaptateur
class WeatherAPIAdapter(StandardWeatherInterface):
    """Adaptateur pour l'API météo externe."""

    def __init__(self):
        self.api = WeatherAPI()
        self._cache = {}

    def _get_data(self, location):
        """Récupère et cache les données."""
        if location not in self._cache:
            self._cache[location] = self.api.get_weather_data(location)
        return self._cache[location]

    def get_temperature(self, location):
        """Retourne la température en Celsius."""
        data = self._get_data(location)
        return data['temp_celsius']

    def get_humidity(self, location):
        """Retourne l'humidité en pourcentage."""
        data = self._get_data(location)
        return data['humidity_percent']

    def get_conditions(self, location):
        """Retourne les conditions météo."""
        data = self._get_data(location)
        return data['conditions']

# Application qui utilise l'interface standard
class WeatherApp:
    """Application météo utilisant l'interface standard."""

    def __init__(self, weather_service):
        self.weather_service = weather_service

    def show_weather(self, city):
        """Affiche la météo d'une ville."""
        print(f"🌍 Météo pour {city}:")

        temp = self.weather_service.get_temperature(city)
        humidity = self.weather_service.get_humidity(city)
        conditions = self.weather_service.get_conditions(city)

        print(f"🌡️  Température: {temp}°C")
        print(f"💧 Humidité: {humidity}%")
        print(f"☀️  Conditions: {conditions}")

# Utilisation
weather_adapter = WeatherAPIAdapter()
app = WeatherApp(weather_adapter)

app.show_weather("Paris")
print()
app.show_weather("Lyon")
```

## Résumé des patterns

### Tableau récapitulatif

| Pattern | Problème résolu | Utilisation typique |
|---------|----------------|-------------------|
| **Singleton** | Une seule instance | Configuration, Logger, Cache |
| **Factory** | Création d'objets complexe | Notifications, Parsers, Drivers |
| **Observer** | Notification automatique | Events, MVC, Reactive programming |
| **Strategy** | Algorithmes interchangeables | Paiements, Tri, Validation |
| **Decorator** | Ajouter des fonctionnalités | Middleware, Logging, Caching |
| **Command** | Encapsuler des actions | Undo/Redo, Queues, Macros |
| **Adapter** | Interfaces incompatibles | APIs externes, Legacy code |

### Conseils pour choisir un pattern

#### Quand utiliser Singleton ?
✅ **Utilisez quand :**
- Vous avez besoin d'une instance unique (config, logger)
- L'objet est coûteux à créer
- Vous voulez un point d'accès global

❌ **Évitez quand :**
- Vous pourriez avoir besoin de plusieurs instances
- Cela complique les tests
- C'est juste pour éviter de passer des paramètres

#### Quand utiliser Factory ?
✅ **Utilisez quand :**
- La création d'objets est complexe
- Vous voulez cacher les détails de création
- Vous avez plusieurs types similaires

❌ **Évitez quand :**
- La création est simple (`MyClass()`)
- Vous n'avez qu'un seul type d'objet

#### Quand utiliser Observer ?
✅ **Utilisez quand :**
- Plusieurs objets doivent réagir à un changement
- Vous voulez un couplage faible
- Les notifications sont asynchrones

❌ **Évitez quand :**
- Vous avez des dépendances circulaires
- L'ordre des notifications est critique

## Exercices pratiques

### Exercice 1 : Système de notification
Créez un système qui peut envoyer des notifications par email, SMS et push. Utilisez les patterns Factory et Observer.

### Exercice 2 : Calculatrice avec historique
Implémentez une calculatrice qui peut annuler/refaire les opérations en utilisant le pattern Command.

### Exercice 3 : Adaptateur de base de données
Créez un adaptateur pour utiliser différentes bases de données (SQLite, MySQL, PostgreSQL) avec la même interface.

### Exercice 4 : Décorateur de cache
Implémentez un décorateur qui cache les résultats de fonctions coûteuses avec une expiration.

## Bonnes pratiques

### 1. Ne pas sur-utiliser les patterns
```python
# ❌ Mauvais : Pattern inutile pour cas simple
class SimpleCalculatorFactory:
    @staticmethod
    def create_calculator():
        return Calculator()

calc = SimpleCalculatorFactory.create_calculator()

# ✅ Bon : Direct pour cas simple
calc = Calculator()
```

### 2. Garder la simplicité
```python
# ✅ Bon : Pattern nécessaire et bien utilisé
class NotificationFactory:
    @staticmethod
    def create(type_name, config):
        if type_name == 'email':
            return EmailNotification(config['smtp_server'])
        elif type_name == 'sms':
            return SMSNotification(config['api_key'])
        # Logique complexe justifiée
```

### 3. Documentation claire
```python
class WeatherObserver:
    """
    Observer pour les changements météo.

    Pattern utilisé: Observer
    Raison: Permet à plusieurs composants UI de réagir
    automatiquement aux mises à jour météo sans couplage fort.
    """

    def update(self, weather_data):
        """Appelé quand les données météo changent."""
        pass
```

## Conclusion

Les patterns de conception sont des outils puissants qui vous aident à :

1. **Résoudre des problèmes récurrents** avec des solutions éprouvées
2. **Communiquer efficacement** avec d'autres développeurs
3. **Écrire du code maintenable** et extensible
4. **Éviter les pièges** de conception

**Règle d'or :** Utilisez un pattern seulement s'il simplifie vraiment votre code et résout un problème réel. Ne forcez jamais un pattern juste pour le plaisir !

La prochaine étape sera d'apprendre à optimiser les performances de vos applications Python.

⏭️
