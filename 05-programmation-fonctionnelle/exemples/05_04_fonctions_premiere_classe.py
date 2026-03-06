# ============================================================================
#   Section 5.5 : Fonctions comme citoyens de première classe
#   Description : Assignées à des variables, passées comme arguments,
#                 retournées, stockées dans des structures
#   Fichier source : 05-closures-et-prog-fonctionnelle.md
# ============================================================================

# --- Assignées à des variables ---
print("=== Assignation ===")

def saluer(nom):
    return f"Bonjour {nom} !"

ma_fonction = saluer
print(ma_fonction("Alice"))  # Bonjour Alice !

# --- Passées comme arguments ---
print("\n=== Arguments ===")

def executer_operation(operation, a, b):
    """Exécute une opération sur deux nombres."""
    return operation(a, b)

def additionner(x, y):
    return x + y

def multiplier(x, y):
    return x * y

print(executer_operation(additionner, 5, 3))  # 8
print(executer_operation(multiplier, 5, 3))   # 15

# --- Retournées par d'autres fonctions ---
print("\n=== Retour de fonctions ===")

def choisir_operation(type_operation):
    """Retourne une fonction selon le type d'opération."""

    def additionner(x, y):
        return x + y

    def soustraire(x, y):
        return x - y

    if type_operation == "addition":
        return additionner
    elif type_operation == "soustraction":
        return soustraire
    else:
        return lambda x, y: 0

operation = choisir_operation("addition")
print(operation(10, 5))  # 15

# --- Stockées dans des structures de données ---
print("\n=== Structures de données ===")

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else None
}

print(operations['+'](10, 5))  # 15
print(operations['*'](10, 5))  # 50
