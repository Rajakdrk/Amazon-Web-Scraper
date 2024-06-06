import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first table on the page
table = soup.find('table', {'class': 'wikitable'})

# Extract the table rows
rows = table.find_all('tr')

# Prepare lists to hold the data
data = []

# Loop through the table rows and extract the relevant data
for row in rows[1:]:  # Skip the header row
    cells = row.find_all('td')
    if len(cells) >= 5:  # Ensure there are enough columns in the row
        location = cells[1].get_text(strip=True)
        population = cells[2].get_text(strip=True).replace(',', '')
        percentage = cells[4].get_text(strip=True).replace('%', '')
        date = cells[3].get_text(strip=True)

        data.append([location, population, percentage, date])

# Write the data to a CSV file
with open('countries_population.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Location', 'Population', '% of World', 'Date'])
    writer.writerows(data)
