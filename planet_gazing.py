from flask import Flask, render_template, url_for, flash, redirect
from forms import SearchForm
import json
from table_scraper import scraper

# Code modified from Corey Schafer's YouTube Series
# Python Flask Tutorial: Full-Featured Web App

app = Flask(__name__)

app.config['SECRET_KEY'] = '8475930875648334'

# with open('planet_visibility.json', 'r') as myfile:
#     data = myfile.read()
#
# print(type(data))
# dump = json.dumps(data)
# print(type(dump))
# print(data)


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

        if '-' in form.location.data:
            input = form.location.data
            input = input.replace(' ', '')
            url = 'https://www.timeanddate.com/astronomy/night/@' + input
            scraper(url)
        else:
            input = form.location.data
            url = 'https://www.timeanddate.com/astronomy/night/@z-us-' + input
            scraper(url)

        flash(f'Search successful for {form.location.data}!', 'success')
        return redirect(url_for('visibility'))
    return render_template('search.html', title='Search', form=form)

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