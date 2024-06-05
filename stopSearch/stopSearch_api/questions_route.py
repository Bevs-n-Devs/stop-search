from flask import Flask, jsonify
from stopSearch import app
from stopSearch.stopSearch_service import question_service

@app.route("/questions")
def questions_route() -> list[dict]:
    status = {
        "Status": []
    }
    app_data = {
        "AppData": []
    }
    app_pages = {
        "AppPages": []
    }
    questions = {
        "Questions": []
    }

    reported_by = {
    "ReportedBy": []
    }
    questions["Questions"].append(reported_by)

    victim_information = {
        "VictimInformation": []
    }
    questions["Questions"].append(victim_information)

    police_public_relation = {
        "PolicePublicRelations": []
    }
    questions["Questions"].append(police_public_relation)

    police_information = {
        "PoliceInformation": []
    }
    questions["Questions"].append(police_information)


    all_questions = question_service.get_all_report_questions()

    # question 1
    question_email = {
        f"question_{all_questions[0].question_id}": f"{all_questions[0].question_name}"
    }
    questions["Questions"][0]["ReportedBy"].append(question_email)

    # question 2
    confirm_email = {
        f"question_{all_questions[1].question_id}": f"{all_questions[1].question_name}"
    }
    questions["Questions"][0]["ReportedBy"].append(confirm_email)

    # question 3
    question_report_type = {
        f"question_{all_questions[2].question_id}": f"{all_questions[2].question_name}",
        "select_options": [],
    }
    questions["Questions"][0]["ReportedBy"].append(question_report_type)

    report_type_options = question_service.get_report_type_options()
    question_report_type_options = {
        f"option_{report_type_options[0].question_report_type_id}": f"{report_type_options[0].report_type_options}"
    }
    question_report_type["select_options"].append(question_report_type_options)

    question_report_type_options_2 = {
        f"option_{report_type_options[1].question_report_type_id}": f"{report_type_options[1].report_type_options}"
    }
    question_report_type["select_options"].append(question_report_type_options_2)

    # question 4
    question_incident_date = {
        f"question_{all_questions[3].question_id}": f"{all_questions[3].question_name}",
        
    }
    questions["Questions"][0]["ReportedBy"].append(question_incident_date)

    # question 5
    incident_location = {
        f"question_{all_questions[4].question_id}": f"{all_questions[4].question_name}",
        "select_options": [],
    }
    questions["Questions"][2]["PolicePublicRelations"].append(incident_location)
    # get list of options
    location_report_options = question_service.get_location_type_options()
    for item in location_report_options:
        question_location_type_options = {
            f"option_{item.question_location_type_id}": f"{item.location_type_options}"
        }
        incident_location["select_options"].append(question_location_type_options)

    # question 6
    victims_involved = {
        f"question_{all_questions[5].question_id}": f"{all_questions[5].question_name}",
        "select_options": [],
    }
    questions["Questions"][1]["VictimInformation"].append(victims_involved)

    victims_involved_options = question_service.get_victims_involved_options()
    for item in victims_involved_options:
        question_victims_involved_options = {
            f"option_{item.question_victims_involved_id}": f"{item.victims_involved_options}"
        }
        victims_involved["select_options"].append(question_victims_involved_options)

    # question 7
    number_of_police = {
        f"question_{all_questions[6].question_id}": f"{all_questions[6].question_name}",
        "select_options": [],
    }
    questions["Questions"][3]["PoliceInformation"].append(number_of_police)

    number_of_police_options = question_service.get_number_of_police_options()
    for item in number_of_police_options:
        question_number_of_police_options = {
            f"option_{item.question_number_of_police_id}": f"{item.number_of_police_options}"
        }
        number_of_police["select_options"].append(question_number_of_police_options)

    # question 8
    search_reason = {
        f"question_{all_questions[7].question_id}": f"{all_questions[7].question_name}",
        "select_options": [],
    }
    questions["Questions"][2]["PolicePublicRelations"].append(search_reason)

    search_reason_options = question_service.get_search_reason_options()
    for item in search_reason_options:
        question_search_reason_options = {
            f"option_{item.question_search_reason_id}": f"{item.search_reason_options}"
        }
        search_reason["select_options"].append(question_search_reason_options)

    # question 9
    search_type = {
        f"question_{all_questions[8].question_id}": f"{all_questions[8].question_name}",
        "select_options": [],
    }
    questions["Questions"][2]["PolicePublicRelations"].append(search_type)

    search_type_options = question_service.get_search_type_options()
    for item in search_type_options:
        question_search_type_options = {
            f"option_{item.question_search_type_id}": f"{item.search_type_options}"
        }
        search_type["select_options"].append(question_search_type_options)

    # question 10
    get_police_details = {
        f"question_{all_questions[9].question_id}": f"{all_questions[9].question_name}",
        "select_options": [],
    }
    questions["Questions"][3]["PoliceInformation"].append(get_police_details)

    yes_no_options1 = {
        "option_1": "yes"
    }
    get_police_details["select_options"].append(yes_no_options1)

    yes_no_options2 = {
        "option_2": "no"
    }
    get_police_details["select_options"].append(yes_no_options2)

    # question 11
    police_officer_info = {
        f"question_{all_questions[10].question_id}": f"{all_questions[10].question_name}",
    }
    questions["Questions"][3]["PoliceInformation"].append(police_officer_info)
    
    # question 12
    victim_age = {
        f"question_{all_questions[11].question_id}": f"{all_questions[11].question_name}",
        "select_options": [],
    }
    questions["Questions"][1]["VictimInformation"].append(victim_age)

    victim_age_options = question_service.get_victim_age_options()
    for item in victim_age_options:
        question_victim_age_options = {
            f"option_{item.question_victim_age_id}": f"{item.victim_age_options}"
        }
        victim_age["select_options"].append(question_victim_age_options)

    # question 13
    victim_gender = {
        f"question_{all_questions[12].question_id}": f"{all_questions[12].question_name}",
        "select_options": [],
    }
    questions["Questions"][1]["VictimInformation"].append(victim_gender)

    victim_gender_options = question_service.get_victim_gender_options()
    for item in victim_gender_options:
        question_victim_gender_options = {
            f"option_{item.question_victim_gender_id}": f"{item.victim_gender_options}"
        }
        victim_gender["select_options"].append(question_victim_gender_options)

    # question 14
    victim_race = {
        f"question_{all_questions[13].question_id}": f"{all_questions[13].question_name}",
        "select_options": [],
    }
    questions["Questions"][1]["VictimInformation"].append(victim_race)

    victim_race_options = question_service.get_victim_race_options()
    for item in victim_race_options:
        question_victim_race_options = {
            f"option_{item.question_victim_race_id}": f"{item.victim_race_options}"
        }
        victim_race["select_options"].append(question_victim_race_options)

    # question 15
    additional_notes = {
        f"question_{all_questions[14].question_id}": f"{all_questions[14].question_name}"
    }
    questions["Questions"][2]["PolicePublicRelations"].append(additional_notes)

    # question 16
    upload_media = {
        f"question_{all_questions[15].question_id}": f"{all_questions[15].question_name}"
    }
    questions["Questions"][2]["PolicePublicRelations"].append(upload_media)

    return jsonify(status, app_data, app_pages, questions)