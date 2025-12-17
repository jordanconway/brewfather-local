
import os
import requests
import json

def download_recipes():
    """
    Downloads all recipes from the Brewfather API and saves them to a local file.
    """
    api_key = os.environ.get("BREWFATHER_API_KEY")
    user_id = os.environ.get("BREWFATHER_USER_ID")

    if not api_key or not user_id:
        print("Error: Please set the BREWFATHER_API_KEY and BREWFATHER_USER_ID environment variables.")
        return

    url = f"https://api.brewfather.app/v2/recipes"
    headers = {
        "Accept": "application/json",
    }
    auth = (user_id, api_key)

    print("Downloading recipes...")
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        recipes = response.json()
        with open("recipes.json", "w") as f:
            json.dump(recipes, f, indent=4)
        print(f"Successfully downloaded {len(recipes)} recipes to recipes.json")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    download_recipes()
