from stopSearch import utils, app
from sqlalchemy import *
from stopSearch.stopSearch_database.extension import LocalSession, init_db
from stopSearch.stopSearch_database.models import (
    ReportData,
    ReportedBy,
    VictimInformation,
    PublicRelations,
    PoliceInformation,
    FormType,
    ReportDate,
    IncidentAddress,
    OfficerInformation,
    MapCoordinates,
    ReportMedia
)
init_db()



def search_all_reports():
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': str(e)}


def search_report_by_data_id(data_id: int):
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        ).where(
            ReportData.report_data_id == data_id
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': str(e)}




def search_all_reports_by_last_30_days():

    with app.app_context():
        import datetime

        session = LocalSession()

        # calculate date 1 month ago
        today = datetime.datetime.now()
        one_month_ago = today - datetime.timedelta(days=1*30) # 30 days for each month

        # adjust year if necessary
        if today.month <= 1: # If current month is Jan
            year = today.year - 1
        else:
            year = today.year
        
        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        ).where(
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= one_month_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}
        

def search_all_reports_by_last_60_days():

    with app.app_context():
        import datetime

        session = LocalSession()

        # calculate date 2 months ago 60 days
        today = datetime.datetime.now()
        two_months_ago = today - datetime.timedelta(days=2*30) # 30 days for each month

        # adjust year if necessary
        if today.month <= 1: # If current month is Jan
            year = today.year - 1
        else:
            year = today.year
        
        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        ).where(
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= two_months_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_last_90_days():

    with app.app_context():
        import datetime

        session = LocalSession()

        # calculate date 3 month ago
        today = datetime.datetime.now()
        three_months_ago = today - datetime.timedelta(days=3*30) # 30 days for each month

        # adjust year if necessary
        if today.month <= 3: 
            year = today.year - 1 # If current month is Jan, Feb, Mar
        else:
            year = today.year

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        ).where(
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= three_months_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_last_6_months():

    with app.app_context():
        import datetime

        session = LocalSession()

        # calculate date 6 month ago
        today = datetime.datetime.now()
        six_months_ago = today - datetime.timedelta(days= 6*30) # 30 days for each month

        # adjust year if necessary
        if today.month <= 6: 
            year = today.year - 1 # If current month is Jan, Feb, Mar
        else:
            year = today.year

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        ).where(
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= six_months_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_last_12_months():
    
    with app.app_context():
        import datetime

        session = LocalSession()

        # calculate date 12 month ago
        today = datetime.datetime.now()
        twelve_months_ago = today - datetime.timedelta(days= 12*30) # 30 days for each month

        # adjust year if necessary
        if today.month <= 12: 
            year = today.year - 1 # If current month is Jan, Feb, Mar .... Dec
        else:
            year = today.year

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        ).where(
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= twelve_months_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}
        

def search_all_reports_by_year(year: int):
    with app.app_context():
        session = LocalSession()

        # convert int year to str
        year = str(year)

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        ).where(
            ReportDate.formatted_year == year
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}

    """
    SET @searchReason = :reason_for_search;
    SELECT RD.report_data_id,
           RT.report_type
           RDate.report_date,
           RDate.formatted_day,
           RDate.formatted_weekday,
           RDate.formatted_year,
           RDate.formatted_time,
           VI.number_of_victims,
           VI.victim_age,
           VI.victim_gender,
           VI.victim_race,
           PR.search_reason,
           PR.search_type,
           PR.additional_notes,
           RM.media_file_path
           IA.address_type,
           IA.street_name,
           IA.town_or_city,
           MC.longitude,
           MC.latitude,
           PI.number_of_police,
           PI.obtain_police_info,
           OI.badge_number,
           OI.officer_name,
           OI.police_station
    FROM stop_search_dev_db.report_data RD 
        JOIN stop_search_dev_db.reported_by RB
            ON RD.report_data_id = RB.reported_by_id
        JOIN stop_search_dev_db.form_type RT
            ON RB.reported_by_id = RD.report_type_id
        JOIN stop_search_dev_db.report_date RDate
            ON RB.reported_by_id = RDate.report_date_id
        JOIN stop_search_dev_db.victim_information VI
            ON RD.report_data_id = VI.victim_information_id
        JOIN stop_search_dev_db.public_relations PR
            ON RD.report_data_id = PR.public_relations_id
        JOIN stop_search_dev_db.report_media RM
            ON PR.public_relations_id = RM.report_media_id
        JOIN stop_search_dev_db.incident_address IA
            ON PR.public_relations_id = IA.incident_address_id
        JOIN stop_search_dev_db.map_coordinates MC
            ON IA.incident_address_id = MC.map_coordinates_id
        JOIN stop_search_dev_db.police_information PI
            ON RD.report_data_id = PI.police_information_id
        JOIN stop_search_dev_db.officer_information OI
            ON PI.police_information_id = OI.officer_information_id
    WHERE PR.search_reason = @searchReason;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_weekday,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id==ReportData.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id==FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
        ).where(
            PublicRelations.search_reason == reason_for_search
        )

        try:
            data_by_search_reason = session.execute(sql_query).all()
            return data_by_search_reason
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_police_badge_number(badge_num: str):
    """
    SET @badgeNumber = :badge_num;
    SELECT RD.report_data_id,
           RT.report_type
           RDate.report_date,
           RDate.formatted_day,
           RDate.formatted_weekday,
           RDate.formatted_year,
           RDate.formatted_time,
           VI.number_of_victims,
           VI.victim_age,
           VI.victim_gender,
           VI.victim_race,
           PR.search_reason,
           PR.search_type,
           PR.additional_notes,
           RM.media_file_path
           IA.address_type,
           IA.street_name,
           IA.town_or_city,
           MC.longitude,
           MC.latitude,
           PI.number_of_police,
           PI.obtain_police_info,
           OI.badge_number,
           OI.officer_name,
           OI.police_station
    FROM stop_search_dev_db.report_data RD 
        JOIN stop_search_dev_db.reported_by RB
            ON RD.report_data_id = RB.reported_by_id
        JOIN stop_search_dev_db.form_type RT
            ON RB.reported_by_id = RD.report_type_id
        JOIN stop_search_dev_db.report_date RDate
            ON RB.reported_by_id = RDate.report_date_id
        JOIN stop_search_dev_db.victim_information VI
            ON RD.report_data_id = VI.victim_information_id
        JOIN stop_search_dev_db.public_relations PR
            ON RD.report_data_id = PR.public_relations_id
        JOIN stop_search_dev_db.report_media RM
            ON PR.public_relations_id = RM.report_media_id
        JOIN stop_search_dev_db.incident_address IA
            ON PR.public_relations_id = IA.incident_address_id
        JOIN stop_search_dev_db.map_coordinates MC
            ON IA.incident_address_id = MC.map_coordinates_id
        JOIN stop_search_dev_db.police_information PI
            ON RD.report_data_id = PI.police_information_id
        JOIN stop_search_dev_db.officer_information OI
            ON PI.police_information_id = OI.officer_information_id
    WHERE OI.badge_number = @badgeNumber;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_weekday,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id==ReportData.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id==FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
        ).where(
            OfficerInformation.badge_number == badge_num
        )

        try:
            data_by_police_badge = session.execute(sql_query).all()
            return data_by_police_badge
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_police_station(station: str):
    """
    SET @policeStation = :station;
    SELECT RD.report_data_id,
           RT.report_type
           RDate.report_date,
           RDate.formatted_day,
           RDate.formatted_weekday,
           RDate.formatted_year,
           RDate.formatted_time,
           VI.number_of_victims,
           VI.victim_age,
           VI.victim_gender,
           VI.victim_race,
           PR.search_reason,
           PR.search_type,
           PR.additional_notes,
           RM.media_file_path
           IA.address_type,
           IA.street_name,
           IA.town_or_city,
           MC.longitude,
           MC.latitude,
           PI.number_of_police,
           PI.obtain_police_info,
           OI.badge_number,
           OI.officer_name,
           OI.police_station
    FROM stop_search_dev_db.report_data RD 
        JOIN stop_search_dev_db.reported_by RB
            ON RD.report_data_id = RB.reported_by_id
        JOIN stop_search_dev_db.form_type RT
            ON RB.reported_by_id = RD.report_type_id
        JOIN stop_search_dev_db.report_date RDate
            ON RB.reported_by_id = RDate.report_date_id
        JOIN stop_search_dev_db.victim_information VI
            ON RD.report_data_id = VI.victim_information_id
        JOIN stop_search_dev_db.public_relations PR
            ON RD.report_data_id = PR.public_relations_id
        JOIN stop_search_dev_db.report_media RM
            ON PR.public_relations_id = RM.report_media_id
        JOIN stop_search_dev_db.incident_address IA
            ON PR.public_relations_id = IA.incident_address_id
        JOIN stop_search_dev_db.map_coordinates MC
            ON IA.incident_address_id = MC.map_coordinates_id
        JOIN stop_search_dev_db.police_information PI
            ON RD.report_data_id = PI.police_information_id
        JOIN stop_search_dev_db.officer_information OI
            ON PI.police_information_id = OI.officer_information_id
    WHERE OI.police_station = @policeStation;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_weekday,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id==ReportData.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id==FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
        ).where(
            OfficerInformation.police_station == station
        )

        try:
            data_by_police_station = session.execute(sql_query).all()
            return data_by_police_station
        
        except Exception as e:
            return {'SQL Error': e}



def search_all_reports_by_street_name(street_name: str):
    """
    SET @streetName = :street_name;
    SELECT RD.report_data_id,
           RT.report_type
           RDate.report_date,
           RDate.formatted_day,
           RDate.formatted_weekday,
           RDate.formatted_year,
           RDate.formatted_time,
           VI.number_of_victims,
           VI.victim_age,
           VI.victim_gender,
           VI.victim_race,
           PR.search_reason,
           PR.search_type,
           PR.additional_notes,
           RM.media_file_path
           IA.address_type,
           IA.street_name,
           IA.town_or_city,
           MC.longitude,
           MC.latitude,
           PI.number_of_police,
           PI.obtain_police_info,
           OI.badge_number,
           OI.officer_name,
           OI.police_station
    FROM stop_search_dev_db.report_data RD 
        JOIN stop_search_dev_db.reported_by RB
            ON RD.report_data_id = RB.reported_by_id
        JOIN stop_search_dev_db.form_type RT
            ON RB.reported_by_id = RD.report_type_id
        JOIN stop_search_dev_db.report_date RDate
            ON RB.reported_by_id = RDate.report_date_id
        JOIN stop_search_dev_db.victim_information VI
            ON RD.report_data_id = VI.victim_information_id
        JOIN stop_search_dev_db.public_relations PR
            ON RD.report_data_id = PR.public_relations_id
        JOIN stop_search_dev_db.report_media RM
            ON PR.public_relations_id = RM.report_media_id
        JOIN stop_search_dev_db.incident_address IA
            ON PR.public_relations_id = IA.incident_address_id
        JOIN stop_search_dev_db.map_coordinates MC
            ON IA.incident_address_id = MC.map_coordinates_id
        JOIN stop_search_dev_db.police_information PI
            ON RD.report_data_id = PI.police_information_id
        JOIN stop_search_dev_db.officer_information OI
            ON PI.police_information_id = OI.officer_information_id
    WHERE IA.street_name = @streetName;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_weekday,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id==ReportData.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id==FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
        ).where(
            IncidentAddress.street_name == street_name
        )

        try:
            data_by_street_name = session.execute(sql_query).all()
            return data_by_street_name
        
        except Exception as e:
            return {'SQL Error': e}

def search_all_reports_by_town_or_city(town_city: str):
    """
    SET @townOrCity = :town_city;
    SELECT RD.report_data_id,
           RT.report_type
           RDate.report_date,
           RDate.formatted_day,
           RDate.formatted_weekday,
           RDate.formatted_year,
           RDate.formatted_time,
           VI.number_of_victims,
           VI.victim_age,
           VI.victim_gender,
           VI.victim_race,
           PR.search_reason,
           PR.search_type,
           PR.additional_notes,
           RM.media_file_path
           IA.address_type,
           IA.street_name,
           IA.town_or_city,
           MC.longitude,
           MC.latitude,
           PI.number_of_police,
           PI.obtain_police_info,
           OI.badge_number,
           OI.officer_name,
           OI.police_station
    FROM stop_search_dev_db.report_data RD 
        JOIN stop_search_dev_db.reported_by RB
            ON RD.report_data_id = RB.reported_by_id
        JOIN stop_search_dev_db.form_type RT
            ON RB.reported_by_id = RD.report_type_id
        JOIN stop_search_dev_db.report_date RDate
            ON RB.reported_by_id = RDate.report_date_id
        JOIN stop_search_dev_db.victim_information VI
            ON RD.report_data_id = VI.victim_information_id
        JOIN stop_search_dev_db.public_relations PR
            ON RD.report_data_id = PR.public_relations_id
        JOIN stop_search_dev_db.report_media RM
            ON PR.public_relations_id = RM.report_media_id
        JOIN stop_search_dev_db.incident_address IA
            ON PR.public_relations_id = IA.incident_address_id
        JOIN stop_search_dev_db.map_coordinates MC
            ON IA.incident_address_id = MC.map_coordinates_id
        JOIN stop_search_dev_db.police_information PI
            ON RD.report_data_id = PI.police_information_id
        JOIN stop_search_dev_db.officer_information OI
            ON PI.police_information_id = OI.officer_information_id
    WHERE IA.town_or_city = @townOrCity;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_weekday,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id==ReportData.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id==FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
        ).where(
            IncidentAddress.town_or_city == town_city
        )

        try:
            data_by_town_or_city = session.execute(sql_query).all()
            return data_by_town_or_city
        
        except Exception as e:
            return {'SQL Error': e}


    """
    SET @weekday = :weekday;
    SELECT RD.report_data_id,
           RT.report_type
           RDate.report_date,
           RDate.formatted_day,
           RDate.formatted_weekday,
           RDate.formatted_year,
           RDate.formatted_time,
           VI.number_of_victims,
           VI.victim_age,
           VI.victim_gender,
           VI.victim_race,
           PR.search_reason,
           PR.search_type,
           PR.additional_notes,
           RM.media_file_path
           IA.address_type,
           IA.street_name,
           IA.town_or_city,
           MC.longitude,
           MC.latitude,
           PI.number_of_police,
           PI.obtain_police_info,
           OI.badge_number,
           OI.officer_name,
           OI.police_station
    FROM stop_search_dev_db.report_data RD 
        JOIN stop_search_dev_db.reported_by RB
            ON RD.report_data_id = RB.reported_by_id
        JOIN stop_search_dev_db.form_type RT
            ON RB.reported_by_id = RD.report_type_id
        JOIN stop_search_dev_db.report_date RDate
            ON RB.reported_by_id = RDate.report_date_id
        JOIN stop_search_dev_db.victim_information VI
            ON RD.report_data_id = VI.victim_information_id
        JOIN stop_search_dev_db.public_relations PR
            ON RD.report_data_id = PR.public_relations_id
        JOIN stop_search_dev_db.report_media RM
            ON PR.public_relations_id = RM.report_media_id
        JOIN stop_search_dev_db.incident_address IA
            ON PR.public_relations_id = IA.incident_address_id
        JOIN stop_search_dev_db.map_coordinates MC
            ON IA.incident_address_id = MC.map_coordinates_id
        JOIN stop_search_dev_db.police_information PI
            ON RD.report_data_id = PI.police_information_id
        JOIN stop_search_dev_db.officer_information OI
            ON PI.police_information_id = OI.officer_information_id
    WHERE RDate.formatted_weekday = @weekday;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_weekday,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id==ReportData.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id==FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
        ).where(
            ReportDate.formatted_weekday == weekday
        )

        try:
            data_by_weekday = session.execute(sql_query).all()
            return data_by_weekday
        
        except Exception as e:
            return {'SQL Error': e}

def search_all_reports_by_formatted_month(month: str):
    """
    SET @month = :month;
    SELECT RD.report_data_id,
           RT.report_type
           RDate.report_date,
           RDate.formatted_day,
           RDate.formatted_weekday,
           RDate.formatted_year,
           RDate.formatted_time,
           VI.number_of_victims,
           VI.victim_age,
           VI.victim_gender,
           VI.victim_race,
           PR.search_reason,
           PR.search_type,
           PR.additional_notes,
           RM.media_file_path
           IA.address_type,
           IA.street_name,
           IA.town_or_city,
           MC.longitude,
           MC.latitude,
           PI.number_of_police,
           PI.obtain_police_info,
           OI.badge_number,
           OI.officer_name,
           OI.police_station
    FROM stop_search_dev_db.report_data RD 
        JOIN stop_search_dev_db.reported_by RB
            ON RD.report_data_id = RB.reported_by_id
        JOIN stop_search_dev_db.form_type RT
            ON RB.reported_by_id = RD.report_type_id
        JOIN stop_search_dev_db.report_date RDate
            ON RB.reported_by_id = RDate.report_date_id
        JOIN stop_search_dev_db.victim_information VI
            ON RD.report_data_id = VI.victim_information_id
        JOIN stop_search_dev_db.public_relations PR
            ON RD.report_data_id = PR.public_relations_id
        JOIN stop_search_dev_db.report_media RM
            ON PR.public_relations_id = RM.report_media_id
        JOIN stop_search_dev_db.incident_address IA
            ON PR.public_relations_id = IA.incident_address_id
        JOIN stop_search_dev_db.map_coordinates MC
            ON IA.incident_address_id = MC.map_coordinates_id
        JOIN stop_search_dev_db.police_information PI
            ON RD.report_data_id = PI.police_information_id
        JOIN stop_search_dev_db.officer_information OI
            ON PI.police_information_id = OI.officer_information_id
    WHERE RDate.formatted_month = @month;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_weekday,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id==ReportData.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id==FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
        ).where(
            ReportDate.formatted_month == month
        )

        try:
            data_by_month = session.execute(sql_query).all()
            return data_by_month
        
        except Exception as e:
            return {'SQL Error': e}



    """
    SET @year = :year;
    SELECT RD.report_data_id,
           RT.report_type
           RDate.report_date,
           RDate.formatted_day,
           RDate.formatted_weekday,
           RDate.formatted_year,
           RDate.formatted_time,
           VI.number_of_victims,
           VI.victim_age,
           VI.victim_gender,
           VI.victim_race,
           PR.search_reason,
           PR.search_type,
           PR.additional_notes,
           RM.media_file_path
           IA.address_type,
           IA.street_name,
           IA.town_or_city,
           MC.longitude,
           MC.latitude,
           PI.number_of_police,
           PI.obtain_police_info,
           OI.badge_number,
           OI.officer_name,
           OI.police_station
    FROM stop_search_dev_db.report_data RD 
        JOIN stop_search_dev_db.reported_by RB
            ON RD.report_data_id = RB.reported_by_id
        JOIN stop_search_dev_db.form_type RT
            ON RB.reported_by_id = RD.report_type_id
        JOIN stop_search_dev_db.report_date RDate
            ON RB.reported_by_id = RDate.report_date_id
        JOIN stop_search_dev_db.victim_information VI
            ON RD.report_data_id = VI.victim_information_id
        JOIN stop_search_dev_db.public_relations PR
            ON RD.report_data_id = PR.public_relations_id
        JOIN stop_search_dev_db.report_media RM
            ON PR.public_relations_id = RM.report_media_id
        JOIN stop_search_dev_db.incident_address IA
            ON PR.public_relations_id = IA.incident_address_id
        JOIN stop_search_dev_db.map_coordinates MC
            ON IA.incident_address_id = MC.map_coordinates_id
        JOIN stop_search_dev_db.police_information PI
            ON RD.report_data_id = PI.police_information_id
        JOIN stop_search_dev_db.officer_information OI
            ON PI.police_information_id = OI.officer_information_id
    WHERE RDate.formatted_year = @year;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_weekday,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id==ReportData.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id==FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
        ).where(
            ReportDate.formatted_year == year
        )

        try:
            data_by_year = session.execute(sql_query).all()
            return data_by_year
        
        except Exception as e:
            return {'SQL Error': e}


# def search_all_reports_by_formatted_time(time: str):
#     """
#     SET @time = :time;
#     SELECT RD.report_data_id,
#            RT.report_type
#            RDate.report_date,
#            RDate.formatted_day,
#            RDate.formatted_weekday,
#            RDate.formatted_year,
#            RDate.formatted_time,
#            VI.number_of_victims,
#            VI.victim_age,
#            VI.victim_gender,
#            VI.victim_race,
#            PR.search_reason,
#            PR.search_type,
#            PR.additional_notes,
#            RM.media_file_path
#            IA.address_type,
#            IA.street_name,
#            IA.town_or_city,
#            MC.longitude,
#            MC.latitude,
#            PI.number_of_police,
#            PI.obtain_police_info,
#            OI.badge_number,
#            OI.officer_name,
#            OI.police_station
#     FROM stop_search_dev_db.report_data RD 
#         JOIN stop_search_dev_db.reported_by RB
#             ON RD.report_data_id = RB.reported_by_id
#         JOIN stop_search_dev_db.form_type RT
#             ON RB.reported_by_id = RD.report_type_id
#         JOIN stop_search_dev_db.report_date RDate
#             ON RB.reported_by_id = RDate.report_date_id
#         JOIN stop_search_dev_db.victim_information VI
#             ON RD.report_data_id = VI.victim_information_id
#         JOIN stop_search_dev_db.public_relations PR
#             ON RD.report_data_id = PR.public_relations_id
#         JOIN stop_search_dev_db.report_media RM
#             ON PR.public_relations_id = RM.report_media_id
#         JOIN stop_search_dev_db.incident_address IA
#             ON PR.public_relations_id = IA.incident_address_id
#         JOIN stop_search_dev_db.map_coordinates MC
#             ON IA.incident_address_id = MC.map_coordinates_id
#         JOIN stop_search_dev_db.police_information PI
#             ON RD.report_data_id = PI.police_information_id
#         JOIN stop_search_dev_db.officer_information OI
#             ON PI.police_information_id = OI.officer_information_id
#     WHERE RDate.formatted_time = @time;
#     """
#     with app.app_context():
#         session = LocalSession()

#         sql_query = select(
#             ReportData.report_data_id,
#             FormType.report_type,
#             ReportDate.report_date,
#             ReportDate.formatted_day,
#             ReportDate.formatted_weekday,
#             ReportDate.formatted_year,
#             ReportDate.formatted_time,
#             VictimInformation.number_of_victims,
#             VictimInformation.victim_age,
#             VictimInformation.victim_gender,
#             VictimInformation.victim_race,
#             PublicRelations.search_reason,
#             PublicRelations.search_type,
#             PublicRelations.additional_notes,
#             ReportMedia.media_file_path,
#             IncidentAddress.address_type,
#             IncidentAddress.street_name,
#             IncidentAddress.town_or_city,
#             MapCoordinates.longitude,
#             MapCoordinates.latitude,
#             PoliceInformation.number_of_police,
#             PoliceInformation.obtain_police_info,
#             OfficerInformation.badge_number,
#             OfficerInformation.officer_name,
#             OfficerInformation.police_station
#         ).join(
#             ReportedBy, ReportData.report_data_id==ReportData.report_data_id
#         ).join(
#             FormType, ReportedBy.reported_by_id==FormType.reported_by_id
#         ).join(
#             ReportDate, ReportedBy.reported_by_id==ReportDate.report_date_id
#         ).join(
#             VictimInformation, ReportData.report_data_id==VictimInformation.victim_information_id
#         ).join(
#             PublicRelations, ReportData.report_data_id==PublicRelations.public_relations_id
#         ).join(
#             ReportMedia, PublicRelations.public_relations_id==ReportMedia.report_media_id
#         ).join(
#             IncidentAddress, PublicRelations.public_relations_id==IncidentAddress.incident_address_id
#         ).join(
#             MapCoordinates, IncidentAddress.incident_address_id==MapCoordinates.map_coordinates_id
#         ).join(
#             PoliceInformation, ReportData.report_data_id==PoliceInformation.police_information_id
#         ).join(
#             OfficerInformation, PoliceInformation.police_information_id==OfficerInformation.officer_information_id
#         ).where(
#             ReportDate.formatted_time == time
#         )

#         try:
#             data_by_time = session.execute(sql_query).all()
#             return data_by_time
        
#         except Exception as e:
#             return {'SQL Error': e}


def search_all_reports_bespoke(**kwargs):
    """
    Service function to search reports based on dynamic filter criteria.
    
    :param kwargs: Dynamic filter criteria for the search
    :return: List of results matching the filter criteria
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            FormType.report_type,
            ReportDate.report_date,
            ReportDate.formatted_day,
            ReportDate.formatted_week,
            ReportDate.formatted_year,
            ReportDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_gender,
            VictimInformation.victim_race,
            PublicRelations.search_reason,
            PublicRelations.search_type,
            PublicRelations.additional_notes,
            ReportMedia.media_file_path,
            IncidentAddress.address_type,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.lattitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            OfficerInformation.badge_number,
            OfficerInformation.officer_name,
            OfficerInformation.police_station
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.reported_by_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.form_type_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.report_date_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.victim_information_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.public_relations_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.report_media_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.incident_address_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.map_coordinates_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.police_information_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.officer_information_id
        )

        # dynamically apply SQL filters based on kwargs
        if 'report_type' in kwargs:
            sql_query = sql_query.where(FormType.report_type == kwargs['report_type'])

        if 'number_of_victims' in kwargs:
            sql_query = sql_query.where(VictimInformation.number_of_victims == kwargs['number_of_victims'])

        if 'victim_age' in kwargs:
            sql_query = sql_query.where(VictimInformation.victim_age == kwargs['victim_age'])

        if 'victim_gender' in kwargs:
            sql_query = sql_query.where(VictimInformation.victim_gender == kwargs['victim_gender'])

        if 'victim_race' in kwargs:
            sql_query = sql_query.where(VictimInformation.victim_race == kwargs['victim_race'])

        if 'search_reason' in kwargs:
            sql_query = sql_query.where(PublicRelations.search_reason == kwargs['search_reason'])

        if 'search_type' in kwargs:
            sql_query = sql_query.where(PublicRelations.search_type == kwargs['search_type'])

        if 'address_type' in kwargs:
            sql_query = sql_query.where(IncidentAddress.address_type == kwargs['address_type'])

        if 'report_weekday' in kwargs:
            sql_query = sql_query.where(ReportDate.formatted_day == kwargs['report_weekday'])

        try:
            bespoke_search = session.execute(sql_query).all()
            return bespoke_search
        
        except Exception as e:
            return {'SQL Error': e}