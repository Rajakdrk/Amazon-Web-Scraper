import requests
from bs4 import BeautifulSoup
import csv

# URL of the Amazon page
url = "https://www.amazon.in/s?k=mobile+under+20000&crid=3G0XLJP7YDE2U&sprefix=mobile%2Caps%2C357&ref=nb_sb_ss_ts-doa-p_7_6"

# Headers to simulate a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to fetch and parse the webpage
def fetch_webpage(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

# Function to parse the HTML and extract product names and prices
def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    # Find all product elements
    product_elements = soup.find_all("div", {"data-component-type": "s-search-result"})

    for element in product_elements:
        try:
            # Extract product name
            name = element.h2.text.strip()

            # Extract product price
            price_whole = element.find("span", "a-price-whole")
            price_fraction = element.find("span", "a-price-fraction")
            if price_whole and price_fraction:
                price = price_whole.text + price_fraction.text
            else:
                price = "N/A"

            products.append((name, price))
        except AttributeError as e:
            # Handle any parsing errors gracefully
            print(f"Error parsing product information: {e}")
            continue

    return products

# Function to save the extracted data to a CSV file
def save_to_csv(products, filename="products.csv"):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price"])
            writer.writerows(products)
    except IOError as e:
        print(f"Error saving data to CSV: {e}")

# Main function to orchestrate the web scraping
def main():
    html = fetch_webpage(url)
    if html:
        products = parse_html(html)
        if products:
            save_to_csv(products)
            print(f"Successfully saved {len(products)} products to CSV.")
        else:
            print("No products found.")
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    main()
