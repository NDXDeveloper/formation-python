# ============================================================================
#   Section 2.3 : namedtuple - Cas d'usage pratiques
#   Description : Coordonnées et distance, employés, configuration,
#                 résultats de fonction (Stats)
#   Fichier source : 03-collections-specialisees.md
# ============================================================================

from collections import namedtuple

# --- Exemple 1 : Coordonnées ---
Point = namedtuple('Point', ['x', 'y'])

p1 = Point(0, 0)
p2 = Point(10, 5)

def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

print(f"Distance : {distance(p1, p2):.4f}")  # 11.1803

# --- Exemple 2 : Employés ---
Employe = namedtuple('Employe', 'nom poste salaire anciennete')

employes = [
    Employe('Alice', 'Développeuse', 50000, 3),
    Employe('Bob', 'Designer', 45000, 2),
    Employe('Charlie', 'Manager', 60000, 5)
]

salaire_moyen = sum(e.salaire for e in employes) / len(employes)
print(f"Salaire moyen : {salaire_moyen:.0f}€")

veterants = [e for e in employes if e.anciennete > 2]
for emp in veterants:
    print(f"  {emp.nom} - {emp.anciennete} ans")

# --- Exemple 3 : Configuration ---
Config = namedtuple('Config', 'host port debug timeout',
                    defaults=['localhost', 8000, False, 30])

config_dev = Config()
print(f"\nConfig dev : {config_dev}")

config_prod = Config(host='api.example.com', port=443, debug=False)
print(f"Config prod : {config_prod}")

# --- Exemple 4 : Résultats de fonction ---
Stats = namedtuple('Stats', 'moyenne mediane ecart_type')

def calculer_statistiques(nombres):
    moyenne = sum(nombres) / len(nombres)
    mediane = sorted(nombres)[len(nombres) // 2]
    ecart_type = (sum((x - moyenne)**2 for x in nombres) / len(nombres))**0.5
    return Stats(moyenne, mediane, ecart_type)

donnees = [10, 20, 30, 40, 50]
resultats = calculer_statistiques(donnees)
print(f"\nMoyenne : {resultats.moyenne}")
print(f"Médiane : {resultats.mediane}")
print(f"Écart-type : {resultats.ecart_type:.2f}")
