# ============================================================================
#   Section 7.3 : Les modules math, random et statistics
#   Description : Exemples complets - simulateur de casino (roulette,
#                 blackjack) et estimation de Pi par Monte Carlo
#   Fichier source : 03-math-random-statistics.md
# ============================================================================

import random
import statistics
import math

# ==========================================
# 1. Simulateur de casino
# ==========================================
print("=== Simulateur de Casino ===")

random.seed(42)

class Casino:
    """Simulateur de jeux de casino"""

    def __init__(self, capital_initial=1000):
        self.capital = capital_initial
        self.historique = [capital_initial]

    def roulette(self, mise, choix):
        if mise > self.capital:
            return "Mise trop élevée!"
        numero = random.randint(0, 36)
        est_rouge = numero in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        est_noir = numero != 0 and not est_rouge
        gain = 0
        if isinstance(choix, int) and choix == numero:
            gain = mise * 35
        elif choix == "rouge" and est_rouge:
            gain = mise
        elif choix == "noir" and est_noir:
            gain = mise
        elif choix == "pair" and numero % 2 == 0 and numero != 0:
            gain = mise
        elif choix == "impair" and numero % 2 == 1:
            gain = mise
        else:
            gain = -mise
        self.capital += gain
        self.historique.append(self.capital)
        couleur = 'vert' if numero == 0 else ('rouge' if est_rouge else 'noir')
        return {'numero': numero, 'couleur': couleur, 'gain': gain, 'capital': self.capital}

    def blackjack_simplifie(self, mise):
        if mise > self.capital:
            return "Mise trop élevée!"
        main_joueur = random.randint(15, 21)
        main_croupier = random.randint(15, 21)
        if main_joueur > 21:
            gain, resultat = -mise, "Perdu (depassement)"
        elif main_croupier > 21:
            gain, resultat = mise, "Gagne (croupier depasse)"
        elif main_joueur > main_croupier:
            gain, resultat = mise, "Gagne"
        elif main_joueur < main_croupier:
            gain, resultat = -mise, "Perdu"
        else:
            gain, resultat = 0, "Egalite"
        self.capital += gain
        self.historique.append(self.capital)
        return {'main_joueur': main_joueur, 'main_croupier': main_croupier,
                'resultat': resultat, 'gain': gain, 'capital': self.capital}

    def statistiques(self):
        print(f"\nStatistiques de jeu")
        print("=" * 50)
        print(f"Capital initial : {self.historique[0]:.2f} EUR")
        print(f"Capital actuel : {self.capital:.2f} EUR")
        benefice = self.capital - self.historique[0]
        print(f"Benefice/Perte : {benefice:+.2f} EUR")
        if len(self.historique) > 1:
            print(f"Nombre de parties : {len(self.historique) - 1}")
            print(f"Capital moyen : {statistics.mean(self.historique):.2f} EUR")
            print(f"Capital médian : {statistics.median(self.historique):.2f} EUR")
            print(f"Écart-type : {statistics.stdev(self.historique):.2f} EUR")
            print(f"Capital max : {max(self.historique):.2f} EUR")
            print(f"Capital min : {min(self.historique):.2f} EUR")
            roi = ((self.capital - self.historique[0]) / self.historique[0]) * 100
            print(f"ROI : {roi:+.2f}%")

casino = Casino(capital_initial=1000)

print("\n--- Roulette ---")
for i in range(5):
    resultat = casino.roulette(50, "rouge")
    print(f"Partie {i+1}: Numero {resultat['numero']} ({resultat['couleur']}) - "
          f"Gain: {resultat['gain']:+} EUR - Capital: {resultat['capital']:.0f} EUR")

print("\n--- Blackjack ---")
for i in range(5):
    resultat = casino.blackjack_simplifie(50)
    print(f"Partie {i+1}: {resultat['resultat']} ({resultat['main_joueur']} vs "
          f"{resultat['main_croupier']}) - Gain: {resultat['gain']:+} EUR - "
          f"Capital: {resultat['capital']:.0f} EUR")

casino.statistiques()

# ==========================================
# 2. Simulation de Monte Carlo
# ==========================================
print("\n\n=== Estimation de Pi (Monte Carlo) ===")

random.seed(42)

def estimer_pi(nombre_points=10000):
    """Estime Pi avec la méthode de Monte Carlo"""
    points_dans_cercle = 0
    for _ in range(nombre_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            points_dans_cercle += 1
    return 4 * (points_dans_cercle / nombre_points)

print("=" * 50)

for n in [100, 1000, 10000, 100000]:
    random.seed(42)  # Même seed pour chaque test
    pi_estime = estimer_pi(n)
    erreur = abs(pi_estime - math.pi)
    print(f"n = {n:7d} : pi ~= {pi_estime:.6f} (erreur: {erreur:.6f})")

print(f"\nValeur réelle : pi = {math.pi:.6f}")

# ==========================================
# 3. Simulation de notes
# ==========================================
print("\n\n=== Simulation de notes d'examen ===")

random.seed(42)

def simuler_notes_examen(nombre_etudiants, moyenne=12, ecart_type=3):
    notes = []
    for _ in range(nombre_etudiants):
        note = random.gauss(moyenne, ecart_type)
        note = max(0, min(20, note))
        notes.append(round(note, 1))
    return notes

notes = simuler_notes_examen(30, moyenne=12, ecart_type=3)
notes_triees = sorted(notes, reverse=True)

print(f"Analyse de {len(notes)} notes :")
print(f"Note la plus haute : {max(notes)}/20")
print(f"Note la plus basse : {min(notes)}/20")
print(f"Moyenne : {sum(notes)/len(notes):.1f}/20")

reussis = sum(1 for note in notes if note >= 10)
taux_reussite = (reussis / len(notes)) * 100
print(f"Taux de réussite : {taux_reussite:.1f}%")
