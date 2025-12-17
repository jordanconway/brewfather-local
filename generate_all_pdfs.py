from download_recipes import get_all_recipes
from get_recipe_details import get_recipe_details
from generate_pdf import generate_pdf
import time

def generate_all_pdfs():
    """
    Downloads all recipes and generates a PDF for each one.
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
            generate_pdf(detailed_recipe)
        else:
            print(f"Could not get details for recipe {recipe_id}. Skipping PDF generation.")
        
        # To avoid hitting API rate limits
        time.sleep(1) 

if __name__ == "__main__":
    generate_all_pdfs()
