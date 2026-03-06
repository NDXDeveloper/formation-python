# ============================================================================
#   Section 11.6.2 : Modeles et relations
#   Description : Relations SQLAlchemy - One-to-Many, Many-to-Many,
#                 One-to-One, cascades, eager loading, auto-referentiel,
#                 Association Object, exemple complet Bibliotheque
#   Fichier source : 06.2-modeles-et-relations.md
# ============================================================================

"""Relations SQLAlchemy : tous les types de relations entre modeles."""

import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload, selectinload

DB_PATH = "/tmp/sqlalchemy_relations_demo.db"
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

Base = declarative_base()
engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)
Session = sessionmaker(bind=engine)


# ============================================================
# PARTIE 1 : One-to-Many (Auteur / Livre)
# ============================================================

class Auteur(Base):
    __tablename__ = 'auteurs'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    nationalite = Column(String(50))

    livres = relationship("Livre", back_populates="auteur")

    def __repr__(self):
        return f"<Auteur(nom='{self.nom}')>"


class Livre(Base):
    __tablename__ = 'livres'

    id = Column(Integer, primary_key=True)
    titre = Column(String(200), nullable=False)
    annee_publication = Column(Integer)

    auteur_id = Column(Integer, ForeignKey('auteurs.id'))
    auteur = relationship("Auteur", back_populates="livres")

    def __repr__(self):
        return f"<Livre(titre='{self.titre}')>"


# ============================================================
# PARTIE 2 : Many-to-One (Article / Commentaire)
# ============================================================

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    titre = Column(String(200), nullable=False)
    contenu = Column(String)

    commentaires = relationship("CommentaireArt", back_populates="article")

    def __repr__(self):
        return f"<Article(titre='{self.titre}')>"


class CommentaireArt(Base):
    __tablename__ = 'commentaires'

    id = Column(Integer, primary_key=True)
    texte = Column(String(500), nullable=False)
    auteur_nom = Column(String(100))

    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship("Article", back_populates="commentaires")

    def __repr__(self):
        return f"<Commentaire(auteur='{self.auteur_nom}')>"


# ============================================================
# PARTIE 3 : Many-to-Many (Etudiant / Cours)
# ============================================================

inscription = Table(
    'inscriptions',
    Base.metadata,
    Column('etudiant_id', Integer, ForeignKey('etudiants.id'), primary_key=True),
    Column('cours_id', Integer, ForeignKey('cours.id'), primary_key=True)
)


class Etudiant(Base):
    __tablename__ = 'etudiants'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

    cours = relationship("Cours", secondary=inscription, back_populates="etudiants")

    def __repr__(self):
        return f"<Etudiant(nom='{self.nom} {self.prenom}')>"


class Cours(Base):
    __tablename__ = 'cours'

    id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, nullable=False)
    intitule = Column(String(200), nullable=False)
    credits = Column(Integer)

    etudiants = relationship("Etudiant", secondary=inscription, back_populates="cours")

    def __repr__(self):
        return f"<Cours(code='{self.code}', intitule='{self.intitule}')>"


# ============================================================
# PARTIE 4 : One-to-One (Utilisateur / Profil)
# ============================================================

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    profil = relationship("Profil", back_populates="utilisateur", uselist=False)

    def __repr__(self):
        return f"<Utilisateur(username='{self.username}')>"


class Profil(Base):
    __tablename__ = 'profils'

    id = Column(Integer, primary_key=True)
    bio = Column(String(500))
    site_web = Column(String(200))
    date_naissance = Column(String(20))

    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'), unique=True)
    utilisateur = relationship("Utilisateur", back_populates="profil")

    def __repr__(self):
        return f"<Profil(utilisateur='{self.utilisateur.username if self.utilisateur else None}')>"


# ============================================================
# PARTIE 5 : Cascade (Auteur / Livre avec delete-orphan)
# ============================================================

class AuteurCascade(Base):
    __tablename__ = 'auteurs_cascade'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100))

    livres = relationship(
        "LivreCascade",
        back_populates="auteur",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<AuteurCascade(nom='{self.nom}')>"


class LivreCascade(Base):
    __tablename__ = 'livres_cascade'

    id = Column(Integer, primary_key=True)
    titre = Column(String(200))
    auteur_id = Column(Integer, ForeignKey('auteurs_cascade.id'))
    auteur = relationship("AuteurCascade", back_populates="livres")

    def __repr__(self):
        return f"<LivreCascade(titre='{self.titre}')>"


# ============================================================
# PARTIE 6 : Auto-referentiel (Employe / Manager)
# ============================================================

class Employe(Base):
    __tablename__ = 'employes'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    poste = Column(String(100))

    manager_id = Column(Integer, ForeignKey('employes.id'))
    manager = relationship("Employe", remote_side=[id], backref="equipe")

    def __repr__(self):
        return f"<Employe(nom='{self.nom}', poste='{self.poste}')>"


# ============================================================
# PARTIE 7 : Association Object (Inscription avec notes)
# ============================================================

class InscriptionNote(Base):
    __tablename__ = 'inscriptions_notes'

    etudiant_id = Column(Integer, ForeignKey('etudiants_v2.id'), primary_key=True)
    cours_id = Column(Integer, ForeignKey('cours_v2.id'), primary_key=True)

    note = Column(Integer)
    date_inscription = Column(String)
    statut = Column(String(20))

    etudiant = relationship("EtudiantV2", back_populates="inscriptions")
    cours = relationship("CoursV2", back_populates="inscriptions")

    def __repr__(self):
        return f"<Inscription(note={self.note}, statut='{self.statut}')>"


class EtudiantV2(Base):
    __tablename__ = 'etudiants_v2'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100))
    prenom = Column(String(100))

    inscriptions = relationship("InscriptionNote", back_populates="etudiant")


class CoursV2(Base):
    __tablename__ = 'cours_v2'

    id = Column(Integer, primary_key=True)
    code = Column(String(20))
    intitule = Column(String(200))

    inscriptions = relationship("InscriptionNote", back_populates="cours")


# ============================================================
# PARTIE 8 : Exemple complet Bibliotheque
# ============================================================

emprunt_livre = Table(
    'emprunts_livres',
    Base.metadata,
    Column('emprunt_id', Integer, ForeignKey('emprunts.id')),
    Column('livre_id', Integer, ForeignKey('livres_bibli.id'))
)


class BibliothequeLieu(Base):
    __tablename__ = 'bibliotheques'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    adresse = Column(String(200))

    livres = relationship("LivreBibli", back_populates="bibliotheque")


class LivreBibli(Base):
    __tablename__ = 'livres_bibli'

    id = Column(Integer, primary_key=True)
    titre = Column(String(200), nullable=False)
    isbn = Column(String(20), unique=True)

    bibliotheque_id = Column(Integer, ForeignKey('bibliotheques.id'))
    bibliotheque = relationship("BibliothequeLieu", back_populates="livres")

    auteur_id = Column(Integer, ForeignKey('auteurs_bibli.id'))
    auteur = relationship("AuteurBibli", back_populates="livres")

    emprunts = relationship("Emprunt", secondary=emprunt_livre, back_populates="livres")


class AuteurBibli(Base):
    __tablename__ = 'auteurs_bibli'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    nationalite = Column(String(50))

    livres = relationship("LivreBibli", back_populates="auteur")


class Membre(Base):
    __tablename__ = 'membres'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

    emprunts = relationship("Emprunt", back_populates="membre")


class Emprunt(Base):
    __tablename__ = 'emprunts'

    id = Column(Integer, primary_key=True)
    date_emprunt = Column(String(20), nullable=False)
    date_retour_prevue = Column(String(20))

    membre_id = Column(Integer, ForeignKey('membres.id'))
    membre = relationship("Membre", back_populates="emprunts")

    livres = relationship("LivreBibli", secondary=emprunt_livre, back_populates="emprunts")


# === Creer toutes les tables ===
Base.metadata.create_all(engine)


# ============================================================
# TESTS
# ============================================================

# === PARTIE 1 : One-to-Many ===
print("=" * 50)
print("PARTIE 1 : One-to-Many (Auteur / Livre)")
print("=" * 50)

session = Session()

# Methode 1 : append
victor_hugo = Auteur(nom="Victor Hugo", nationalite="Francaise")
livre1 = Livre(titre="Les Miserables", annee_publication=1862)
livre2 = Livre(titre="Notre-Dame de Paris", annee_publication=1831)
livre3 = Livre(titre="Les Contemplations", annee_publication=1856)

victor_hugo.livres.append(livre1)
victor_hugo.livres.append(livre2)
victor_hugo.livres.append(livre3)

session.add(victor_hugo)
session.commit()

print(f"  Auteur cree avec {len(victor_hugo.livres)} livres")

# Methode 2 : association directe
moliere = Auteur(nom="Moliere", nationalite="Francaise")
session.add(moliere)
session.flush()

livre4 = Livre(titre="Le Malade imaginaire", annee_publication=1673, auteur=moliere)
livre5 = Livre(titre="Tartuffe", annee_publication=1664, auteur_id=moliere.id)

session.add_all([livre4, livre5])
session.commit()

# Recuperation des donnees liees
auteur = session.query(Auteur).filter(Auteur.nom == "Victor Hugo").first()
print(f"\n  {auteur.nom} a ecrit {len(auteur.livres)} livres :")
for livre in auteur.livres:
    print(f"    - {livre.titre} ({livre.annee_publication})")

livre = session.query(Livre).filter(Livre.titre == "Les Miserables").first()
print(f"\n  '{livre.titre}' a ete ecrit par {livre.auteur.nom}")

auteur2 = session.query(Auteur).filter(Auteur.nom == "Moliere").first()
print(f"\n  {auteur2.nom} a ecrit {len(auteur2.livres)} livres :")
for l in auteur2.livres:
    print(f"    - {l.titre} ({l.annee_publication})")

session.close()


# === PARTIE 2 : Many-to-One ===
print(f"\n{'=' * 50}")
print("PARTIE 2 : Many-to-One (Article / Commentaire)")
print("=" * 50)

session = Session()

article = Article(
    titre="Introduction a SQLAlchemy",
    contenu="SQLAlchemy est un ORM puissant..."
)

commentaire1 = CommentaireArt(texte="Excellent article !", auteur_nom="Alice")
commentaire2 = CommentaireArt(texte="Tres instructif", auteur_nom="Bob")
commentaire3 = CommentaireArt(texte="Merci pour le partage", auteur_nom="Claire")

article.commentaires.extend([commentaire1, commentaire2, commentaire3])

session.add(article)
session.commit()

print(f"\n  Article : {article.titre}")
print(f"  Nombre de commentaires : {len(article.commentaires)}")
for comm in article.commentaires:
    print(f"    - {comm.auteur_nom} : {comm.texte}")

session.close()


# === PARTIE 3 : Many-to-Many ===
print(f"\n{'=' * 50}")
print("PARTIE 3 : Many-to-Many (Etudiant / Cours)")
print("=" * 50)

session = Session()

etudiant1 = Etudiant(nom="Durand", prenom="Sophie", email="sophie.durand@school.com")
etudiant2 = Etudiant(nom="Martin", prenom="Lucas", email="lucas.martin@school.com")
etudiant3 = Etudiant(nom="Bernard", prenom="Emma", email="emma.bernard@school.com")

cours1 = Cours(code="MATH101", intitule="Mathematiques avancees", credits=6)
cours2 = Cours(code="INFO202", intitule="Programmation Python", credits=5)
cours3 = Cours(code="PHYS150", intitule="Physique quantique", credits=4)

# Sophie : Math + Python
etudiant1.cours.append(cours1)
etudiant1.cours.append(cours2)

# Lucas : Python + Physique
etudiant2.cours.extend([cours2, cours3])

# Emma : les trois
etudiant3.cours = [cours1, cours2, cours3]

session.add_all([etudiant1, etudiant2, etudiant3])
session.commit()

print("\n  === Inscriptions par etudiant ===")
for etudiant in session.query(Etudiant).all():
    print(f"\n  {etudiant.prenom} {etudiant.nom} :")
    for c in etudiant.cours:
        print(f"    - {c.code} : {c.intitule}")

print("\n  === Etudiants par cours ===")
for c in session.query(Cours).all():
    print(f"\n  {c.code} - {c.intitule} ({len(c.etudiants)} etudiants) :")
    for e in c.etudiants:
        print(f"    - {e.prenom} {e.nom}")

# Manipulation : ajouter puis retirer
sophie = session.query(Etudiant).filter(Etudiant.prenom == "Sophie").first()
physique = session.query(Cours).filter(Cours.code == "PHYS150").first()
sophie.cours.append(physique)
session.commit()
print(f"\n  Sophie inscrite a {len(sophie.cours)} cours (apres ajout Physique)")

sophie.cours.remove(physique)
session.commit()
print(f"  Sophie inscrite a {len(sophie.cours)} cours (apres retrait Physique)")

# Verification d'appartenance
if cours2 in etudiant2.cours:
    print(f"  Lucas est inscrit au cours de Python")

session.close()


# === PARTIE 4 : One-to-One ===
print(f"\n{'=' * 50}")
print("PARTIE 4 : One-to-One (Utilisateur / Profil)")
print("=" * 50)

session = Session()

user = Utilisateur(username="alice_dev", email="alice@dev.com")
profil = Profil(
    bio="Developpeuse Python passionnee",
    site_web="https://alice-dev.com",
    date_naissance="15/03/1990"
)

user.profil = profil

session.add(user)
session.commit()

print(f"\n  Utilisateur : {user.username}")
print(f"  Bio : {user.profil.bio}")
print(f"  Site web : {user.profil.site_web}")

# Sens inverse
profil_recupere = session.query(Profil).first()
print(f"\n  Ce profil appartient a : {profil_recupere.utilisateur.username}")

# Verifier que uselist=False donne un objet, pas une liste
print(f"  Type de user.profil : {type(user.profil).__name__} (pas une liste)")

session.close()


# === PARTIE 5 : Cascade delete-orphan ===
print(f"\n{'=' * 50}")
print("PARTIE 5 : Cascade (delete-orphan)")
print("=" * 50)

session = Session()

auteur_c = AuteurCascade(nom="Auteur Test")
livre_c1 = LivreCascade(titre="Livre Cascade 1")
livre_c2 = LivreCascade(titre="Livre Cascade 2")
livre_c3 = LivreCascade(titre="Livre Cascade 3")

auteur_c.livres = [livre_c1, livre_c2, livre_c3]
session.add(auteur_c)
session.commit()

print(f"\n  Auteur: {auteur_c.nom}, {len(auteur_c.livres)} livres")

# Retirer un livre -> delete-orphan le supprime de la base
auteur_c.livres.remove(livre_c3)
session.commit()

count = session.query(LivreCascade).count()
print(f"  Apres retrait d'un livre : {count} livres en base (orphelin supprime)")

# Supprimer l'auteur -> cascade supprime tous ses livres
session.delete(auteur_c)
session.commit()

count = session.query(LivreCascade).count()
print(f"  Apres suppression auteur : {count} livres en base (cascade)")

session.close()


# === PARTIE 6 : Auto-referentiel ===
print(f"\n{'=' * 50}")
print("PARTIE 6 : Auto-referentiel (Employe / Manager)")
print("=" * 50)

session = Session()

ceo = Employe(nom="Directrice Generale", poste="CEO")
manager1 = Employe(nom="Chef Ventes", poste="Manager", manager=ceo)
manager2 = Employe(nom="Chef IT", poste="Manager", manager=ceo)
employe1 = Employe(nom="Vendeur 1", poste="Commercial", manager=manager1)
employe2 = Employe(nom="Vendeur 2", poste="Commercial", manager=manager1)
employe3 = Employe(nom="Developpeur", poste="Developer", manager=manager2)

session.add(ceo)
session.commit()

print(f"\n  {ceo.nom} manage :")
for manager in ceo.equipe:
    print(f"    - {manager.nom} ({manager.poste})")
    if manager.equipe:
        for employe in manager.equipe:
            print(f"      - {employe.nom} ({employe.poste})")

session.close()


# === PARTIE 7 : Association Object ===
print(f"\n{'=' * 50}")
print("PARTIE 7 : Association Object (Inscription avec notes)")
print("=" * 50)

session = Session()

etudiant_v2 = EtudiantV2(nom="Dupont", prenom="Marie")
cours_v2 = CoursV2(code="MATH101", intitule="Mathematiques")

insc = InscriptionNote(
    etudiant=etudiant_v2,
    cours=cours_v2,
    note=15,
    date_inscription="2024-09-01",
    statut="en_cours"
)

session.add_all([etudiant_v2, cours_v2, insc])
session.commit()

print(f"\n  Inscription creee:")
for i in etudiant_v2.inscriptions:
    print(f"    {etudiant_v2.prenom} a eu {i.note}/20 en {i.cours.intitule}")
    print(f"    Date: {i.date_inscription}, Statut: {i.statut}")

session.close()


# === PARTIE 8 : Exemple complet Bibliotheque ===
print(f"\n{'=' * 50}")
print("PARTIE 8 : Exemple complet Bibliotheque")
print("=" * 50)

session = Session()

bibli = BibliothequeLieu(nom="Bibliotheque Municipale", adresse="12 rue de la Paix")

hugo = AuteurBibli(nom="Victor Hugo", nationalite="Francaise")
dumas = AuteurBibli(nom="Alexandre Dumas", nationalite="Francaise")

l1 = LivreBibli(titre="Les Miserables", isbn="978-0-1234-5678-9", auteur=hugo, bibliotheque=bibli)
l2 = LivreBibli(titre="Notre-Dame de Paris", isbn="978-0-1234-5679-6", auteur=hugo, bibliotheque=bibli)
l3 = LivreBibli(titre="Les Trois Mousquetaires", isbn="978-0-1234-5680-2", auteur=dumas, bibliotheque=bibli)

membre = Membre(nom="Sophie Martin", email="sophie.martin@email.com")

emprunt = Emprunt(
    date_emprunt="2024-01-15",
    date_retour_prevue="2024-02-15",
    membre=membre
)
emprunt.livres.extend([l1, l3])

session.add_all([bibli, hugo, dumas, membre, emprunt])
session.commit()

print(f"\n  === {bibli.nom} ===")
print(f"  Nombre de livres : {len(bibli.livres)}")
print(f"\n  Livres de Victor Hugo :")
for livre in hugo.livres:
    print(f"    - {livre.titre}")

print(f"\n  Emprunts de {membre.nom} :")
for emp in membre.emprunts:
    print(f"    Date : {emp.date_emprunt}")
    print(f"    Livres empruntes :")
    for livre in emp.livres:
        print(f"      - {livre.titre} par {livre.auteur.nom}")

session.close()


# === Eager loading demo ===
print(f"\n{'=' * 50}")
print("BONUS : Eager Loading (joinedload / selectinload)")
print("=" * 50)

session = Session()

# joinedload : une seule requete avec JOIN
auteurs_joined = session.query(Auteur).options(joinedload(Auteur.livres)).all()
print(f"\n  joinedload - {len(auteurs_joined)} auteurs charges avec leurs livres :")
for a in auteurs_joined:
    print(f"    {a.nom} : {len(a.livres)} livres")

session.close()

session = Session()

# selectinload : deux requetes optimisees
auteurs_selectin = session.query(Auteur).options(selectinload(Auteur.livres)).all()
print(f"\n  selectinload - {len(auteurs_selectin)} auteurs charges avec leurs livres :")
for a in auteurs_selectin:
    print(f"    {a.nom} : {len(a.livres)} livres")

session.close()


# === Etat final ===
print(f"\n{'=' * 50}")
print("ETAT FINAL")
print("=" * 50)

session = Session()
print(f"  Auteurs : {session.query(Auteur).count()}")
print(f"  Livres : {session.query(Livre).count()}")
print(f"  Articles : {session.query(Article).count()}")
print(f"  Commentaires : {session.query(CommentaireArt).count()}")
print(f"  Etudiants : {session.query(Etudiant).count()}")
print(f"  Cours : {session.query(Cours).count()}")
print(f"  Utilisateurs : {session.query(Utilisateur).count()}")
print(f"  Employes : {session.query(Employe).count()}")
print(f"  Bibliotheques : {session.query(BibliothequeLieu).count()}")
print(f"  Membres : {session.query(Membre).count()}")
print(f"  Emprunts : {session.query(Emprunt).count()}")
session.close()

# Nettoyage
os.remove(DB_PATH)
print("\nBase de donnees nettoyee.")
