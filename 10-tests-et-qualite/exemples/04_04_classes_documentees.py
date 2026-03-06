# ============================================================================
#   Section 10.4 : Documentation avec docstrings
#   Description : Classes documentees - CompteBancaire, Vehicule, Voiture
#                 avec heritage et docstrings Google Style
#   Fichier source : 04-documentation-docstrings.md
# ============================================================================


class CompteBancaire:
    """Represente un compte bancaire.

    Cette classe permet de gerer un compte bancaire avec
    des operations de depot et de retrait.

    Attributes:
        titulaire (str): Le nom du titulaire du compte.
        solde (float): Le solde actuel du compte.
        numero (str): Le numero unique du compte.

    Example:
        >>> compte = CompteBancaire("Alice", "FR123456")
        >>> compte.deposer(1000)
        >>> compte.solde
        1000.0
    """

    def __init__(self, titulaire, numero):
        """Initialise un nouveau compte bancaire.

        Args:
            titulaire (str): Le nom du titulaire.
            numero (str): Le numero de compte.
        """
        self.titulaire = titulaire
        self.numero = numero
        self.solde = 0.0

    def deposer(self, montant):
        """Depose de l'argent sur le compte.

        Args:
            montant (float): Le montant a deposer.

        Raises:
            ValueError: Si le montant est negatif ou nul.
        """
        if montant <= 0:
            raise ValueError("Le montant doit etre positif")
        self.solde += montant

    def retirer(self, montant):
        """Retire de l'argent du compte.

        Args:
            montant (float): Le montant a retirer.

        Raises:
            ValueError: Si le montant est negatif, nul,
                ou superieur au solde.
        """
        if montant <= 0:
            raise ValueError("Le montant doit etre positif")
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant


class Vehicule:
    """Classe de base pour representer un vehicule.

    Attributes:
        marque (str): La marque du vehicule.
        modele (str): Le modele du vehicule.
        annee (int): L'annee de fabrication.
    """

    def __init__(self, marque, modele, annee):
        """Initialise un vehicule.

        Args:
            marque (str): La marque.
            modele (str): Le modele.
            annee (int): L'annee.
        """
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def description(self):
        """Retourne une description du vehicule.

        Returns:
            str: Description formatee du vehicule.
        """
        return f"{self.marque} {self.modele} ({self.annee})"


class Voiture(Vehicule):
    """Represente une voiture.

    Herite de Vehicule et ajoute le nombre de portes.

    Attributes:
        marque (str): Herite de Vehicule.
        modele (str): Herite de Vehicule.
        annee (int): Herite de Vehicule.
        nb_portes (int): Le nombre de portes.

    Example:
        >>> voiture = Voiture("Renault", "Clio", 2020, 5)
        >>> voiture.description()
        'Renault Clio (2020) - 5 portes'
    """

    def __init__(self, marque, modele, annee, nb_portes):
        """Initialise une voiture.

        Args:
            marque (str): La marque.
            modele (str): Le modele.
            annee (int): L'annee.
            nb_portes (int): Le nombre de portes (3 ou 5).

        Raises:
            ValueError: Si le nombre de portes n'est pas 3 ou 5.
        """
        super().__init__(marque, modele, annee)
        if nb_portes not in [3, 5]:
            raise ValueError("Une voiture a 3 ou 5 portes")
        self.nb_portes = nb_portes

    def description(self):
        """Retourne une description detaillee de la voiture.

        Surcharge la methode de la classe parente pour inclure
        le nombre de portes.

        Returns:
            str: Description formatee de la voiture.
        """
        desc_base = super().description()
        return f"{desc_base} - {self.nb_portes} portes"


# --- Demonstration ---
print("=== CompteBancaire ===")
compte = CompteBancaire("Alice", "FR123456")
compte.deposer(1000)
print(f"Titulaire : {compte.titulaire}")
print(f"Numero : {compte.numero}")
print(f"Solde apres depot de 1000 : {compte.solde}")
compte.retirer(300)
print(f"Solde apres retrait de 300 : {compte.solde}")

try:
    compte.retirer(2000)
except ValueError as e:
    print(f"Retrait de 2000 -> ValueError: {e}")

print("\n=== Vehicule et Voiture (heritage) ===")
vehicule = Vehicule("Toyota", "Yaris", 2022)
print(f"Vehicule : {vehicule.description()}")

voiture = Voiture("Renault", "Clio", 2020, 5)
print(f"Voiture : {voiture.description()}")

voiture3p = Voiture("Peugeot", "208", 2021, 3)
print(f"Voiture 3 portes : {voiture3p.description()}")

try:
    Voiture("Fiat", "500", 2023, 4)
except ValueError as e:
    print(f"Voiture 4 portes -> ValueError: {e}")
