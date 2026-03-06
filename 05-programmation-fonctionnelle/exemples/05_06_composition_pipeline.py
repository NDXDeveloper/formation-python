# ============================================================================
#   Section 5.5 : Composition de fonctions et pipeline
#   Description : Composition manuelle, fonction composer(), pipeline
#                 de traitement de texte
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

# --- Composition manuelle ---
print("=== Composition manuelle ===")

def ajouter_5(x):
    return x + 5

def multiplier_par_2(x):
    return x * 2

def mettre_au_carre(x):
    return x ** 2

nombre = 3
resultat = mettre_au_carre(multiplier_par_2(ajouter_5(nombre)))
print(resultat)  # ((3 + 5) * 2)^2 = (16)^2 = 256

# --- Fonction de composition ---
print("\n=== Fonction composer() ===")

def composer(*fonctions):
    """Compose plusieurs fonctions de droite à gauche."""
    def fonction_composee(x):
        resultat = x
        for fonction in reversed(fonctions):
            resultat = fonction(resultat)
        return resultat
    return fonction_composee

traitement = composer(mettre_au_carre, multiplier_par_2, ajouter_5)
print(traitement(3))  # 256

# --- Pipeline de traitement ---
print("\n=== Pipeline ===")

def creer_pipeline(*fonctions):
    """Crée un pipeline de fonctions (gauche à droite)."""
    def executer(valeur_initiale):
        resultat = valeur_initiale
        for fonction in fonctions:
            resultat = fonction(resultat)
        return resultat
    return executer

def mettre_en_majuscules(texte):
    return texte.upper()

def ajouter_points_exclamation(texte):
    return f"{texte}!!!"

def entourer_etoiles(texte):
    return f"*** {texte} ***"

pipeline_texte = creer_pipeline(
    mettre_en_majuscules,
    ajouter_points_exclamation,
    entourer_etoiles
)

resultat = pipeline_texte("python")
print(resultat)  # *** PYTHON!!! ***
