# ============================================================================
#   Section 11.6.1 : Introduction a SQLAlchemy
#   Description : CRUD complet avec SQLAlchemy ORM - configuration, modeles,
#                 sessions, transactions, context manager, types de colonnes
#   Fichier source : 06.1-introduction-sqlalchemy.md
# ============================================================================

"""CRUD complet avec SQLAlchemy ORM."""

import os
from contextlib import contextmanager
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DB_PATH = "/tmp/sqlalchemy_crud_demo.db"
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# --- Configuration ---
Base = declarative_base()
engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)
Session = sessionmaker(bind=engine)


# --- Modele ---
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, nom='{self.nom}', email='{self.email}', age={self.age})>"


class Produit(Base):
    __tablename__ = 'produits'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    description = Column(Text)
    prix = Column(Float)
    en_stock = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Produit('{self.nom}', prix={self.prix}, stock={self.en_stock})>"


# Creer les tables
Base.metadata.create_all(engine)


# --- Context manager pour les sessions ---
@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


# === CREATE ===
print("=== CREATE ===")

with get_session() as session:
    # Ajouter un seul utilisateur
    alice = User(nom="Alice Dupont", email="alice@example.com", age=28)
    session.add(alice)
    session.flush()  # Pour obtenir l'ID avant le commit
    print(f"  Cree: {alice}")

    # Ajouter plusieurs a la fois
    users = [
        User(nom="Bob Martin", email="bob@example.com", age=35),
        User(nom="Claire Petit", email="claire@example.com", age=42),
        User(nom="David Leroux", email="david@example.com", age=29),
    ]
    session.add_all(users)

print(f"  {3 + 1} utilisateurs crees")

# Produits
with get_session() as session:
    produits = [
        Produit(nom="Laptop", description="Ordinateur portable", prix=899.99, en_stock=True),
        Produit(nom="Souris", description="Souris sans fil", prix=29.99, en_stock=True),
        Produit(nom="Clavier", description="Clavier mecanique", prix=79.99, en_stock=False),
    ]
    session.add_all(produits)

print(f"  3 produits crees")


# === READ ===
print("\n=== READ ===")

with get_session() as session:
    # Tous les utilisateurs
    all_users = session.query(User).all()
    print(f"\n  Tous ({len(all_users)} users):")
    for u in all_users:
        print(f"    {u}")

    # Par ID
    user_1 = session.get(User, 1)
    print(f"\n  Par ID (1): {user_1}")

    # Filtrer : age > 30
    users_30plus = session.query(User).filter(User.age > 30).all()
    print(f"\n  Age > 30 ({len(users_30plus)}):")
    for u in users_30plus:
        print(f"    {u.nom} ({u.age} ans)")

    # Par email (first)
    user = session.query(User).filter(User.email == "alice@example.com").first()
    print(f"\n  Par email: {user}")

    # Compter
    count = session.query(User).count()
    print(f"\n  Nombre total: {count}")

    # Produits en stock
    en_stock = session.query(Produit).filter(Produit.en_stock == True).all()
    print(f"\n  Produits en stock ({len(en_stock)}):")
    for p in en_stock:
        print(f"    {p.nom} - {p.prix} EUR")


# === UPDATE ===
print("\n=== UPDATE ===")

with get_session() as session:
    # Modifier un utilisateur
    user = session.query(User).filter(User.nom == "Alice Dupont").first()
    print(f"  Avant: {user}")
    user.age = 29
    user.email = "alice.dupont@example.com"

# Verification
with get_session() as session:
    user = session.get(User, 1)
    print(f"  Apres: {user}")


# === DELETE ===
print("\n=== DELETE ===")

with get_session() as session:
    user = session.query(User).filter(User.nom == "Bob Martin").first()
    print(f"  Suppression de: {user}")
    session.delete(user)

with get_session() as session:
    count = session.query(User).count()
    print(f"  Utilisateurs restants: {count}")


# === TRANSACTIONS (rollback) ===
print("\n=== TRANSACTIONS (rollback sur erreur) ===")

try:
    with get_session() as session:
        session.add(User(nom="Test", email="test@example.com", age=20))
        # Tenter d'ajouter un email en double -> IntegrityError
        session.add(User(nom="Test2", email="test@example.com", age=25))
except Exception as e:
    print(f"  Erreur capturee: {type(e).__name__}")
    print(f"  Transaction annulee (rollback automatique)")

with get_session() as session:
    test_user = session.query(User).filter(User.nom == "Test").first()
    print(f"  User 'Test' existe ? {test_user is not None}")


# === Types de colonnes ===
print("\n=== Types de colonnes ===")

with get_session() as session:
    produit = session.query(Produit).first()
    print(f"  String: nom = '{produit.nom}'")
    print(f"  Text: description = '{produit.description}'")
    print(f"  Float: prix = {produit.prix}")
    print(f"  Boolean: en_stock = {produit.en_stock}")
    print(f"  Integer: id = {produit.id}")


# === Etat final ===
print("\n=== Etat final ===")

with get_session() as session:
    print(f"  Utilisateurs: {session.query(User).count()}")
    print(f"  Produits: {session.query(Produit).count()}")
    for u in session.query(User).all():
        print(f"    {u}")

# Nettoyage
os.remove(DB_PATH)
print("\nBase de donnees nettoyee.")
