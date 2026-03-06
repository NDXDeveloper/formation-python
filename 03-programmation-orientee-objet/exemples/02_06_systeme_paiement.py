# ============================================================================
#   Section 3.2 : Système de paiement
#   Description : Polymorphisme avec CarteBancaire, PayPal, Especes, Cheque
#   Fichier source : 02-heritage-et-polymorphisme.md
# ============================================================================

class MoyenPaiement:
    """Classe de base pour tous les moyens de paiement."""

    def __init__(self, montant):
        self.montant = montant

    def payer(self):
        pass

    def afficher_recu(self):
        print(f"Paiement de {self.montant}€ effectué.")


class CarteBancaire(MoyenPaiement):
    def __init__(self, montant, numero_carte):
        super().__init__(montant)
        self.numero_carte = numero_carte

    def payer(self):
        carte_masquee = "**** **** **** " + self.numero_carte[-4:]
        print(f"Paiement par carte bancaire ({carte_masquee})")
        self.afficher_recu()


class PayPal(MoyenPaiement):
    def __init__(self, montant, email):
        super().__init__(montant)
        self.email = email

    def payer(self):
        print(f"Paiement via PayPal avec le compte : {self.email}")
        self.afficher_recu()


class Especes(MoyenPaiement):
    def payer(self):
        print(f"Paiement en espèces")
        self.afficher_recu()


class Cheque(MoyenPaiement):
    def __init__(self, montant, numero_cheque):
        super().__init__(montant)
        self.numero_cheque = numero_cheque

    def payer(self):
        print(f"Paiement par chèque n°{self.numero_cheque}")
        self.afficher_recu()


def traiter_paiement(moyen_paiement):
    """Cette fonction fonctionne avec tous les types de paiement !"""
    print("\n--- Traitement du paiement ---")
    moyen_paiement.payer()
    print("--- Paiement terminé ---")


# Utilisation avec différents moyens de paiement
paiements = [
    CarteBancaire(150.50, "1234567890123456"),
    PayPal(75.00, "user@example.com"),
    Especes(30.00),
    Cheque(200.00, "CH123456")
]

for paiement in paiements:
    traiter_paiement(paiement)
