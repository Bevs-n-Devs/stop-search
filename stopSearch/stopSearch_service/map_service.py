from sqlalchemy import *
from stopSearch import utils, app
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

def get_all_map_data():
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
           OI.police_station,

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

        sql_query = select(ReportData).join(
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