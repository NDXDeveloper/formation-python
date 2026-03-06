# ============================================================================
#   Section 7.6 : Le module typing - Annotations avancées
#   Description : Callable (types de fonctions), TypeVar (variables de
#                 type génériques), contraintes et bornes
#   Fichier source : 06-typing-annotations-avancees.md
# ============================================================================

from typing import Callable, TypeVar

# ==========================================
# 1. Callable - Types de fonctions
# ==========================================
print("=== Callable ===")

# Fonction qui prend deux int et retourne un int
Operation = Callable[[int, int], int]

def additionner(a: int, b: int) -> int:
    return a + b

def multiplier(a: int, b: int) -> int:
    return a * b

def appliquer_operation(a: int, b: int, operation: Operation) -> int:
    """Applique une opération sur deux nombres"""
    return operation(a, b)

resultat = appliquer_operation(5, 3, additionner)
print(f"additionner(5, 3) = {resultat}")

resultat = appliquer_operation(5, 3, multiplier)
print(f"multiplier(5, 3) = {resultat}")

# Fonction sans paramètres qui retourne str
GenerateurMessage = Callable[[], str]

def dire_bonjour() -> str:
    return "Bonjour!"

def executer_generateur(gen: GenerateurMessage) -> None:
    print(f"  {gen()}")

executer_generateur(dire_bonjour)

# Fonction de transformation
Transformateur = Callable[[str], str]

def mettre_en_majuscules(texte: str) -> str:
    return texte.upper()

def appliquer_transformation(textes: list[str],
                            transform: Transformateur) -> list[str]:
    """Applique une transformation à une liste de textes"""
    return [transform(texte) for texte in textes]

mots = ["bonjour", "monde"]
resultat_list = appliquer_transformation(mots, mettre_en_majuscules)
print(f"Transformation: {mots} -> {resultat_list}")

# ==========================================
# 2. TypeVar - Variables de type génériques
# ==========================================
print("\n=== TypeVar ===")

T = TypeVar('T')

def premier_element(liste: list[T]) -> T:
    """Retourne le premier élément d'une liste (de n'importe quel type)"""
    return liste[0]

nombres: list[int] = [1, 2, 3]
premier: int = premier_element(nombres)
print(f"Premier de {nombres}: {premier}")

mots_list: list[str] = ["a", "b", "c"]
premier_mot: str = premier_element(mots_list)
print(f"Premier de {mots_list}: {premier_mot}")

# ==========================================
# 3. TypeVar avec contraintes
# ==========================================
print("\n=== TypeVar avec contraintes ===")

Numerique = TypeVar('Numerique', int, float)

def doubler(valeur: Numerique) -> Numerique:
    """Double un nombre (int ou float)"""
    return valeur * 2

print(f"doubler(5) = {doubler(5)}")
print(f"doubler(3.14) = {doubler(3.14)}")

# ==========================================
# 4. TypeVar avec borne supérieure
# ==========================================
print("\n=== TypeVar avec bound ===")

T_str = TypeVar('T_str', bound=str)

def concatener(items: list[T_str]) -> T_str:
    """Concatène des éléments (doivent être des strings ou sous-classes)"""
    return items[0].__class__(''.join(items))

result = concatener(["Hello", " ", "World"])
print(f"concatener(['Hello', ' ', 'World']) = {result}")
