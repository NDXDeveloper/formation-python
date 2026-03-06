# ============================================================================
#   Section 3.1 : Classe Compte Bancaire
#   Description : Exemple complet avec dépôt, retrait, intérêts, historique
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class CompteBancaire:
    # Attribut de classe
    taux_interet = 0.02  # 2% d'intérêt

    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial
        self.historique = []

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            self.historique.append(f"Dépôt : +{montant}€")
            print(f"Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print("Le montant doit être positif.")

    def retirer(self, montant):
        if montant > 0:
            if montant <= self.solde:
                self.solde -= montant
                self.historique.append(f"Retrait : -{montant}€")
                print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€")
            else:
                print("Solde insuffisant !")
        else:
            print("Le montant doit être positif.")

    def afficher_solde(self):
        print(f"Compte de {self.titulaire} : {self.solde}€")

    def appliquer_interets(self):
        interets = self.solde * self.taux_interet
        self.solde += interets
        self.historique.append(f"Intérêts : +{interets:.2f}€")
        print(f"Intérêts de {interets:.2f}€ appliqués.")

    def afficher_historique(self):
        print(f"Historique du compte de {self.titulaire} :")
        for operation in self.historique:
            print(f"  - {operation}")

# Utilisation
compte1 = CompteBancaire("Alice", 1000)
compte1.afficher_solde()       # Compte de Alice : 1000€
compte1.deposer(500)           # Dépôt de 500€ effectué. Nouveau solde : 1500€
compte1.retirer(200)           # Retrait de 200€ effectué. Nouveau solde : 1300€
compte1.appliquer_interets()   # Intérêts de 26.00€ appliqués.
compte1.afficher_historique()

compte2 = CompteBancaire("Bob", 500)
compte2.afficher_solde()       # Compte de Bob : 500€
