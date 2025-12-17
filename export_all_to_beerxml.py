from download_recipes import get_all_recipes
from get_recipe_details import get_recipe_details
from export_to_beerxml import export_to_beerxml
import time

def export_all_to_beerxml():
    """
    Downloads all recipes and exports each one to BeerXML format.
    """
    recipes = get_all_recipes()
    if not recipes:
        print("Could not download recipes. Aborting.")
        return

    for recipe_summary in recipes:
        recipe_id = recipe_summary.get("_id")
        if not recipe_id:
            print(f"Skipping recipe without ID: {recipe_summary.get('name')}")
            continue

        print("-" * 20)
        detailed_recipe = get_recipe_details(recipe_id)
        if detailed_recipe:
            export_to_beerxml(detailed_recipe)
        else:
            print(f"Could not get details for recipe {recipe_id}. Skipping BeerXML export.")
        
        # To avoid hitting API rate limits
        time.sleep(1) 

if __name__ == "__main__":
    export_all_to_beerxml()
