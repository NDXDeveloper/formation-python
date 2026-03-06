# ============================================================================
#   Section 3.5 : Duck typing et protocoles
#   Description : Duck typing avec Fichier/Logger, protocoles avec
#                 typing.Protocol (Drawable)
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# --- Duck typing ---
class Fichier:
    def __init__(self, nom):
        self.nom = nom
        self.contenu = []

    def write(self, texte):
        self.contenu.append(texte)

    def read(self):
        return ''.join(self.contenu)

class Logger:
    def __init__(self, sortie):
        self.sortie = sortie  # Peut être un fichier, ou notre Fichier

    def log(self, message):
        self.sortie.write(f"[LOG] {message}\n")

# Fonctionne avec notre classe Fichier !
fake_file = Fichier("memory.txt")
logger2 = Logger(fake_file)
logger2.log("Message 1")
logger2.log("Message 2")

print(fake_file.read())

# --- Protocoles avec typing.Protocol ---
print()

from typing import Protocol

class Drawable(Protocol):
    """Protocole : définit une interface sans héritage"""
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "O"

class Square:
    def draw(self) -> str:
        return "[]"

def render(shape: Drawable) -> None:
    """Accepte n'importe quel objet qui a une méthode draw()"""
    print(shape.draw())

# Fonctionne sans que Circle ou Square héritent de Drawable
render(Circle())  # O
render(Square())  # []
