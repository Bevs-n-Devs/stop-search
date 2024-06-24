from stopSearch import utils, app
from sqlalchemy import *
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


def search_all_reports():
    """
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
        JOIN stop_search_dev_db.report_type RT
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
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}


def search_report_by_data_id(data_id: int):
    """
    SET @dataID = :report_data_id;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE RD.reported_by_id = @dataID;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            ReportData.report_data_id == data_id
        )

        try:
            data_by_id = session.execute(sql_query).first()
            return data_by_id
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_report_type(report_type: str):
    """
    SET @reportType = :report_type;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE RT.report_type = @reportType;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            ReportType.report_type == report_type
        )
    try:
        data_report_type = session.execute(sql_query).all()
        return data_report_type
        
    except Exception as e:
        return {'SQL Error': e}


def search_all_reports_by_last_30_days():
    """
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE (Rdate.formatted_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH))
          AND (RDate.formatted_year = YEAR(DATE_SUB(CURDATE(), INTERVAL 1 MONTH)));
    """
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= one_month_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_last_90_days():
    """
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE (Rdate.formatted_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH))
          AND (RDate.formatted_year = YEAR(DATE_SUB(CURDATE(), INTERVAL 3 MONTH)));
    """
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= three_months_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_last_6_months():
    """
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE (Rdate.formatted_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH))
          AND (RDate.formatted_year = YEAR(DATE_SUB(CURDATE(), INTERVAL 6 MONTH)));
    """
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= six_months_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_last_12_months():
    """
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE (Rdate.formatted_date >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH))
          AND (RDate.formatted_year = YEAR(DATE_SUB(CURDATE(), INTERVAL 12 MONTH)));
    """
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            (ReportDate.formatted_year == year) &
            (ReportDate.report_date >= twelve_months_ago)
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_victim_age(age: str):
    """
    SET @age = :victim_age;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE VI.victim_age = @age;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            VictimInformation.victim_age == age
        )

        try:
            data_by_victim_age = session.execute(sql_query).all()
            return data_by_victim_age
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_victim_gender(gender: str):
    """
    SET @gender = :victim_gender;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE VI.victim_gender = @gender;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            VictimInformation.victim_gender == gender
        )

        try:
            data_by_victim_gender = session.execute(sql_query).all()
            return data_by_victim_gender
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_victim_race(race: str):
    """
    SET @race = :victim_race;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE VI.victim_race = @race;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            VictimInformation.victim_race == race
        )

        try:
            data_by_victim_race = session.execute(sql_query).all()
            return data_by_victim_race
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_search_type(type_of_search: str):
    """
    SET @searchType = :reason_for_search;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE PR.search_type = @searchType;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            PublicRelations.search_type == type_of_search
        )

        try:
            data_by_search_type = session.execute(sql_query).all()
            return data_by_search_type
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_search_reason(reason_for_search: str):
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
        JOIN stop_search_dev_db.report_type RT
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
        JOIN stop_search_dev_db.report_type RT
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
        JOIN stop_search_dev_db.report_type RT
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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


def search_all_reports_by_number_of_police(police_name: str):
    """
    SET @officerName = :police_name;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE OI.officer_name = @officerName;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            OfficerInformation.officer_name == police_name
        )

        try:
            data_by_officer_name = session.execute(sql_query).all()
            return data_by_officer_name
        
        except Exception as e:
            return {'SQL Error': e}


def search_all_reports_by_address_type(address_type: str):
    """
    SET @addressType = :address_type;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE IA.address_type = @addressType;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            IncidentAddress.address_type == address_type
        )

        try:
            data_by_address_type = session.execute(sql_query).all()
            return data_by_address_type
        
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
        JOIN stop_search_dev_db.report_type RT
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
        JOIN stop_search_dev_db.report_type RT
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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

def search_all_reports_by_formatted_weekday(weekday: str):
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
        JOIN stop_search_dev_db.report_type RT
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
        JOIN stop_search_dev_db.report_type RT
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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


def search_all_reports_by_formatted_year(year: str):
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
        JOIN stop_search_dev_db.report_type RT
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
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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


def search_all_reports_by_formatted_time(time: str):
    """
    SET @time = :time;
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
        JOIN stop_search_dev_db.report_type RT
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
    WHERE RDate.formatted_time = @time;
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            ReportData.report_data_id,
            ReportType.report_type,
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
            ReportType, ReportedBy.reported_by_id==ReportType.reported_by_id
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
            ReportDate.formatted_time == time
        )

        try:
            data_by_time = session.execute(sql_query).all()
            return data_by_time
        
        except Exception as e:
            return {'SQL Error': e}

