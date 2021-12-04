import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import json
import os

# Code is modified from:
# https://medium.com/analytics-vidhya/how-to-web-scrape-tables-online-using-python-and-beautifulsoup-36d5bafeb982
# How to Web Scrape Tables Online, Using Python and BeautifulSoup by Christopher Zita

def scraper(input_data):
    """Table scraper that scrapes planet visibility data from timeanddate.com
    and generates a .json file with data for planet rise, set, meridian, and additional info"""
    # If '-' in string, must be lat/long data
    if '-' in input_data:
        input = input_data
        input = input.replace(' ', '')
        url = 'https://www.timeanddate.com/astronomy/night/@' + input
    # Otherwise, must be a zip code
    else:
        input = input_data
        url = 'https://www.timeanddate.com/astronomy/night/@z-us-' + input

    # Reset the .json file
    f = open("planet_visibility.json", "r+")
    f.seek(0)
    f.truncate()

    # Get the url for the corresponding planet visibility data
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    # Find the table with the matching class
    table_data = soup.find('table', class_='tb-wc zebra sep fw')

    # Find all of the table headers
    headers = []
    count = 0
    for i in table_data.find_all('th'):
        if count < 7:
            title = i.text
            headers.append(title)
            count += 1
        else:
            break
    headers.pop(0)
    date = headers.pop(0)
    headers.pop(0)

    df = pd.DataFrame(columns=headers)

    # Find all of the table rows
    for j in table_data.find_all('tr')[2:]:
            row_data = j.find_all('td')
            row = [tr.text.strip() for tr in row_data]
            length = len(df)
            df.loc[length] = row

    json_list = df.to_json(orient='records')

    json_list = json.loads(json_list)

    # Add planet name to the list of .json objects
    planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    count = 0
    for item in json_list:
        item['Planet'] = planets[count]
        count += 1

    # Write planet_visibility.json file with scraped data
    with open('planet_visibility.json', 'w') as fout:
        json.dump(json_list, fout)