# ============================================================================
#   Section 2.1 : Dépaqueter avec * et ** (passer et combiner des collections)
#   Description : * pour les séquences, ** pour les dicts ; dépaquetage dans un
#                 appel de fonction et fusion de collections ([*a,*b], {**a,**b})
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# --- Passer une collection à une fonction ---
nombres = [3, 1, 4, 1, 5]
print(max(nombres))      # 5 (la liste = un seul argument)
print(*nombres)          # 3 1 4 1 5 (chaque élément = un argument de print)


def afficher(a, b, c):
    print(f"{a}, {b}, {c}")


afficher(*[10, 20, 30])  # 10, 20, 30  (* dépaquète la liste)
afficher(**{"a": 1, "b": 2, "c": 3})  # 1, 2, 3  (** dépaquète le dict)

# --- Combiner des collections ---
tout = [*[1, 2], 3, *[4, 5]]
print(tout)              # [1, 2, 3, 4, 5]

fusion = {**{"couleur": "noir", "taille": "M"}, **{"taille": "L"}}
print(fusion)            # {'couleur': 'noir', 'taille': 'L'} (droite l'emporte)
