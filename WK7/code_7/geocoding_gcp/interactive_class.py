import requests 
import urllib.parse
import json
import pandas as pd


list_of_address = [
    '5 bleecker st ny ny', 
    '1910 bishop rd belmonet ca',
    'white house', 
    '535 8th Ave, New York',
    '1600 Amphitheatre Parkway Mountain View, CA'
]

google_response = []

for address in list_of_address: 
    api_key = ''

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    print(f'....finished with {address}')


df = pd.DataFrame(google_response)



##### reverse code 

reverse_geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
latitude = '38.897676'
longitude = '-77.036530'
step1 = reverse_geocode_url + latitude + ',' + longitude + '&key=' + api_key



###### function

def geocode(address_here): 

    api_key = ''

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address_here
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address_here, 'lat': lat_response, 'lon': lng_response}

    return final 


geocode('5 bleecker st ny ny')