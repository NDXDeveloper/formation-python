# ============================================================================
#   Section 5.4 : Méthodes avancées des générateurs
#   Description : send() pour envoyer des valeurs, close() pour fermer,
#                 throw() pour envoyer une exception
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- send() ---
print("=== send() ===")

def generateur_avec_send():
    """Générateur qui peut recevoir des valeurs."""
    total = 0
    while True:
        valeur = yield total
        if valeur is not None:
            total += valeur

gen = generateur_avec_send()

# Démarrer le générateur
print(next(gen))  # 0

# Envoyer des valeurs
print(gen.send(10))  # 10
print(gen.send(5))   # 15
print(gen.send(3))   # 18

# --- close() ---
print("\n=== close() ===")

def mon_generateur():
    """Générateur avec gestion de la fermeture."""
    try:
        for i in range(10):
            yield i
    finally:
        print("Générateur fermé")

gen = mon_generateur()

print(next(gen))  # 0
print(next(gen))  # 1

# Fermer le générateur
gen.close()  # Affiche : Générateur fermé

# --- throw() ---
print("\n=== throw() ===")

def generateur_resilient():
    """Générateur qui gère les exceptions."""
    while True:
        try:
            valeur = yield
            print(f"Reçu : {valeur}")
        except ValueError:
            print("Erreur ValueError capturée !")

gen = generateur_resilient()
next(gen)  # Démarrer

gen.send(10)  # Reçu : 10
gen.throw(ValueError("Une erreur"))  # Erreur ValueError capturée !
gen.send(20)  # Reçu : 20

# --- return dans un générateur ---
print("\n=== return dans un générateur ===")

# return seul : arrête le générateur prématurément
def generer_jusqu_a_negatif(nombres):
    for n in nombres:
        if n < 0:
            return          # stoppe dès qu'on rencontre un négatif
        yield n

print(list(generer_jusqu_a_negatif([1, 2, 3, -1, 4])))  # [1, 2, 3]

# return valeur : récupéré par yield from
def sous_generateur():
    yield "a"
    yield "b"
    return "FINI"

def delegue():
    resultat = yield from sous_generateur()
    print(f"Valeur de return : {resultat}")

list(delegue())  # affiche : Valeur de return : FINI
