import sys
from get_recipe_details import get_recipe_details

def export_to_beerxml(recipe_data):
    """
    Exports a recipe to BeerXML format.
    """
    if not recipe_data:
        print("Error: No recipe data provided.")
        return

    recipe_name = recipe_data.get("name", "Unknown Recipe")
    if not recipe_name or recipe_name.isspace():
        recipe_name = f"recipe_{recipe_data.get('_id', 'unknown_id')}"
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<RECIPES>\n'
    xml += '  <RECIPE>\n'
    xml += f'    <NAME>{recipe_name}</NAME>\n'
    xml += f'    <VERSION>1</VERSION>\n'
    xml += f'    <TYPE>{recipe_data.get("type", "All Grain")}</TYPE>\n'
    xml += f'    <BREWER>{recipe_data.get("author", "")}</BREWER>\n'
    xml += f'    <BATCH_SIZE>{recipe_data.get("batchSize", 0)}</BATCH_SIZE>\n'
    xml += f'    <BOIL_SIZE>{recipe_data.get("boilSize", 0)}</BOIL_SIZE>\n'
    xml += f'    <BOIL_TIME>{recipe_data.get("boilTime", 0)}</BOIL_TIME>\n'
    xml += f'    <EFFICIENCY>{recipe_data.get("efficiency", 0)}</EFFICIENCY>\n'
    
    if recipe_data.get("hops"):
        xml += '    <HOPS>\n'
        for hop in recipe_data["hops"]:
            xml += '      <HOP>\n'
            xml += f'        <NAME>{hop.get("name")}</NAME>\n'
            xml += f'        <VERSION>1</VERSION>\n'
            xml += f'        <ALPHA>{hop.get("alpha")}</ALPHA>\n'
            xml += f'        <AMOUNT>{hop.get("amount") / 1000}</AMOUNT>\n'
            xml += f'        <USE>{hop.get("use")}</USE>\n'
            xml += f'        <TIME>{hop.get("time")}</TIME>\n'
            xml += f'        <FORM>{hop.get("type")}</FORM>\n'
            xml += '      </HOP>\n'
        xml += '    </HOPS>\n'

    if recipe_data.get("fermentables"):
        xml += '    <FERMENTABLES>\n'
        for fermentable in recipe_data["fermentables"]:
            xml += '      <FERMENTABLE>\n'
            xml += f'        <NAME>{fermentable.get("name")}</NAME>\n'
            xml += f'        <VERSION>1</VERSION>\n'
            xml += f'        <TYPE>{fermentable.get("type")}</TYPE>\n'
            xml += f'        <AMOUNT>{fermentable.get("amount")}</AMOUNT>\n'
            xml += f'        <YIELD>{fermentable.get("potentialPercentage", 0)}</YIELD>\n'
            xml += f'        <COLOR>{fermentable.get("color", 0)}</COLOR>\n'
            xml += '      </FERMENTABLE>\n'
        xml += '    </FERMENTABLES>\n'
        
    if recipe_data.get("yeasts"):
        xml += '    <YEASTS>\n'
        for yeast in recipe_data["yeasts"]:
            xml += '      <YEAST>\n'
            xml += f'        <NAME>{yeast.get("name")}</NAME>\n'
            xml += f'        <VERSION>1</VERSION>\n'
            xml += f'        <TYPE>{yeast.get("type")}</TYPE>\n'
            xml += f'        <FORM>{yeast.get("form")}</FORM>\n'
            xml += f'        <AMOUNT>{yeast.get("amount") / 1000}</AMOUNT>\n'
            xml += f'        <ATTENUATION>{yeast.get("attenuation")}</ATTENUATION>\n'
            xml += '      </YEAST>\n'
        xml += '    </YEASTS>\n'

    if recipe_data.get("mash") and recipe_data["mash"].get("steps"):
        xml += '    <MASH>\n'
        xml += f'      <NAME>Mash</NAME>\n'
        xml += f'      <VERSION>1</VERSION>\n'
        xml += f'      <GRAIN_TEMP>20.0</GRAIN_TEMP>\n'
        xml += '      <MASH_STEPS>\n'
        for step in recipe_data["mash"]["steps"]:
            xml += '        <MASH_STEP>\n'
            xml += f'          <NAME>{step.get("name")}</NAME>\n'
            xml += f'          <VERSION>1</VERSION>\n'
            xml += f'          <TYPE>{step.get("type")}</TYPE>\n'
            xml += f'          <STEP_TEMP>{step.get("stepTemp")}</STEP_TEMP>\n'
            xml += f'          <STEP_TIME>{step.get("stepTime")}</STEP_TIME>\n'
            xml += '        </MASH_STEP>\n'
        xml += '      </MASH_STEPS>\n'
        xml += '    </MASH>\n'

    xml += '  </RECIPE>\n'
    xml += '</RECIPES>\n'

    filename = f"{recipe_name.replace(' ', '_')}.xml"
    with open(filename, "w") as f:
        f.write(xml)

    print(f"Successfully exported {recipe_name} to {filename}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        recipe_id = sys.argv[1]
    else:
        recipe_id = "514t8SJ4n2lLmqT7CRMjMLCD6uiO2N"

    recipe_data = get_recipe_details(recipe_id)
    if recipe_data:
        export_to_beerxml(recipe_data)
