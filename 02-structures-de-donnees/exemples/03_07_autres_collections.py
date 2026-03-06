# ============================================================================
#   Section 2.3 : Autres collections - deque, OrderedDict, ChainMap
#   Description : File double deque, dictionnaire ordonné, chaîner dicts
#   Fichier source : 03-collections-specialisees.md
# ============================================================================

from collections import deque, OrderedDict, ChainMap

# --- deque - File double ---
d = deque([1, 2, 3])

# Ajouter à droite et à gauche
d.append(4)      # [1, 2, 3, 4]
d.appendleft(0)  # [0, 1, 2, 3, 4]

# Retirer à droite et à gauche
d.pop()          # Retire 4
d.popleft()      # Retire 0

print(f"deque : {d}")  # deque([1, 2, 3])

# Rotation
d.rotate(1)   # Rotation à droite
print(f"rotate(1) : {d}")   # deque([3, 1, 2])
d.rotate(-1)  # Rotation à gauche
print(f"rotate(-1) : {d}")  # deque([1, 2, 3])

# --- OrderedDict ---
print()
od = OrderedDict()
od['b'] = 2
od['a'] = 1
od['c'] = 3
print(f"OrderedDict : {od}")

# move_to_end
od.move_to_end('a')
print(f"move_to_end('a') : {od}")

# --- ChainMap ---
print()
config_defaut = {'couleur': 'bleu', 'taille': 'M'}
config_utilisateur = {'couleur': 'rouge'}

config = ChainMap(config_utilisateur, config_defaut)
print(f"couleur : {config['couleur']}")  # 'rouge' (priorité)
print(f"taille : {config['taille']}")    # 'M' (défaut)
print(f"config : {dict(config)}")
