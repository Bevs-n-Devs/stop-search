
import os
from flask import Flask, jsonify, request
from stopSearch import app
from stopSearch.stopSearch_service import question_service, report_service
import stopSearch.utils as utils
from datetime import datetime
import geocoder
from werkzeug.utils import secure_filename

@app.route("/submit_report", methods=["POST"])
def submit_report():
    try:
        # get data from form
        form_data = {
            "report_email" : request.form.get('report_email'),
            "confirm_report_email" : request.form.get('confirm_report_email'),
            "form_type" : request.form.get('form_type'),
            "form_date" : request.form.get('form_date'),
            "address_type" : request.form.get('address_type'),
            "street_name" : request.form.get('street_name'),
            "town_or_city" : request.form.get('town_or_city'),
            "victims_involved" : request.form.get('victims_involved'),
            "victim_age" : request.form.get('victim_age'),
            "victim_gender" : request.form.get('victim_gender'),
            "victim_race" : request.form.get('victim_race'),
            "number_of_police" : request.form.get('number_of_police'),
            "search_type" : request.form.get('search_type'),
            "search_reason" : request.form.get('search_reason'),
            "get_police_info" : request.form.get('getPoliceInfo'),
            "additional_notes" : request.form.get('additional_notes'),
            "media_files": []
        }

        # validate user email
        if form_data['report_email'] != form_data['confirm_report_email']:
            email_error = "Email does not match."
            return jsonify({'status': 'error', 'message': email_error}), 400
         
        # convert date
        get_date = utils.convert_datetime_to_string_and_parse_object(form_date=form_data['form_date'])

        # get address & coordinates
        if form_data['address_type'] == "Manual Address":
            default_country = "United Kingdom"
            user_coordinates = geocoder.arcgis(location=f"{form_data['street_name']}, {form_data['town_or_city']}, {default_country}")
            # map coordinates
            map_latitude = user_coordinates.latlng[0]
            map_longitude = user_coordinates.latlng[1]
            form_data['map'] = []
            form_data['map'].append({
                "lattitude": map_latitude,
                "longitude": map_longitude
            }) 

        if form_data['address_type'] == "Automatic Address":
            map_latitude = request.form.get('latitude')            
            map_longitude = request.form.get('longitude')
            # update form map & address
            form_data['map'] = []
            form_data['map'].append({
                "lattitude": map_latitude,
                "longitude": map_longitude
            })
            coordinate_address = utils.convert_coordinates_to_address(
                latitude=map_latitude,
                longitude=map_longitude
            )  
            address_list = coordinate_address.split(', ')
            form_data['street_name'] = f"{address_list[0]}, {address_list[1]}"
            form_data['town_or_city'] = f"{address_list[2]}, {address_list[3]}"

        # get officer details
        officers = []
        officer_index = 0
        while True:
            police_name = request.form.get(f"police_name_{officer_index}")
            police_badge = request.form.get(f"police_badge_{officer_index}")
            police_station = request.form.get(f"police_badge_{officer_index}")
            if not police_name and not police_badge and not police_station:
                break
            officers.append({
                "police_name": police_name,
                "police_badge": police_badge,
                "police_station": police_station
            })
            officer_index += 1

        form_data['police_officers'] = officers

        # handle media file upload
        if "media_files" in request.files:
            media_files = request.files.getlist('media_files')

            # Iterate through each file in the list of uploaded files
            for file in media_files:
                # Check if the filename attribute of the current file object is empty
                if file.filename == '':
                    # If filename is empty, skip to the next iteration of the loop
                    continue

                if file and utils.allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    # Store file_path in media_files list
                    form_data['media_files'].append(file_path)

                else:
                    return jsonify({'status': 'error', 'message': f'File type not allowed for {file.filename}'}), 400


        # add form data to database
        with app.app_context():
            # add to ReportData
            user_data = report_service.create_new_report_data(
                email=form_data['report_email']
            )

            # add to ReportedBy
            user_reported_by = report_service.create_new_report_by(
                confirm_email=form_data['confirm_report_email'],
                new_report_data_id=user_data
            )

            # add to ReportType 
            user_report_type = report_service.create_new_report_type(
                report_type=form_data['form_type'],
                new_report_by_id=user_reported_by
            )

            # add to ReportDate
            user_report_date = report_service.create_new_report_date(
                get_date=get_date,
                new_report_by_id=user_reported_by,
            )

            # add to VictimInformation
            user_victim_info = report_service.create_new_victim_information(
                num_victims=form_data['victims_involved'],
                victim_age=form_data['victim_age'],
                victim_race=form_data['victim_race'],
                victim_gender=form_data['victim_gender'],
                new_report_data_id=user_data
            )

            # add to PublicRelations
            user_public_relations = report_service.create_new_public_relations(
                search_reason=form_data['search_reason'],
                search_type=form_data['search_type'],
                report_notes=form_data['additional_notes'],
                new_report_data_id=user_data
            )

            # add to IncidentAddress
            user_incident_address = report_service.create_new_incident_address(
                address_type=form_data['address_type'],
                street_name=form_data['street_name'],
                town_city=form_data['town_or_city'],
                new_public_relations_id=user_public_relations
            )

            # add to MapCoordinates
            user_map_coordinates = report_service.create_new_map_coordinates(
                lattitude=form_data['map'][0]['lattitude'],
                longitude=form_data['map'][0]['longitude'],
                new_incident_address_id=user_incident_address
            )

            # add to ReportMedia
            if form_data['media_files'] != None:

                for file in form_data['media_files']:
                    user_report_media = report_service.create_new_report_media(
                        media_path=file,
                        new_public_id=user_public_relations
                    ) 

            # add to PoliceInformation
            user_police_info = report_service.create_new_police_officer_information(
                num_police=form_data['number_of_police'],
                get_police_info=form_data['get_police_info'],
                new_report_data_id=user_data
            )
            
            # add to OfficerInformation
            if form_data['police_officers'] != None:
                for officer in form_data['police_officers']:

                    user_officer_info = report_service.create_new_officer_information(
                        badge_num=officer['police_badge'],
                        police_name=officer['police_name'],
                        police_station=officer['police_station'],
                        new_police_info_id=user_police_info
                    )
        
        return jsonify({'status': 'success', 'message': 'Report submitted successfully'}, form_data, coordinate_address), 200
        
            

    except Exception as e:
        # Log the error
        app.logger.error(f"Error in /submit_report: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Internal Server Error'}), 500
    


