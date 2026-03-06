# ============================================================================
#   Section 12.3 : Patterns de conception courants
#   Description : Patterns comportementaux - Observer (notifications, blog),
#                 Strategy (paiement, compression), Iterator (playlist,
#                 countdown, pagination, generateurs)
#   Fichier source : 03-patterns-de-conception.md
# ============================================================================

"""Patterns comportementaux : Observer, Strategy, Iterator."""

from abc import ABC, abstractmethod


# ============================================================
# PATTERN 4 : OBSERVER
# ============================================================
print("=" * 50)
print("PATTERN 4 : OBSERVER")
print("=" * 50)

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


class Subject:
    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)


# --- Notifications ---

class EmailNotifier(Observer):
    def update(self, message: str):
        print(f"  [Email] {message}")


class SMSNotifier(Observer):
    def update(self, message: str):
        print(f"  [SMS] {message}")


class PushNotifier(Observer):
    def update(self, message: str):
        print(f"  [Push] {message}")


commande = Subject()
commande.attach(EmailNotifier())
commande.attach(SMSNotifier())
commande.attach(PushNotifier())

print("\n  --- Notification commande ---")
commande.notify("Votre commande a ete expediee !")


# --- Systeme de blog ---

class BlogPost(Subject):
    def __init__(self, titre: str):
        super().__init__()
        self.titre = titre
        self.contenu = ""

    def publier(self, contenu: str):
        self.contenu = contenu
        self.notify(f"Nouvel article publie : {self.titre}")

    def modifier(self, nouveau_contenu: str):
        self.contenu = nouveau_contenu
        self.notify(f"Article modifie : {self.titre}")


class Abonne(Observer):
    def __init__(self, nom: str):
        self.nom = nom

    def update(self, message: str):
        print(f"  {self.nom} a recu : {message}")


article = BlogPost("Introduction a Python")

alice = Abonne("Alice")
bob = Abonne("Bob")
charlie = Abonne("Charlie")

article.attach(alice)
article.attach(bob)
article.attach(charlie)

print("\n  --- Publication ---")
article.publier("Python est un langage genial...")

article.detach(bob)

print("\n  --- Modification (Bob desabonne) ---")
article.modifier("Python est vraiment genial!")


# ============================================================
# PATTERN 5 : STRATEGY
# ============================================================
print(f"\n{'=' * 50}")
print("PATTERN 5 : STRATEGY")
print("=" * 50)

# --- Strategies de paiement ---

class PaymentStrategy(ABC):
    @abstractmethod
    def payer(self, montant: float) -> str:
        pass


class CarteBancaire(PaymentStrategy):
    def __init__(self, numero: str):
        self.numero = numero

    def payer(self, montant: float) -> str:
        return f"Paiement de {montant} EUR par carte {self.numero[-4:]}"


class PayPal(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def payer(self, montant: float) -> str:
        return f"Paiement de {montant} EUR via PayPal ({self.email})"


class Crypto(PaymentStrategy):
    def __init__(self, wallet: str):
        self.wallet = wallet

    def payer(self, montant: float) -> str:
        return f"Paiement de {montant} EUR en crypto (wallet: {self.wallet})"


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def ajouter_item(self, item: str, prix: float):
        self.items.append({"item": item, "prix": prix})

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def checkout(self):
        total = round(sum(item["prix"] for item in self.items), 2)
        if self.payment_strategy is None:
            return "Veuillez choisir un moyen de paiement"
        return self.payment_strategy.payer(total)


cart = ShoppingCart()
cart.ajouter_item("Livre Python", 29.99)
cart.ajouter_item("Clavier", 79.99)

cart.set_payment_strategy(CarteBancaire("1234-5678-9012-3456"))
print(f"\n  {cart.checkout()}")

cart.set_payment_strategy(PayPal("user@example.com"))
print(f"  {cart.checkout()}")

cart.set_payment_strategy(Crypto("0xABC123"))
print(f"  {cart.checkout()}")


# --- Strategies de compression ---

class CompressionStrategy(ABC):
    @abstractmethod
    def compresser(self, data: str) -> str:
        pass


class ZipCompression(CompressionStrategy):
    def compresser(self, data: str) -> str:
        return f"[ZIP] {data[:20]}... (compresse)"


class RarCompression(CompressionStrategy):
    def compresser(self, data: str) -> str:
        return f"[RAR] {data[:20]}... (compresse)"


class GzipCompression(CompressionStrategy):
    def compresser(self, data: str) -> str:
        return f"[GZIP] {data[:20]}... (compresse)"


class FileCompressor:
    def __init__(self, strategy: CompressionStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CompressionStrategy):
        self.strategy = strategy

    def compress_file(self, filename: str, data: str):
        compressed = self.strategy.compresser(data)
        print(f"  Fichier {filename} : {compressed}")


data = "Beaucoup de donnees a compresser..." * 10

print(f"\n  --- Compression ---")
compressor = FileCompressor(ZipCompression())
compressor.compress_file("document.txt", data)

compressor.set_strategy(GzipCompression())
compressor.compress_file("image.jpg", data)

compressor.set_strategy(RarCompression())
compressor.compress_file("archive.dat", data)


# ============================================================
# PATTERN 7 : ITERATOR
# ============================================================
print(f"\n{'=' * 50}")
print("PATTERN 7 : ITERATOR")
print("=" * 50)

# --- Playlist ---

class Playlist:
    def __init__(self, nom: str):
        self.nom = nom
        self.chansons = []

    def ajouter_chanson(self, chanson: str):
        self.chansons.append(chanson)

    def __iter__(self):
        return iter(self.chansons)


playlist = Playlist("Ma playlist")
playlist.ajouter_chanson("Song 1")
playlist.ajouter_chanson("Song 2")
playlist.ajouter_chanson("Song 3")

print(f"\n  --- {playlist.nom} ---")
for chanson in playlist:
    print(f"  > {chanson}")


# --- Iterateur personnalise : CountDown ---

class CountDown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


print(f"\n  --- CountDown ---")
countdown = CountDown(5)
for num in countdown:
    print(f"  {num}")


# --- Pagination ---

class Paginator:
    def __init__(self, items: list, page_size: int = 10):
        self.items = items
        self.page_size = page_size
        self.num_pages = (len(items) + page_size - 1) // page_size

    def __iter__(self):
        self.current_page = 0
        return self

    def __next__(self):
        if self.current_page >= self.num_pages:
            raise StopIteration
        start = self.current_page * self.page_size
        end = start + self.page_size
        page = self.items[start:end]
        self.current_page += 1
        return page


data = list(range(1, 26))
paginator = Paginator(data, page_size=10)

print(f"\n  --- Pagination ---")
for page_num, page in enumerate(paginator, 1):
    print(f"  Page {page_num}: {page}")


# --- Generateurs ---

def countdown_gen(start: int):
    while start > 0:
        yield start
        start -= 1


def paginate(items: list, page_size: int = 10):
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]


print(f"\n  --- Generateur countdown ---")
print(f"  {list(countdown_gen(5))}")

print(f"\n  --- Generateur pagination ---")
for page in paginate(list(range(1, 16)), page_size=5):
    print(f"  {page}")
