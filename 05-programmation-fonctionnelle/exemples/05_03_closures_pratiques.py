# ============================================================================
#   Section 5.5 : Cas d'usage pratiques des closures
#   Description : Fabrique de fonctions, configuration, encapsulation,
#                 décorateur compteur, callbacks avec contexte
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

# --- Fabrique de fonctions ---
print("=== Fabrique de puissances ===")

def creer_puissance(exposant):
    """Crée une fonction qui élève à une puissance donnée."""
    def calculer(base):
        return base ** exposant
    return calculer

carre = creer_puissance(2)
cube = creer_puissance(3)
puissance_quatre = creer_puissance(4)

print(carre(5))            # 25
print(cube(3))             # 27
print(puissance_quatre(2)) # 16

# --- Configuration de fonctions ---
print("\n=== Formateur ===")

def creer_formateur(prefixe, suffixe):
    """Crée une fonction de formatage personnalisée."""
    def formater(texte):
        return f"{prefixe}{texte}{suffixe}"
    return formater

html_bold = creer_formateur("<b>", "</b>")
html_italic = creer_formateur("<i>", "</i>")
parentheses = creer_formateur("(", ")")

print(html_bold("Important"))      # <b>Important</b>
print(html_italic("Emphase"))      # <i>Emphase</i>
print(parentheses("note"))         # (note)

# --- Encapsulation de données privées ---
print("\n=== Compte bancaire ===")

def creer_compte_bancaire(solde_initial):
    """Crée un compte bancaire avec encapsulation."""
    solde = solde_initial

    def deposer(montant):
        nonlocal solde
        if montant > 0:
            solde += montant
            return f"Dépôt de {montant}EUR. Nouveau solde : {solde}EUR"
        return "Montant invalide"

    def retirer(montant):
        nonlocal solde
        if 0 < montant <= solde:
            solde -= montant
            return f"Retrait de {montant}EUR. Nouveau solde : {solde}EUR"
        return "Montant invalide ou insuffisant"

    def consulter_solde():
        return f"Solde actuel : {solde}EUR"

    return {
        'deposer': deposer,
        'retirer': retirer,
        'solde': consulter_solde
    }

compte = creer_compte_bancaire(1000)
print(compte['solde']())           # Solde actuel : 1000EUR
print(compte['deposer'](500))      # Dépôt de 500EUR. Nouveau solde : 1500EUR
print(compte['retirer'](200))      # Retrait de 200EUR. Nouveau solde : 1300EUR
print(compte['solde']())           # Solde actuel : 1300EUR

# --- Décorateur compteur d'appels ---
print("\n=== Compteur d'appels ===")

def compteur_appels(fonction):
    """Décorateur qui compte les appels d'une fonction."""
    nombre_appels = 0

    def wrapper(*args, **kwargs):
        nonlocal nombre_appels
        nombre_appels += 1
        print(f"Appel n.{nombre_appels} de {fonction.__name__}")
        return fonction(*args, **kwargs)

    wrapper.nombre_appels = lambda: nombre_appels
    return wrapper

@compteur_appels
def dire_bonjour(nom):
    return f"Bonjour {nom} !"

print(dire_bonjour("Alice"))
print(dire_bonjour("Bob"))
print(dire_bonjour("Charlie"))
print(f"Total d'appels : {dire_bonjour.nombre_appels()}")  # 3

# --- Callbacks avec contexte ---
print("\n=== Callbacks ===")

def creer_gestionnaire_evenement(nom_evenement):
    """Crée un gestionnaire d'événement avec contexte."""
    compteur = 0

    def gestionnaire(message):
        nonlocal compteur
        compteur += 1
        print(f"[{nom_evenement}] Événement #{compteur}: {message}")

    return gestionnaire

on_click = creer_gestionnaire_evenement("CLICK")
on_hover = creer_gestionnaire_evenement("HOVER")

on_click("Bouton pressé")
on_hover("Souris sur élément")
on_click("Nouveau clic")
