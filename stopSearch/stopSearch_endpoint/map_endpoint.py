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
    # make a request to the /map-data API
    search_all_reports_api = f'http://localhost:{os.environ["API_PORT"]}/search/all'
    map_data_response = requests.get(search_all_reports_api)
    
    # check if the response is valid
    if map_data_response.status_code == 200:
        # turn response into json object
        map_data = map_data_response.json()
    else:
        # Handle error
        return {"Error": "Map failed to load data"}
    
    # create start location for map
    latitude = '51.49667998379874'
    longitude = '-0.10402997960522953'
    start_location = (float(latitude), float(longitude))
    map = folium.Map(
        location=start_location,
        tiles="OpenStreetMap",
        zoom_start=7,
    )

    # loop through map_data to display data in map
    for data in map_data['Results']:
        # create frame for location data
        map_data_pinpoint = 'map_data.html'
        iframe = folium.IFrame(
            html=render_template(
                map_data_pinpoint,
                data_id=data['ReportedBy']['dataID'],
                form_type=data['ReportedBy']['reportType'],
                report_date=data['ReportedBy']['reportDate'],
                street_name=data['PublicRelations']['streetName'],
                town_or_city=data['PublicRelations']['townCity'],
                incident_longitude=data['PublicRelations']['lattitude'],  # Correct key
                incident_latitude=data['PublicRelations']['longitude'],    # Correct key
                victim_age=data['VictimInformation']['victimAge'],
                victim_gender=data["VictimInformation"]['victimGender'],
                victim_race=data["VictimInformation"]['victimRace'],
                number_of_victims=data["VictimInformation"]['numberOfVictims'],
                number_of_police=data["PoliceInformation"]['numberOfPolice'],
                type_of_search=data["PublicRelations"]['searchType'],
                search_reason=data["PublicRelations"]['searchReason'],
                get_police_details=data['PoliceInformation']['getPoliceInfo']
            ),
            width=500,
            height=500
        )

        popup = folium.Popup(iframe, max_width=2650)

        # add the coordinates on the map
        folium.Marker(
            location=[float(data['PublicRelations']['longitude']), float(data['PublicRelations']['lattitude'])],  # Convert to float
            popup=popup,
            icon=folium.Icon(color='blue', icon_color='red', icon='info', prefix='fa')
        ).add_to(map)

    return map._repr_html_()


@app.route('/map/<data_id>')
def map_via_data_id(data_id: int):
    # make a request to the /map-data API
    get_report_by_data_id_api = f'http://localhost:{os.environ["API_PORT"]}/search/{data_id}'
    map_data_response = requests.get(get_report_by_data_id_api)
    
    # check if the response is valid
    if map_data_response.status_code == 200:
        # turn response into json object
        map_data = map_data_response.json()
    else:
        # Handle error
        return {"Error": "Map failed to load data"}
    
    # create start location for map
    latitude = '51.49667998379874'
    longitude = '-0.10402997960522953'
    start_location = (float(latitude), float(longitude))
    map = folium.Map(
        location=start_location,
        tiles="OpenStreetMap",
        zoom_start=7,
    )

    # loop through map_data to display data in map
    for data in map_data['Results']:
        # create frame for location data
        map_data_pinpoint = 'map_data.html'
        iframe = folium.IFrame(
            html=render_template(
                map_data_pinpoint,
                data_id=data['ReportedBy']['dataID'],
                form_type=data['ReportedBy']['reportType'],
                report_date=data['ReportedBy']['reportDate'],
                street_name=data['PublicRelations']['streetName'],
                town_or_city=data['PublicRelations']['townCity'],
                incident_longitude=data['PublicRelations']['lattitude'],  # Correct key
                incident_latitude=data['PublicRelations']['longitude'],    # Correct key
                victim_age=data['VictimInformation']['victimAge'],
                victim_gender=data["VictimInformation"]['victimGender'],
                victim_race=data["VictimInformation"]['victimRace'],
                number_of_victims=data["VictimInformation"]['numberOfVictims'],
                number_of_police=data["PoliceInformation"]['numberOfPolice'],
                type_of_search=data["PublicRelations"]['searchType'],
                search_reason=data["PublicRelations"]['searchReason'],
                get_police_details=data['PoliceInformation']['getPoliceInfo']
            ),
            width=500,
            height=500
        )

        popup = folium.Popup(iframe, max_width=2650)

        # add the coordinates on the map
        folium.Marker(
            location=[float(data['PublicRelations']['longitude']), float(data['PublicRelations']['lattitude'])],  # Convert to float
            popup=popup,
            icon=folium.Icon(color='blue', icon_color='red', icon='info', prefix='fa')
        ).add_to(map)

    return map._repr_html_()


@app.route('/map/30days')
def map_via_30_days():
    # make a request to the /map-data API
    get_reports_from_30_days_api = f'http://localhost:{os.environ["API_PORT"]}/search/30days'
    map_data_response = requests.get(get_reports_from_30_days_api)
    
    # check if the response is valid
    if map_data_response.status_code == 200:
        # turn response into json object
        map_data = map_data_response.json()
    else:
        # Handle error
        return {"Error": "Map failed to load data"}
    
    # create start location for map
    latitude = '51.49667998379874'
    longitude = '-0.10402997960522953'
    start_location = (float(latitude), float(longitude))
    map = folium.Map(
        location=start_location,
        tiles="OpenStreetMap",
        zoom_start=7,
    )

    # loop through map_data to display data in map
    for data in map_data['Results']:
        # create frame for location data
        map_data_pinpoint = 'map_data.html'
        iframe = folium.IFrame(
            html=render_template(
                map_data_pinpoint,
                data_id=data['ReportedBy']['dataID'],
                form_type=data['ReportedBy']['reportType'],
                report_date=data['ReportedBy']['reportDate'],
                street_name=data['PublicRelations']['streetName'],
                town_or_city=data['PublicRelations']['townCity'],
                incident_longitude=data['PublicRelations']['lattitude'],  # Correct key
                incident_latitude=data['PublicRelations']['longitude'],    # Correct key
                victim_age=data['VictimInformation']['victimAge'],
                victim_gender=data["VictimInformation"]['victimGender'],
                victim_race=data["VictimInformation"]['victimRace'],
                number_of_victims=data["VictimInformation"]['numberOfVictims'],
                number_of_police=data["PoliceInformation"]['numberOfPolice'],
                type_of_search=data["PublicRelations"]['searchType'],
                search_reason=data["PublicRelations"]['searchReason'],
                get_police_details=data['PoliceInformation']['getPoliceInfo']
            ),
            width=500,
            height=500
        )

        popup = folium.Popup(iframe, max_width=2650)

        # add the coordinates on the map
        folium.Marker(
            location=[float(data['PublicRelations']['longitude']), float(data['PublicRelations']['lattitude'])],  # Convert to float
            popup=popup,
            icon=folium.Icon(color='blue', icon_color='red', icon='info', prefix='fa')
        ).add_to(map)

    return map._repr_html_()

# TODO: get data from last 60 days

# TODO: get data from last 90 days

# TODO: get data from last 6 months

# TODO: get data from last 1 year

# TODO: get data from specified year

# TODO: dynamic seach route where params are submitted as SQL params for where clause


