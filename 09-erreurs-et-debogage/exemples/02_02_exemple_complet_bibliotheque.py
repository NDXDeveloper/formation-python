# ============================================================================
#   Section 9.2 : Creation d'exceptions personnalisees
#   Description : Exemple complet - Systeme de gestion de bibliotheque avec
#                 hierarchie d'exceptions (LivreNonDisponibleError,
#                 LimiteEmpruntsDepasseeError, RetardRetourError)
#   Fichier source : 02-exceptions-personnalisees.md
# ============================================================================

from datetime import datetime, timedelta

# ==========================================
# Hierarchie d'exceptions
# ==========================================

class ErreurBibliotheque(Exception):
    """Exception de base pour la bibliotheque"""
    pass

class LivreNonDisponibleError(ErreurBibliotheque):
    """Le livre n'est pas disponible a l'emprunt"""
    def __init__(self, livre, date_retour_prevue=None):
        self.livre = livre
        self.date_retour_prevue = date_retour_prevue
        message = f"Le livre '{livre}' n'est pas disponible"
        if date_retour_prevue:
            message += f" (retour prevu le {date_retour_prevue.strftime('%d/%m/%Y')})"
        super().__init__(message)

class LimiteEmpruntsDepasseeError(ErreurBibliotheque):
    """L'utilisateur a atteint sa limite d'emprunts"""
    def __init__(self, utilisateur, limite):
        self.utilisateur = utilisateur
        self.limite = limite
        super().__init__(
            f"{utilisateur} a atteint la limite de {limite} emprunts simultanes"
        )

class RetardRetourError(ErreurBibliotheque):
    """Le livre est en retard"""
    def __init__(self, livre, jours_retard, amende):
        self.livre = livre
        self.jours_retard = jours_retard
        self.amende = amende
        super().__init__(
            f"Retard de {jours_retard} jours pour '{livre}'. Amende : {amende}EUR"
        )

# ==========================================
# Classe Bibliotheque
# ==========================================

class Bibliotheque:
    def __init__(self):
        self.livres = {}  # livre -> disponible (True/False)
        self.emprunts = {}  # utilisateur -> [livres empruntes]
        self.limite_emprunts = 3

    def ajouter_livre(self, titre):
        self.livres[titre] = True

    def emprunter(self, utilisateur, livre):
        if livre not in self.livres:
            raise ValueError(f"Le livre '{livre}' n'existe pas dans la bibliotheque")

        if not self.livres[livre]:
            date_retour = datetime.now() + timedelta(days=14)
            raise LivreNonDisponibleError(livre, date_retour)

        emprunts_utilisateur = self.emprunts.get(utilisateur, [])
        if len(emprunts_utilisateur) >= self.limite_emprunts:
            raise LimiteEmpruntsDepasseeError(utilisateur, self.limite_emprunts)

        self.livres[livre] = False
        if utilisateur not in self.emprunts:
            self.emprunts[utilisateur] = []
        self.emprunts[utilisateur].append(livre)
        print(f"  '{livre}' emprunte par {utilisateur}")

# ==========================================
# Utilisation
# ==========================================
print("=== Systeme de gestion de bibliotheque ===\n")

biblio = Bibliotheque()
biblio.ajouter_livre("Python pour les debutants")
biblio.ajouter_livre("Le Seigneur des Anneaux")
biblio.ajouter_livre("Clean Code")
biblio.ajouter_livre("Design Patterns")

# Test 1: Emprunt reussi
print("Test 1 - Emprunt reussi:")
try:
    biblio.emprunter("Alice", "Python pour les debutants")
except ErreurBibliotheque as e:
    print(f"  Erreur : {e}")

# Test 2: Livre deja emprunte
print("\nTest 2 - Livre deja emprunte:")
try:
    biblio.emprunter("Bob", "Python pour les debutants")
except LivreNonDisponibleError as e:
    print(f"  Erreur : {e}")
    if e.date_retour_prevue:
        print(f"  Reservez-le pour le {e.date_retour_prevue.strftime('%d/%m/%Y')}")
except ErreurBibliotheque as e:
    print(f"  Erreur : {e}")

# Test 3: Limite d'emprunts
print("\nTest 3 - Limite d'emprunts:")
try:
    biblio.emprunter("Alice", "Le Seigneur des Anneaux")
    biblio.emprunter("Alice", "Clean Code")
    biblio.emprunter("Alice", "Design Patterns")  # 4eme emprunt -> erreur
except LimiteEmpruntsDepasseeError as e:
    print(f"  Erreur : {e}")
    print(f"  Limite : {e.limite} emprunts pour {e.utilisateur}")
except ErreurBibliotheque as e:
    print(f"  Erreur : {e}")

# Test 4: Livre inexistant
print("\nTest 4 - Livre inexistant:")
try:
    biblio.emprunter("Alice", "Livre inconnu")
except ValueError as e:
    print(f"  Erreur : {e}")

# Test 5: RetardRetourError
print("\nTest 5 - Retard de retour:")
try:
    raise RetardRetourError("Python pour les debutants", jours_retard=5, amende=2.5)
except RetardRetourError as e:
    print(f"  Erreur : {e}")
    print(f"  Jours de retard : {e.jours_retard}")
    print(f"  Amende : {e.amende}EUR")
