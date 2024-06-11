import requests
from bs4 import BeautifulSoup
import csv
import os
import datetime

# Helper function to convert numbers to words
def number_to_words(n):
    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty"]

    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n < 60:
        return tens[n // 10] + (" " + ones[n % 10] if (n % 10 != 0) else "")
    else:
        return "out of range"

def time_to_words(hour, minute, second):
    return f"{number_to_words(hour)}_{number_to_words(minute)}_{number_to_words(second)}"

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
try:
    # Send a GET request to the page
    response = requests.get(url)
    response.raise_for_status()  # Check that the request was successful

    # Get the current date and time
    now = datetime.datetime.now()
    hour = now.strftime("%I")  # 12-hour format
    minute = now.strftime("%M")
    second = now.strftime("%S")
    am_pm = now.strftime("%p").lower()

    # Convert time to words
    time_words = time_to_words(int(hour), int(minute), int(second)) + "_" + am_pm

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the data
    table = soup.find('table', {'class': 'wikitable'})

    if table is None:
        raise ValueError("Table not found on the page")

    # Extract the headers
    headers = [header.text.strip() for header in table.find_all('th')]
    headers = headers[0:11]

    if not headers:
        raise ValueError("No headers found in the table")

    # Extract the rows
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all(['td', 'th'])
        cells = [cell.text.strip() for cell in cells]
        if cells:  # Ensure the row is not empty
            rows.append(cells)

    if not rows:
        raise ValueError("No rows found in the table")

    # Save to CSV file
    filename = f'largest_companies_by_revenue_{time_words}.csv'
    if os.path.exists(filename):
        os.remove(filename)  # Remove the file if it already exists

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)  # Write headers
        csvwriter.writerows(rows)  # Write data rows

    print(f"Data has been saved to {filename}")

except requests.RequestException as e:
    print(f"Network error: {e}")
except ValueError as e:
    print(f"Parsing error: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
