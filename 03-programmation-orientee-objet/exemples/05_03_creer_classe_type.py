# ============================================================================
#   Section 3.5 : Créer des classes avec type()
#   Description : Classe vide, avec attributs/méthodes, et avec héritage
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# --- Classe vide ---
MaClasse = type('MaClasse', (), {})

obj = MaClasse()
print(type(obj))  # <class '__main__.MaClasse'>

# --- Classe avec attributs ---
print()

def saluer(self):
    return f"Bonjour, je suis {self.nom}"

Personne = type('Personne', (), {
    'espece': 'Homo sapiens',  # Attribut de classe
    'saluer': saluer           # Méthode
})

p = Personne()
p.nom = "Alice"
print(p.saluer())     # Bonjour, je suis Alice
print(p.espece)       # Homo sapiens

# --- Classe avec héritage ---
print()

class Animal:
    def respirer(self):
        return "Je respire"

def aboyer(self):
    return "Wouf !"

Chien = type('Chien', (Animal,), {
    'aboyer': aboyer
})

rex = Chien()
print(rex.respirer())  # Je respire (hérité)
print(rex.aboyer())    # Wouf !
