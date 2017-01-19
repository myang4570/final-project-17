#import requests in order to access an api 
import requests

#import pandas and numpy
import numpy as np 
import pandas as pd 

#set up URL for requests 
endpoint = "http://food2fork.com/api/search"
api_key =  "7d04269097d461c362524a4d13987a64"
#allow the user to choose a specific food to make
foodchoice = input("Choose a food that you would like to make!")
#sort by rating, set up url 
payload = {"key": api_key, "count": 15, "recipes": "title", "q":foodchoice}

#search for the recipe in the database
req = requests.get(endpoint, params=payload)
#format results through json 
results = req.json()
#create a Data Frame, which will be the "recipes" outputs
rec = results["recipes"]

#use vplot to organize multiple graphs 
from bokeh.io import output_file, save, vplot
#import the Bar chart from bokeh 
from bokeh.charts import Bar
df = pd.DataFrame(rec)
#set parameters for the chart, such as where to find the data, which key of data to use as the x-axis, color, title, etc.
p = Bar(df, "publisher", color = "navy", fill_alpha = 0.75, bar_width=1.1, title="Number of Recipes per Source")
#create a histogram by importing it from bokeh first
from bokeh.charts import Histogram
#create the chart; however, since most of the recipes are ranked very close to 100, the graph should look like a single line at/near 100.
p1 = Histogram(df, "social_rank", color = "lavender", fill_alpha = 1, bar_width=1.9, title="Social Rank of Recipe by Interval")
#save the graphs for preview at foodapi.html 
v = vplot(p, p1) 
save(v)
