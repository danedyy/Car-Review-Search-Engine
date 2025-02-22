import csv
import re


car_brands = [
# American Brands
"Chevrolet", "Ford", "Tesla", "Dodge", "Cadillac", "Jeep", "GMC", 
"Lincoln", "Chrysler", "Buick", "Ram", "Hennessey", "Saleen", 
"Rivian", "Lucid Motors",

# European Brands
# German
"BMW", "Mercedes-Benz", "Audi", "Porsche", "Volkswagen", "Opel", 
"Smart", "MAN",

# British
"Aston Martin", "Rolls-Royce", "Bentley", "Jaguar", "Land Rover", 
"Mini", "Morgan", "Lotus", "TVR", "Caterham","McLaren",

# Italian
"Ferrari", "Lamborghini", "Maserati", "Fiat", "Alfa Romeo", 
"Lancia", "Pagani", "Dallara",

# French
"Peugeot", "Renault", "Citroen", "Bugatti", "DS Automobiles", 
"Venturi Automobiles", "Ligier",

# Swedish
"Volvo", "Koenigsegg", "Polestar", "Scania",

# Czech
"Skoda",

# Spanish
"SEAT", "Cupra",

# Romanian
"Dacia",

# African Brands
# Nigerian
"Innoson",

# Ugandan
"Kiira Motors",

# South African
"Birkin", "Paramount", "Perana Performance Group",

# Moroccan
"Laraki",

# Asian Brands
# Japanese
"Toyota", "Honda", "Nissan", "Mazda", "Subaru", "Mitsubishi", 
"Suzuki", "Lexus", "Infiniti", "Acura", "Daihatsu", "Isuzu",

# South Korean
"Hyundai", "Kia", "Genesis",

# Chinese
"Geely", "BYD", "Nio", "Chery", "Great Wall Motors", "Xpeng",
"Wuling", "Hongqi", "Roewe", "Lynk & Co", "Aiways", 
"Zotye", "Baojun", "JAC Motors",

# Indian Brands
"Tata Motors", "Mahindra", "Maruti Suzuki", "Ashok Leyland", "Force Motors",

# Russian Brands
"Lada", "GAZ", "UAZ", "Kamaz",

# Australian Brands
"Holden", "Elfin", "Bolwell",

# Other Niche/Small Brands
"Donkervoort", "Spyker", "Wiesmann", "Ginetta", "Noble", 
"Zenvo", "Sin Cars", "Arrinera", "Fornasari", "Faraday Future", 
"Ariel", "Radical", "BAC", "Rimac", "Gumpert", "Apollo Automobil", "Piëch"
]

# Path to the input CSV file
input_file = "carsguide_scrape.csv"
# Path to the output CSV file
output_file = "cleaned_car_data.csv"


TAGS_PATTERN = r'<\/?div.*?>|<\/?p.*?>|<\/?a.*?>|<\/?img.*?>'

# Pattern to match a year (e.g. 1999, 2024)
YEAR_PATTERN = r'\b(18|19|20)\d{2}\b'

def clean_html_tags(text):
 # Remove HTML tags
text = re.sub(TAGS_PATTERN, '', text)
# Remove newlines and leading/trailing whitespace
text = text.replace('\\n ', '').strip()
text = text.replace('\\n', '').strip()
text = text.replace("'',", '').strip()
text = text.replace("']", '').strip()
text = text.replace("['", '').strip()
text = text.replace('["', '').strip()
text = text.replace('"]', '').strip()
text = text.replace('[', '').strip()
text = text.replace(']', '').strip()
text = text.replace('\'', '').strip()
text = text.replace('/ 10', '').strip()
text = text.replace('"', '')

# Replace multiple spaces with a single space
text = re.sub(r'\s+', ' ', text)
return text

def clean_name_column(text):
# Remove the word 'review' from the Name column
return re.sub(r'\breview:?\s*', '', text, flags=re.IGNORECASE).strip()

def extract_year(text):
# Search for a year in the text
match = re.search(YEAR_PATTERN, text)
return match.group(0) if match else None


def find_car_brand(car_name):
# Convert the brand list to lowercase and split by space or hyphen for case-insensitive comparison
car_brands_lower = [[subword for subword in re.split(r'[ \-]', brand.lower())] for brand in car_brands]

# Split the car name by spaces, hyphens and convert each word to lowercase
words = re.split(r'[ \-]', car_name.lower())

# Check each brand's word(s) against the car name's words
for i, brand_words in enumerate(car_brands_lower):
# Check if any of the brand's subwords are in the car name words
if any(word in words for word in brand_words):
# Return the original brand name with correct casing
return car_brands[i]

return None


def clean_csv(input_file, output_file):
# Open the input CSV file
with open(input_file, 'r', newline='') as csvfile:
reader = csv.DictReader(csvfile)


# Get the field names from the input file and add new columns for "Year" and "Brand"
fieldnames = reader.fieldnames + ['Year', 'Brand']# Add both 'Year' and 'Brand' columns


# Open the output CSV file to save the cleaned content
with open(output_file, 'w', newline='') as cleaned_csv:
writer = csv.DictWriter(cleaned_csv, fieldnames=fieldnames)
writer.writeheader()

# Loop through each row of the CSV
for row in reader:
# Clean each cell in the row
for key, value in row.items():
cleaned_value = clean_html_tags(value)

# Apply additional cleaning if it's the "Name" column
if key.lower() == 'name':# Case insensitive check for "Name" column
cleaned_value = clean_name_column(cleaned_value)

row[key] = cleaned_value

# Try to extract year from the "Name" column first
year = extract_year(row.get('Name', ''))

# If no year found, check other columns
if year is None:
for key, value in row.items():
if key.lower() != 'name':# Avoid checking the "Name" column again
year = extract_year(value)
if year:# Stop checking if a year is found
break


brand = find_car_brand(row.get('Name', ''))

# Skip this row if either the brand or year is None or missing (i.e. "--")
if year == None or brand == None:
continue# Skip this iteration and move to the next row

# Add the extracted year to the row (default to "--" if no year is found)
row['Year'] = year
# Find the car brand from the "Name" column
row['Brand'] = brand

# Write the cleaned row to the output CSV file
writer.writerow(row)



clean_csv(input_file, output_file)

print("Cleaning completed and saved to:", output_file)