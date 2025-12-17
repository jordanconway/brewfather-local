import sys
from beerxml.recipe import Recipe
from beerxml.hop import Hop
from beerxml.fermentable import Fermentable
from beerxml.yeast import Yeast
from beerxml.style import Style
from beerxml.mash import Mash
from beerxml.mash_step import MashStep

from get_recipe_details import get_recipe_details

def export_to_beerxml(recipe_data):
    """
    Exports a recipe to BeerXML format.
    """
    if not recipe_data:
        print("Error: No recipe data provided.")
        return

    recipe = Recipe()
    recipe.name = recipe_data.get("name")
    recipe.brewer = recipe_data.get("author")
    recipe.batch_size = recipe_data.get("batchSize")
    recipe.boil_size = recipe_data.get("boilSize")
    recipe.boil_time = recipe_data.get("boilTime")
    recipe.efficiency = recipe_data.get("efficiency")
    recipe.notes = recipe_data.get("notes")

    # Style
    if recipe_data.get("style"):
        style_data = recipe_data["style"]
        style = Style()
        style.name = style_data.get("name")
        style.category = style_data.get("category")
        style.style_guide = style_data.get("styleGuide")
        style.type = style_data.get("type")
        recipe.style = style

    # Hops
    if recipe_data.get("hops"):
        for hop_data in recipe_data["hops"]:
            hop = Hop()
            hop.name = hop_data.get("name")
            hop.alpha = hop_data.get("alpha")
            hop.amount = hop_data.get("amount") / 1000 # convert g to kg
            hop.use = hop_data.get("use")
            hop.time = hop_data.get("time")
            recipe.hops.append(hop)
            
    # Fermentables
    if recipe_data.get("fermentables"):
        for fermentable_data in recipe_data["fermentables"]:
            fermentable = Fermentable()
            fermentable.name = fermentable_data.get("name")
            fermentable.amount = fermentable_data.get("amount")
            fermentable.type = fermentable_data.get("type")
            fermentable.color = fermentable_data.get("color")
            recipe.fermentables.append(fermentable)
            
    # Yeasts
    if recipe_data.get("yeasts"):
        for yeast_data in recipe_data["yeasts"]:
            yeast = Yeast()
            yeast.name = yeast_data.get("name")
            yeast.amount = yeast_data.get("amount")
            yeast.type = yeast_data.get("type")
            yeast.form = yeast_data.get("form")
            yeast.attenuation = yeast_data.get("attenuation")
            recipe.yeasts.append(yeast)

    # Mash
    if recipe_data.get("mash") and recipe_data["mash"].get("steps"):
        mash = Mash()
        for step_data in recipe_data["mash"]["steps"]:
            mash_step = MashStep()
            mash_step.name = step_data.get("name")
            mash_step.step_time = step_data.get("stepTime")
            mash_step.step_temp = step_data.get("stepTemp")
            mash_step.type = step_data.get("type")
            mash.mash_steps.append(mash_step)
        recipe.mash = mash

    # Generate XML
    xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_string += "".join(recipe.to_xml())

    # Save to file
    filename = f"{recipe.name.replace(' ', '_')}.xml"
    with open(filename, "w") as f:
        f.write(xml_string)

    print(f"Successfully exported {recipe.name} to {filename}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        recipe_id = sys.argv[1]
    else:
        # Use the first recipe ID from the existing recipes.json as a default
        recipe_id = "514t8SJ4n2lLmqT7CRMjMLCD6uiO2N"

    recipe_data = get_recipe_details(recipe_id)
    if recipe_data:
        export_to_beerxml(recipe_data)
