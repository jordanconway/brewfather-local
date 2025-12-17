
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY download_recipes.py .
COPY get_recipe_details.py .
COPY generate_pdf.py .
COPY generate_all_pdfs.py .
COPY export_to_beerxml.py .
COPY export_all_to_beerxml.py .
COPY pdf_utils.py .
COPY brewstepdaddy.png .

# Command to run the script
CMD ["python", "download_recipes.py"]
