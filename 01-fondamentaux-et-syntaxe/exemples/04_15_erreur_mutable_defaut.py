# ============================================================================
#   Section 4.15 : Erreur classique : valeur par défaut mutable
#   Description : Piège de la liste comme valeur par défaut, solution avec None
#   Fichier source : 04-fonctions-et-portee.md
# ============================================================================

# --- Erreur classique ---
def ajouter_a_liste_bug(element, liste=[]):
    liste.append(element)
    return liste

print("Bug avec valeur par défaut mutable :")
print(ajouter_a_liste_bug(1))  # [1]
print(ajouter_a_liste_bug(2))  # [1, 2] - la liste est partagée !

# --- Solution correcte ---
print()

def ajouter_a_liste(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

print("Version corrigée :")
print(ajouter_a_liste(1))  # [1]
print(ajouter_a_liste(2))  # [2] - chaque appel a sa propre liste

# --- Erreur : modifier l'argument original ---
print()

def ajouter_element_bug(liste, element):
    liste.append(element)
    return liste

ma_liste = [1, 2, 3]
nouvelle_liste = ajouter_element_bug(ma_liste, 4)
print(f"ma_liste : {ma_liste}")  # [1, 2, 3, 4] - modifié !

# --- Solution : copier la liste ---
print()

def ajouter_element_safe(liste, element):
    nouvelle = liste.copy()
    nouvelle.append(element)
    return nouvelle

ma_liste = [1, 2, 3]
nouvelle_liste = ajouter_element_safe(ma_liste, 4)
print(f"ma_liste : {ma_liste}")       # [1, 2, 3] - inchangé
print(f"nouvelle_liste : {nouvelle_liste}")  # [1, 2, 3, 4]
