import os
import folium
import requests
from stopSearch import app
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
from flask import render_template
load_dotenv()

@app.route('/map')
def map_page():

    # make a request to the search engine API
    search_engine_response = requests.get(f'http://localhost:{os.environ["API_PORT"]}/search/all')

    # check if the response is valid
    if search_engine_response.status_code == 200:
        # turn response into a json object
        map_data = search_engine_response.json()
    else:
        # handle error
        return {'Error': 'Map failed to load data.'}
    
    # create start location for map
    latitude = '51.49667998379874'
    longitude = '-0.10402997960522953'
    start_location = (float(latitude), float(longitude))
    map = folium.Map(
        location=start_location,
        tiles="OpenStreetMap",
        zoom_start=7,
    )

    for data in map_data:
        pass
