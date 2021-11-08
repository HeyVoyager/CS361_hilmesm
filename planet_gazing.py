from flask import Flask, render_template, url_for, flash, redirect, jsonify, request
from forms import SearchForm
import json
from table_scraper import scraper
import requests

# Code modified from Corey Schafer's YouTube Series
# Python Flask Tutorial: Full-Featured Web App

app = Flask(__name__)

app.config['SECRET_KEY'] = '8475930875648334'

weather = [
    {'low': '55', 'high': '75',  'median': '65'}
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/visibility")
def visibility():
    with open('planet_visibility.json', 'r') as myfile:
        data = myfile.read()

    print(type(data))
    dump = json.dumps(data)
    print(type(dump))
    print(data)
    return render_template('visibility.html', weather=weather, jsonfile=json.loads(data), title='Tonight')

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():

        # if '-' in form.location.data:
        #     api_url = 'http://localhost:3030/current-weather/latitude-longitude'
        #     input = form.location.data
        #     input = input.replace(' ', '')
        #     input = input.split(',')
        #     send_data = {}
        #     send_data['latitude'] = input[0]
        #     send_data['longitude'] = input[1]
        # else:
        #     api_url = 'http://localhost:3030/current-weather/zip-code'
        #     zipcode = form.location.data
        #     send_data = {}
        #     send_data['zipCode'] = zipcode
        # r = requests.post(url=api_url, json=send_data)

        scraper(form.location.data)
        # if '-' in form.location.data:
        #     input = form.location.data
        #     input = input.replace(' ', '')
        #     url = 'https://www.timeanddate.com/astronomy/night/@' + input
        #     scraper(url)
        # else:
        #     input = form.location.data
        #     url = 'https://www.timeanddate.com/astronomy/night/@z-us-' + input
        #     scraper(url)

        flash(f'Search successful for {form.location.data}!', 'success')
        return redirect(url_for('visibility'))
    return render_template('search.html', title='Search', form=form)

@app.route("/planet-gazing-data/latitude-longitude", methods=['GET', 'POST'])
def planet_gazing_latlong():
    req_data = request.get_json()
    latitude = req_data['latitude']
    longitude = req_data['longitude']
    #
    # latitude = request.args.get('latitude')
    # longitude = request.args.get('longitude')
    string = str(latitude) + ',' + str(longitude)
    scraper(string)

    with open('planet_visibility.json', 'r') as myfile:
        data = myfile.read()

    # print(type(data))
    dump = json.dumps(data)
    # print(type(dump))
    # print(data)
    # return data
    return '''<body>{}</body>'''.format(data)
#
#
@app.route("/planet-gazing-data/zip-code", methods=['GET', 'POST'])
def planet_gazing_zipcode():
    req_data = request.get_json()
    zipCode = req_data['zipCode']


    # zipCode = request.args.get('zipCode')
    string = str(zipCode)
    scraper(string)

    with open('planet_visibility.json', 'r') as myfile:
        data = myfile.read()

    print(type(data))
    dump = json.dumps(data)
    print(type(dump))
    print(data)
    # return data
    return '''<body>{}</body>'''.format(data)

@app.route("/json_example", methods=['POST'])
def json_example():
    req_data = request.get_json()
    zipCode = req_data['zipCode']
    return '''<body>{}</body>'''.format(zipCode)

def write_weather(weather):
    return

@app.route("/mercury")
def mercury():
    return render_template('mercury.html')

@app.route("/venus")
def venus():
    return render_template('venus.html')

@app.route("/mars")
def mars():
    return render_template('mars.html')

@app.route("/jupiter")
def jupiter():
    return render_template('jupiter.html')

@app.route("/saturn")
def saturn():
    return render_template('saturn.html')

@app.route("/uranus")
def uranus():
    return render_template('uranus.html')

@app.route("/neptune")
def neptune():
    return render_template('neptune.html')

if __name__ == '__main__':
    app.run(debug=True)