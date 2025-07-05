🔝 Retour au [Sommaire](/SOMMAIRE.md)

# 6.3 : Gestion des dépendances avec pip

## Introduction

**pip** (Pip Installs Packages) est l'outil standard pour installer et gérer les packages Python. C'est votre passerelle vers l'écosystème Python qui compte plus de 400 000 packages disponibles sur PyPI (Python Package Index).

### Analogie simple
Imaginez pip comme un **magasin d'applications** pour Python :
- **PyPI** = magasin en ligne avec toutes les applications
- **pip** = gestionnaire qui télécharge et installe les applications
- **Packages** = applications/bibliothèques que vous pouvez utiliser

## Qu'est-ce qu'une dépendance ?

Une **dépendance** est un package externe dont votre projet a besoin pour fonctionner. Par exemple :
- Votre projet utilise `requests` pour faire des requêtes HTTP
- `requests` devient une dépendance de votre projet
- pip s'assure que `requests` est installé avec la bonne version

## Installation de base avec pip

### Vérifier que pip est installé

```bash
# Vérifier la version de pip
pip --version

# Ou avec Python
python -m pip --version

# Sur certains systèmes Linux/Mac
pip3 --version
```

**Résultat attendu :**
```
pip 23.3.1 from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
```

### Installer un package

```bash
# Installation basique
pip install requests

# Installation d'une version spécifique
pip install requests==2.31.0

# Installation de la dernière version compatible
pip install "requests>=2.25.0"

# Installation de plusieurs packages
pip install requests beautifulsoup4 pandas
```

### Exemples pratiques d'installation

```bash
# Packages populaires pour débuter
pip install requests          # Requêtes HTTP simples
pip install beautifulsoup4    # Parsing HTML/XML
pip install pandas           # Manipulation de données
pip install matplotlib       # Graphiques et visualisations
pip install pillow          # Manipulation d'images
pip install flask           # Framework web léger
```

## Utilisation des packages installés

### Exemple avec requests

Après `pip install requests` :

```python
# test_requests.py
import requests

# Faire une requête GET
response = requests.get('https://api.github.com/users/octocat')

# Vérifier le statut
if response.status_code == 200:
    data = response.json()
    print(f"Utilisateur : {data['name']}")
    print(f"Followers : {data['followers']}")
else:
    print("Erreur lors de la requête")
```

### Exemple avec BeautifulSoup

Après `pip install beautifulsoup4 requests` :

```python
# scraping_simple.py
import requests
from bs4 import BeautifulSoup

# Récupérer une page web
url = "https://httpbin.org/html"
response = requests.get(url)

# Parser le HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Extraire des informations
titre = soup.find('h1').text
print(f"Titre de la page : {titre}")

# Trouver tous les liens
liens = soup.find_all('a')
for lien in liens:
    print(f"Lien : {lien.get('href')} - Texte : {lien.text}")
```

### Exemple avec pandas

Après `pip install pandas` :

```python
# analyse_donnees.py
import pandas as pd

# Créer un DataFrame
donnees = {
    'nom': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse'],
    'salaire': [45000, 55000, 60000, 50000]
}

df = pd.DataFrame(donnees)

# Afficher les données
print("Données :")
print(df)

# Statistiques de base
print(f"\nÂge moyen : {df['age'].mean():.1f} ans")
print(f"Salaire médian : {df['salaire'].median():.0f}€")

# Filtrer les données
jeunes = df[df['age'] < 30]
print(f"\nPersonnes de moins de 30 ans :")
print(jeunes[['nom', 'age']])
```

## Gestion des versions

### Spécifier des versions

```bash
# Version exacte
pip install django==4.2.0

# Version minimale
pip install "django>=4.0"

# Plage de versions
pip install "django>=4.0,<5.0"

# Version compatible (recommandé)
pip install "django~=4.2.0"  # Équivaut à >=4.2.0, <4.3.0
```

### Comprendre les numéros de version

Format : `MAJEUR.MINEUR.PATCH` (exemple : 2.31.0)

- **MAJEUR** : changements incompatibles
- **MINEUR** : nouvelles fonctionnalités compatibles
- **PATCH** : corrections de bugs

## Commandes pip essentielles

### Lister les packages installés

```bash
# Lister tous les packages
pip list

# Format détaillé
pip list --format=freeze

# Packages obsolètes
pip list --outdated
```

### Obtenir des informations sur un package

```bash
# Informations détaillées
pip show requests

# Dépendances d'un package
pip show --verbose requests
```

**Exemple de sortie :**
```
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Author: Kenneth Reitz
Requires: charset-normalizer, idna, urllib3, certifi
Required-by: beautifulsoup4
```

### Mettre à jour les packages

```bash
# Mettre à jour un package
pip install --upgrade requests

# Mettre à jour pip lui-même
pip install --upgrade pip

# Forcer la réinstallation
pip install --force-reinstall requests
```

### Désinstaller des packages

```bash
# Désinstaller un package
pip uninstall requests

# Désinstaller plusieurs packages
pip uninstall requests beautifulsoup4

# Désinstaller avec confirmation automatique
pip uninstall -y requests
```

## Fichier requirements.txt

Le fichier `requirements.txt` liste toutes les dépendances de votre projet.

### Créer un requirements.txt

```bash
# Générer le fichier avec les versions actuelles
pip freeze > requirements.txt
```

**Contenu du fichier généré :**
```
beautifulsoup4==4.12.2
certifi==2023.7.22
charset-normalizer==3.2.0
idna==3.4
pandas==2.0.3
python-dateutil==2.8.2
pytz==2023.3
requests==2.31.0
six==1.16.0
soupsieve==2.4.1
urllib3==2.0.4
```

### Créer un requirements.txt manuel

```txt
# requirements.txt
# Dépendances principales avec versions flexibles
requests>=2.25.0
beautifulsoup4>=4.9.0
pandas>=1.3.0
matplotlib>=3.3.0

# Dépendances de développement (optionnel)
pytest>=6.0.0
black>=21.0.0

# Dépendances avec commentaires
flask>=2.0.0  # Framework web
pillow>=8.0.0  # Manipulation d'images
```

### Installer depuis requirements.txt

```bash
# Installer toutes les dépendances
pip install -r requirements.txt

# Installer en mode mise à jour
pip install -r requirements.txt --upgrade
```

## Exemple de projet complet

Créons un projet de scraping web avec gestion des dépendances.

### Structure du projet

```
projet_scraping/
├── requirements.txt
├── scraper.py
├── analyzer.py
└── main.py
```

### requirements.txt

```txt
# requirements.txt
requests>=2.25.0
beautifulsoup4>=4.9.0
pandas>=1.3.0
matplotlib>=3.3.0
lxml>=4.6.0
```

### scraper.py

```python
# scraper.py
import requests
from bs4 import BeautifulSoup
import time

class WebScraper:
    """Classe pour faire du scraping web simple."""

    def __init__(self, delay=1):
        self.session = requests.Session()
        self.delay = delay  # Délai entre les requêtes

    def get_page(self, url):
        """Récupère le contenu d'une page web."""
        try:
            response = self.session.get(url)
            response.raise_for_status()  # Lève une exception pour les erreurs HTTP
            return response
        except requests.RequestException as e:
            print(f"Erreur lors de la requête : {e}")
            return None

    def extract_quotes(self, url="http://quotes.toscrape.com"):
        """Extrait des citations depuis quotes.toscrape.com."""
        quotes_data = []
        page = 1

        while True:
            print(f"Scraping page {page}...")
            page_url = f"{url}/page/{page}/"

            response = self.get_page(page_url)
            if not response:
                break

            soup = BeautifulSoup(response.content, 'html.parser')
            quotes = soup.find_all('div', class_='quote')

            if not quotes:  # Plus de citations
                break

            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]

                quotes_data.append({
                    'text': text,
                    'author': author,
                    'tags': tags
                })

            page += 1
            time.sleep(self.delay)  # Respecter le site web

        return quotes_data

    def save_to_file(self, data, filename):
        """Sauvegarde les données en JSON."""
        import json
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Données sauvegardées dans {filename}")
```

### analyzer.py

```python
# analyzer.py
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import json

class QuoteAnalyzer:
    """Classe pour analyser les citations."""

    def __init__(self, data_file=None):
        if data_file:
            self.load_data(data_file)
        else:
            self.quotes_df = None

    def load_data(self, filename):
        """Charge les données depuis un fichier JSON."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Créer un DataFrame pandas
            self.quotes_df = pd.DataFrame(data)
            print(f"Chargé {len(self.quotes_df)} citations")

        except FileNotFoundError:
            print(f"Fichier {filename} non trouvé")
            self.quotes_df = None

    def analyze_authors(self):
        """Analyse la répartition des auteurs."""
        if self.quotes_df is None:
            return

        author_counts = self.quotes_df['author'].value_counts()
        print("Top 10 des auteurs :")
        print(author_counts.head(10))

        # Graphique
        plt.figure(figsize=(12, 6))
        author_counts.head(10).plot(kind='bar')
        plt.title('Top 10 des auteurs les plus cités')
        plt.xlabel('Auteurs')
        plt.ylabel('Nombre de citations')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('auteurs_top10.png')
        plt.show()

    def analyze_tags(self):
        """Analyse les tags les plus populaires."""
        if self.quotes_df is None:
            return

        # Aplatir la liste des tags
        all_tags = []
        for tags_list in self.quotes_df['tags']:
            all_tags.extend(tags_list)

        tag_counts = Counter(all_tags)
        print("Top 15 des tags :")
        for tag, count in tag_counts.most_common(15):
            print(f"{tag}: {count}")

        # Graphique
        top_tags = dict(tag_counts.most_common(15))
        plt.figure(figsize=(12, 6))
        plt.bar(top_tags.keys(), top_tags.values())
        plt.title('Top 15 des tags les plus populaires')
        plt.xlabel('Tags')
        plt.ylabel('Fréquence')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('tags_top15.png')
        plt.show()

    def get_stats(self):
        """Affiche des statistiques générales."""
        if self.quotes_df is None:
            return

        print("=== STATISTIQUES GÉNÉRALES ===")
        print(f"Nombre total de citations : {len(self.quotes_df)}")
        print(f"Nombre d'auteurs uniques : {self.quotes_df['author'].nunique()}")

        # Longueur des citations
        self.quotes_df['text_length'] = self.quotes_df['text'].str.len()
        print(f"Longueur moyenne des citations : {self.quotes_df['text_length'].mean():.1f} caractères")
        print(f"Citation la plus courte : {self.quotes_df['text_length'].min()} caractères")
        print(f"Citation la plus longue : {self.quotes_df['text_length'].max()} caractères")
```

### main.py

```python
# main.py
from scraper import WebScraper
from analyzer import QuoteAnalyzer

def main():
    """Fonction principale du programme."""
    print("=== SCRAPING ET ANALYSE DE CITATIONS ===\n")

    # Étape 1 : Scraping
    print("1. Lancement du scraping...")
    scraper = WebScraper(delay=0.5)
    quotes = scraper.extract_quotes()

    if quotes:
        scraper.save_to_file(quotes, 'quotes.json')
        print(f"Scraping terminé : {len(quotes)} citations collectées\n")
    else:
        print("Erreur lors du scraping")
        return

    # Étape 2 : Analyse
    print("2. Lancement de l'analyse...")
    analyzer = QuoteAnalyzer('quotes.json')

    # Statistiques générales
    analyzer.get_stats()
    print()

    # Analyse des auteurs
    analyzer.analyze_authors()
    print()

    # Analyse des tags
    analyzer.analyze_tags()

    print("Analyse terminée ! Vérifiez les graphiques générés.")

if __name__ == "__main__":
    main()
```

### Installation et exécution

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Exécuter le programme
python main.py
```

## Bonnes pratiques avec pip

### 1. Toujours utiliser requirements.txt

```bash
# ✅ Bon : spécifier les versions
echo "requests>=2.25.0" >> requirements.txt
pip install -r requirements.txt

# ❌ Éviter : installation sans traçabilité
pip install requests
```

### 2. Séparer les dépendances par environnement

```txt
# requirements-dev.txt (développement)
pytest>=6.0.0
black>=21.0.0
flake8>=4.0.0
jupyter>=1.0.0

# requirements-prod.txt (production)
requests>=2.25.0
flask>=2.0.0
gunicorn>=20.0.0
```

### 3. Vérifier les vulnérabilités de sécurité

```bash
# Installer l'outil de sécurité
pip install safety

# Vérifier les vulnérabilités
safety check

# Audit des dépendances
pip-audit
```

### 4. Nettoyer les packages inutilisés

```bash
# Installer pip-autoremove
pip install pip-autoremove

# Supprimer les packages non utilisés
pip-autoremove
```

## Résolution des problèmes courants

### Problème : Package non trouvé

```bash
# Vérifier l'orthographe du nom
pip search beautiful
# Ou chercher sur pypi.org

# Mettre à jour la liste des packages
pip install --upgrade pip
```

### Problème : Conflits de versions

```bash
# Voir l'arbre des dépendances
pip install pipdeptree
pipdeptree

# Forcer une version spécifique
pip install "package==version" --force-reinstall
```

### Problème : Permissions

```bash
# Installation pour l'utilisateur seulement
pip install --user package_name

# Ou utiliser un environnement virtuel (recommandé)
python -m venv mon_env
source mon_env/bin/activate  # Linux/Mac
# ou
mon_env\Scripts\activate     # Windows
pip install package_name
```

## Exercices pratiques

### Exercice 1 : Création d'un projet de météo

Créez un projet qui utilise l'API OpenWeatherMap :

1. Créez le requirements.txt avec : `requests`, `python-dotenv`
2. Créez un script qui récupère la météo d'une ville
3. Gérez les erreurs et les clés API

### Exercice 2 : Analyse de données CSV

Créez un projet d'analyse de données :

1. Requirements : `pandas`, `matplotlib`, `seaborn`
2. Chargez un fichier CSV (création manuelle ou téléchargement)
3. Créez des graphiques et statistiques

### Exercice 3 : Bot Discord simple

Créez un bot Discord basique :

1. Requirements : `discord.py`, `python-dotenv`
2. Bot qui répond à des commandes simples
3. Gestion des tokens et configuration

## Solutions des exercices

### Solution Exercice 1 : Projet météo

```txt
# requirements.txt
requests>=2.25.0
python-dotenv>=0.19.0
```

```python
# weather.py
import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class WeatherAPI:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

        if not self.api_key:
            raise ValueError("Clé API manquante. Créez un fichier .env avec OPENWEATHER_API_KEY=votre_clé")

    def get_weather(self, city):
        """Récupère la météo d'une ville."""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'fr'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()

        except requests.RequestException as e:
            print(f"Erreur de requête : {e}")
            return None

    def format_weather(self, data):
        """Formate les données météo."""
        if not data:
            return "Données non disponibles"

        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        return f"""
📍 {city}, {country}
🌡️  Température : {temp:.1f}°C (ressenti : {feels_like:.1f}°C)
💧 Humidité : {humidity}%
☁️  Conditions : {description}
        """.strip()

def main():
    weather = WeatherAPI()

    while True:
        city = input("\nEntrez le nom d'une ville (ou 'quit' pour quitter) : ")

        if city.lower() == 'quit':
            break

        data = weather.get_weather(city)
        print(weather.format_weather(data))

if __name__ == "__main__":
    main()
```

```bash
# Fichier .env à créer
OPENWEATHER_API_KEY=votre_clé_api_ici
```

### Solution Exercice 2 : Analyse de données

```txt
# requirements.txt
pandas>=1.3.0
matplotlib>=3.3.0
seaborn>=0.11.0
```

```python
# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Créer des données d'exemple
def create_sample_data():
    """Crée un fichier CSV d'exemple."""
    import random
    from datetime import datetime, timedelta

    # Données de ventes fictives
    start_date = datetime(2023, 1, 1)
    data = []

    products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Mouse']
    regions = ['Nord', 'Sud', 'Est', 'Ouest', 'Centre']

    for i in range(1000):
        date = start_date + timedelta(days=random.randint(0, 365))
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'product': random.choice(products),
            'region': random.choice(regions),
            'quantity': random.randint(1, 10),
            'price': round(random.uniform(50, 1500), 2),
            'discount': round(random.uniform(0, 0.3), 2)
        })

    df = pd.DataFrame(data)
    df.to_csv('sales_data.csv', index=False)
    print("Fichier sales_data.csv créé avec 1000 lignes de données")
    return df

def analyze_sales(df):
    """Analyse les données de ventes."""
    # Convertir la date
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['revenue'] = df['quantity'] * df['price'] * (1 - df['discount'])

    # Statistiques de base
    print("=== STATISTIQUES GÉNÉRALES ===")
    print(f"Nombre de ventes : {len(df)}")
    print(f"Revenus total : {df['revenue'].sum():,.2f}€")
    print(f"Vente moyenne : {df['revenue'].mean():.2f}€")

    # Analyse par produit
    plt.figure(figsize=(15, 10))

    # Graphique 1 : Revenus par produit
    plt.subplot(2, 2, 1)
    product_revenue = df.groupby('product')['revenue'].sum().sort_values(ascending=True)
    product_revenue.plot(kind='barh')
    plt.title('Revenus par produit')
    plt.xlabel('Revenus (€)')

    # Graphique 2 : Ventes par région
    plt.subplot(2, 2, 2)
    region_sales = df.groupby('region')['quantity'].sum()
    plt.pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%')
    plt.title('Répartition des ventes par région')

    # Graphique 3 : Évolution mensuelle
    plt.subplot(2, 2, 3)
    monthly_revenue = df.groupby('month')['revenue'].sum()
    monthly_revenue.plot(kind='line', marker='o')
    plt.title('Évolution mensuelle des revenus')
    plt.xlabel('Mois')
    plt.ylabel('Revenus (€)')

    # Graphique 4 : Heatmap prix vs quantité
    plt.subplot(2, 2, 4)
    correlation_data = df[['quantity', 'price', 'discount', 'revenue']].corr()
    sns.heatmap(correlation_data, annot=True, cmap='coolwarm', center=0)
    plt.title('Corrélations entre variables')

    plt.tight_layout()
    plt.savefig('sales_analysis.png', dpi=300)
    plt.show()

def main():
    # Créer ou charger les données
    try:
        df = pd.read_csv('sales_data.csv')
        print("Données chargées depuis sales_data.csv")
    except FileNotFoundError:
        print("Création de données d'exemple...")
        df = create_sample_data()

    # Analyser les données
    analyze_sales(df)

if __name__ == "__main__":
    main()
```

## Résumé

Dans cette section, nous avons appris :

1. **Utiliser pip** pour installer et gérer les packages Python
2. **Spécifier les versions** pour assurer la compatibilité
3. **Créer et utiliser** des fichiers requirements.txt
4. **Appliquer les bonnes pratiques** de gestion des dépendances
5. **Résoudre les problèmes** courants avec pip
6. **Créer des projets complets** avec gestion des dépendances

Dans la prochaine section, nous verrons comment utiliser les environnements virtuels pour isoler les dépendances de chaque projet.

⏭️
