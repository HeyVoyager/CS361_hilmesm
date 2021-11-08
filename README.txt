-The planet_gazing.py file has library dependencies, including:
flask
json
forms

-The table-scraper.py also has library dependencies, including:
requests
pandas
bs4 (Beautiful Soup)
json

-To run:
CD into the folder where you save the code.
Run the command "flask run" in the terminal.
By default it should run on http://localhost:5000

Routes:
/planet-gazing-data/latitude-longitude

/planet-gazing-data/zip-code

JSON Format Example:
[
  {"Rise": "Sat 6:25 am", "Set": "Sat 5:22 pm", "Meridian": "Sat 11:54 am", "Comment": "Slightly difficult to see", "Planet": "Mercury"},
  {"Rise": "Fri 11:39 am", "Set": "Fri 8:23 pm", "Meridian": "Fri 4:01 pm", "Comment": "Great visibility", "Planet": "Venus"},
  {"Rise": "Sat 6:47 am", "Set": "Sat 5:25 pm", "Meridian": "Sat 12:06 pm", "Comment": "Extremely difficult to see", "Planet": "Mars"},
  {"Rise": "Fri 2:30 pm", "Set": "Sat 12:51 am", "Meridian": "Fri 7:40 pm", "Comment": "Perfect visibility", "Planet": "Jupiter"},
  {"Rise": "Fri 1:43 pm", "Set": "Fri 11:33 pm", "Meridian": "Fri 6:38 pm", "Comment": "Average visibility", "Planet": "Saturn"},
  {"Rise": "Fri 5:44 pm", "Set": "Sat 7:33 am", "Meridian": "Sat 12:39 am", "Comment": "Average visibility", "Planet": "Uranus"},
  {"Rise": "Fri 3:39 pm", "Set": "Sat 3:11 am", "Meridian": "Fri 9:25 pm", "Comment": "Difficult to see", "Planet": "Neptune"}
]