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
        get_all_reports = search_engine_service.temp_serach()

        for data in get_all_reports:
            result_data = {
                'ReportedBy': {
                    'dataID': data[0],
                    'reportType': data[1],
                    'reportDate': data[2],
                    'reportDay': data[3],
                    'reportWeekday': data[4],
                    'reportYear': data[5],
                    'reportTime': data[6],
                },
                'VictimInformation': {
                    'numberOfVictims': data[7],
                    'victimAge': data[8],
                    'victimGender': data[9],
                    'victimRace': data[10],
                },
                'PublicRelations': {
                    'searchReason': data[11],
                    'searchType': data[12],
                    'additionalNotes': data[13],
                    'reportMedia': data[14],
                    'addressType': data[15],
                    'streetName': data[16],
                    'townCity': data[17],
                    'lattitude': data[18],
                    'longitude': data[19],
                },
                'PoliceInformation': {
                    'numberOfPolice': data[20],
                    'getPoliceInfo': data[21],
                    'badgeNumber': data[22],
                    'officerName': data[23],
                    'policeStation': data[24]
                }
            }
            results['Results'].append(result_data)
    
        
        return jsonify(results)

@app.route('/search/<data_id>')
def search_all_reports_by_data_id(data_id: int):
    data_id = str(data_id)
    results = {
        'Results': []
    }

    with app.app_context():
        get_result = search_engine_service.search_report_by_data_id(data_id)

        result_data = {
                'ReportedBy': {
                    'dataID': get_result[0],
                    'reportType': get_result[1],
                    'reportDate': get_result[2],
                    'reportDay': get_result[3],
                    'reportWeekday': get_result[4],
                    'reportYear': get_result[5],
                    'reportTime': get_result[6],
                },
                'VictimInformation': {
                    'numberOfVictims': get_result[7],
                    'victimAge': get_result[8],
                    'victimGender': get_result[9],
                    'victimRace': get_result[10],
                },
                'PublicRelations': {
                    'searchReason': get_result[11],
                    'searchType': get_result[12],
                    'additionalNotes': get_result[13],
                    'reportMedia': get_result[14],
                    'addressType': get_result[15],
                    'streetName': get_result[16],
                    'townCity': get_result[17],
                    'lattitude': get_result[18],
                    'longitude': get_result[19],
                },
                'PoliceInformation': {
                    'numberOfPolice': get_result[20],
                    'getPoliceInfo': get_result[21],
                    'badgeNumber': get_result[22],
                    'officerName': get_result[23],
                    'policeStation': get_result[24]
                }
            }
        
        results['Results'].append(result_data)
        
        return jsonify(results)