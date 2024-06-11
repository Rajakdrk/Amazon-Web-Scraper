# Largest Companies by Revenue Scraper

This repository contains a Python script to scrape the list of the largest companies by revenue from Wikipedia and save the data to a CSV file. The filename of the CSV file includes the current time in words.

## Features

- Scrapes the table of largest companies by revenue from the Wikipedia page.
- Extracts the table headers and rows.
- Saves the extracted data to a CSV file with a timestamp in words in the filename.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup4 library

## Installation

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/Rajakdrk/largest-companies-revenue-scraper.git
    ```
2. Navigate to the project directory.
    ```bash
    cd Web_Scraper_largest_companies_by_revene
    ```
3. Install the required Python libraries.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script to scrape data and save it to a CSV file.
    ```bash
    python main.py
    ```
2. The script will create a CSV file with a name in the format `largest_companies_by_revenue_<time_in_words>.csv` in the current directory.

## File Structure

- `main.py`: The main Python script for scraping the data and saving it to a CSV file.
- `requirements.txt`: A file listing the required Python libraries.
- `README.md`: This readme file.


## Error Handling

The script includes error handling for the following scenarios:

- Network errors during the GET request.
- Parsing errors if the table or headers are not found.
- Permission errors when trying to write the CSV file.
- Any unexpected errors.


## Acknowledgments

- Wikipedia for providing the data.
- BeautifulSoup and Requests libraries for making web scraping easier.

Feel free to contribute to this project by opening issues or submitting pull requests.
