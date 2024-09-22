import os
import folium
import requests
from stopSearch import app
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
from flask import render_template, request, jsonify, redirect, url_for
load_dotenv()

@app.route('/map/searchEngine', methods=['GET', 'POST'])
def map_search_engine():
    if request.method == 'GET':
        return render_template('map_search.html')
    
    if request.method == 'POST':
        params = {
            'report_type': request.form.get('report_type'),
            'number_of_victims': request.form.get('number_of_victims'),
            'victim_information_age': request.form.get('victim_information_age'),
            'victim_information_race': request.form.get('victim_information_race'),
            'victim_information_gender': request.form.get('victim_information_gender'),
            'get_police_info': request.form.get('get_police_info'),
            'number_of_police': request.form.get('number_of_police'),
            'type_of_search': request.form.get('type_of_search'),
            'reason_for_search': request.form.get('reason_for_search'),
            'address_type': request.form.get('address_type'),
            'report_weekday': request.form.get('report_weekday')
        }

        # Filter out empty parameters
        filtered_params = {key: value for key, value in params.items() if value}

        # Redirect to map/search with parameters as query string
        return redirect(url_for('map_search', **filtered_params))


# TODO: dynamic seach route where params are submitted as SQL params for where clause
@app.route('/map')
def map_search():
    if request.method == 'GET':
        # get SQL parameters from form
        params = {
            'dataID': request.form.get('dataID'),
            'reportType': request.form.get('reportType'),
            'numberOfVictims': request.form.get('numberOfVictims'),
            'victimAge': request.form.get('victimAge'),
            'victimGender': request.form.get('victimGender'),
            'victimRace': request.form.get('victimRace'),
            'searchReason': request.form.get('searchReason'),
            'searchOutcome': request.form.get('searchOutcome'),
            'searchType': request.form.get('searchType'),
            'search_reason': request.form.get('search_reason'),
            'addressType': request.form.get('addressType'),
            'reportWeekday': request.form.get('reportWeekday'),
            'reportWeek': request.form.get('reportWeek'),
            'reportMonth': request.form.get('reportMonth'),
            'reportYear': request.form.get('reportYear'),
            'policeInfo': request.form.get('policeInfo'),
            'bodyCamera': request.form.get('bodyCamera'),
            'bodyCameraWorn': request.form.get('bodyCameraWorn'),
            'badgeNumber': request.form.get('badgeNumber'),
            'officerName': request.form.get('officerName'),
            'streetName': request.form.get('streetName'),
            'townOrCity': request.form.get('townOrCity'),
        }

        # filter out any parameters that are None or empty
        filetered_params = {key: value for key, value in params.items() if value}        

        # build a request to the search/report API dynamically
        base_url = f'http://localhost:{os.environ["API_PORT"]}/search/report'
        query_string = '&'.join([f'{key}={value}' for key, value in filetered_params.items()])
        get_reports_from_bespoke_search_api = f'{base_url}?{query_string}'

        # make the API request
        map_data_response = requests.get(get_reports_from_bespoke_search_api)

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
                # TODO: uppdate to correct iteration -> data['ReportData'][0]['ReportBy']['dataID'] etc..
                data_id=data['ReportData'][0]['ReportedBy']['dataID'],
                form_type=data['ReportData'][0]['ReportedBy']['reportType'],
                report_date=data['ReportData'][0]['ReportedBy']['reportDate'],
                
                victim_age=data['ReportData'][1]['VictimInformation']['victimAge'],
                victim_gender=data["ReportData"][1]['VictimInformation']['victimGender'],
                victim_race=data["ReportData"][1]['VictimInformation']['victimRace'],
                number_of_victims=data["ReportData"][1]['VictimInformation']['numberOfVictims'],
                
                street_name=data['ReportData'][2]['PublicRelations']['streetName'],
                town_or_city=data['ReportData'][2]['PublicRelations']['townCity'],
                incident_longitude=data['ReportData'][2]['PublicRelations']['lattitude'],
                incident_latitude=data['ReportData'][2]['PublicRelations']['longitude'],  
                address_type=data['ReportData'][2]['PublicRelations']['addressType'],
                search_type=data["ReportData"][2]['PublicRelations']['searchType'],
                search_reason=data["ReportData"][2]['PublicRelations']['searchReason'],
                search_outcome=data["ReportData"][2]['PublicRelations']['searchOutcome'],
                
                get_police_info=data['ReportData'][3]['PoliceInformation']['getPoliceInfo'],
                number_of_police=data["ReportData"][3]['PoliceInformation']['numberOfPolice'],
                body_camera_worn=data["ReportData"][3]['PoliceInformation']['bodyCameraWorn'],
                badge_number=data["ReportData"][3]['PoliceInformation']['badgeNumber'],
                officer_name=data["ReportData"][3]['PoliceInformation']['officerName'],
                police_station=data["ReportData"][3]['PoliceInformation']['policeStation']
            ),
            width=500,
            height=500
        )

        popup = folium.Popup(iframe, max_width=2650)

        # add the coordinates on the map
        folium.Marker(
            location=[float(data['ReportData'][2]['PublicRelations']['longitude']), float(data['ReportData'][2]['PublicRelations']['lattitude'])],  # Convert to float
            popup=popup,
            icon=folium.Icon(color='red', icon_color='white', icon='exclamation-triangle', prefix='fa'),
            # icon=folium.Icon(color='blue', icon_color='red', icon='info', prefix='fa')
        ).add_to(map)

    # return render_template('map_search.html')
    return map._repr_html_()



# @app.route('/map/<data_id>')
# def map_via_data_id(data_id: int):
#     # make a request to the /map-data API
#     get_report_by_data_id_api = f'http://localhost:{os.environ["API_PORT"]}/search/{data_id}'
#     map_data_response = requests.get(get_report_by_data_id_api)
    
#     # check if the response is valid
#     if map_data_response.status_code == 200:
#         # turn response into json object
#         map_data = map_data_response.json()
#     else:
#         # Handle error
#         return {"Error": "Map failed to load data"}
    
#     # create start location for map
#     latitude = '51.49667998379874'
#     longitude = '-0.10402997960522953'
#     start_location = (float(latitude), float(longitude))
#     map = folium.Map(
#         location=start_location,
#         tiles="OpenStreetMap",
#         zoom_start=7,
#     )

#     # loop through map_data to display data in map
#     for data in map_data['Results']:
#         # create frame for location data
#         map_data_pinpoint = 'map_data.html'
#         iframe = folium.IFrame(
#             html=render_template(
#                 map_data_pinpoint,
#                 data_id=data['ReportedBy']['dataID'],
#                 form_type=data['ReportedBy']['reportType'],
#                 report_date=data['ReportedBy']['reportDate'],
#                 street_name=data['PublicRelations']['streetName'],
#                 town_or_city=data['PublicRelations']['townCity'],
#                 incident_longitude=data['PublicRelations']['lattitude'],  # Correct key
#                 incident_latitude=data['PublicRelations']['longitude'],    # Correct key
#                 victim_age=data['VictimInformation']['victimAge'],
#                 victim_gender=data["VictimInformation"]['victimGender'],
#                 victim_race=data["VictimInformation"]['victimRace'],
#                 number_of_victims=data["VictimInformation"]['numberOfVictims'],
#                 number_of_police=data["PoliceInformation"]['numberOfPolice'],
#                 type_of_search=data["PublicRelations"]['searchType'],
#                 search_reason=data["PublicRelations"]['searchReason'],
#                 get_police_details=data['PoliceInformation']['getPoliceInfo']
#             ),
#             width=500,
#             height=500
#         )

#         popup = folium.Popup(iframe, max_width=2650)

#         # add the coordinates on the map
#         folium.Marker(
#             location=[float(data['PublicRelations']['longitude']), float(data['PublicRelations']['lattitude'])],  # Convert to float
#             popup=popup,
#             icon=folium.Icon(color='blue', icon_color='red', icon='info', prefix='fa')
#         ).add_to(map)

#     return map._repr_html_()


# @app.route('/map/30days')
# def map_via_30_days():
#     # make a request to the /map-data API
#     get_reports_from_30_days_api = f'http://localhost:{os.environ["API_PORT"]}/search/30days'
#     map_data_response = requests.get(get_reports_from_30_days_api)
    
#     # check if the response is valid
#     if map_data_response.status_code == 200:
#         # turn response into json object
#         map_data = map_data_response.json()
#     else:
#         # Handle error
#         return {"Error": "Map failed to load data"}
    
#     # create start location for map
#     latitude = '51.49667998379874'
#     longitude = '-0.10402997960522953'
#     start_location = (float(latitude), float(longitude))
#     map = folium.Map(
#         location=start_location,
#         tiles="OpenStreetMap",
#         zoom_start=7,
#     )

#     # loop through map_data to display data in map
#     for data in map_data['Results']:
#         # create frame for location data
#         map_data_pinpoint = 'map_data.html'
#         iframe = folium.IFrame(
#             html=render_template(
#                 map_data_pinpoint,
#                 data_id=data['ReportedBy']['dataID'],
#                 form_type=data['ReportedBy']['reportType'],
#                 report_date=data['ReportedBy']['reportDate'],
#                 street_name=data['PublicRelations']['streetName'],
#                 town_or_city=data['PublicRelations']['townCity'],
#                 incident_longitude=data['PublicRelations']['lattitude'],  # Correct key
#                 incident_latitude=data['PublicRelations']['longitude'],    # Correct key
#                 victim_age=data['VictimInformation']['victimAge'],
#                 victim_gender=data["VictimInformation"]['victimGender'],
#                 victim_race=data["VictimInformation"]['victimRace'],
#                 number_of_victims=data["VictimInformation"]['numberOfVictims'],
#                 number_of_police=data["PoliceInformation"]['numberOfPolice'],
#                 type_of_search=data["PublicRelations"]['searchType'],
#                 search_reason=data["PublicRelations"]['searchReason'],
#                 get_police_details=data['PoliceInformation']['getPoliceInfo']
#             ),
#             width=500,
#             height=500
#         )

#         popup = folium.Popup(iframe, max_width=2650)

#         # add the coordinates on the map
#         folium.Marker(
#             location=[float(data['PublicRelations']['longitude']), float(data['PublicRelations']['lattitude'])],  # Convert to float
#             popup=popup,
#             icon=folium.Icon(color='blue', icon_color='red', icon='info', prefix='fa')
#         ).add_to(map)

#     return map._repr_html_()

# TODO: get data from last 60 days

# TODO: get data from last 90 days

# TODO: get data from last 6 months

# TODO: get data from last 1 year

# TODO: get data from specified year

