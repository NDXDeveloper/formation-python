# ============================================================================
#   Section 3.1 : Gestionnaire de tâches
#   Description : Exemple pratique combinant deux classes (Tache et
#                 GestionnaireTaches), composition d'objets
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

class Tache:
    """Représente une tâche à accomplir."""

    def __init__(self, titre, description=""):
        self.titre = titre
        self.description = description
        self.terminee = False

    def marquer_terminee(self):
        self.terminee = True
        print(f"Tâche '{self.titre}' marquée comme terminée.")

    def marquer_non_terminee(self):
        self.terminee = False
        print(f"Tâche '{self.titre}' marquée comme non terminée.")

    def afficher(self):
        statut = "[x]" if self.terminee else "[ ]"
        print(f"{statut} {self.titre}")
        if self.description:
            print(f"  Description : {self.description}")


class GestionnaireTaches:
    """Gère une liste de tâches."""

    def __init__(self):
        self.taches = []

    def ajouter_tache(self, titre, description=""):
        nouvelle_tache = Tache(titre, description)
        self.taches.append(nouvelle_tache)
        print(f"Tâche '{titre}' ajoutée.")

    def afficher_toutes(self):
        if not self.taches:
            print("Aucune tâche.")
            return

        print("\n=== Liste des tâches ===")
        for i, tache in enumerate(self.taches, 1):
            print(f"{i}. ", end="")
            tache.afficher()

    def afficher_non_terminees(self):
        taches_non_terminees = [t for t in self.taches if not t.terminee]
        if not taches_non_terminees:
            print("Toutes les tâches sont terminées !")
            return

        print("\n=== Tâches à faire ===")
        for tache in taches_non_terminees:
            tache.afficher()

    def nombre_taches_terminees(self):
        return sum(1 for t in self.taches if t.terminee)

    def nombre_taches_total(self):
        return len(self.taches)

# Utilisation
gestionnaire = GestionnaireTaches()

gestionnaire.ajouter_tache("Faire les courses", "Acheter du pain et du lait")
gestionnaire.ajouter_tache("Répondre aux emails")
gestionnaire.ajouter_tache("Réviser Python", "Chapitre sur les classes")

gestionnaire.afficher_toutes()

# Marquer une tâche comme terminée
gestionnaire.taches[0].marquer_terminee()

gestionnaire.afficher_non_terminees()

print(f"\nProgression : {gestionnaire.nombre_taches_terminees()}/{gestionnaire.nombre_taches_total()} tâches terminées")
