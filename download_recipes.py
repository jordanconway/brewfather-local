
import os
import requests
import json
import time
from datetime import datetime

def download_and_save_recipes(filename="recipes.json"):
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
        with open(filename, "w") as f:
            json.dump(recipes, f, indent=4)
        print(f"Successfully downloaded {len(recipes)} recipes to {filename}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    run_as_service = os.environ.get("RUN_AS_SERVICE", "false").lower() == "true"
    
    if run_as_service:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"recipes_{timestamp}.json"
            download_and_save_recipes(filename)
            print("Waiting 10 minutes before next download...")
            time.sleep(600)
    else:
        download_and_save_recipes()
