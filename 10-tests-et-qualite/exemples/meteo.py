# ============================================================================
#   Section 10.2 : Mocking et fixtures
#   Description : Module meteo - obtenir temperature et recommander vetements
#                 (utilise par les tests de mocking API)
#   Fichier source : 02-mocking-et-fixtures.md
# ============================================================================

import requests


def obtenir_temperature(ville):
    """Obtient la temperature d'une ville via une API."""
    url = f"https://api.meteo.com/ville/{ville}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Erreur API")

    data = response.json()
    return data["temperature"]


def recommander_vetements(ville):
    """Recommande des vetements selon la temperature."""
    temp = obtenir_temperature(ville)

    if temp < 10:
        return "Manteau et écharpe"
    elif temp < 20:
        return "Pull léger"
    else:
        return "T-shirt"
