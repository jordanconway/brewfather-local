import os
import requests
import json

def get_recipe_details(recipe_id):
    """
    Downloads a single recipe from the Brewfather API and returns it as a dictionary.
    """
    api_key = os.environ.get("BREWFATHER_API_KEY")
    user_id = os.environ.get("BREWFATHER_USER_ID")

    if not api_key or not user_id:
        print("Error: Please set the BREWFATHER_API_KEY and BREWFATHER_USER_ID environment variables.")
        return None

    url = f"https://api.brewfather.app/v2/recipes/{recipe_id}"
    headers = {
        "Accept": "application/json",
    }
    auth = (user_id, api_key)

    print(f"Downloading recipe {recipe_id}...")
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        recipe = response.json()
        print(f"Successfully downloaded recipe {recipe_id}.")
        return recipe
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    # Use the first recipe ID from the existing recipes.json
    # In a real application, this would be passed as an argument
    recipe_id = "514t8SJ4n2lLmqT7CRMjMLCD6uiO2N"
    recipe_data = get_recipe_details(recipe_id)
    if recipe_data:
        print(json.dumps(recipe_data, indent=4))
