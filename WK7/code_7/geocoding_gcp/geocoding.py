## GCP
# https://developers.google.com/maps/documentation/geocoding/start
# https://developers.google.com/maps/documentation/geocoding/requests-reverse-geocoding

import requests
import pandas as pd
import numpy as np
import re
import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

search = 'https://maps.googleapis.com/maps/api/geocode/json?address='
location = 'New York City'
api_key = os.getenv("GOOGLE_MAPS_API")

# convert location to url friendly string
location = urllib.parse.quote(location)
url = search + location + '&key=' + api_key

# get response
response = requests.get(url)

# get json
json = response.json()

results = json['results'][0]
geometry = results['geometry']
location = geometry['location']
lat = location['lat']
lng = location['lng']


### create loop, exampple list of data address to go through 
### and hit the API 