🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 11.5 Création et consommation d'APIs REST

## Introduction

Maintenant que vous savez créer des applications web avec FastAPI et Flask, et que vous maîtrisez les requêtes HTTP avec requests, il est temps de tout rassembler pour comprendre et créer des **APIs REST** complètes et professionnelles.

Une API REST bien conçue est comme un contrat clair entre votre serveur et ses clients. Elle définit précisément comment accéder aux ressources, quelles opérations sont possibles, et comment gérer les erreurs. C'est un savoir-faire essentiel pour tout développeur backend moderne.

## Qu'est-ce qu'une API REST ?

**REST** signifie **RE**presentational **S**tate **T**ransfer. C'est un style d'architecture pour concevoir des APIs web, créé par Roy Fielding en 2000.

### Les principes fondamentaux de REST

REST repose sur plusieurs principes clés qui le rendent puissant et facile à utiliser.

#### 1. Ressources et URLs

En REST, tout est une **ressource**. Une ressource peut être n'importe quel objet ou concept : un utilisateur, un article, une commande, une photo, etc.

Chaque ressource est identifiée par une **URL unique** :

```
https://api.monsite.com/utilisateurs/123
                      │            │
                      │            └─ ID de la ressource
                      └────────────── Type de ressource
```

**Exemples de ressources :**
- `/utilisateurs` - Collection d'utilisateurs
- `/utilisateurs/123` - Un utilisateur spécifique
- `/articles` - Collection d'articles
- `/articles/456` - Un article spécifique
- `/articles/456/commentaires` - Commentaires d'un article

#### 2. Verbes HTTP standards

REST utilise les verbes HTTP pour définir les opérations :

| Verbe | Opération | Exemple |
|-------|-----------|---------|
| **GET** | Lire / Récupérer | `GET /utilisateurs/123` |
| **POST** | Créer | `POST /utilisateurs` |
| **PUT** | Remplacer complètement | `PUT /utilisateurs/123` |
| **PATCH** | Modifier partiellement | `PATCH /utilisateurs/123` |
| **DELETE** | Supprimer | `DELETE /utilisateurs/123` |

#### 3. Représentations (généralement JSON)

Les ressources peuvent avoir plusieurs représentations (JSON, XML, etc.). En pratique, on utilise presque toujours JSON.

**Exemple de représentation JSON d'un utilisateur :**
```json
{
  "id": 123,
  "nom": "Alice Dupont",
  "email": "alice@example.com",
  "date_inscription": "2024-01-15"
}
```

#### 4. Sans état (Stateless)

Chaque requête est **indépendante** et contient toutes les informations nécessaires. Le serveur ne conserve pas d'état entre les requêtes.

```
Requête 1 : GET /utilisateurs/123 (avec token d'authentification)
Requête 2 : GET /articles (avec token d'authentification)
```

Chaque requête inclut ses propres informations d'authentification.

#### 5. Codes de statut HTTP

REST utilise les codes HTTP standards pour indiquer le résultat :

| Code | Signification | Usage |
|------|---------------|-------|
| **200** | OK | Requête réussie |
| **201** | Created | Ressource créée |
| **204** | No Content | Succès sans contenu à retourner |
| **400** | Bad Request | Données invalides |
| **401** | Unauthorized | Authentification requise |
| **403** | Forbidden | Accès refusé |
| **404** | Not Found | Ressource introuvable |
| **409** | Conflict | Conflit (ex: email déjà utilisé) |
| **500** | Server Error | Erreur serveur |

## Conventions de nommage REST

Pour créer une API cohérente, suivez ces conventions de nommage.

### Noms de ressources

**✅ Bonnes pratiques :**

```
GET    /utilisateurs          → Lire tous les utilisateurs
GET    /utilisateurs/123      → Lire l'utilisateur 123
POST   /utilisateurs          → Créer un utilisateur
PUT    /utilisateurs/123      → Remplacer l'utilisateur 123
PATCH  /utilisateurs/123      → Modifier l'utilisateur 123
DELETE /utilisateurs/123      → Supprimer l'utilisateur 123
```

**Règles :**
- ✅ Utilisez des **noms au pluriel** : `/utilisateurs`, `/articles`
- ✅ Utilisez des **noms**, pas des verbes : `/utilisateurs`, pas `/obtenirUtilisateurs`
- ✅ Utilisez des **minuscules** avec des tirets : `/articles-blog`
- ✅ Soyez **cohérent** dans toute votre API

**❌ Mauvaises pratiques :**

```
/obtenirUtilisateurs        ← Verbe (redondant avec GET)
/utilisateur                ← Singulier (incohérent)
/UTILISATEURS               ← Majuscules
/utilisateurs/obtenir/123   ← Verbe dans l'URL
```

### Ressources imbriquées

Pour les relations entre ressources :

```
GET    /utilisateurs/123/articles       → Articles de l'utilisateur 123
GET    /articles/456/commentaires       → Commentaires de l'article 456
POST   /articles/456/commentaires       → Ajouter un commentaire à l'article 456
GET    /articles/456/commentaires/789   → Commentaire 789 de l'article 456
```

**Attention :** Ne créez pas de hiérarchies trop profondes (max 2-3 niveaux).

### Filtrage, tri et pagination

Utilisez les **query parameters** pour filtrer, trier et paginer :

```
GET /articles?statut=publie                  → Filtrer
GET /articles?sort=date&order=desc           → Trier
GET /articles?page=2&per_page=10             → Paginer
GET /articles?auteur=alice&categorie=tech    → Filtres multiples
```

## Concevoir une API REST

Avant de coder, il faut concevoir votre API. Voici les étapes.

### 1. Identifier les ressources

Listez les entités principales de votre application :

**Exemple : Blog**
- Utilisateurs
- Articles
- Commentaires
- Catégories
- Tags

### 2. Définir les endpoints

Pour chaque ressource, définissez les opérations CRUD :

#### Utilisateurs

```
GET    /api/utilisateurs              → Lister les utilisateurs
POST   /api/utilisateurs              → Créer un utilisateur
GET    /api/utilisateurs/{id}         → Récupérer un utilisateur
PUT    /api/utilisateurs/{id}         → Remplacer un utilisateur
PATCH  /api/utilisateurs/{id}         → Modifier un utilisateur
DELETE /api/utilisateurs/{id}         → Supprimer un utilisateur
```

#### Articles

```
GET    /api/articles                  → Lister les articles
POST   /api/articles                  → Créer un article
GET    /api/articles/{id}             → Récupérer un article
PUT    /api/articles/{id}             → Remplacer un article
PATCH  /api/articles/{id}             → Modifier un article
DELETE /api/articles/{id}             → Supprimer un article
```

#### Commentaires (sous-ressource)

```
GET    /api/articles/{id}/commentaires     → Lister les commentaires d'un article
POST   /api/articles/{id}/commentaires     → Ajouter un commentaire
GET    /api/commentaires/{id}              → Récupérer un commentaire
DELETE /api/commentaires/{id}               → Supprimer un commentaire
```

### 3. Définir les structures de données

Définissez le format JSON de vos ressources.

**Utilisateur :**
```json
{
  "id": 1,
  "nom": "Alice Dupont",
  "email": "alice@example.com",
  "bio": "Développeuse Python passionnée",
  "date_inscription": "2024-01-15T10:30:00Z"
}
```

**Article :**
```json
{
  "id": 1,
  "titre": "Introduction à REST",
  "contenu": "REST est un style d'architecture...",
  "auteur_id": 1,
  "categorie": "Tech",
  "tags": ["REST", "API", "Python"],
  "date_publication": "2024-01-20T14:00:00Z",
  "nombre_vues": 150
}
```

### 4. Documenter l'API

Créez une documentation claire avec :
- La liste des endpoints
- Les paramètres requis et optionnels
- Les formats de requête et réponse
- Les codes d'erreur possibles
- Des exemples

## Créer une API REST complète avec FastAPI

Créons une API REST complète pour gérer un blog.

### Structure du projet

```
blog_api/
│
├── main.py              # Point d'entrée
├── models.py            # Modèles Pydantic
├── database.py          # Configuration base de données
├── crud.py              # Opérations CRUD
└── requirements.txt
```

### Modèles de données (models.py)

```python
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# Modèles pour les utilisateurs
class UtilisateurBase(BaseModel):
    nom: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    bio: Optional[str] = None

class UtilisateurCreate(UtilisateurBase):
    mot_de_passe: str = Field(..., min_length=8)

class Utilisateur(UtilisateurBase):
    id: int
    date_inscription: datetime

    class Config:
        from_attributes = True

# Modèles pour les articles
class ArticleBase(BaseModel):
    titre: str = Field(..., min_length=5, max_length=200)
    contenu: str = Field(..., min_length=10)
    categorie: str
    tags: List[str] = []

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int
    auteur_id: int
    date_publication: datetime
    nombre_vues: int = 0

    class Config:
        from_attributes = True

# Modèle avec l'auteur inclus
class ArticleAvecAuteur(Article):
    auteur: Utilisateur

# Modèles pour les commentaires
class CommentaireBase(BaseModel):
    contenu: str = Field(..., min_length=1, max_length=500)

class CommentaireCreate(CommentaireBase):
    pass

class Commentaire(CommentaireBase):
    id: int
    article_id: int
    auteur_id: int
    date_creation: datetime

    class Config:
        from_attributes = True
```

### Configuration base de données (database.py)

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de données SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Créer le moteur
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles
Base = declarative_base()

# Dépendance pour obtenir la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Application principale (main.py)

```python
from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import models
import database

app = FastAPI(
    title="Blog API",
    description="Une API REST complète pour gérer un blog",
    version="1.0.0"
)

# Créer les tables
database.Base.metadata.create_all(bind=database.engine)

# ==================== UTILISATEURS ====================

@app.post("/api/utilisateurs",
          response_model=models.Utilisateur,
          status_code=status.HTTP_201_CREATED,
          tags=["Utilisateurs"])
def creer_utilisateur(
    utilisateur: models.UtilisateurCreate,
    db: Session = Depends(database.get_db)
):
    """Créer un nouvel utilisateur"""
    # Vérifier si l'email existe déjà
    db_user = db.query(User).filter(User.email == utilisateur.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cet email est déjà utilisé"
        )

    # Créer l'utilisateur (en production, hasher le mot de passe !)
    db_utilisateur = User(
        nom=utilisateur.nom,
        email=utilisateur.email,
        bio=utilisateur.bio,
        mot_de_passe=utilisateur.mot_de_passe,  # À hasher !
        date_inscription=datetime.now()
    )

    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)

    return db_utilisateur

@app.get("/api/utilisateurs",
         response_model=List[models.Utilisateur],
         tags=["Utilisateurs"])
def lire_utilisateurs(
    skip: int = Query(0, ge=0, description="Nombre d'éléments à sauter"),
    limit: int = Query(10, ge=1, le=100, description="Nombre d'éléments à retourner"),
    db: Session = Depends(database.get_db)
):
    """Lister tous les utilisateurs avec pagination"""
    utilisateurs = db.query(User).offset(skip).limit(limit).all()
    return utilisateurs

@app.get("/api/utilisateurs/{utilisateur_id}",
         response_model=models.Utilisateur,
         tags=["Utilisateurs"])
def lire_utilisateur(
    utilisateur_id: int,
    db: Session = Depends(database.get_db)
):
    """Récupérer un utilisateur par son ID"""
    utilisateur = db.query(User).filter(User.id == utilisateur_id).first()

    if not utilisateur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouvé"
        )

    return utilisateur

@app.put("/api/utilisateurs/{utilisateur_id}",
         response_model=models.Utilisateur,
         tags=["Utilisateurs"])
def modifier_utilisateur(
    utilisateur_id: int,
    utilisateur: models.UtilisateurCreate,
    db: Session = Depends(database.get_db)
):
    """Mettre à jour un utilisateur"""
    db_utilisateur = db.query(User).filter(User.id == utilisateur_id).first()

    if not db_utilisateur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouvé"
        )

    # Mettre à jour les champs
    db_utilisateur.nom = utilisateur.nom
    db_utilisateur.email = utilisateur.email
    db_utilisateur.bio = utilisateur.bio

    db.commit()
    db.refresh(db_utilisateur)

    return db_utilisateur

@app.delete("/api/utilisateurs/{utilisateur_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            tags=["Utilisateurs"])
def supprimer_utilisateur(
    utilisateur_id: int,
    db: Session = Depends(database.get_db)
):
    """Supprimer un utilisateur"""
    db_utilisateur = db.query(User).filter(User.id == utilisateur_id).first()

    if not db_utilisateur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouvé"
        )

    db.delete(db_utilisateur)
    db.commit()

    return None

# ==================== ARTICLES ====================

@app.post("/api/articles",
          response_model=models.Article,
          status_code=status.HTTP_201_CREATED,
          tags=["Articles"])
def creer_article(
    article: models.ArticleCreate,
    auteur_id: int,
    db: Session = Depends(database.get_db)
):
    """Créer un nouvel article"""
    # Vérifier que l'auteur existe
    auteur = db.query(User).filter(User.id == auteur_id).first()
    if not auteur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Auteur non trouvé"
        )

    db_article = Article(
        titre=article.titre,
        contenu=article.contenu,
        categorie=article.categorie,
        tags=",".join(article.tags),  # Stocker comme chaîne
        auteur_id=auteur_id,
        date_publication=datetime.now(),
        nombre_vues=0
    )

    db.add(db_article)
    db.commit()
    db.refresh(db_article)

    return db_article

@app.get("/api/articles",
         response_model=List[models.Article],
         tags=["Articles"])
def lire_articles(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    categorie: Optional[str] = None,
    auteur_id: Optional[int] = None,
    sort: str = Query("date_publication", regex="^(date_publication|nombre_vues|titre)$"),
    order: str = Query("desc", regex="^(asc|desc)$"),
    db: Session = Depends(database.get_db)
):
    """
    Lister les articles avec filtrage, tri et pagination

    - **skip**: Nombre d'éléments à sauter
    - **limit**: Nombre d'éléments à retourner
    - **categorie**: Filtrer par catégorie
    - **auteur_id**: Filtrer par auteur
    - **sort**: Champ de tri (date_publication, nombre_vues, titre)
    - **order**: Ordre (asc ou desc)
    """
    query = db.query(Article)

    # Filtres
    if categorie:
        query = query.filter(Article.categorie == categorie)
    if auteur_id:
        query = query.filter(Article.auteur_id == auteur_id)

    # Tri
    if order == "desc":
        query = query.order_by(getattr(Article, sort).desc())
    else:
        query = query.order_by(getattr(Article, sort).asc())

    # Pagination
    articles = query.offset(skip).limit(limit).all()

    return articles

@app.get("/api/articles/{article_id}",
         response_model=models.ArticleAvecAuteur,
         tags=["Articles"])
def lire_article(
    article_id: int,
    db: Session = Depends(database.get_db)
):
    """Récupérer un article par son ID avec les informations de l'auteur"""
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouvé"
        )

    # Incrémenter le nombre de vues
    article.nombre_vues += 1
    db.commit()

    return article

@app.patch("/api/articles/{article_id}",
           response_model=models.Article,
           tags=["Articles"])
def modifier_article_partiel(
    article_id: int,
    titre: Optional[str] = None,
    contenu: Optional[str] = None,
    categorie: Optional[str] = None,
    db: Session = Depends(database.get_db)
):
    """Modifier partiellement un article"""
    db_article = db.query(Article).filter(Article.id == article_id).first()

    if not db_article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouvé"
        )

    # Mettre à jour uniquement les champs fournis
    if titre is not None:
        db_article.titre = titre
    if contenu is not None:
        db_article.contenu = contenu
    if categorie is not None:
        db_article.categorie = categorie

    db.commit()
    db.refresh(db_article)

    return db_article

@app.delete("/api/articles/{article_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            tags=["Articles"])
def supprimer_article(
    article_id: int,
    db: Session = Depends(database.get_db)
):
    """Supprimer un article"""
    db_article = db.query(Article).filter(Article.id == article_id).first()

    if not db_article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouvé"
        )

    db.delete(db_article)
    db.commit()

    return None

# ==================== COMMENTAIRES ====================

@app.post("/api/articles/{article_id}/commentaires",
          response_model=models.Commentaire,
          status_code=status.HTTP_201_CREATED,
          tags=["Commentaires"])
def creer_commentaire(
    article_id: int,
    commentaire: models.CommentaireCreate,
    auteur_id: int,
    db: Session = Depends(database.get_db)
):
    """Ajouter un commentaire à un article"""
    # Vérifier que l'article existe
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouvé"
        )

    db_commentaire = Commentaire(
        contenu=commentaire.contenu,
        article_id=article_id,
        auteur_id=auteur_id,
        date_creation=datetime.now()
    )

    db.add(db_commentaire)
    db.commit()
    db.refresh(db_commentaire)

    return db_commentaire

@app.get("/api/articles/{article_id}/commentaires",
         response_model=List[models.Commentaire],
         tags=["Commentaires"])
def lire_commentaires_article(
    article_id: int,
    db: Session = Depends(database.get_db)
):
    """Récupérer tous les commentaires d'un article"""
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article non trouvé"
        )

    commentaires = db.query(Commentaire).filter(
        Commentaire.article_id == article_id
    ).all()

    return commentaires

@app.delete("/api/commentaires/{commentaire_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            tags=["Commentaires"])
def supprimer_commentaire(
    commentaire_id: int,
    db: Session = Depends(database.get_db)
):
    """Supprimer un commentaire"""
    db_commentaire = db.query(Commentaire).filter(
        Commentaire.id == commentaire_id
    ).first()

    if not db_commentaire:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Commentaire non trouvé"
        )

    db.delete(db_commentaire)
    db.commit()

    return None

# ==================== ENDPOINTS UTILITAIRES ====================

@app.get("/api/stats",
         tags=["Statistiques"])
def obtenir_statistiques(db: Session = Depends(database.get_db)):
    """Obtenir des statistiques globales"""
    return {
        "nombre_utilisateurs": db.query(User).count(),
        "nombre_articles": db.query(Article).count(),
        "nombre_commentaires": db.query(Commentaire).count(),
        "article_plus_vu": db.query(Article).order_by(
            Article.nombre_vues.desc()
        ).first()
    }

@app.get("/",
         tags=["Root"])
def root():
    """Endpoint racine de l'API"""
    return {
        "message": "Bienvenue sur l'API Blog",
        "version": "1.0.0",
        "documentation": "/docs"
    }
```

## Consommer l'API avec requests

Maintenant que nous avons créé l'API, voyons comment la consommer.

### Client Python pour l'API

```python
import requests
from typing import List, Dict, Optional

class BlogAPIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()

    # ==================== UTILISATEURS ====================

    def creer_utilisateur(self, nom: str, email: str,
                          mot_de_passe: str, bio: str = None) -> Dict:
        """Créer un nouvel utilisateur"""
        data = {
            "nom": nom,
            "email": email,
            "mot_de_passe": mot_de_passe,
            "bio": bio
        }

        response = self.session.post(
            f"{self.base_url}/api/utilisateurs",
            json=data
        )
        response.raise_for_status()
        return response.json()

    def obtenir_utilisateurs(self, skip: int = 0,
                             limit: int = 10) -> List[Dict]:
        """Obtenir la liste des utilisateurs"""
        params = {"skip": skip, "limit": limit}

        response = self.session.get(
            f"{self.base_url}/api/utilisateurs",
            params=params
        )
        response.raise_for_status()
        return response.json()

    def obtenir_utilisateur(self, utilisateur_id: int) -> Dict:
        """Obtenir un utilisateur par son ID"""
        response = self.session.get(
            f"{self.base_url}/api/utilisateurs/{utilisateur_id}"
        )
        response.raise_for_status()
        return response.json()

    def modifier_utilisateur(self, utilisateur_id: int,
                            nom: str, email: str,
                            mot_de_passe: str, bio: str = None) -> Dict:
        """Modifier un utilisateur"""
        data = {
            "nom": nom,
            "email": email,
            "mot_de_passe": mot_de_passe,
            "bio": bio
        }

        response = self.session.put(
            f"{self.base_url}/api/utilisateurs/{utilisateur_id}",
            json=data
        )
        response.raise_for_status()
        return response.json()

    def supprimer_utilisateur(self, utilisateur_id: int) -> None:
        """Supprimer un utilisateur"""
        response = self.session.delete(
            f"{self.base_url}/api/utilisateurs/{utilisateur_id}"
        )
        response.raise_for_status()

    # ==================== ARTICLES ====================

    def creer_article(self, titre: str, contenu: str,
                     categorie: str, auteur_id: int,
                     tags: List[str] = None) -> Dict:
        """Créer un nouvel article"""
        data = {
            "titre": titre,
            "contenu": contenu,
            "categorie": categorie,
            "tags": tags or []
        }

        response = self.session.post(
            f"{self.base_url}/api/articles",
            json=data,
            params={"auteur_id": auteur_id}
        )
        response.raise_for_status()
        return response.json()

    def obtenir_articles(self, skip: int = 0, limit: int = 10,
                        categorie: str = None, auteur_id: int = None,
                        sort: str = "date_publication",
                        order: str = "desc") -> List[Dict]:
        """Obtenir la liste des articles avec filtres"""
        params = {
            "skip": skip,
            "limit": limit,
            "sort": sort,
            "order": order
        }

        if categorie:
            params["categorie"] = categorie
        if auteur_id:
            params["auteur_id"] = auteur_id

        response = self.session.get(
            f"{self.base_url}/api/articles",
            params=params
        )
        response.raise_for_status()
        return response.json()

    def obtenir_article(self, article_id: int) -> Dict:
        """Obtenir un article par son ID"""
        response = self.session.get(
            f"{self.base_url}/api/articles/{article_id}"
        )
        response.raise_for_status()
        return response.json()

    def modifier_article_partiel(self, article_id: int,
                                titre: str = None,
                                contenu: str = None,
                                categorie: str = None) -> Dict:
        """Modifier partiellement un article"""
        params = {}
        if titre:
            params["titre"] = titre
        if contenu:
            params["contenu"] = contenu
        if categorie:
            params["categorie"] = categorie

        response = self.session.patch(
            f"{self.base_url}/api/articles/{article_id}",
            params=params
        )
        response.raise_for_status()
        return response.json()

    def supprimer_article(self, article_id: int) -> None:
        """Supprimer un article"""
        response = self.session.delete(
            f"{self.base_url}/api/articles/{article_id}"
        )
        response.raise_for_status()

    # ==================== COMMENTAIRES ====================

    def creer_commentaire(self, article_id: int, contenu: str,
                         auteur_id: int) -> Dict:
        """Créer un commentaire"""
        data = {"contenu": contenu}

        response = self.session.post(
            f"{self.base_url}/api/articles/{article_id}/commentaires",
            json=data,
            params={"auteur_id": auteur_id}
        )
        response.raise_for_status()
        return response.json()

    def obtenir_commentaires_article(self, article_id: int) -> List[Dict]:
        """Obtenir les commentaires d'un article"""
        response = self.session.get(
            f"{self.base_url}/api/articles/{article_id}/commentaires"
        )
        response.raise_for_status()
        return response.json()

    def supprimer_commentaire(self, commentaire_id: int) -> None:
        """Supprimer un commentaire"""
        response = self.session.delete(
            f"{self.base_url}/api/commentaires/{commentaire_id}"
        )
        response.raise_for_status()

    # ==================== UTILITAIRES ====================

    def obtenir_statistiques(self) -> Dict:
        """Obtenir les statistiques"""
        response = self.session.get(f"{self.base_url}/api/stats")
        response.raise_for_status()
        return response.json()

# Utilisation
def main():
    client = BlogAPIClient()

    try:
        # Créer un utilisateur
        print("Création d'un utilisateur...")
        utilisateur = client.creer_utilisateur(
            nom="Alice Dupont",
            email="alice@example.com",
            mot_de_passe="motdepasse123",
            bio="Développeuse Python"
        )
        print(f"✅ Utilisateur créé : {utilisateur['nom']}")
        utilisateur_id = utilisateur['id']

        # Créer un article
        print("\nCréation d'un article...")
        article = client.creer_article(
            titre="Introduction à REST",
            contenu="REST est un style d'architecture pour les APIs...",
            categorie="Tech",
            auteur_id=utilisateur_id,
            tags=["REST", "API", "Python"]
        )
        print(f"✅ Article créé : {article['titre']}")
        article_id = article['id']

        # Lire l'article
        print("\nLecture de l'article...")
        article = client.obtenir_article(article_id)
        print(f"📖 Article : {article['titre']}")
        print(f"   Auteur : {article['auteur']['nom']}")
        print(f"   Vues : {article['nombre_vues']}")

        # Créer un commentaire
        print("\nAjout d'un commentaire...")
        commentaire = client.creer_commentaire(
            article_id=article_id,
            contenu="Excellent article !",
            auteur_id=utilisateur_id
        )
        print(f"✅ Commentaire ajouté")

        # Lire tous les articles
        print("\nListe des articles...")
        articles = client.obtenir_articles(limit=5)
        for art in articles:
            print(f"- {art['titre']} ({art['categorie']})")

        # Statistiques
        print("\nStatistiques...")
        stats = client.obtenir_statistiques()
        print(f"Utilisateurs : {stats['nombre_utilisateurs']}")
        print(f"Articles : {stats['nombre_articles']}")
        print(f"Commentaires : {stats['nombre_commentaires']}")

    except requests.exceptions.HTTPError as e:
        print(f"❌ Erreur HTTP : {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion : {e}")

if __name__ == "__main__":
    main()
```

## Pagination

La pagination est essentielle pour gérer de grandes quantités de données.

### Stratégies de pagination

#### 1. Pagination par offset (la plus courante)

```python
@app.get("/api/articles")
def lire_articles(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100)
):
    skip = (page - 1) * per_page
    articles = db.query(Article).offset(skip).limit(per_page).all()

    total = db.query(Article).count()
    total_pages = (total + per_page - 1) // per_page

    return {
        "items": articles,
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages
    }
```

**Utilisation :**
```
GET /api/articles?page=1&per_page=10
GET /api/articles?page=2&per_page=10
```

#### 2. Pagination par curseur (pour de très grandes bases)

```python
@app.get("/api/articles")
def lire_articles(
    cursor: Optional[int] = None,
    limit: int = Query(10, ge=1, le=100)
):
    query = db.query(Article)

    if cursor:
        query = query.filter(Article.id > cursor)

    articles = query.order_by(Article.id).limit(limit).all()

    next_cursor = articles[-1].id if articles else None

    return {
        "items": articles,
        "next_cursor": next_cursor
    }
```

**Utilisation :**
```
GET /api/articles?limit=10
GET /api/articles?cursor=42&limit=10
```

## Versioning d'API

Il est important de versionner votre API pour gérer les changements.

### Méthodes de versioning

#### 1. Dans l'URL (recommandé)

```python
# v1/
@app.get("/api/v1/articles")
def lire_articles_v1():
    return {"version": "1.0", "data": []}

# v2/
@app.get("/api/v2/articles")
def lire_articles_v2():
    return {"version": "2.0", "data": [], "metadata": {}}
```

#### 2. Dans les headers

```python
@app.get("/api/articles")
def lire_articles(version: str = Header("v1", alias="API-Version")):
    if version == "v1":
        return {"version": "1.0", "data": []}
    elif version == "v2":
        return {"version": "2.0", "data": [], "metadata": {}}
```

#### 3. Avec des query parameters

```python
@app.get("/api/articles")
def lire_articles(version: str = Query("v1")):
    if version == "v1":
        return {"version": "1.0", "data": []}
    elif version == "v2":
        return {"version": "2.0", "data": [], "metadata": {}}
```

## Gestion des erreurs

Une bonne API retourne des erreurs claires et cohérentes.

### Format d'erreur standard

```python
from fastapi import HTTPException

class APIError(BaseModel):
    error: str
    message: str
    details: Optional[Dict] = None

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.status_code,
            "message": exc.detail,
            "path": str(request.url)
        }
    )
```

### Erreurs personnalisées

```python
class ResourceNotFound(HTTPException):
    def __init__(self, resource: str, id: int):
        super().__init__(
            status_code=404,
            detail=f"{resource} avec l'ID {id} n'a pas été trouvé"
        )

class ValidationError(HTTPException):
    def __init__(self, message: str, errors: List[str]):
        super().__init__(
            status_code=400,
            detail={
                "message": message,
                "errors": errors
            }
        )

# Utilisation
@app.get("/api/articles/{article_id}")
def lire_article(article_id: int):
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        raise ResourceNotFound("Article", article_id)

    return article
```

## CORS (Cross-Origin Resource Sharing)

Pour permettre à des applications frontend d'accéder à votre API :

```python
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuration CORS
origins = [
    "http://localhost:3000",  # React dev server
    "http://localhost:8080",  # Vue dev server
    "https://monsite.com",    # Production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Ou ["*"] pour tout autoriser (développement uniquement)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Rate Limiting

Limiter le nombre de requêtes pour éviter les abus :

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/api/articles")
@limiter.limit("10/minute")  # 10 requêtes par minute
def lire_articles(request: Request):
    return {"articles": []}
```

## Authentification et autorisation

### JWT (JSON Web Tokens)

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "votre-clé-secrète"
ALGORITHM = "HS256"

security = HTTPBearer()

def creer_token(user_id: int) -> str:
    """Créer un JWT"""
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verifier_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> int:
    """Vérifier un JWT et retourner l'user_id"""
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expiré"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide"
        )

# Utilisation
@app.post("/api/login")
def login(email: str, password: str):
    # Vérifier les credentials (simplifié)
    user = verify_credentials(email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Identifiants invalides")

    token = creer_token(user.id)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/profil")
def obtenir_profil(user_id: int = Depends(verifier_token)):
    # user_id est extrait du token automatiquement
    user = db.query(User).filter(User.id == user_id).first()
    return user
```

## Tests d'API

### Tester avec pytest

```python
# test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_creer_utilisateur():
    response = client.post(
        "/api/utilisateurs",
        json={
            "nom": "Test User",
            "email": "test@example.com",
            "mot_de_passe": "password123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nom"] == "Test User"
    assert data["email"] == "test@example.com"

def test_lire_utilisateur():
    response = client.get("/api/utilisateurs/1")
    assert response.status_code == 200
    data = response.json()
    assert "nom" in data
    assert "email" in data

def test_utilisateur_inexistant():
    response = client.get("/api/utilisateurs/9999")
    assert response.status_code == 404

def test_creer_article():
    response = client.post(
        "/api/articles",
        json={
            "titre": "Test Article",
            "contenu": "Contenu de test",
            "categorie": "Tech",
            "tags": ["test"]
        },
        params={"auteur_id": 1}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["titre"] == "Test Article"

def test_filtrer_articles():
    response = client.get("/api/articles?categorie=Tech&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5
```

## Bonnes pratiques REST

### 1. Utilisez les bons codes de statut HTTP

```python
# 200 OK - Succès général
return {"data": data}

# 201 Created - Ressource créée
return Response(status_code=201, content=json.dumps(data))

# 204 No Content - Succès sans contenu
return Response(status_code=204)

# 400 Bad Request - Données invalides
raise HTTPException(status_code=400, detail="Données invalides")

# 401 Unauthorized - Authentification requise
raise HTTPException(status_code=401, detail="Authentification requise")

# 403 Forbidden - Accès refusé
raise HTTPException(status_code=403, detail="Accès refusé")

# 404 Not Found - Ressource introuvable
raise HTTPException(status_code=404, detail="Ressource non trouvée")

# 409 Conflict - Conflit (ex: email déjà utilisé)
raise HTTPException(status_code=409, detail="Email déjà utilisé")

# 500 Internal Server Error - Erreur serveur
raise HTTPException(status_code=500, detail="Erreur serveur")
```

### 2. Soyez cohérent dans vos URLs

```
✅ Bon
GET    /api/utilisateurs
GET    /api/articles
GET    /api/commentaires

❌ Incohérent
GET    /api/users
GET    /api/posts
GET    /api/comment
```

### 3. Utilisez des noms de ressources, pas de verbes

```
✅ Bon
GET    /api/articles
POST   /api/articles

❌ Mauvais
GET    /api/obtenirArticles
POST   /api/creerArticle
```

### 4. Fournissez une documentation claire

Utilisez la documentation automatique de FastAPI et ajoutez des descriptions :

```python
@app.get("/api/articles",
         summary="Lister les articles",
         description="Récupère une liste paginée d'articles avec filtres optionnels",
         response_description="Liste d'articles")
def lire_articles(
    page: int = Query(1, description="Numéro de la page"),
    limit: int = Query(10, description="Nombre d'articles par page")
):
    pass
```

### 5. Implémentez HATEOAS (optionnel)

HATEOAS (Hypermedia As The Engine Of Application State) ajoute des liens vers les ressources liées :

```python
{
  "id": 1,
  "titre": "Mon article",
  "auteur_id": 5,
  "_links": {
    "self": "/api/articles/1",
    "auteur": "/api/utilisateurs/5",
    "commentaires": "/api/articles/1/commentaires"
  }
}
```

### 6. Validez toutes les entrées

Utilisez Pydantic pour valider automatiquement :

```python
class ArticleCreate(BaseModel):
    titre: str = Field(..., min_length=5, max_length=200)
    contenu: str = Field(..., min_length=10)
    categorie: str = Field(..., regex="^(Tech|Science|Culture)$")

    @validator('titre')
    def titre_pas_vide(cls, v):
        if not v.strip():
            raise ValueError("Le titre ne peut pas être vide")
        return v
```

### 7. Gérez la sécurité

```python
# N'exposez jamais les mots de passe
class UtilisateurReponse(BaseModel):
    id: int
    nom: str
    email: str
    # Pas de mot_de_passe !

# Utilisez HTTPS en production
# Implémentez rate limiting
# Validez toutes les entrées
# Utilisez des tokens JWT sécurisés
# Loggez les accès
```

## Récapitulatif

Dans cette section, vous avez appris :

✅ Les principes fondamentaux de REST
✅ Les conventions de nommage et structure d'URLs
✅ Comment concevoir une API REST complète
✅ Comment créer une API REST avec FastAPI
✅ Comment consommer une API avec requests
✅ La pagination, le filtrage et le tri
✅ Le versioning d'API
✅ La gestion des erreurs de manière professionnelle
✅ CORS et rate limiting
✅ L'authentification avec JWT
✅ Comment tester une API
✅ Les bonnes pratiques REST

Vous avez maintenant toutes les compétences nécessaires pour créer et consommer des APIs REST professionnelles avec Python. REST est le standard de facto pour les APIs web modernes, et sa maîtrise est essentielle pour tout développeur backend.

---


⏭️ [Bases de données et ORM (SQLite + SQLAlchemy)](/11-developpement-web-et-apis/06-bases-de-donnees-orm-sqlalchemy.md)
