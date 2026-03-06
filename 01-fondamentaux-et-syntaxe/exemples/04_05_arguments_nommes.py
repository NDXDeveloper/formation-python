# ============================================================================
#   Section 4.5 : Arguments nommés (keyword arguments)
#   Description : Appel par nom, mélange positionnels et nommés
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Arguments nommés ---
def presenter(nom, age, ville):
    print(f"{nom}, {age} ans, {ville}")

# Appel avec arguments positionnels (ordre important)
presenter("Alice", 25, "Paris")

# Appel avec arguments nommés (ordre n'importe pas)
presenter(ville="Lyon", nom="Bob", age=30)
presenter(age=35, ville="Marseille", nom="Charlie")

# --- Mélanger positionnels et nommés ---
print()

def creer_profil(nom, age, ville="Paris", pays="France"):
    print(f"{nom}, {age} ans, {ville}, {pays}")

creer_profil("Alice", 25)
creer_profil("Bob", 30, ville="Lyon")
creer_profil("Charlie", 35, pays="Belgique")
creer_profil("David", 40, "Marseille", pays="France")
