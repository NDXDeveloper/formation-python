# ============================================================================
#   Section 12.3 : Patterns de conception courants
#   Description : Patterns de creation - Singleton (classique et decorateur),
#                 Factory (animaux, exporteurs), Builder (Pizza, requete SQL)
#   Fichier source : 03-patterns-de-conception.md
# ============================================================================

"""Patterns de creation : Singleton, Factory, Builder."""

from abc import ABC, abstractmethod


# ============================================================
# PATTERN 1 : SINGLETON
# ============================================================
print("=" * 50)
print("PATTERN 1 : SINGLETON")
print("=" * 50)

# --- Solution classique avec __new__ ---

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connexion a la base de donnees"
        return cls._instance


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(f"\n  db1 is db2 : {db1 is db2}")
print(f"  id(db1) == id(db2) : {id(db1) == id(db2)}")


# --- Solution Pythonique avec decorateur ---

def singleton(cls):
    """Decorateur qui transforme une classe en Singleton."""
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


config1 = Configuration()
config1.set("database", "postgresql")

config2 = Configuration()
print(f"\n  config2.get('database') : {config2.get('database')}")
print(f"  config1 is config2 : {config1 is config2}")


# --- Exemple pratique : Logger ---

@singleton
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)
        print(f"  {log_entry}")

    def get_logs(self):
        return self.logs


logger = Logger()
logger.log("Application demarree")

logger2 = Logger()
logger2.log("Traitement des donnees")
print(f"  Nombre total de logs : {len(logger.get_logs())}")


# ============================================================
# PATTERN 2 : FACTORY
# ============================================================
print(f"\n{'=' * 50}")
print("PATTERN 2 : FACTORY")
print("=" * 50)

# --- Factory d'animaux ---

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


class AnimalFactory:
    @staticmethod
    def creer_animal(type_animal: str) -> Animal:
        animaux = {
            "chien": Chien,
            "chat": Chat,
            "vache": Vache
        }
        classe_animal = animaux.get(type_animal.lower())
        if classe_animal is None:
            raise ValueError(f"Type d'animal inconnu : {type_animal}")
        return classe_animal()


factory = AnimalFactory()

animal1 = factory.creer_animal("chien")
print(f"\n  Chien : {animal1.parler()}")

animal2 = factory.creer_animal("chat")
print(f"  Chat : {animal2.parler()}")

animal3 = factory.creer_animal("vache")
print(f"  Vache : {animal3.parler()}")

try:
    factory.creer_animal("dragon")
except ValueError as e:
    print(f"  Erreur : {e}")


# --- Factory d'exporteurs ---

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
            raise ValueError(f"Format non supporte : {format}")
        return exporter_class()


data = {"nom": "Rapport", "date": "2024-01-15"}

print(f"\n  --- Exporteurs ---")
for fmt in ["pdf", "excel", "csv"]:
    exporter = ExporterFactory.get_exporter(fmt)
    print(f"  {exporter.export(data)}")


# ============================================================
# PATTERN 3 : BUILDER
# ============================================================
print(f"\n{'=' * 50}")
print("PATTERN 3 : BUILDER")
print("=" * 50)

# --- Builder de Pizza ---

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
        return self

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


pizza = (PizzaBuilder()
         .set_taille("grande")
         .ajouter_fromage()
         .ajouter_pepperoni()
         .ajouter_champignons()
         .build())

print(f"\n  {pizza}")


# --- Builder de requetes SQL ---

class SQLQuery:
    def __init__(self):
        self.select_fields = []
        self.from_table = None
        self.where_conditions = []
        self.order_by_field = None
        self.limit_value = None

    def to_sql(self) -> str:
        query_parts = []
        fields = ", ".join(self.select_fields) if self.select_fields else "*"
        query_parts.append(f"SELECT {fields}")
        if self.from_table:
            query_parts.append(f"FROM {self.from_table}")
        if self.where_conditions:
            conditions = " AND ".join(self.where_conditions)
            query_parts.append(f"WHERE {conditions}")
        if self.order_by_field:
            query_parts.append(f"ORDER BY {self.order_by_field}")
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


query = (QueryBuilder()
         .select("nom", "email", "age")
         .from_table("users")
         .where("age > 18")
         .where("pays = 'France'")
         .order_by("nom")
         .limit(10)
         .build())

print(f"\n  SQL : {query}")

# Requete simple
query2 = (QueryBuilder()
          .select("*")
          .from_table("products")
          .build())
print(f"  SQL : {query2}")
