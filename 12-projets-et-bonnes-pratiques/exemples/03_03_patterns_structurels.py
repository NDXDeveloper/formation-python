# ============================================================================
#   Section 12.3 : Patterns de conception courants
#   Description : Patterns structurels et pythoniques - Decorator (classe cafe,
#                 decorateurs fonctions, permissions), Adapter (media, meteo),
#                 Repository (InMemory, Database), Context Manager (timer,
#                 transaction, fichier temporaire)
#   Fichier source : 03-patterns-de-conception.md
# ============================================================================

"""Patterns structurels et pythoniques : Decorator, Adapter, Repository, Context Manager."""

import os
import time
from abc import ABC, abstractmethod
from contextlib import contextmanager
from functools import wraps


# ============================================================
# PATTERN 6 : DECORATOR
# ============================================================
print("=" * 50)
print("PATTERN 6 : DECORATOR")
print("=" * 50)

# --- Decorator avec classes : Cafe ---

class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class SimpleCoffee(Coffee):
    def get_description(self) -> str:
        return "Cafe simple"

    def get_cost(self) -> float:
        return 2.0


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_description(self) -> str:
        return self._coffee.get_description()

    def get_cost(self) -> float:
        return self._coffee.get_cost()


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


print("\n  --- Cafe avec decorateurs ---")
coffee = SimpleCoffee()
print(f"  {coffee.get_description()}: {coffee.get_cost():.1f} EUR")

coffee = MilkDecorator(coffee)
print(f"  {coffee.get_description()}: {coffee.get_cost():.1f} EUR")

coffee = SugarDecorator(coffee)
print(f"  {coffee.get_description()}: {coffee.get_cost():.1f} EUR")

coffee = WhippedCreamDecorator(coffee)
print(f"  {coffee.get_description()}: {coffee.get_cost():.1f} EUR")


# --- Decorateurs de fonctions Python ---

def timer_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} a pris {end - start:.4f} secondes")
        return result
    return wrapper


def logger_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Appel de {func.__name__} avec args={args}")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} a retourne {result}")
        return result
    return wrapper


def validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("Tous les arguments doivent etre des nombres")
        return func(*args, **kwargs)
    return wrapper


@timer_deco
@logger_deco
@validator
def calculer_moyenne(a, b, c):
    """Calcule la moyenne de trois nombres."""
    return (a + b + c) / 3


print("\n  --- Decorateurs de fonctions ---")
resultat = calculer_moyenne(10, 20, 30)


# --- Decorateurs de permissions ---

def requires_authentication(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise PermissionError("Utilisateur non authentifie")
        return func(user, *args, **kwargs)
    return wrapper


def requires_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            raise PermissionError("Droits admin requis")
        return func(user, *args, **kwargs)
    return wrapper


def log_action(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        print(f"  Action {func.__name__} par {user.get('name', 'Inconnu')}")
        return func(user, *args, **kwargs)
    return wrapper


@log_action
@requires_authentication
@requires_admin
def supprimer_utilisateur(user, user_id):
    print(f"  Suppression de l'utilisateur {user_id}")
    return True


print("\n  --- Permissions ---")
admin_user = {"name": "Alice", "is_authenticated": True, "is_admin": True}
supprimer_utilisateur(admin_user, 123)

normal_user = {"name": "Bob", "is_authenticated": True, "is_admin": False}
try:
    supprimer_utilisateur(normal_user, 123)
except PermissionError as e:
    print(f"  Erreur : {e}")


# ============================================================
# PATTERN 8 : ADAPTER
# ============================================================
print(f"\n{'=' * 50}")
print("PATTERN 8 : ADAPTER")
print("=" * 50)

# --- Adapter media ---

class MediaPlayer:
    def play(self, filename: str):
        pass


class MP3Player:
    def play_mp3(self, filename: str):
        print(f"  Lecture MP3 : {filename}")


class MP4Player:
    def play_mp4(self, filename: str):
        print(f"  Lecture MP4 : {filename}")


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


def lire_media(player: MediaPlayer, filename: str):
    player.play(filename)


print("\n  --- Media Adapter ---")
lire_media(MP3Adapter(), "musique.mp3")
lire_media(MP4Adapter(), "video.mp4")


# --- Adapter meteo (APIs externes) ---

class WeatherService:
    def get_temperature(self, city: str) -> float:
        pass


class OpenWeatherAPI:
    def fetch_weather_data(self, location: str) -> dict:
        return {
            "location": location,
            "temp_kelvin": 293.15,
            "humidity": 65
        }


class WeatherDotComAPI:
    def get_current_weather(self, place: str) -> dict:
        return {
            "place": place,
            "temperature_fahrenheit": 68,
            "conditions": "Sunny"
        }


class OpenWeatherAdapter(WeatherService):
    def __init__(self):
        self.api = OpenWeatherAPI()

    def get_temperature(self, city: str) -> float:
        data = self.api.fetch_weather_data(city)
        return round(data["temp_kelvin"] - 273.15, 1)


class WeatherDotComAdapter(WeatherService):
    def __init__(self):
        self.api = WeatherDotComAPI()

    def get_temperature(self, city: str) -> float:
        data = self.api.get_current_weather(city)
        return round((data["temperature_fahrenheit"] - 32) * 5 / 9, 1)


def afficher_meteo(service: WeatherService, ville: str):
    temp = service.get_temperature(ville)
    print(f"  Temperature a {ville} : {temp} C")


print("\n  --- Weather Adapter ---")
afficher_meteo(OpenWeatherAdapter(), "Paris")
afficher_meteo(WeatherDotComAdapter(), "Paris")


# ============================================================
# PATTERN 9 : REPOSITORY
# ============================================================
print(f"\n{'=' * 50}")
print("PATTERN 9 : REPOSITORY")
print("=" * 50)


class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


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


repository = InMemoryUserRepository()
service = UserService(repository)

user1 = service.register_user("Alice", "alice@example.com")
user2 = service.register_user("Bob", "bob@example.com")

print(f"\n  Utilisateurs crees :")
for user in service.list_users():
    print(f"    {user}")

print(f"\n  Recherche id=1 : {service.get_user(1)}")

repository.delete(2)
print(f"  Apres suppression id=2 : {len(service.list_users())} utilisateur(s)")


# ============================================================
# PATTERN 10 : CONTEXT MANAGER
# ============================================================
print(f"\n{'=' * 50}")
print("PATTERN 10 : CONTEXT MANAGER")
print("=" * 50)


# --- Timer context manager ---

@contextmanager
def timer_cm(name: str):
    print(f"\n  Debut de {name}")
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"  {name} termine en {end - start:.4f}s")


with timer_cm("operation"):
    time.sleep(0.1)
    print("  Traitement en cours...")


# --- Transaction simulee ---

class Database:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None

    def connect(self):
        print(f"\n  Connexion a {self.connection_string}")
        self.connection = f"Connection to {self.connection_string}"

    def disconnect(self):
        if self.connection:
            print("  Deconnexion de la base de donnees")
            self.connection = None

    @contextmanager
    def transaction(self):
        print("  Debut de la transaction")
        try:
            yield self.connection
            print("  Commit de la transaction")
        except Exception as e:
            print(f"  Rollback de la transaction : {e}")
            raise
        finally:
            print("  Fin de la transaction")


db = Database("postgresql://localhost/mydb")
db.connect()

with db.transaction() as conn:
    print("  Insertion de donnees...")
    print("  Mise a jour de donnees...")

db.disconnect()


# --- Fichier temporaire ---

@contextmanager
def temporary_file(filename: str):
    print(f"\n  Creation du fichier temporaire {filename}")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Contenu temporaire")
    try:
        yield filename
    finally:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"  Suppression du fichier {filename}")


with temporary_file("/tmp/temp_pattern_test.txt") as filename:
    print(f"  Utilisation de {filename}")
    with open(filename, 'r', encoding='utf-8') as f:
        print(f"  Contenu : {f.read()}")

# Verifier que le fichier est supprime
print(f"  Fichier existe encore ? {os.path.exists('/tmp/temp_pattern_test.txt')}")
