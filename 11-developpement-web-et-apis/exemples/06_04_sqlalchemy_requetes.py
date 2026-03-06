# ============================================================================
#   Section 11.6.3 : Requetes et migrations
#   Description : Requetes avancees SQLAlchemy - filtres multiples, operateurs
#                 logiques (and_, or_, not_), comparaisons (like, in_, between),
#                 tri, pagination, jointures, agregations, sous-requetes,
#                 SQL brut, eager loading, fonction de recherche avancee
#   Fichier source : 06.3-requetes-et-migrations.md
# ============================================================================

"""Requetes avancees avec SQLAlchemy."""

import os
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey,
    func, and_, or_, not_, text
)
from sqlalchemy.orm import (
    declarative_base, relationship, sessionmaker,
    joinedload, selectinload
)

DB_PATH = "/tmp/sqlalchemy_requetes_demo.db"
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

Base = declarative_base()
engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)
Session = sessionmaker(bind=engine)


# --- Modeles ---

class Auteur(Base):
    __tablename__ = 'auteurs'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    nationalite = Column(String(50))
    annee_naissance = Column(Integer)

    livres = relationship("Livre", back_populates="auteur")

    def __repr__(self):
        return f"<Auteur(nom='{self.nom}')>"


class Livre(Base):
    __tablename__ = 'livres'

    id = Column(Integer, primary_key=True)
    titre = Column(String(200), nullable=False)
    annee_publication = Column(Integer)
    prix = Column(Float)
    nb_pages = Column(Integer)

    auteur_id = Column(Integer, ForeignKey('auteurs.id'))
    auteur = relationship("Auteur", back_populates="livres")

    def __repr__(self):
        return f"<Livre(titre='{self.titre}')>"


Base.metadata.create_all(engine)


# --- Peupler la base ---

session = Session()

auteurs = [
    Auteur(nom="Victor Hugo", nationalite="Francaise", annee_naissance=1802),
    Auteur(nom="Alexandre Dumas", nationalite="Francaise", annee_naissance=1802),
    Auteur(nom="Charles Dickens", nationalite="Anglaise", annee_naissance=1812),
    Auteur(nom="Guido van Rossum", nationalite="Neerlandaise", annee_naissance=1956),
]
session.add_all(auteurs)
session.flush()

livres = [
    # Victor Hugo
    Livre(titre="Les Miserables", annee_publication=1862, prix=12.50,
          nb_pages=1900, auteur_id=auteurs[0].id),
    Livre(titre="Notre-Dame de Paris", annee_publication=1831, prix=9.90,
          nb_pages=940, auteur_id=auteurs[0].id),
    Livre(titre="Les Contemplations", annee_publication=1856, prix=8.50,
          nb_pages=400, auteur_id=auteurs[0].id),
    # Alexandre Dumas
    Livre(titre="Les Trois Mousquetaires", annee_publication=1844, prix=11.00,
          nb_pages=700, auteur_id=auteurs[1].id),
    Livre(titre="Le Comte de Monte-Cristo", annee_publication=1846, prix=14.90,
          nb_pages=1200, auteur_id=auteurs[1].id),
    # Charles Dickens
    Livre(titre="Oliver Twist", annee_publication=1839, prix=10.50,
          nb_pages=450, auteur_id=auteurs[2].id),
    Livre(titre="A Tale of Two Cities", annee_publication=1859, prix=9.00,
          nb_pages=350, auteur_id=auteurs[2].id),
    # Guido van Rossum
    Livre(titre="Python Programming", annee_publication=2005, prix=35.00,
          nb_pages=500, auteur_id=auteurs[3].id),
    Livre(titre="Advanced Python Patterns", annee_publication=2018, prix=42.00,
          nb_pages=380, auteur_id=auteurs[3].id),
    # Livre sans auteur (pour tester outerjoin)
    Livre(titre="Anonyme ancien", annee_publication=1750, prix=None,
          nb_pages=200, auteur_id=None),
]
session.add_all(livres)
session.commit()

print(f"Base peuplee : {session.query(Auteur).count()} auteurs, "
      f"{session.query(Livre).count()} livres")


# ============================================================
# FILTRES MULTIPLES
# ============================================================
print(f"\n{'=' * 50}")
print("FILTRES MULTIPLES")
print("=" * 50)

# Methode 1 : Chainage de filter()
livres_r = session.query(Livre)\
    .filter(Livre.annee_publication > 1840)\
    .filter(Livre.prix < 15)\
    .all()
print(f"\n  Chainage filter (annee>1840 ET prix<15) : {len(livres_r)} livres")
for l in livres_r:
    print(f"    {l.titre} - {l.prix} EUR ({l.annee_publication})")

# Methode 2 : Conditions dans un seul filter()
livres_r2 = session.query(Livre)\
    .filter(
        Livre.annee_publication > 1840,
        Livre.prix < 15
    ).all()
print(f"\n  Multi-conditions dans filter() : {len(livres_r2)} livres (meme resultat)")


# ============================================================
# OPERATEURS LOGIQUES (and_, or_, not_)
# ============================================================
print(f"\n{'=' * 50}")
print("OPERATEURS LOGIQUES")
print("=" * 50)

# AND
livres_and = session.query(Livre).filter(
    and_(
        Livre.annee_publication > 1840,
        Livre.prix < 15
    )
).all()
print(f"\n  and_(annee>1840, prix<15) : {len(livres_and)} livres")

# OR
livres_or = session.query(Livre).filter(
    or_(
        Livre.annee_publication < 1840,
        Livre.annee_publication > 2000
    )
).all()
print(f"\n  or_(annee<1840, annee>2000) : {len(livres_or)} livres")
for l in livres_or:
    print(f"    {l.titre} ({l.annee_publication})")

# NOT
livres_not = session.query(Livre).filter(
    not_(Livre.titre.like('%Python%'))
).all()
print(f"\n  not_(titre contient 'Python') : {len(livres_not)} livres")

# Combinaison complexe : (annee > 2000 ET prix < 40) OU (auteur francais ET pages > 500)
livres_complex = session.query(Livre)\
    .join(Auteur)\
    .filter(
        or_(
            and_(Livre.annee_publication > 2000, Livre.prix < 40),
            and_(Auteur.nationalite == "Francaise", Livre.nb_pages > 500)
        )
    ).all()
print(f"\n  Combinaison complexe : {len(livres_complex)} livres")
for l in livres_complex:
    print(f"    {l.titre} ({l.annee_publication}, {l.nb_pages}p, {l.prix} EUR)")


# ============================================================
# OPERATEURS DE COMPARAISON
# ============================================================
print(f"\n{'=' * 50}")
print("OPERATEURS DE COMPARAISON")
print("=" * 50)

# LIKE
livres_like = session.query(Livre).filter(Livre.titre.like('Le%')).all()
print(f"\n  LIKE 'Le%' : {len(livres_like)} livres")
for l in livres_like:
    print(f"    {l.titre}")

# func.lower pour insensibilite a la casse
livres_lower = session.query(Livre).filter(
    func.lower(Livre.titre).like('%python%')
).all()
print(f"\n  LIKE insensible casse '%python%' : {len(livres_lower)} livres")
for l in livres_lower:
    print(f"    {l.titre}")

# IN
livres_in = session.query(Livre).filter(
    Livre.annee_publication.in_([1862, 1844, 2005])
).all()
print(f"\n  IN [1862, 1844, 2005] : {len(livres_in)} livres")
for l in livres_in:
    print(f"    {l.titre} ({l.annee_publication})")

# NOT IN
livres_notin = session.query(Livre).filter(
    Livre.annee_publication.notin_([1862, 1844, 2005])
).all()
print(f"\n  NOT IN [1862, 1844, 2005] : {len(livres_notin)} livres")

# BETWEEN
livres_between = session.query(Livre).filter(
    Livre.annee_publication.between(1840, 1860)
).all()
print(f"\n  BETWEEN 1840 et 1860 : {len(livres_between)} livres")
for l in livres_between:
    print(f"    {l.titre} ({l.annee_publication})")

# IS NULL
livres_null = session.query(Livre).filter(Livre.prix.is_(None)).all()
print(f"\n  IS NULL (prix) : {len(livres_null)} livres")
for l in livres_null:
    print(f"    {l.titre}")

# IS NOT NULL
livres_notnull = session.query(Livre).filter(Livre.prix.is_not(None)).all()
print(f"\n  IS NOT NULL (prix) : {len(livres_notnull)} livres")


# ============================================================
# TRI (ORDER BY)
# ============================================================
print(f"\n{'=' * 50}")
print("TRI")
print("=" * 50)

# Tri croissant par titre
livres_tri = session.query(Livre).order_by(Livre.titre).all()
print(f"\n  Tri par titre (croissant) :")
for l in livres_tri[:3]:
    print(f"    {l.titre}")
print(f"    ... ({len(livres_tri)} au total)")

# Tri decroissant par prix
livres_tri_desc = session.query(Livre)\
    .filter(Livre.prix.is_not(None))\
    .order_by(Livre.prix.desc())\
    .all()
print(f"\n  Tri par prix (decroissant) :")
for l in livres_tri_desc[:3]:
    print(f"    {l.titre} - {l.prix} EUR")

# Tri multi-colonnes
auteurs_tri = session.query(Auteur)\
    .order_by(Auteur.nationalite, Auteur.nom)\
    .all()
print(f"\n  Tri par nationalite puis nom :")
for a in auteurs_tri:
    print(f"    {a.nom} ({a.nationalite})")


# ============================================================
# PAGINATION (LIMIT / OFFSET)
# ============================================================
print(f"\n{'=' * 50}")
print("PAGINATION")
print("=" * 50)

# Limit
livres_5 = session.query(Livre).limit(5).all()
print(f"\n  limit(5) : {len(livres_5)} livres")

# Offset + Limit (page 2, 3 par page)
page = 2
par_page = 3
livres_page = session.query(Livre)\
    .offset((page - 1) * par_page)\
    .limit(par_page)\
    .all()
print(f"  Page {page} (par_page={par_page}) : {len(livres_page)} livres")
for l in livres_page:
    print(f"    {l.titre}")

# first() vs one_or_none()
livre_first = session.query(Livre).filter(Livre.id == 1).first()
print(f"\n  first() id=1 : {livre_first.titre}")

livre_none = session.query(Livre).filter(Livre.titre == "Inexistant").one_or_none()
print(f"  one_or_none() inexistant : {livre_none}")


# ============================================================
# SELECTION DE COLONNES
# ============================================================
print(f"\n{'=' * 50}")
print("SELECTION DE COLONNES")
print("=" * 50)

# Colonnes specifiques
resultats = session.query(Livre.titre, Livre.prix)\
    .filter(Livre.prix.is_not(None))\
    .order_by(Livre.prix)\
    .limit(4)\
    .all()
print(f"\n  Titre et prix (top 4 moins chers) :")
for titre, prix in resultats:
    print(f"    {titre} : {prix} EUR")

# Avec jointure
resultats_join = session.query(Livre.titre, Auteur.nom)\
    .join(Auteur)\
    .limit(5)\
    .all()
print(f"\n  Titre + Auteur (via JOIN) :")
for titre_livre, nom_auteur in resultats_join:
    print(f"    {titre_livre} par {nom_auteur}")

# Labels
resultats_label = session.query(
    Livre.titre.label('titre_livre'),
    Auteur.nom.label('nom_auteur')
).join(Auteur).limit(3).all()
print(f"\n  Avec labels :")
for row in resultats_label:
    print(f"    {row.titre_livre} par {row.nom_auteur}")


# ============================================================
# JOINTURES
# ============================================================
print(f"\n{'=' * 50}")
print("JOINTURES")
print("=" * 50)

# JOIN implicite
livres_join = session.query(Livre).join(Auteur).all()
print(f"\n  JOIN : {len(livres_join)} livres (avec auteur)")

# JOIN avec filtre
livres_fr = session.query(Livre)\
    .join(Auteur, Livre.auteur_id == Auteur.id)\
    .filter(Auteur.nationalite == "Francaise")\
    .all()
print(f"\n  JOIN + filtre nationalite='Francaise' : {len(livres_fr)} livres")
for l in livres_fr:
    print(f"    {l.titre} par {l.auteur.nom}")

# LEFT JOIN (outerjoin)
livres_outer = session.query(Livre).outerjoin(Auteur).all()
print(f"\n  OUTERJOIN : {len(livres_outer)} livres (y compris sans auteur)")
for l in livres_outer:
    auteur_nom = l.auteur.nom if l.auteur else "Inconnu"
    print(f"    {l.titre} par {auteur_nom}")

# JOIN avec filtre complexe
livres_fr_apres = session.query(Livre)\
    .join(Auteur)\
    .filter(Auteur.nationalite == "Francaise")\
    .filter(Livre.annee_publication > 1850)\
    .all()
print(f"\n  Francais + annee>1850 : {len(livres_fr_apres)} livres")
for l in livres_fr_apres:
    print(f"    {l.titre} ({l.annee_publication})")


# ============================================================
# AGREGATIONS
# ============================================================
print(f"\n{'=' * 50}")
print("AGREGATIONS")
print("=" * 50)

# COUNT
nb = session.query(func.count(Livre.id)).scalar()
print(f"\n  COUNT : {nb} livres")

# SUM
total = session.query(func.sum(Livre.prix)).scalar()
print(f"  SUM(prix) : {total:.2f} EUR")

# AVG
moy = session.query(func.avg(Livre.prix)).scalar()
print(f"  AVG(prix) : {moy:.2f} EUR")

# MIN / MAX
prix_min = session.query(func.min(Livre.prix)).scalar()
prix_max = session.query(func.max(Livre.prix)).scalar()
print(f"  MIN(prix) : {prix_min} EUR, MAX(prix) : {prix_max} EUR")

# GROUP BY
print(f"\n  GROUP BY auteur :")
resultats_group = session.query(
    Auteur.nom,
    func.count(Livre.id).label('nombre_livres')
)\
    .join(Livre)\
    .group_by(Auteur.nom)\
    .all()
for nom, nb in resultats_group:
    print(f"    {nom} a ecrit {nb} livre(s)")

# HAVING
print(f"\n  HAVING count > 2 :")
auteurs_prolif = session.query(
    Auteur.nom,
    func.count(Livre.id).label('nombre_livres')
)\
    .join(Livre)\
    .group_by(Auteur.nom)\
    .having(func.count(Livre.id) > 2)\
    .all()
for nom, nb in auteurs_prolif:
    print(f"    {nom} : {nb} livres")


# ============================================================
# SOUS-REQUETES
# ============================================================
print(f"\n{'=' * 50}")
print("SOUS-REQUETES")
print("=" * 50)

# Livres plus chers que la moyenne
prix_moyen_subq = session.query(func.avg(Livre.prix)).scalar_subquery()
livres_chers = session.query(Livre)\
    .filter(Livre.prix > prix_moyen_subq)\
    .all()
print(f"\n  Livres plus chers que la moyenne ({moy:.2f} EUR) : {len(livres_chers)}")
for l in livres_chers:
    print(f"    {l.titre} - {l.prix} EUR")

# Auteurs avec au moins un livre apres 2000
subq = session.query(Livre.auteur_id)\
    .filter(Livre.annee_publication > 2000)\
    .scalar_subquery()
auteurs_modernes = session.query(Auteur)\
    .filter(Auteur.id.in_(subq))\
    .all()
print(f"\n  Auteurs avec livre apres 2000 : {len(auteurs_modernes)}")
for a in auteurs_modernes:
    print(f"    {a.nom}")

# Sous-requete correlee
livre_subq = session.query(
    func.count(Livre.id)
).filter(Livre.auteur_id == Auteur.id).correlate(Auteur).scalar_subquery()

auteurs_avec_compte = session.query(
    Auteur.nom,
    livre_subq.label('nb_livres')
).all()
print(f"\n  Sous-requete correlee (auteur + nb livres) :")
for nom, nb in auteurs_avec_compte:
    print(f"    {nom} : {nb} livre(s)")


# ============================================================
# SQL BRUT
# ============================================================
print(f"\n{'=' * 50}")
print("SQL BRUT")
print("=" * 50)

resultat = session.execute(
    text("SELECT titre, prix FROM livres WHERE prix > :prix ORDER BY prix DESC"),
    {"prix": 20}
)
print(f"\n  SQL brut (prix > 20) :")
for row in resultat:
    print(f"    {row[0]} - {row[1]} EUR")

resultat2 = session.execute(
    text("SELECT titre, annee_publication FROM livres WHERE annee_publication > :annee"),
    {"annee": 2000}
)
print(f"\n  SQL brut (annee > 2000) :")
for row in resultat2:
    print(f"    {row[0]} ({row[1]})")


# ============================================================
# EAGER LOADING
# ============================================================
print(f"\n{'=' * 50}")
print("EAGER LOADING")
print("=" * 50)

session.close()
session = Session()

# selectinload
auteurs_sel = session.query(Auteur)\
    .options(selectinload(Auteur.livres))\
    .all()
print(f"\n  selectinload - {len(auteurs_sel)} auteurs :")
for a in auteurs_sel:
    print(f"    {a.nom} : {len(a.livres)} livres")

session.close()
session = Session()

# joinedload
auteurs_jl = session.query(Auteur)\
    .options(joinedload(Auteur.livres))\
    .all()
print(f"\n  joinedload - {len(auteurs_jl)} auteurs :")
for a in auteurs_jl:
    print(f"    {a.nom} : {len(a.livres)} livres")

session.close()


# ============================================================
# FONCTION DE RECHERCHE AVANCEE
# ============================================================
print(f"\n{'=' * 50}")
print("FONCTION DE RECHERCHE AVANCEE")
print("=" * 50)

session = Session()


def rechercher_livres(
    titre=None,
    auteur_nom=None,
    annee_min=None,
    annee_max=None,
    prix_max=None,
    nationalite=None,
    tri_par='titre',
    ordre='asc',
    page=1,
    par_page=10
):
    """Fonction de recherche flexible avec multiples criteres."""
    query = session.query(Livre).join(Auteur)

    if titre:
        query = query.filter(Livre.titre.like(f'%{titre}%'))
    if auteur_nom:
        query = query.filter(Auteur.nom.like(f'%{auteur_nom}%'))
    if annee_min:
        query = query.filter(Livre.annee_publication >= annee_min)
    if annee_max:
        query = query.filter(Livre.annee_publication <= annee_max)
    if prix_max:
        query = query.filter(Livre.prix <= prix_max)
    if nationalite:
        query = query.filter(Auteur.nationalite == nationalite)

    if tri_par == 'titre':
        colonne = Livre.titre
    elif tri_par == 'prix':
        colonne = Livre.prix
    elif tri_par == 'annee':
        colonne = Livre.annee_publication
    else:
        colonne = Livre.titre

    if ordre == 'desc':
        query = query.order_by(colonne.desc())
    else:
        query = query.order_by(colonne)

    total = query.count()
    livres_res = query.offset((page - 1) * par_page).limit(par_page).all()

    return {
        'livres': livres_res,
        'total': total,
        'page': page,
        'par_page': par_page,
        'total_pages': (total + par_page - 1) // par_page
    }


# Recherche 1 : livres francais
print(f"\n  Recherche : auteurs francais, tri par annee desc")
res = rechercher_livres(nationalite="Francaise", tri_par='annee', ordre='desc')
print(f"  Trouve {res['total']} livre(s), page {res['page']}/{res['total_pages']}")
for l in res['livres']:
    print(f"    {l.titre} ({l.annee_publication}) - {l.prix} EUR")

# Recherche 2 : Python
print(f"\n  Recherche : titre contient 'Python'")
res2 = rechercher_livres(titre='Python', tri_par='annee', ordre='desc')
print(f"  Trouve {res2['total']} livre(s)")
for l in res2['livres']:
    print(f"    {l.titre} ({l.annee_publication}) - {l.prix} EUR")

# Recherche 3 : prix max 12, pagination
print(f"\n  Recherche : prix <= 12, page 1, 2 par page")
res3 = rechercher_livres(prix_max=12, par_page=2, page=1, tri_par='prix')
print(f"  Trouve {res3['total']} livre(s), page {res3['page']}/{res3['total_pages']}")
for l in res3['livres']:
    print(f"    {l.titre} - {l.prix} EUR")

print(f"\n  Page 2 :")
res4 = rechercher_livres(prix_max=12, par_page=2, page=2, tri_par='prix')
print(f"  page {res4['page']}/{res4['total_pages']}")
for l in res4['livres']:
    print(f"    {l.titre} - {l.prix} EUR")

session.close()


# === Etat final ===
print(f"\n{'=' * 50}")
print("ETAT FINAL")
print("=" * 50)

session = Session()
print(f"  Auteurs : {session.query(Auteur).count()}")
print(f"  Livres : {session.query(Livre).count()}")
session.close()

# Nettoyage
os.remove(DB_PATH)
print("\nBase de donnees nettoyee.")
