import requests

def get_team_information(team_name):
    base_url = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"
    params = {"t": team_name}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Vérifier s'il y a des erreurs HTTP

        # Analyser la réponse JSON
        data = response.json()

        # Vérifier si l'équipe a été trouvée
        if data["teams"]:
            team = data["teams"][0]
            print(f"Nom de l'équipe: {team['strTeam']}")
            print(f"Pays: {team['strCountry']}")
            print(f"Stade: {team['strStadium']}")

        else:
            print(f"Aucune information trouvée pour l'équipe {team_name}")

    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la requête : {e}")

# Exemple d'utilisation
get_team_information("Arsenal")
