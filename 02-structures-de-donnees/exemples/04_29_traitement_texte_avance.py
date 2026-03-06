# ============================================================================
#   Section 2.4 : Regex - Traitement de texte avancé
#   Description : Extraction de hashtags et mentions, conversion camelCase
#                 vers snake_case et inversement
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# Extraire les hashtags d'un tweet
tweet = "J'adore #Python et #Programming ! #Dev #Code"
hashtags = re.findall(r'#(\w+)', tweet)
print("Hashtags :", hashtags)  # ['Python', 'Programming', 'Dev', 'Code']

# Extraire les mentions
texte = "Merci @Alice et @Bob pour votre aide !"
mentions = re.findall(r'@(\w+)', texte)
print("Mentions :", mentions)  # ['Alice', 'Bob']

# Camel case vers snake case
def camel_to_snake(nom):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', nom).lower()

print(camel_to_snake("MonNomDeVariable"))  # mon_nom_de_variable
print(camel_to_snake("HTTPServer"))        # h_t_t_p_server (limité pour les acronymes)

# Snake case vers camel case
def snake_to_camel(nom):
    components = nom.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

print(snake_to_camel("mon_nom_de_variable"))  # monNomDeVariable
