# ============================================================================
#   Section 2.4 : Regex - Groupes de capture
#   Description : Groupes (), groupes nommés (?P<nom>), groups(), groupdict()
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

import re

# Extraire le nom et le domaine d'un email
email = "utilisateur@example.com"
match = re.search(r'(\w+)@(\w+\.\w+)', email)

if match:
    print("Email complet :", match.group(0))  # utilisateur@example.com
    print("Nom :", match.group(1))            # utilisateur
    print("Domaine :", match.group(2))        # example.com
    print("Tous les groupes :", match.groups())  # ('utilisateur', 'example.com')

# Groupes nommés
print()
match = re.search(r'(?P<nom>\w+)@(?P<domaine>\w+\.\w+)', email)
if match:
    print("Nom :", match.group('nom'))        # utilisateur
    print("Domaine :", match.group('domaine'))  # example.com
    print("Dict :", match.groupdict())  # {'nom': 'utilisateur', 'domaine': 'example.com'}
