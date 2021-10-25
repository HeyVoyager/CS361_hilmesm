from flask import Flask, render_template, url_for, flash, redirect
from forms import SearchForm
import json

# Code modified from Corey Shafer's YouTube Series
# Python Flask Tutorial: Full-Featured Web App

app = Flask(__name__)

app.config['SECRET_KEY'] = '8475930875648334'

with open('planet_visibility.json', 'r') as myfile:
    data = myfile.read()

print(type(data))
dump = json.dumps(data)
print(type(dump))
print(data)

# posts = [
#     {
#         'planet': 'Mercury',
#         'rise': '6:00 pm',
#         'comment': 'Barely visible'
#     },
#     {
#         'planet': 'Venus',
#         'rise': '7:00 pm',
#         'comment': 'Clearly visible'
#     }
# ]
#
# posts_2 = [
#     {'planet': 'Mercury', 'rise': 'Sat 6:01 am',  'comment': 'Slightly difficult to see'},
#     {'planet': 'Venus', 'rise': 'Fri 11:58 am', 'comment': 'Great visibility'},
#     {'planet': 'Mars', 'rise': 'Sat 7:12 am', 'comment': 'Extremely difficult to see'},
#     {'planet': 'Jupiter', 'rise': 'Fri 3:45 pm', 'comment': 'Perfect visibility'},
#     {'planet': 'Saturn', 'rise': 'Fri 3:02 pm', 'comment': 'Perfect visibility'},
#     {'planet': 'Uranus', 'rise': 'Fri 6:43 pm', 'comment': 'Average visibility'},
#     {'planet': 'Neptune', 'rise': 'Fri 4:50 pm', 'comment': 'Difficult to see'}
# ]

weather = [
    {'low': '55', 'high': '75',  'median': '65'}
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/visibility")
def visibility():
    return render_template('visibility.html', weather=weather, jsonfile=json.loads(data), title='Tonight')

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash(f'Search successful for {form.location.data}!', 'success')
        return redirect(url_for('visibility'))
    return render_template('search.html', title='Search', form=form)

@app.route("/mercury")
def mercury():
    return render_template('mercury.html')

if __name__ == '__main__':
    app.run(debug=True)