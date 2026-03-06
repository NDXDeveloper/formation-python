# ============================================================================
#   Section 3.3 : __len__, __getitem__, __setitem__, __delitem__
#   Description : Classe Playlist avec indexation, slicing, suppression
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self.chansons = []

    def ajouter(self, chanson):
        self.chansons.append(chanson)

    def __getitem__(self, index):
        return self.chansons[index]

    def __setitem__(self, index, valeur):
        self.chansons[index] = valeur

    def __delitem__(self, index):
        del self.chansons[index]

    def __len__(self):
        return len(self.chansons)

    def __str__(self):
        return f"Playlist '{self.nom}' avec {len(self)} chansons"

# --- __len__ et __getitem__ ---
ma_playlist = Playlist("Mes favoris")
ma_playlist.ajouter("Bohemian Rhapsody")
ma_playlist.ajouter("Imagine")
ma_playlist.ajouter("Hotel California")

print(len(ma_playlist))  # 3
print(ma_playlist)        # Playlist 'Mes favoris' avec 3 chansons

print(ma_playlist[0])    # Bohemian Rhapsody
print(ma_playlist[1])    # Imagine
print(ma_playlist[-1])   # Hotel California (dernier)

# Slicing
print(ma_playlist[0:2])  # ['Bohemian Rhapsody', 'Imagine']

# --- __setitem__ ---
print()
ma_playlist[0] = "Stairway to Heaven"
print(ma_playlist[0])    # Stairway to Heaven

# --- __delitem__ ---
print(f"Avant suppression : {len(ma_playlist)} chansons")
del ma_playlist[1]       # Supprime "Imagine"
print(f"Après suppression : {len(ma_playlist)} chansons")
