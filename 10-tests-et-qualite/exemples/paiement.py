# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Module paiement - ServicePaiement avec API et base de donnees
#                 (utilise par les tests complets de mocking)
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import requests
from datetime import datetime


class ServicePaiement:
    """Gere les paiements."""

    def __init__(self, api_url, api_key, base_de_donnees):
        self.api_url = api_url
        self.api_key = api_key
        self.db = base_de_donnees

    def traiter_paiement(self, utilisateur_id, montant):
        """Traite un paiement."""
        # Valider le montant
        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        # Verifier l'utilisateur dans la base
        utilisateur = self.db.obtenir_utilisateur(utilisateur_id)
        if not utilisateur:
            raise ValueError("Utilisateur introuvable")

        # Appeler l'API de paiement
        response = requests.post(
            f"{self.api_url}/charge",
            json={
                "user_id": utilisateur_id,
                "amount": montant,
                "currency": "EUR"
            },
            headers={"Authorization": f"Bearer {self.api_key}"}
        )

        if response.status_code != 200:
            raise Exception("Échec du paiement")

        # Enregistrer la transaction
        transaction = {
            "utilisateur_id": utilisateur_id,
            "montant": montant,
            "date": datetime.now(),
            "statut": "réussi",
            "transaction_id": response.json()["transaction_id"]
        }

        self.db.sauvegarder_transaction(transaction)

        return transaction
