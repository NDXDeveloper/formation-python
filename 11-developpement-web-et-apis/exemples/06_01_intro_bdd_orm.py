# ============================================================================
#   Section 11.6 : Bases de donnees et ORM (SQLite + SQLAlchemy)
#   Description : Comparaison SQL brut (sqlite3) vs ORM (SQLAlchemy),
#                 concepts fondamentaux, CRUD basique
#   Fichier source : 06-bases-de-donnees-orm-sqlalchemy.md
# ============================================================================

"""Comparaison SQL brut vs ORM SQLAlchemy."""

import sqlite3
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_FILE_RAW = "/tmp/demo_raw.db"
DB_FILE_ORM = "/tmp/demo_orm.db"

# Nettoyage des fichiers precedents
for f in [DB_FILE_RAW, DB_FILE_ORM]:
    if os.path.exists(f):
        os.remove(f)


# ============================================================
# PARTIE 1 : SQL brut avec sqlite3
# ============================================================
print("=" * 50)
print("PARTIE 1 : SQL brut avec sqlite3")
print("=" * 50)

conn = sqlite3.connect(DB_FILE_RAW)
cursor = conn.cursor()

# Creer une table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
''')

# Inserer des donnees
cursor.execute(
    "INSERT INTO users (nom, email, age) VALUES (?, ?, ?)",
    ("Alice", "alice@example.com", 28)
)
cursor.execute(
    "INSERT INTO users (nom, email, age) VALUES (?, ?, ?)",
    ("Bob", "bob@example.com", 35)
)
cursor.execute(
    "INSERT INTO users (nom, email, age) VALUES (?, ?, ?)",
    ("Claire", "claire@example.com", 42)
)
conn.commit()

# Lire toutes les donnees
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("\nTous les utilisateurs (SQL brut) :")
for row in rows:
    print(f"  ID: {row[0]}, Nom: {row[1]}, Email: {row[2]}, Age: {row[3]}")

# Filtrer
cursor.execute("SELECT * FROM users WHERE age > ?", (30,))
rows = cursor.fetchall()
print(f"\nUtilisateurs age > 30 : {len(rows)}")
for row in rows:
    print(f"  {row[1]} ({row[3]} ans)")

# Mettre a jour
cursor.execute("UPDATE users SET age = ? WHERE nom = ?", (29, "Alice"))
conn.commit()

# Verifier la mise a jour
cursor.execute("SELECT * FROM users WHERE nom = ?", ("Alice",))
row = cursor.fetchone()
print(f"\nApres mise a jour : {row[1]} a {row[3]} ans")

# Supprimer
cursor.execute("DELETE FROM users WHERE id = ?", (3,))
conn.commit()

cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]
print(f"\nApres suppression : {count} utilisateurs")

conn.close()


# ============================================================
# PARTIE 2 : ORM avec SQLAlchemy
# ============================================================
print("\n" + "=" * 50)
print("PARTIE 2 : ORM avec SQLAlchemy")
print("=" * 50)

# Configuration
Base = declarative_base()
engine = create_engine(f'sqlite:///{DB_FILE_ORM}', echo=False)
Session = sessionmaker(bind=engine)


# Definir le modele
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    age = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, nom='{self.nom}', age={self.age})"


# Creer les tables
Base.metadata.create_all(engine)

# Utiliser une session
session = Session()

# Inserer des donnees (comme des objets Python)
alice = User(nom="Alice", email="alice@example.com", age=28)
bob = User(nom="Bob", email="bob@example.com", age=35)
claire = User(nom="Claire", email="claire@example.com", age=42)

session.add_all([alice, bob, claire])
session.commit()

# Lire toutes les donnees
users = session.query(User).all()
print("\nTous les utilisateurs (ORM) :")
for user in users:
    print(f"  {user}")

# Filtrer
users_30plus = session.query(User).filter(User.age > 30).all()
print(f"\nUtilisateurs age > 30 : {len(users_30plus)}")
for user in users_30plus:
    print(f"  {user.nom} ({user.age} ans)")

# Chercher un utilisateur specifique
alice = session.query(User).filter(User.nom == "Alice").first()
print(f"\nAlice trouvee : ID={alice.id}, Email={alice.email}")

# Mettre a jour (naturellement en Python)
alice.age = 29
session.commit()
print(f"Apres mise a jour : Alice a {alice.age} ans")

# Supprimer
claire = session.query(User).filter(User.nom == "Claire").first()
session.delete(claire)
session.commit()

count = session.query(User).count()
print(f"\nApres suppression : {count} utilisateurs")

session.close()


# ============================================================
# COMPARAISON
# ============================================================
print("\n" + "=" * 50)
print("COMPARAISON")
print("=" * 50)

comparaison = [
    ("Creation table", "cursor.execute('CREATE TABLE...')", "class User(Base): ..."),
    ("Insertion", "cursor.execute('INSERT...')", "session.add(User(...))"),
    ("Lecture", "cursor.fetchall() -> tuples", "session.query(User) -> objets"),
    ("Mise a jour", "cursor.execute('UPDATE...')", "user.age = 29"),
    ("Suppression", "cursor.execute('DELETE...')", "session.delete(user)"),
    ("Securite", "Injections SQL possibles", "Protection automatique"),
]

print(f"\n{'Operation':15s} {'SQL brut':35s} {'SQLAlchemy ORM'}")
print("-" * 85)
for op, sql, orm in comparaison:
    print(f"{op:15s} {sql:35s} {orm}")

# Nettoyage
os.remove(DB_FILE_RAW)
os.remove(DB_FILE_ORM)
print("\nFichiers temporaires nettoyes.")
