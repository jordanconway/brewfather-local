import json
import sys
from fpdf import XPos, YPos
from pdf_utils import PDF, COLOR_DEEP_CHARCOAL

def generate_pdf(recipe_id):
    """
    Generates a PDF for a given recipe ID from the detailed_recipe.json file.
    """
    try:
        with open("detailed_recipe.json", "r") as f:
            recipe_data = json.load(f)
    except FileNotFoundError:
        print("Error: detailed_recipe.json not found.")
        print("Please run 'docker-compose run --rm brewfather-local python get_recipe_details.py > detailed_recipe.json' first.")
        return

    if recipe_data["_id"] != recipe_id:
        print(f"Error: Recipe with ID '{recipe_id}' not found in detailed_recipe.json.")
        return

    pdf = PDF()
    pdf.set_title(f"Recipe: {recipe_data['name']}")
    pdf.add_page()

    # Ingredients
    pdf.chapter_title("Ingredients")
    
    # Fermentables
    if recipe_data.get("fermentables"):
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal
        pdf.cell(0, 10, "Fermentables", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(0, 0, 0) # Reset text color
        
        header = ["Name", "Amount", "Type"]
        data = [[item.get('name', 'N/A'), f"{item.get('amount', 'N/A')} kg", item.get('type', 'N/A')] for item in recipe_data["fermentables"]]
        pdf.ingredient_table(header, data, [90, 40, 40])

    # Hops
    if recipe_data.get("hops"):
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal
        pdf.cell(0, 10, "Hops", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(0, 0, 0) # Reset text color
        
        header = ["Name", "Amount", "Use"]
        data = [[item.get('name', 'N/A'), f"{item.get('amount', 'N/A')} g", f"{item.get('time', 'N/A')} min ({item.get('use', 'N/A')})"] for item in recipe_data["hops"]]
        pdf.ingredient_table(header, data, [90, 40, 40])

    # Yeasts
    if recipe_data.get("yeasts"):
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal
        pdf.cell(0, 10, "Yeast", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(0, 0, 0) # Reset text color
        for item in recipe_data["yeasts"]:
            pdf.cell(0, 5, f"- {item.get('name', 'N/A')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

    # Miscs
    if recipe_data.get("miscs"):
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal
        pdf.cell(0, 10, "Miscs", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(0, 0, 0) # Reset text color
        for item in recipe_data["miscs"]:
            pdf.cell(0, 5, f"- {item.get('name', 'N/A')}: {item.get('amount', 'N/A')} g", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

    # Instructions
    pdf.chapter_title("Instructions")

    # Mash Steps
    if recipe_data.get("mash") and recipe_data["mash"].get("steps"):
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal
        pdf.cell(0, 10, "Mash Steps", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(0, 0, 0) # Reset text color
        for i, step in enumerate(recipe_data["mash"]["steps"]):
            pdf.cell(0, 5, f"{i+1}. {step.get('name', 'Mash Step')} at {step.get('stepTemp', 'N/A'):.1f} C for {step.get('stepTime', 'N/A')} min", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

    # Fermentation Steps
    if recipe_data.get("fermentation") and recipe_data["fermentation"].get("steps"):
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*COLOR_DEEP_CHARCOAL) # Deep Charcoal
        pdf.cell(0, 10, "Fermentation Steps", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(0, 0, 0) # Reset text color
        for i, step in enumerate(recipe_data["fermentation"]["steps"]):
            pdf.cell(0, 5, f"{i+1}. {step.get('type', 'Fermentation')} at {step.get('stepTemp', 'N/A'):.1f} C for {step.get('stepTime', 'N/A')} days", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)
        
    # Notes
    if recipe_data.get("notes"):
        pdf.chapter_title("Notes")
        pdf.chapter_body(recipe_data["notes"])

    pdf_file_name = f"{recipe_data['name'].replace(' ', '_')}_final.pdf"
    pdf.output(pdf_file_name)
    print(f"Successfully generated {pdf_file_name}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        recipe_id = sys.argv[1]
    else:
        # Use the first recipe ID from the existing recipes.json as a default
        recipe_id = "514t8SJ4n2lLmqT7CRMjMLCD6uiO2N"
        
    generate_pdf(recipe_id)
