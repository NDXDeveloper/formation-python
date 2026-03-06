# ============================================================================
#   Section 5.3 : Retry et empiler plusieurs décorateurs
#   Description : Décorateur retry (réessayer en cas d'échec),
#                 empiler plusieurs décorateurs, ordre d'application
#   Fichier source : 03-decorateurs-avances.md
# ============================================================================

# --- Retry (sans time.sleep pour éviter l'attente) ---
print("=== Retry ===")

def retry(nombre_essais=3, delai=0):
    """Réessaie l'exécution d'une fonction en cas d'erreur."""
    def decorateur(fonction):
        def fonction_modifiee(*args, **kwargs):
            for tentative in range(1, nombre_essais + 1):
                try:
                    print(f"[retry] Tentative {tentative}/{nombre_essais}")
                    resultat = fonction(*args, **kwargs)
                    print(f"[ok] Succès !")
                    return resultat
                except Exception as e:
                    print(f"[erreur] Erreur : {e}")
                    if tentative < nombre_essais:
                        print(f"[attente] Nouvel essai...")
                    else:
                        print(f"[echec] Échec après {nombre_essais} tentatives")
                        raise
        return fonction_modifiee
    return decorateur

compteur_appels = 0

@retry(nombre_essais=3)
def operation_instable():
    """Simule une opération qui échoue les 2 premières fois."""
    global compteur_appels
    compteur_appels += 1
    if compteur_appels < 3:
        raise Exception("Connexion perdue")
    return "Données récupérées"

resultat = operation_instable()
print(f"Résultat : {resultat}")

# --- Empiler plusieurs décorateurs ---
print("\n=== Empiler décorateurs ===")

def decorateur_1(fonction):
    def fonction_modifiee(*args, **kwargs):
        print(">>> Décorateur 1 - Avant")
        resultat = fonction(*args, **kwargs)
        print("<<< Décorateur 1 - Après")
        return resultat
    return fonction_modifiee

def decorateur_2(fonction):
    def fonction_modifiee(*args, **kwargs):
        print("  >> Décorateur 2 - Avant")
        resultat = fonction(*args, **kwargs)
        print("  << Décorateur 2 - Après")
        return resultat
    return fonction_modifiee

@decorateur_1
@decorateur_2
def ma_fonction():
    print("    Exécution de la fonction")

ma_fonction()
# >>> Décorateur 1 - Avant
#   >> Décorateur 2 - Avant
#     Exécution de la fonction
#   << Décorateur 2 - Après
# <<< Décorateur 1 - Après
