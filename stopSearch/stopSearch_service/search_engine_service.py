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

        sql_query = select(                                     # search index:
            distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
            FormType.report_type,                               # 1
            ReportDate.report_date,                             # 2
            ReportDate.formatted_week,                          # 3
            ReportDate.formatted_month,                         # 4
            VictimInformation.number_of_victims,                # 5
            VictimInformation.victim_age,                       # 6
            VictimInformation.victim_gender,                    # 7
            VictimInformation.victim_race,                      # 8
            PublicRelations.search_reason,                      # 9
            PublicRelations.search_type,                        # 10
            PublicRelations.search_outcome,                     # 11
            PublicRelations.additional_notes,                   # 12
            ReportMedia.media_file_path,                        # 13
            IncidentAddress.address_type,                       # 14
            IncidentAddress.street_name,                        # 15
            IncidentAddress.town_or_city,                       # 16
            MapCoordinates.longitude,                           # 17
            MapCoordinates.lattitude,                           # 18
            PoliceInformation.number_of_police,                 # 19
            PoliceInformation.obtain_police_info,               # 20
            PoliceInformation.body_camera,                      # 21
            OfficerInformation.badge_number,                    # 22
            OfficerInformation.officer_name,                    # 23
            OfficerInformation.police_station                   # 24
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
        )

        try:
            all_data = session.execute(sql_query).all()
            
            return all_data
        
        except Exception as e:
            return {'SQL Error': str(e)}



def search_report_by_data_id(data_id: int):
    with app.app_context():
        session = LocalSession()

        sql_query = select(                                     # search index:
            distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
            FormType.report_type,                               # 1
            ReportDate.report_date,                             # 2
            ReportDate.formatted_week,                          # 3
            ReportDate.formatted_month,                         # 4
            VictimInformation.number_of_victims,                # 5
            VictimInformation.victim_age,                       # 6
            VictimInformation.victim_gender,                    # 7
            VictimInformation.victim_race,                      # 8
            PublicRelations.search_reason,                      # 9
            PublicRelations.search_type,                        # 10
            PublicRelations.search_outcome,                     # 11
            PublicRelations.additional_notes,                   # 12
            ReportMedia.media_file_path,                        # 13
            IncidentAddress.address_type,                       # 14
            IncidentAddress.street_name,                        # 15
            IncidentAddress.town_or_city,                       # 16
            MapCoordinates.longitude,                           # 17
            MapCoordinates.lattitude,                           # 18
            PoliceInformation.number_of_police,                 # 19
            PoliceInformation.obtain_police_info,               # 20
            PoliceInformation.body_camera,                      # 21
            OfficerInformation.badge_number,                    # 22
            OfficerInformation.officer_name,                    # 23
            OfficerInformation.police_station                   # 24
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
        ).where(
            ReportData.report_data_id == data_id
        )

        try:
            all_data = session.execute(sql_query).all()
            
            return all_data
        
        except Exception as e:
            return {'SQL Error': str(e)}


def search_all_reports_by_day_of_the_week(day: str):
    with app.app_context():
        session = LocalSession()

        sql_query = select(                                     # search index:
            distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
            FormType.report_type,                               # 1
            ReportDate.report_date,                             # 2
            ReportDate.formatted_week,                          # 3
            ReportDate.formatted_month,                         # 4
            VictimInformation.number_of_victims,                # 5
            VictimInformation.victim_age,                       # 6
            VictimInformation.victim_gender,                    # 7
            VictimInformation.victim_race,                      # 8
            PublicRelations.search_reason,                      # 9
            PublicRelations.search_type,                        # 10
            PublicRelations.search_outcome,                     # 11
            PublicRelations.additional_notes,                   # 12
            ReportMedia.media_file_path,                        # 13
            IncidentAddress.address_type,                       # 14
            IncidentAddress.street_name,                        # 15
            IncidentAddress.town_or_city,                       # 16
            MapCoordinates.longitude,                           # 17
            MapCoordinates.lattitude,                           # 18
            PoliceInformation.number_of_police,                 # 19
            PoliceInformation.obtain_police_info,               # 20
            PoliceInformation.body_camera,                      # 21
            OfficerInformation.badge_number,                    # 22
            OfficerInformation.officer_name,                    # 23
            OfficerInformation.police_station                   # 24
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
        ).where(or_(
            func.lower(ReportDate.formatted_week) == func.lower(day),
            func.lower(ReportDate.formatted_week).contains(func.lower(day)),        # m, mon, mo in mon..
            func.lower(func.lower(day)).contains(ReportDate.formatted_week)         # if mon in monday etc
        ))

        try:
            all_data = session.execute(sql_query).all()
            
            return all_data
        
        except Exception as e:
            return {'SQL Error': str(e)}


def search_all_reports_by_month(month: str):
    with app.app_context():
        session = LocalSession()

        sql_query = select(                                     # search index:
            distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
            FormType.report_type,                               # 1
            ReportDate.report_date,                             # 2
            ReportDate.formatted_week,                          # 3
            ReportDate.formatted_month,                         # 4
            VictimInformation.number_of_victims,                # 5
            VictimInformation.victim_age,                       # 6
            VictimInformation.victim_gender,                    # 7
            VictimInformation.victim_race,                      # 8
            PublicRelations.search_reason,                      # 9
            PublicRelations.search_type,                        # 10
            PublicRelations.search_outcome,                     # 11
            PublicRelations.additional_notes,                   # 12
            ReportMedia.media_file_path,                        # 13
            IncidentAddress.address_type,                       # 14
            IncidentAddress.street_name,                        # 15
            IncidentAddress.town_or_city,                       # 16
            MapCoordinates.longitude,                           # 17
            MapCoordinates.lattitude,                           # 18
            PoliceInformation.number_of_police,                 # 19
            PoliceInformation.obtain_police_info,               # 20
            PoliceInformation.body_camera,                      # 21
            OfficerInformation.badge_number,                    # 22
            OfficerInformation.officer_name,                    # 23
            OfficerInformation.police_station                   # 24
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
        ).where(or_(
            func.lower(ReportDate.formatted_month) == func.lower(month),
            func.lower(func.lower(month)).contains(ReportDate.formatted_month),        # if aug in august etc
            func.lower(ReportDate.formatted_month).contains(func.lower(month))         # if a, au, aug in aug.. 
        ))

        try:
            all_data = session.execute(sql_query).all()
            
            return all_data
        
        except Exception as e:
            return {'SQL Error': str(e)}


# def search_all_reports_by_last_30_days():

#     with app.app_context():
#         import datetime

#         session = LocalSession()

#         # calculate date 1 month ago
#         today = datetime.datetime.now()
#         one_month_ago = today - datetime.timedelta(days=1*30) # 30 days for each month

#         # adjust year if necessary
#         if today.month <= 1: # If current month is Jan
#             year = today.year - 1
#         else:
#             year = today.year
        
#         sql_query = select(                                     # search index:
#             distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
#             FormType.report_type,                               # 1
#             ReportDate.report_date,                             # 2
#             ReportDate.formatted_day,                           # 3
#             ReportDate.formatted_week,                          # 4
#             ReportDate.formatted_year,                          # 5
#             ReportDate.formatted_time,                          # 6
#             VictimInformation.number_of_victims,                # 7
#             VictimInformation.victim_age,                       # 8
#             VictimInformation.victim_gender,                    # 9
#             VictimInformation.victim_race,                      # 10
#             PublicRelations.search_reason,                      # 11
#             PublicRelations.search_type,                        # 12
#             PublicRelations.search_outcome,                     # 13
#             PublicRelations.additional_notes,                   # 14
#             ReportMedia.media_file_path,                        # 15
#             IncidentAddress.address_type,                       # 16
#             IncidentAddress.street_name,                        # 17
#             IncidentAddress.town_or_city,                       # 18
#             MapCoordinates.longitude,                           # 19
#             MapCoordinates.lattitude,                           # 20
#             PoliceInformation.number_of_police,                 # 21
#             PoliceInformation.obtain_police_info,               # 22
#             PoliceInformation.body_camera,                      # 23
#             OfficerInformation.badge_number,                    # 24
#             OfficerInformation.officer_name,                    # 25
#             OfficerInformation.police_station                   # 26
#         ).join(
#             ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
#         ).join(
#             FormType, ReportedBy.reported_by_id == FormType.reported_by_id
#         ).join(
#             ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
#         ).join(
#             VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
#         ).join(
#             PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
#         ).join(
#             ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
#         ).join(
#             IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
#         ).join(
#             MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
#         ).join(
#             PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
#         ).join(
#             OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
#         ).where(
#             (ReportDate.formatted_year == year) &
#             (ReportDate.report_date >= one_month_ago)
#         )

#         try:
#             all_data = session.execute(sql_query).all()
#             return all_data
        
#         except Exception as e:
#             return {'SQL Error': e}
        

# def search_all_reports_by_last_60_days():

#     with app.app_context():
#         import datetime

#         session = LocalSession()

#         # calculate date 2 months ago 60 days
#         today = datetime.datetime.now()
#         two_months_ago = today - datetime.timedelta(days=2*30) # 30 days for each month

#         # adjust year if necessary
#         if today.month <= 1: # If current month is Jan
#             year = today.year - 1
#         else:
#             year = today.year
        
#         sql_query = select(                                     # search index:
#             distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
#             FormType.report_type,                               # 1
#             ReportDate.report_date,                             # 2
#             ReportDate.formatted_day,                           # 3
#             ReportDate.formatted_week,                          # 4
#             ReportDate.formatted_year,                          # 5
#             ReportDate.formatted_time,                          # 6
#             VictimInformation.number_of_victims,                # 7
#             VictimInformation.victim_age,                       # 8
#             VictimInformation.victim_gender,                    # 9
#             VictimInformation.victim_race,                      # 10
#             PublicRelations.search_reason,                      # 11
#             PublicRelations.search_type,                        # 12
#             PublicRelations.search_outcome,                     # 13
#             PublicRelations.additional_notes,                   # 14
#             ReportMedia.media_file_path,                        # 15
#             IncidentAddress.address_type,                       # 16
#             IncidentAddress.street_name,                        # 17
#             IncidentAddress.town_or_city,                       # 18
#             MapCoordinates.longitude,                           # 19
#             MapCoordinates.lattitude,                           # 20
#             PoliceInformation.number_of_police,                 # 21
#             PoliceInformation.obtain_police_info,               # 22
#             PoliceInformation.body_camera,                      # 23
#             OfficerInformation.badge_number,                    # 24
#             OfficerInformation.officer_name,                    # 25
#             OfficerInformation.police_station                   # 26
#         ).join(
#             ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
#         ).join(
#             FormType, ReportedBy.reported_by_id == FormType.reported_by_id
#         ).join(
#             ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
#         ).join(
#             VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
#         ).join(
#             PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
#         ).join(
#             ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
#         ).join(
#             IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
#         ).join(
#             MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
#         ).join(
#             PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
#         ).join(
#             OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
#         ).where(
#             (ReportDate.formatted_year == year) &
#             (ReportDate.report_date >= two_months_ago)
#         )

#         try:
#             all_data = session.execute(sql_query).all()
#             return all_data
        
#         except Exception as e:
#             return {'SQL Error': e}


# def search_all_reports_by_last_90_days():

#     with app.app_context():
#         import datetime

#         session = LocalSession()

#         # calculate date 3 month ago
#         today = datetime.datetime.now()
#         three_months_ago = today - datetime.timedelta(days=3*30) # 30 days for each month

#         # adjust year if necessary
#         if today.month <= 3: 
#             year = today.year - 1 # If current month is Jan, Feb, Mar
#         else:
#             year = today.year

#         sql_query = select(                                     # search index:
#             distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
#             FormType.report_type,                               # 1
#             ReportDate.report_date,                             # 2
#             ReportDate.formatted_day,                           # 3
#             ReportDate.formatted_week,                          # 4
#             ReportDate.formatted_year,                          # 5
#             ReportDate.formatted_time,                          # 6
#             VictimInformation.number_of_victims,                # 7
#             VictimInformation.victim_age,                       # 8
#             VictimInformation.victim_gender,                    # 9
#             VictimInformation.victim_race,                      # 10
#             PublicRelations.search_reason,                      # 11
#             PublicRelations.search_type,                        # 12
#             PublicRelations.search_outcome,                     # 13
#             PublicRelations.additional_notes,                   # 14
#             ReportMedia.media_file_path,                        # 15
#             IncidentAddress.address_type,                       # 16
#             IncidentAddress.street_name,                        # 17
#             IncidentAddress.town_or_city,                       # 18
#             MapCoordinates.longitude,                           # 19
#             MapCoordinates.lattitude,                           # 20
#             PoliceInformation.number_of_police,                 # 21
#             PoliceInformation.obtain_police_info,               # 22
#             PoliceInformation.body_camera,                      # 23
#             OfficerInformation.badge_number,                    # 24
#             OfficerInformation.officer_name,                    # 25
#             OfficerInformation.police_station                   # 26
#         ).join(
#             ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
#         ).join(
#             FormType, ReportedBy.reported_by_id == FormType.reported_by_id
#         ).join(
#             ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
#         ).join(
#             VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
#         ).join(
#             PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
#         ).join(
#             ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
#         ).join(
#             IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
#         ).join(
#             MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
#         ).join(
#             PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
#         ).join(
#             OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
#         ).where(
#             (ReportDate.formatted_year == year) &
#             (ReportDate.report_date >= three_months_ago)
#         )

#         try:
#             all_data = session.execute(sql_query).all()
#             return all_data
        
#         except Exception as e:
#             return {'SQL Error': e}


# def search_all_reports_by_last_6_months():

#     with app.app_context():
#         import datetime

#         session = LocalSession()

#         # calculate date 6 month ago
#         today = datetime.datetime.now()
#         six_months_ago = today - datetime.timedelta(days= 6*30) # 30 days for each month

#         # adjust year if necessary
#         if today.month <= 6: 
#             year = today.year - 1 # If current month is Jan, Feb, Mar
#         else:
#             year = today.year

#         sql_query = select(                                     # search index:
#             distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
#             FormType.report_type,                               # 1
#             ReportDate.report_date,                             # 2
#             ReportDate.formatted_day,                           # 3
#             ReportDate.formatted_week,                          # 4
#             ReportDate.formatted_year,                          # 5
#             ReportDate.formatted_time,                          # 6
#             VictimInformation.number_of_victims,                # 7
#             VictimInformation.victim_age,                       # 8
#             VictimInformation.victim_gender,                    # 9
#             VictimInformation.victim_race,                      # 10
#             PublicRelations.search_reason,                      # 11
#             PublicRelations.search_type,                        # 12
#             PublicRelations.search_outcome,                     # 13
#             PublicRelations.additional_notes,                   # 14
#             ReportMedia.media_file_path,                        # 15
#             IncidentAddress.address_type,                       # 16
#             IncidentAddress.street_name,                        # 17
#             IncidentAddress.town_or_city,                       # 18
#             MapCoordinates.longitude,                           # 19
#             MapCoordinates.lattitude,                           # 20
#             PoliceInformation.number_of_police,                 # 21
#             PoliceInformation.obtain_police_info,               # 22
#             PoliceInformation.body_camera,                      # 23
#             OfficerInformation.badge_number,                    # 24
#             OfficerInformation.officer_name,                    # 25
#             OfficerInformation.police_station                   # 26
#         ).join(
#             ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
#         ).join(
#             FormType, ReportedBy.reported_by_id == FormType.reported_by_id
#         ).join(
#             ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
#         ).join(
#             VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
#         ).join(
#             PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
#         ).join(
#             ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
#         ).join(
#             IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
#         ).join(
#             MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
#         ).join(
#             PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
#         ).join(
#             OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
#         ).where(
#             (ReportDate.formatted_year == year) &
#             (ReportDate.report_date >= six_months_ago)
#         )

#         try:
#             all_data = session.execute(sql_query).all()
#             return all_data
        
#         except Exception as e:
#             return {'SQL Error': e}


# def search_all_reports_by_last_12_months():
    
#     with app.app_context():
#         import datetime

#         session = LocalSession()

#         # calculate date 12 month ago
#         today = datetime.datetime.now()
#         twelve_months_ago = today - datetime.timedelta(days= 12*30) # 30 days for each month

#         # adjust year if necessary
#         if today.month <= 12: 
#             year = today.year - 1 # If current month is Jan, Feb, Mar .... Dec
#         else:
#             year = today.year

#         sql_query = select(                                     # search index:
#             distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
#             FormType.report_type,                               # 1
#             ReportDate.report_date,                             # 2
#             ReportDate.formatted_day,                           # 3
#             ReportDate.formatted_week,                          # 4
#             ReportDate.formatted_year,                          # 5
#             ReportDate.formatted_time,                          # 6
#             VictimInformation.number_of_victims,                # 7
#             VictimInformation.victim_age,                       # 8
#             VictimInformation.victim_gender,                    # 9
#             VictimInformation.victim_race,                      # 10
#             PublicRelations.search_reason,                      # 11
#             PublicRelations.search_type,                        # 12
#             PublicRelations.search_outcome,                     # 13
#             PublicRelations.additional_notes,                   # 14
#             ReportMedia.media_file_path,                        # 15
#             IncidentAddress.address_type,                       # 16
#             IncidentAddress.street_name,                        # 17
#             IncidentAddress.town_or_city,                       # 18
#             MapCoordinates.longitude,                           # 19
#             MapCoordinates.lattitude,                           # 20
#             PoliceInformation.number_of_police,                 # 21
#             PoliceInformation.obtain_police_info,               # 22
#             PoliceInformation.body_camera,                      # 23
#             OfficerInformation.badge_number,                    # 24
#             OfficerInformation.officer_name,                    # 25
#             OfficerInformation.police_station                   # 26
#         ).join(
#             ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
#         ).join(
#             FormType, ReportedBy.reported_by_id == FormType.reported_by_id
#         ).join(
#             ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
#         ).join(
#             VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
#         ).join(
#             PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
#         ).join(
#             ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
#         ).join(
#             IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
#         ).join(
#             MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
#         ).join(
#             PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
#         ).join(
#             OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
#         ).where(
#             (ReportDate.formatted_year == year) &
#             (ReportDate.report_date >= twelve_months_ago)
#         )

#         try:
#             all_data = session.execute(sql_query).all()
#             return all_data
        
#         except Exception as e:
#             return {'SQL Error': e}
        

def search_all_reports_by_year(year: int):
    with app.app_context():
        session = LocalSession()

        # convert int year to str
        year = str(year)

        sql_query = select(                                     # search index:
            distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
            FormType.report_type,                               # 1
            ReportDate.report_date,                             # 2
            ReportDate.formatted_week,                          # 3
            ReportDate.formatted_month,                         # 4
            VictimInformation.number_of_victims,                # 5
            VictimInformation.victim_age,                       # 6
            VictimInformation.victim_gender,                    # 7
            VictimInformation.victim_race,                      # 8
            PublicRelations.search_reason,                      # 9
            PublicRelations.search_type,                        # 10
            PublicRelations.search_outcome,                     # 11
            PublicRelations.additional_notes,                   # 12
            ReportMedia.media_file_path,                        # 13
            IncidentAddress.address_type,                       # 14
            IncidentAddress.street_name,                        # 15
            IncidentAddress.town_or_city,                       # 16
            MapCoordinates.longitude,                           # 17
            MapCoordinates.lattitude,                           # 18
            PoliceInformation.number_of_police,                 # 19
            PoliceInformation.obtain_police_info,               # 20
            PoliceInformation.body_camera,                      # 21
            OfficerInformation.badge_number,                    # 22
            OfficerInformation.officer_name,                    # 23
            OfficerInformation.police_station                   # 24
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
        ).where(
            ReportDate.report_date.contains(year) 
        )

        try:
            all_data = session.execute(sql_query).all()
            return all_data
        
        except Exception as e:
            return {'SQL Error': e}
        

def search_all_reports_bespoke(**kwargs):
    """
    Service function to search reports based on dynamic filter criteria.
    
    :param kwargs: Dynamic filter criteria for the search
    :return: List of results matching the filter criteria
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(                                     # search index:
            distinct(ReportData.report_data_id),                # 0  DISTINCT clause reduces duplicate report_data_id responses
            FormType.report_type,                               # 1
            ReportDate.report_date,                             # 2
            ReportDate.formatted_week,                          # 3
            ReportDate.formatted_month,                         # 4
            VictimInformation.number_of_victims,                # 5
            VictimInformation.victim_age,                       # 6
            VictimInformation.victim_gender,                    # 7
            VictimInformation.victim_race,                      # 8
            PublicRelations.search_reason,                      # 9
            PublicRelations.search_type,                        # 10
            PublicRelations.search_outcome,                     # 11
            PublicRelations.additional_notes,                   # 12
            ReportMedia.media_file_path,                        # 13
            IncidentAddress.address_type,                       # 14
            IncidentAddress.street_name,                        # 15
            IncidentAddress.town_or_city,                       # 16
            MapCoordinates.longitude,                           # 17
            MapCoordinates.lattitude,                           # 18
            PoliceInformation.number_of_police,                 # 19
            PoliceInformation.obtain_police_info,               # 20
            PoliceInformation.body_camera,                      # 21
            OfficerInformation.badge_number,                    # 22
            OfficerInformation.officer_name,                    # 23
            OfficerInformation.police_station                   # 24
        ).join(
            ReportedBy, ReportData.report_data_id == ReportedBy.report_data_id
        ).join(
            FormType, ReportedBy.reported_by_id == FormType.reported_by_id
        ).join(
            ReportDate, ReportedBy.reported_by_id == ReportDate.reported_by_id
        ).join(
            VictimInformation, ReportData.report_data_id == VictimInformation.report_data_id
        ).join(
            PublicRelations, ReportData.report_data_id == PublicRelations.report_data_id
        ).join(
            ReportMedia, PublicRelations.public_relations_id == ReportMedia.public_relations_id
        ).join(
            IncidentAddress, PublicRelations.public_relations_id == IncidentAddress.public_relations_id
        ).join(
            MapCoordinates, IncidentAddress.incident_address_id == MapCoordinates.incident_address_id
        ).join(
            PoliceInformation, ReportData.report_data_id == PoliceInformation.report_data_id
        ).join(
            OfficerInformation, PoliceInformation.police_information_id == OfficerInformation.police_information_id
        )

        # dynamically apply SQL filters based on kwargs
        if 'dataID' in kwargs:
            sql_query = sql_query.where(ReportData.report_data_id == kwargs['dataID'])
        
        if 'reportType' in kwargs:
            sql_query = sql_query.where(func.lower(FormType.report_type) == func.lower(kwargs['reportType']))

        if 'numberOfVictims' in kwargs:
            sql_query = sql_query.where(VictimInformation.number_of_victims == kwargs['numberOfVictims'])

        if 'victimAge' in kwargs:
            # TODO: Create logic to process single int and convert to age range
            #       16 ->  15 - 17, 12 -> 14 or Under, 27 -> 25 - 50 etc  (utility function)
            sql_query = sql_query.where(VictimInformation.victim_age == kwargs['victimAge'])

        if 'victimGender' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(VictimInformation.victim_gender) == func.lower(kwargs['victimGender']),
                func.lower(VictimInformation.victim_gender).contains(func.lower(kwargs['victimGender'])),
            ))

        if 'victimRace' in kwargs:
            # this will check if victimRace is exact exact macth or partial match.
            sql_query = sql_query.where(or_(
                func.lower(VictimInformation.victim_race) == func.lower(kwargs['victimRace']),
                func.lower(VictimInformation.victim_race).contains(func.lower(kwargs['victimRace']))
            ))

        if 'searchReason' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(PublicRelations.search_reason) == func.lower(kwargs['searchReason']),
                func.lower(PublicRelations.search_reason).contains(func.lower(kwargs['searchReason']))
            ))
            
        if 'searchOutcome' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(PublicRelations.search_outcome) == func.lower(kwargs['saerchOutcome']),
                func.lower(PublicRelations.search_outcome).contains(func.lower(kwargs['saerchOutcome']))
            ))

        if 'searchType' in kwargs:
            sql_query = sql_query.where(func.lower(PublicRelations.search_type) == func.lower(kwargs['searchType']))

        if 'addressType' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(IncidentAddress.address_type) == func.lower(kwargs['addressType']),
                func.lower(IncidentAddress.address_type).contains(func.lower(kwargs['addressType']))
            ))

        if 'reportWeekday' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(ReportDate.formatted_week) == func.lower(kwargs['reportWeekday']),
                func.lower(ReportDate.formatted_week).contains(func.lower(kwargs['reportWeekday'])),
                func.lower(kwargs['reportWeekday']).contains(func.lower(ReportDate.formatted_week)),
            ))
            
        if 'reportWeek' in kwargs:
            sql_query = sql_query.where(or_(
            func.lower(ReportDate.formatted_week) == func.lower(kwargs['reportWeek']),
            func.lower(ReportDate.formatted_week).contains(func.lower(kwargs['reportWeek'])),
            func.lower(kwargs['reportWeek']).contains(func.lower(ReportDate.formatted_week)),
        ))
        
        if 'reportMonth' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(ReportDate.formatted_month) == func.lower(kwargs['reportMonth']),
                func.lower(ReportDate.formatted_month).contains(func.lower(kwargs['reportMonth'])),
                func.lower(kwargs['reportMonth']).contains(func.lower(ReportDate.formatted_month))
            ))
            
        if 'reportYear' in kwargs:
            sql_query = sql_query.where(ReportDate.report_date.contains(kwargs['reportMonth']))

        # add extra filters 
        if 'policeInfo' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(PoliceInformation.obtain_police_info) == func.lower(kwargs['policeInfo']),
                func.lower(PoliceInformation.obtain_police_info).contains(func.lower(kwargs['policeInfo']))
            ))
            
        if 'bodyCamera' in kwargs or 'bodyCameraWorn' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(PoliceInformation.body_camera) == func.lower(kwargs['bodyCamera']),
                func.lower(PoliceInformation.body_camera).contains(func.lower(kwargs['bodyCamera'])),
            ))
            
        if 'bodyCam' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(PoliceInformation.body_camera) == func.lower(kwargs['bodyCam']),
                func.lower(PoliceInformation.body_camera).contains(func.lower(kwargs['bodyCam'])),
            ))
            
        if 'bodyCameraWorn' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(PoliceInformation.body_camera) == func.lower(kwargs['bodyCameraWorn']),
                func.lower(PoliceInformation.body_camera).contains(func.lower(kwargs['bodyCameraWorn'])),
            ))    
            
                
        if 'badgeNumber' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(OfficerInformation.badge_number) == func.lower(kwargs['badgeNumber']),
                func.lower(OfficerInformation.badge_number).contains(kwargs['badgeNumber'])
            ))

        if 'policeStation' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(OfficerInformation.badge_number) == func.lower(kwargs['bapoliceStationgeNumber']),
                func.lower(OfficerInformation.badge_number).contains(kwargs['policeStation'])
            ))

        if 'officerName' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(OfficerInformation.badge_number) == func.lower(kwargs['badgeNumber']),
                func.lower(OfficerInformation.badge_number).contains(kwargs['badgeNumber'])
            ))
        
        if 'streetName' in kwargs:
            sql_query = sql_query.where(or_(
                func.lower(IncidentAddress.street_name) == func.lower(kwargs['streetName']),
                func.lower(IncidentAddress.street_name).contains(func.lower(kwargs['streetName'])),
                func.lower(func.lower(kwargs['streetName'])).contains(IncidentAddress.street_name)
            ))
        
        if 'townOrCity' in kwargs:
            sql_query = sql_query.where(or_(
                 func.lower(IncidentAddress.street_name) == func.lower(kwargs['townOrCity']),
                func.lower(IncidentAddress.street_name).contains(func.lower(kwargs['townOrCity'])),
                func.lower(func.lower(kwargs['townOrCity'])).contains(IncidentAddress.street_name)
            ))


        try:
            bespoke_search = session.execute(sql_query).all()
            return bespoke_search
        
        except Exception as e:
            return {'SQL Error': e}