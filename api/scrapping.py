import requests
import json

def get_team_information(ingredient_name):
    base_url = "https://www.themealdb.com/api/json/v1/1/filter.php"
    params = {"i": ingredient_name}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Vérifier s'il y a des erreurs HTTP

        # Analyser la réponse JSON
        data = response.json()
        
        filename = "data.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la requête : {e}")

# Exemple d'utilisation
get_team_information("chicken_breast")
