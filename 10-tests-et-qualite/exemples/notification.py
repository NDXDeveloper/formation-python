# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Module notification - ServiceNotification avec envoi email
#                 (utilise par les tests de mocking SMTP)
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import smtplib
from email.message import EmailMessage


class ServiceNotification:
    """Service pour envoyer des notifications."""

    def __init__(self, serveur_smtp):
        self.serveur_smtp = serveur_smtp

    def envoyer_email(self, destinataire, sujet, corps):
        """Envoie un email."""
        msg = EmailMessage()
        msg['Subject'] = sujet
        msg['From'] = 'noreply@example.com'
        msg['To'] = destinataire
        msg.set_content(corps)

        with smtplib.SMTP(self.serveur_smtp, 587) as smtp:
            smtp.send_message(msg)

    def notifier_inscription(self, utilisateur):
        """Notifie un utilisateur de son inscription."""
        sujet = "Bienvenue !"
        corps = f"Bonjour {utilisateur['nom']}, bienvenue sur notre plateforme !"
        self.envoyer_email(utilisateur['email'], sujet, corps)
