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

    if '-' in input_data:
        input = input_data
        input = input.replace(' ', '')
        url = 'https://www.timeanddate.com/astronomy/night/@' + input

    else:
        input = input_data
        url = 'https://www.timeanddate.com/astronomy/night/@z-us-' + input

    f = open("planet_visibility.json", "r+")
    f.seek(0)
    f.truncate()

    requests.get(url)
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')
    # print(soup)

    table_data = soup.find('table', class_='tb-wc zebra sep fw')

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

    for j in table_data.find_all('tr')[2:]:
            row_data = j.find_all('td')
            row = [tr.text.strip() for tr in row_data]
            length = len(df)
            df.loc[length] = row

    json_list = df.to_json(orient='records')

    # print(df)
    # print(json_list)

    json_list = json.loads(json_list)

    planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    count = 0
    for item in json_list:
        item['Planet'] = planets[count]
        count += 1

    # print(json_list)

    with open('planet_visibility.json', 'w') as fout:
        json.dump(json_list, fout)

    with open('planet_visibility.json', 'r') as myfile:
        data = myfile.read()

    # print(data)

# url = 'https://www.timeanddate.com/astronomy/night/usa/portland-or'
# scraper(url)