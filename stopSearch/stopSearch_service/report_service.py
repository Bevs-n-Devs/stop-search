import datetime
from sqlalchemy import *
from stopSearch import app
from stopSearch.stopSearch_database.extension import LocalSession, init_db
from stopSearch.stopSearch_database.models import (
    ReportData,
    ReportedBy,
    VictimInformation,
    PublicRelations,
    PoliceInformation,
    ReportType,
    ReportDate,
    IncidentAddress,
    OfficerInformation,
    MapCoordinates,
    ReportMedia
)
init_db()

# save form data to database
def create_new_report_data(email: str) -> list[ReportData]:
    """
    Takes the user email to save report data.
    
    Returns ReportData object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_report_email = ReportData(
                report_email = email.lower()
            )

            session.add(new_report_email)
            session.commit()

            return new_report_email
        
        except Exception as e:
            return {"SQL Error": e}

def create_new_report_by(confirm_email: str, new_report_data_id: ReportData) -> list[ReportedBy]:
    """
    Stores the users confirmation email in ReportedBy table.
    Table linked to ReportData via foreign key.

    Returns ReportedBy object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_report_by = ReportedBy(
                confirm_email = confirm_email,
                reported_by = new_report_data_id
            )

            session.add(new_report_by)
            session.commit()

            return new_report_by
        
        except Exception as e:
            return {"SQL Error": e}


def create_new_report_type(confirm_email: str, new_report_data_id: ReportData) -> list[ReportedBy]:
    """
    Takes the users confirmation email to store in ReportedBy table.
    Table linked to ReportData via foreign key.

    Returns ReportedBy object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_report_by = ReportedBy(
                confirm_email = confirm_email.lower(),
                reported_by = new_report_data_id
            )

            session.add(new_report_by)
            session.commit()

            return new_report_by
        
        except Exception as e:
            return {"SQL Error": e}
        

def create_new_report_type(report_type: str, new_report_by_id: ReportedBy) -> list[ReportType]:
    """
    Records if user is a victim or witness into ReportType table.
    Table linked to ReportedBy via foerign key.

    Returns ReportType object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_report_type = ReportType(
                report_type = report_type,
                form_type = new_report_by_id
            )

            session.add(new_report_type)
            session.commit()

            return new_report_type
        
        except Exception as e:
            return {'SQL Error': e}
        

def create_new_report_date(get_date: str, new_report_by_id: ReportedBy) -> list[ReportDate]:
    """
    Converts a datetime object into string, storing in ReportDate table.
    Table linked to ReportedBy via foerign key.

    Returns ReportDate object.
    """
    import stopSearch.utils as utils
    with app.app_context():
        try:
            session = LocalSession()
            # convert date into string
            datetime_object = get_date
            date_list_object = utils.convert_datetime_to_string_and_parse_object(form_date=get_date)

            new_report_date = ReportDate(
                report_date = datetime_object[1][0],
                formatted_day = date_list_object[0][2],
                formatted_weekday = date_list_object[0][0],
                formatted_month = date_list_object[0][1],
                formatted_year = date_list_object[0][4],
                formatted_time = date_list_object[0][3],
                form_date = new_report_by_id
            )

            session.add(new_report_date)
            session.commit()

            return new_report_date
        
        except Exception as e:
            return {'SQL Error': e} 


def create_new_victim_information(num_victims: str, victim_age: str, victim_gender: str, victim_race: str, new_report_data_id: ReportData) -> list[VictimInformation]:
    """
    Takes the victim information to store in VictimInformation table.
    Table linked to ReportData via foreign key.

    Returns VictimInformation object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_victim_info = VictimInformation(
              number_of_victims = num_victims,
              victim_age = victim_age,
              victim_gender = victim_gender,
              victim_race = victim_race, 
              victim_information = new_report_data_id
            )

            session.add(new_victim_info)
            session.commit()

            return new_victim_info
        
        except Exception as e:
            return {'SQL Error': e}
        

def create_new_public_relations(search_reason: str, search_type: str, report_notes: str, new_report_data_id: ReportData) -> list[PublicRelations]:
    """
    This collects interactions between the police and the public, storing it in PublicRelations table.
    Table linked to ReportData via foreign key.

    Returns PublicRelations object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_public_relations = PublicRelations(
                search_reason = search_reason,
                search_type = search_type,
                additional_notes = report_notes,
                public_relations = new_report_data_id
            )

            session.add(new_public_relations)
            session.commit()

            return new_public_relations

        except Exception as e:
            return {'SQL Error': e}


def  create_new_incident_address(address_type: str, street_name: str, town_city: str, new_public_relations_id: PublicRelations) -> list[IncidentAddress]:
    """
    Records where the incident took place and stores in IncidentAddress table.
    Table linked to PublicRelations via foreign key.

    Returns IncidentAddress object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_incident_address = IncidentAddress(
                address_type = address_type,
                street_name = street_name,
                town_or_city = town_city,
                incident_address = new_public_relations_id
            )

            session.add(new_incident_address)
            session.commit()

            return new_incident_address
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_map_coordinates(lattitude: float, longitude: float, new_incident_address_id: IncidentAddress) -> list[MapCoordinates]:
    """
    Records the lattitude & longitude of and stores into MapCoordinates table.
    Table linked to IncidentAddress via foreign key.

    Returns MapCoordinates object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_map_coordinates = MapCoordinates(
                lattitude = lattitude,
                longitude = longitude,
                map_coordinates = new_incident_address_id
            )

            session.add(new_map_coordinates)
            session.commit()

            return new_map_coordinates
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_police_officer_information(num_police: str, get_police_info: str, new_report_data_id: ReportData) -> list[PoliceInformation]:
    """
    Records the actions of the police at the scene into PoliceInformation table.
    Table linked to ReportData via foreign key.

    Returns PoliceInformation object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_police_info = PoliceInformation(
                number_of_police = num_police,
                obtain_police_info = get_police_info,
                police_information = new_report_data_id
            )

            session.add(new_police_info)
            session.commit()

            return new_police_info
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_officer_information(badge_num: str, police_name: str, police_station: str, new_police_info_id: PoliceInformation) -> list[OfficerInformation]:
    """
    Records any police officer's details who were at the scene into OfficerInformation table.
    Table linked to PoliceInformation via foreign key.

    Returns OfficerInformation object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_officer_info = OfficerInformation(
                badge_number = badge_num,
                officer_name = police_name,
                police_station = police_station,
                officer_information = new_police_info_id
            )

            session.add(new_officer_info)
            session.commit()

            return new_officer_info
        
        except Exception as e:
            return {'SQL Error': e}

def create_new_report_media(media_path: str, new_public_id: PublicRelations) -> list[ReportMedia]:
    """
    Records any images associated to the incident in ReportMedia.
    Table linked to PublicRelations object.

    Returns FormMedia object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_report_media = ReportMedia(
                media_file_path = media_path,
                report_media_file = new_public_id
            )

            session.add(new_report_media)
            session.commit()

            return new_report_media
        
        except Exception as e:
            return {'SQL Error': e}
        
# get form data from database
