# ============================================================================
#   Section 7.2 : Les modules datetime et time
#   Description : Exemples pratiques - système de rappels, journal de logs,
#                 calculateur de travail, calculateur d'échéances
#   Fichier source : 02-datetime-et-time.md
# ============================================================================

from datetime import datetime, timedelta
import os
import calendar

# ==========================================
# 1. Système de rappels
# ==========================================
print("=== 1. Système de rappels ===")

class Rappel:
    """Système simple de rappels"""

    def __init__(self):
        self.rappels = []

    def ajouter(self, message, dans_combien_de_temps):
        moment = datetime.now() + dans_combien_de_temps
        self.rappels.append({
            'message': message,
            'moment': moment
        })
        print(f"  Rappel ajouté pour {moment.strftime('%d/%m/%Y a %H:%M')}")

    def verifier(self):
        maintenant = datetime.now()
        rappels_a_supprimer = []
        for i, rappel in enumerate(self.rappels):
            if maintenant >= rappel['moment']:
                print(f"  RAPPEL : {rappel['message']}")
                rappels_a_supprimer.append(i)
        for i in reversed(rappels_a_supprimer):
            del self.rappels[i]

    def lister(self):
        if not self.rappels:
            print("  Aucun rappel actif")
            return
        print("  Rappels actifs :")
        for rappel in sorted(self.rappels, key=lambda r: r['moment']):
            temps_restant = rappel['moment'] - datetime.now()
            jours = temps_restant.days
            heures = temps_restant.seconds // 3600
            minutes = (temps_restant.seconds % 3600) // 60
            print(f"    - {rappel['message']} (dans {jours}j {heures}h {minutes}min)")

systeme = Rappel()
systeme.ajouter("Réunion d'équipe", timedelta(hours=2))
systeme.ajouter("Appeler le dentiste", timedelta(days=1))
systeme.ajouter("Réviser Python", timedelta(hours=1, minutes=30))
systeme.lister()
systeme.verifier()

# ==========================================
# 2. Journal de logs avec horodatage
# ==========================================
print("\n=== 2. Journal de logs ===")

class Journal:
    """Système simple de journal avec horodatage"""

    def __init__(self, nom_fichier="journal.txt"):
        self.nom_fichier = nom_fichier
        self.lignes = []

    def log(self, message, niveau="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = f"[{timestamp}] [{niveau}] {message}"
        self.lignes.append(ligne)
        print(f"  {ligne}")

    def info(self, message):
        self.log(message, "INFO")

    def warning(self, message):
        self.log(message, "WARNING")

    def error(self, message):
        self.log(message, "ERROR")

    def sauvegarder(self):
        with open(self.nom_fichier, "w", encoding="utf-8") as f:
            for ligne in self.lignes:
                f.write(ligne + "\n")

    def lire(self, dernieres=10):
        print(f"\n  Dernières {min(dernieres, len(self.lignes))} entrées :")
        for ligne in self.lignes[-dernieres:]:
            print(f"    {ligne}")

journal = Journal("_temp_journal.txt")
journal.info("Application démarrée")
journal.info("Connexion à la base de données")
journal.warning("Mémoire utilisée : 80%")
journal.error("Échec de connexion au serveur")
journal.info("Application arrêtée")
journal.lire()
journal.sauvegarder()

# Nettoyage
os.remove("_temp_journal.txt")

# ==========================================
# 3. Calculateur de temps de travail
# ==========================================
print("\n=== 3. Calculateur de temps de travail ===")

class CalculateurTravail:
    """Calcule les heures de travail"""

    def __init__(self):
        self.entrees = []

    def pointer(self, type_pointage, moment):
        self.entrees.append({'type': type_pointage, 'moment': moment})
        type_texte = "Entree" if type_pointage == 'entree' else "Sortie"
        print(f"  {type_texte} : {moment.strftime('%H:%M:%S')}")

    def calculer_temps_travail(self):
        temps_total = timedelta()
        dernier_entree = None
        for entree in self.entrees:
            if entree['type'] == 'entree':
                dernier_entree = entree['moment']
            elif entree['type'] == 'sortie' and dernier_entree:
                temps_total += entree['moment'] - dernier_entree
                dernier_entree = None
        return temps_total.total_seconds() / 3600

    def afficher_resume(self):
        heures = self.calculer_temps_travail()
        taux_horaire = 15.0
        salaire = heures * taux_horaire
        print(f"  Temps de travail total : {heures:.2f} heures")
        print(f"  Salaire estimé ({taux_horaire} EUR/h) : {salaire:.2f} EUR")

calc = CalculateurTravail()

# Simuler une journée avec des heures fixes
base = datetime(2025, 10, 27)
calc.pointer('entree', base.replace(hour=8, minute=0))
calc.pointer('sortie', base.replace(hour=12, minute=0))   # Pause déjeuner
calc.pointer('entree', base.replace(hour=13, minute=0))    # Reprise
calc.pointer('sortie', base.replace(hour=17, minute=0))    # Fin

print("\n  Résumé :")
calc.afficher_resume()

# ==========================================
# 4. Calculateur d'échéances
# ==========================================
print("\n=== 4. Calculateur d'échéances ===")

def calculer_echeances(date_debut, montant_total, nombre_mensualites):
    """Calcule les échéances d'un prêt"""
    echeances = []
    montant_mensuel = montant_total / nombre_mensualites

    for i in range(nombre_mensualites):
        mois_total = date_debut.month + i
        annee = date_debut.year + (mois_total - 1) // 12
        mois = ((mois_total - 1) % 12) + 1

        _, max_jour = calendar.monthrange(annee, mois)
        jour = min(date_debut.day, max_jour)

        date_echeance = datetime(annee, mois, jour)
        echeances.append({
            'numero': i + 1,
            'date': date_echeance,
            'montant': montant_mensuel,
            'reste': montant_total - (montant_mensuel * (i + 1))
        })

    return echeances

date_debut = datetime(2025, 1, 15)
montant = 10000
duree = 12

print("Plan de remboursement")
print("=" * 60)

echeances = calculer_echeances(date_debut, montant, duree)

for ech in echeances:
    date_str = ech['date'].strftime('%d/%m/%Y')
    print(f"  Mensualité {ech['numero']:2d} - {date_str} : "
          f"{ech['montant']:7.2f} EUR (reste : {ech['reste']:7.2f} EUR)")

print("=" * 60)
print(f"Total : {montant:.2f} EUR")
