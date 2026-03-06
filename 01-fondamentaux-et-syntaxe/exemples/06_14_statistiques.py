# ============================================================================
#   Section 6.20 : Exemple pratique - Calculateur de statistiques
#   Description : Type aliases Nombre et Statistiques, calcul de moyenne,
#                 médiane, écart-type, analyse de notes avec appréciations
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from statistics import mean, median, stdev

Nombre = int | float
Statistiques = dict[str, Nombre]

def calculer_statistiques(donnees: list[Nombre]) -> Statistiques:
    """
    Calcule diverses statistiques sur une liste de nombres.

    Args:
        donnees: Liste de nombres (int ou float)

    Returns:
        Dictionnaire contenant les statistiques calculées

    Raises:
        ValueError: Si la liste est vide
    """
    if not donnees:
        raise ValueError("La liste ne peut pas être vide")

    return {
        "moyenne": mean(donnees),
        "mediane": median(donnees),
        "minimum": min(donnees),
        "maximum": max(donnees),
        "ecart_type": stdev(donnees) if len(donnees) > 1 else 0.0
    }

def analyser_notes(notes: list[int]) -> tuple[float, list[str]]:
    """
    Analyse une liste de notes et retourne la moyenne et les appréciations.

    Args:
        notes: Liste de notes (0-20)

    Returns:
        Tuple contenant (moyenne, liste d'appréciations)
    """
    stats = calculer_statistiques(notes)
    moyenne = stats["moyenne"]

    appreciations: list[str] = []
    for note in notes:
        if note >= 16:
            appreciations.append("Très bien")
        elif note >= 14:
            appreciations.append("Bien")
        elif note >= 12:
            appreciations.append("Assez bien")
        elif note >= 10:
            appreciations.append("Passable")
        else:
            appreciations.append("Insuffisant")

    return moyenne, appreciations

# Utilisation
notes_classe = [12, 15, 8, 18, 14, 11, 16, 13]
moyenne, appreciations = analyser_notes(notes_classe)
print(f"Moyenne de la classe : {moyenne:.2f}")

print("\nDétail :")
for note, appreciation in zip(notes_classe, appreciations):
    print(f"  {note}/20 - {appreciation}")

print("\nStatistiques complètes :")
stats = calculer_statistiques(notes_classe)
for cle, valeur in stats.items():
    print(f"  {cle}: {valeur:.2f}")
