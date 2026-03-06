# ============================================================================
#   Section 10.3 : Couverture de code
#   Description : Module utilisateur etendu avec roles et
#                 GestionnaireUtilisateurs (pour demo couverture complete)
#   Fichier source : 03-couverture-de-code.md
# ============================================================================


class Utilisateur:
    """Represente un utilisateur du systeme."""

    def __init__(self, nom, email, age):
        self.nom = nom
        self.email = email
        self.age = age
        self.actif = True
        self.roles = []

    def est_majeur(self):
        """Verifie si l'utilisateur est majeur."""
        return self.age >= 18

    def desactiver(self):
        """Desactive l'utilisateur."""
        self.actif = False

    def activer(self):
        """Active l'utilisateur."""
        self.actif = True

    def ajouter_role(self, role):
        """Ajoute un role a l'utilisateur."""
        if role not in self.roles:
            self.roles.append(role)

    def retirer_role(self, role):
        """Retire un role a l'utilisateur."""
        if role in self.roles:
            self.roles.remove(role)

    def a_role(self, role):
        """Verifie si l'utilisateur a un role."""
        return role in self.roles

    def est_admin(self):
        """Verifie si l'utilisateur est administrateur."""
        return "admin" in self.roles


class GestionnaireUtilisateurs:
    """Gere une collection d'utilisateurs."""

    def __init__(self):
        self.utilisateurs = {}
        self._prochain_id = 1

    def ajouter(self, utilisateur):
        """Ajoute un utilisateur."""
        user_id = self._prochain_id
        self.utilisateurs[user_id] = utilisateur
        self._prochain_id += 1
        return user_id

    def obtenir(self, user_id):
        """Obtient un utilisateur par son ID."""
        return self.utilisateurs.get(user_id)

    def supprimer(self, user_id):
        """Supprime un utilisateur."""
        if user_id in self.utilisateurs:
            del self.utilisateurs[user_id]
            return True
        return False

    def lister_actifs(self):
        """Liste tous les utilisateurs actifs."""
        return [u for u in self.utilisateurs.values() if u.actif]

    def lister_admins(self):
        """Liste tous les administrateurs."""
        return [u for u in self.utilisateurs.values() if u.est_admin()]

    def compter(self):
        """Compte le nombre d'utilisateurs."""
        return len(self.utilisateurs)
