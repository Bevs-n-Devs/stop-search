import os
from flask import jsonify, request
from stopSearch import app
from stopSearch.stopSearch_service import search_engine_service


@app.route('/search/all')
def search_all_reports() -> list[dict]:
    results = {
        'Results': []
    }

    with app.app_context():
        get_all_reports = search_engine_service.search_all_reports()
        
        for data in get_all_reports:
            # convert SQL rows into dict objects
            reported_by = dict(
                dataID=data[0],
                reportType=data[1],
                reportDate=data[2],
                reportWeek=data[3],
                reportMonth=data[4],
            )
            
            victim_information = dict(
                numberOfVictims=data[5],
                victimAge=data[6],
                victimGender=data[7],
                victimRace=data[8],
            )
            
            public_relations = dict(
                searchReason=data[9],
                searchType=data[10],
                searchOutcome=data[11],
                additionalNotes=data[12],
                reportMedia=data[13],
                addressType=data[14],
                streetName=data[15],
                townCity=data[16],
                lattitude=data[17],
                longitude=data[18],
            )
            
            police_information = dict(
                numberOfPolice=data[19],
                getPoliceInfo=data[20],
                bodyCameraWorn=data[21],
                badgeNumber=data[22],
                officerName=data[23],
                policeStation=data[24]
            )
            
            # created nested dict of each report category
            reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
            victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
            publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
            policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
            # create dict nested dict object for report results 
            report_data = dict(
                ReportData=[
                    reportedBy,
                    victimInformation,
                    publicRelations,
                    policeInformation
                ]
            )
            results['Results'].append(report_data)

        return jsonify(results)

@app.route('/search/<data_id>')
def search_all_reports_by_data_id(data_id: int):
    data_id = str(data_id)
    results = {
        'Results': []
    }

    with app.app_context():
        get_result = search_engine_service.search_report_by_data_id(data_id) # returns [list (tuple)]
        
        # convert SQL rows into dict objects
        reported_by = dict(
            dataID=get_result[0][0],
            reportType=get_result[0][1],
            reportDate=get_result[0][2],
            reportWeek=get_result[0][3],
            reportMonth=get_result[0][4],
        )
        
        victim_information = dict(
            numberOfVictims=get_result[0][5],
            victimAge=get_result[0][6],
            victimGender=get_result[0][7],
            victimRace=get_result[0][8],
        )
        
        public_relations = dict(
            searchReason=get_result[0][9],
            searchType=get_result[0][10],
            searchOutcome=get_result[0][11],
            additionalNotes=get_result[0][12],
            reportMedia=get_result[0][13],
            addressType=get_result[0][14],
            streetName=get_result[0][15],
            townCity=get_result[0][16],
            lattitude=get_result[0][17],
            longitude=get_result[0][18],
        )
        
        police_information = dict(
            numberOfPolice=get_result[0][19],
            getPoliceInfo=get_result[0][20],
            bodyCameraWorn=get_result[0][21],
            badgeNumber=get_result[0][22],
            officerName=get_result[0][23],
            policeStation=get_result[0][24]
        )
        
         # created nested dict of each report category
        reportedBy = dict(ReportedBy=reported_by)                         
        victimInformation = dict(VictimInformation=victim_information)    
        publicRelations = dict(PublicRelations=public_relations)
        policeInformation = dict(PoliceInformation=police_information)
        
        # create dict nested dict object for report results 
        report_data = dict(
            ReportData=[
                reportedBy,
                victimInformation,
                publicRelations,
                policeInformation
            ]
        )
        results['Results'].append(report_data)
        
        

    return jsonify(results)
        
# TODO: get data by day of the week - Mon, Tues, Wed, Thu, Fri, Sat, Sun
@app.route('/search/day/<day>')
def search_reports_by_day_of_the_week(day: str):
    day = str(day)
    results = {
        'Results': []
    }

    with app.app_context():
        get_result = search_engine_service.search_all_reports_by_day_of_the_week(day)
        
        for data in get_result:
            # convert SQL rows into dict objects
            reported_by = dict(
                dataID=data[0],
                reportType=data[1],
                reportDate=data[2],
                reportWeek=data[3],
                reportMonth=data[4],
            )
            
            victim_information = dict(
                numberOfVictims=data[5],
                victimAge=data[6],
                victimGender=data[7],
                victimRace=data[8],
            )
            
            public_relations = dict(
                searchReason=data[9],
                searchType=data[10],
                searchOutcome=data[11],
                additionalNotes=data[12],
                reportMedia=data[13],
                addressType=data[14],
                streetName=data[15],
                townCity=data[16],
                lattitude=data[17],
                longitude=data[18],
            )
            
            police_information = dict(
                numberOfPolice=data[19],
                getPoliceInfo=data[20],
                bodyCameraWorn=data[21],
                badgeNumber=data[22],
                officerName=data[23],
                policeStation=data[24]
            )
            
            # created nested dict of each report category
            reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
            victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
            publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
            policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
            # create dict nested dict object for report results 
            report_data = dict(
                ReportData=[
                    reportedBy,
                    victimInformation,
                    publicRelations,
                    policeInformation
                ]
            )
            results['Results'].append(report_data)

        return jsonify(results)
    
    
# TODO: get data by month - Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
@app.route('/search/month/<month>')
def search_reports_by_month(month: str):
    month = str(month)
    results = {
        'Results': []
    }

    with app.app_context():
        get_result = search_engine_service.search_all_reports_by_month(month)
        
        for data in get_result:
            # convert SQL rows into dict objects
            reported_by = dict(
                dataID=data[0],
                reportType=data[1],
                reportDate=data[2],
                reportWeek=data[3],
                reportMonth=data[4],
            )
            
            victim_information = dict(
                numberOfVictims=data[5],
                victimAge=data[6],
                victimGender=data[7],
                victimRace=data[8],
            )
            
            public_relations = dict(
                searchReason=data[9],
                searchType=data[10],
                searchOutcome=data[11],
                additionalNotes=data[12],
                reportMedia=data[13],
                addressType=data[14],
                streetName=data[15],
                townCity=data[16],
                lattitude=data[17],
                longitude=data[18],
            )
            
            police_information = dict(
                numberOfPolice=data[19],
                getPoliceInfo=data[20],
                bodyCameraWorn=data[21],
                badgeNumber=data[22],
                officerName=data[23],
                policeStation=data[24]
            )
            
            # created nested dict of each report category
            reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
            victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
            publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
            policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
            # create dict nested dict object for report results 
            report_data = dict(
                ReportData=[
                    reportedBy,
                    victimInformation,
                    publicRelations,
                    policeInformation
                ]
            )
            results['Results'].append(report_data)

        return jsonify(results)
    
    
# # TODO: get data from last 30 days
# @app.route('/search/30days')
# def search_reports_from_last_30_days():
#     results = {
#         'Results': []
#     }

#     with app.app_context():
#         get_result = search_engine_service.search_all_reports_by_last_30_days()

#         for data in get_result:
#             # convert SQL rows into dict objects
#             reported_by = dict(
#                 dataID=data[0],
#                 reportType=data[1],
#                 reportDate=data[2],
#                 reportDay=data[3],
#                 reportWeekday=data[4],
#                 reportYear=data[5],
#                 reportTime=data[6],
#             )
            
#             victim_information = dict(
#                 numberOfVictims=data[7],
#                 victimAge=data[8],
#                 victimGender=data[9],
#                 victimRace=data[10],
#             )
            
#             public_relations = dict(
#                 searchReason=data[11],
#                 searchType=data[12],
#                 searchOutcome=data[13],
#                 additionalNotes=data[14],
#                 reportMedia=data[15],
#                 addressType=data[16],
#                 streetName=data[17],
#                 townCity=data[18],
#                 lattitude=data[19],
#                 longitude=data[20],
#             )
            
#             police_information = dict(
#                 numberOfPolice=data[21],
#                 getPoliceInfo=data[22],
#                 bodyCameraWorn=data[23],
#                 badgeNumber=data[24],
#                 officerName=data[25],
#                 policeStation=data[26]
#             )
            
#             # created nested dict of each report category
#             reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
#             victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
#             publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
#             policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
#             # create dict nested dict object for report results 
#             report_data = dict(
#                 ReportData=[
#                     reportedBy,
#                     victimInformation,
#                     publicRelations,
#                     policeInformation
#                 ]
#             )
#             results['Results'].append(report_data)
        
#         return jsonify(results)

# # TODO: get data from last 60 days
# @app.route('/search/60days')
# def search_reports_from_last_60_days():
#     results = {
#         'Results': []
#     }
    
#     with app.app_context():
#         get_result = search_engine_service.search_all_reports_by_last_60_days()

#         for data in get_result:
#             # convert SQL rows into dict objects
#             reported_by = dict(
#                 dataID=data[0],
#                 reportType=data[1],
#                 reportDate=data[2],
#                 reportDay=data[3],
#                 reportWeekday=data[4],
#                 reportYear=data[5],
#                 reportTime=data[6],
#             )
            
#             victim_information = dict(
#                 numberOfVictims=data[7],
#                 victimAge=data[8],
#                 victimGender=data[9],
#                 victimRace=data[10],
#             )
            
#             public_relations = dict(
#                 searchReason=data[11],
#                 searchType=data[12],
#                 searchOutcome=data[13],
#                 additionalNotes=data[14],
#                 reportMedia=data[15],
#                 addressType=data[16],
#                 streetName=data[17],
#                 townCity=data[18],
#                 lattitude=data[19],
#                 longitude=data[20],
#             )
            
#             police_information = dict(
#                 numberOfPolice=data[21],
#                 getPoliceInfo=data[22],
#                 bodyCameraWorn=data[23],
#                 badgeNumber=data[24],
#                 officerName=data[25],
#                 policeStation=data[26]
#             )
            
#             # created nested dict of each report category
#             reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
#             victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
#             publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
#             policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
#             # create dict nested dict object for report results 
#             report_data = dict(
#                 ReportData=[
#                     reportedBy,
#                     victimInformation,
#                     publicRelations,
#                     policeInformation
#                 ]
#             )
#             results['Results'].append(report_data)
        
#         return jsonify(results)

# # TODO: get data from last 90 days
# @app.route('/search/90days')
# def search_reports_from_last_90_days():
#     results = {
#         'Results': []
#     }
    
#     with app.app_context():
#         get_result = search_engine_service.search_all_reports_by_last_90_days()

#         for data in get_result:
#             # convert SQL rows into dict objects
#             reported_by = dict(
#                 dataID=data[0],
#                 reportType=data[1],
#                 reportDate=data[2],
#                 reportDay=data[3],
#                 reportWeekday=data[4],
#                 reportYear=data[5],
#                 reportTime=data[6],
#             )
            
#             victim_information = dict(
#                 numberOfVictims=data[7],
#                 victimAge=data[8],
#                 victimGender=data[9],
#                 victimRace=data[10],
#             )
            
#             public_relations = dict(
#                 searchReason=data[11],
#                 searchType=data[12],
#                 searchOutcome=data[13],
#                 additionalNotes=data[14],
#                 reportMedia=data[15],
#                 addressType=data[16],
#                 streetName=data[17],
#                 townCity=data[18],
#                 lattitude=data[19],
#                 longitude=data[20],
#             )
            
#             police_information = dict(
#                 numberOfPolice=data[21],
#                 getPoliceInfo=data[22],
#                 bodyCameraWorn=data[23],
#                 badgeNumber=data[24],
#                 officerName=data[25],
#                 policeStation=data[26]
#             )
            
#             # created nested dict of each report category
#             reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
#             victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
#             publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
#             policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
#             # create dict nested dict object for report results 
#             report_data = dict(
#                 ReportData=[
#                     reportedBy,
#                     victimInformation,
#                     publicRelations,
#                     policeInformation
#                 ]
#             )
#             results['Results'].append(report_data)
        
#         return jsonify(results)

# # TODO: get data from last 6 months
# @app.route('/search/6months')
# def search_reports_from_last_6_months():
#     results = {
#         'Results': []
#     }
    
#     with app.app_context():
#         get_result = search_engine_service.search_all_reports_by_last_6_months()

#         for data in get_result:
#             # convert SQL rows into dict objects
#             reported_by = dict(
#                 dataID=data[0],
#                 reportType=data[1],
#                 reportDate=data[2],
#                 reportDay=data[3],
#                 reportWeekday=data[4],
#                 reportYear=data[5],
#                 reportTime=data[6],
#             )
            
#             victim_information = dict(
#                 numberOfVictims=data[7],
#                 victimAge=data[8],
#                 victimGender=data[9],
#                 victimRace=data[10],
#             )
            
#             public_relations = dict(
#                 searchReason=data[11],
#                 searchType=data[12],
#                 searchOutcome=data[13],
#                 additionalNotes=data[14],
#                 reportMedia=data[15],
#                 addressType=data[16],
#                 streetName=data[17],
#                 townCity=data[18],
#                 lattitude=data[19],
#                 longitude=data[20],
#             )
            
#             police_information = dict(
#                 numberOfPolice=data[21],
#                 getPoliceInfo=data[22],
#                 bodyCameraWorn=data[23],
#                 badgeNumber=data[24],
#                 officerName=data[25],
#                 policeStation=data[26]
#             )
            
#             # created nested dict of each report category
#             reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
#             victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
#             publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
#             policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
#             # create dict nested dict object for report results 
#             report_data = dict(
#                 ReportData=[
#                     reportedBy,
#                     victimInformation,
#                     publicRelations,
#                     policeInformation
#                 ]
#             )
#             results['Results'].append(report_data)
        
#         return jsonify(results)

# # TODO: get data from last 1 year
# @app.route('/search/1year')
# def search_reports_from_last_1_year():
#     results = {
#         'Results': []
#     }
    
#     with app.app_context():
#         get_result = search_engine_service.search_all_reports_by_last_12_months()

#         for data in get_result:
#             # convert SQL rows into dict objects
#             reported_by = dict(
#                 dataID=data[0],
#                 reportType=data[1],
#                 reportDate=data[2],
#                 reportDay=data[3],
#                 reportWeekday=data[4],
#                 reportYear=data[5],
#                 reportTime=data[6],
#             )
            
#             victim_information = dict(
#                 numberOfVictims=data[7],
#                 victimAge=data[8],
#                 victimGender=data[9],
#                 victimRace=data[10],
#             )
            
#             public_relations = dict(
#                 searchReason=data[11],
#                 searchType=data[12],
#                 searchOutcome=data[13],
#                 additionalNotes=data[14],
#                 reportMedia=data[15],
#                 addressType=data[16],
#                 streetName=data[17],
#                 townCity=data[18],
#                 lattitude=data[19],
#                 longitude=data[20],
#             )
            
#             police_information = dict(
#                 numberOfPolice=data[21],
#                 getPoliceInfo=data[22],
#                 bodyCameraWorn=data[23],
#                 badgeNumber=data[24],
#                 officerName=data[25],
#                 policeStation=data[26]
#             )
            
#             # created nested dict of each report category
#             reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
#             victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
#             publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
#             policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
#             # create dict nested dict object for report results 
#             report_data = dict(
#                 ReportData=[
#                     reportedBy,
#                     victimInformation,
#                     publicRelations,
#                     policeInformation
#                 ]
#             )
#             results['Results'].append(report_data)
        
#         return jsonify(results)

# TODO: get data from specified year
@app.route('/search/year/<year>')
def search_reports_from_year(year: int):
    results = {
        'Results': []
    }
    
    with app.app_context():
        get_result = search_engine_service.search_all_reports_by_year(year)

        for data in get_result:
            # convert SQL rows into dict objects
            reported_by = dict(
                dataID=data[0],
                reportType=data[1],
                reportDate=data[2],
                reportWeek=data[3],
                reportMonth=data[4],
            )
            
            victim_information = dict(
                numberOfVictims=data[5],
                victimAge=data[6],
                victimGender=data[7],
                victimRace=data[8],
            )
            
            public_relations = dict(
                searchReason=data[9],
                searchType=data[10],
                searchOutcome=data[11],
                additionalNotes=data[12],
                reportMedia=data[13],
                addressType=data[14],
                streetName=data[15],
                townCity=data[16],
                lattitude=data[17],
                longitude=data[18],
            )
            
            police_information = dict(
                numberOfPolice=data[19],
                getPoliceInfo=data[20],
                bodyCameraWorn=data[21],
                badgeNumber=data[22],
                officerName=data[23],
                policeStation=data[24]
            )
            
            # created nested dict of each report category
            reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
            victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
            publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
            policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
            
            # create dict nested dict object for report results 
            report_data = dict(
                ReportData=[
                    reportedBy,
                    victimInformation,
                    publicRelations,
                    policeInformation
                ]
            )
            results['Results'].append(report_data)
        
        return jsonify(results)

# TODO: dynamic seach route where params are submitted as SQL params for where clause
@app.route('/search/report', methods=['GET'])
def search_report():
    results = {
        'Results': []
    }

    # get query parameters from the request
    sql_query_params = request.args.to_dict()
    try:
        with app.app_context():
            get_result = search_engine_service.search_all_reports_bespoke(**sql_query_params)

            for data in get_result:
                # convert SQL rows into dict objects
                reported_by = dict(
                    dataID=data[0],
                    reportType=data[1],
                    reportDate=data[2],
                    reportWeek=data[3],
                    reportMonth=data[4],
                )
                
                victim_information = dict(
                    numberOfVictims=data[5],
                    victimAge=data[6],
                    victimGender=data[7],
                    victimRace=data[8],
                )
                
                public_relations = dict(
                    searchReason=data[9],
                    searchType=data[10],
                    searchOutcome=data[11],
                    additionalNotes=data[12],
                    reportMedia=data[13],
                    addressType=data[14],
                    streetName=data[15],
                    townCity=data[16],
                    lattitude=data[17],
                    longitude=data[18],
                )
                
                police_information = dict(
                    numberOfPolice=data[19],
                    getPoliceInfo=data[20],
                    bodyCameraWorn=data[21],
                    badgeNumber=data[22],
                    officerName=data[23],
                    policeStation=data[24]
                )
                
                # created nested dict of each report category
                reportedBy = dict(ReportedBy=reported_by)                           # {'ReportedBy': {'dataID': 1},{...}...}
                victimInformation = dict(VictimInformation=victim_information)      # {'VictimInformation': {'numberOfVictims': '10 or more'},{...}...}
                publicRelations = dict(PublicRelations=public_relations)            # {'PublicRelations': {'addressType': 'Manual Address'},{...}...}
                policeInformation = dict(PoliceInformation=police_information)      # {'PoliceInformation': {'numberOfPolice': '15 or more'},{...}...}
                
                # create dict nested dict object for report results 
                report_data = dict(
                    ReportData=[
                        reportedBy,
                        victimInformation,
                        publicRelations,
                        policeInformation
                    ]
                )
                results['Results'].append(report_data)
            
            return jsonify(results)
        
    except Exception as e:
        return jsonify({'Service Function Error': str(e)}), 500
