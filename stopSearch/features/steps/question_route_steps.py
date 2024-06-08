import json
from stopSearch.main import app
from behave import given, when, then 

@given("the questions_route is running")
def step_implimentation(context):
    with app.app_context():
        context.client = app.test_client()
        

@when("a request is made to the questions_route")
def step_impl(context):
    with app.app_context():
        context.endpoint_url = "/questions"
        context.http_response = context.client.get(context.endpoint_url)


@then("the Status information should be displayed.")
def step_impl(context):
    with app.app_context():
        context.response_payload = json.loads(context.http_response.data)
        response_payload = context.response_payload[0]
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        assert ("Status" in response_payload), "Expected Status in payload"


@then("the AppData information should be displayed.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[1]
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        assert ("AppData" in response_payload), "Expected AppData in payload."


@then("the Questions should be in the response.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[3]
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        assert ("Questions" in response_payload), "Expected Questions in payload."


@then("the ReportedBy question objects should be displayed in the Questions response payload in the expected format.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[3]["Questions"][0]

        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["ReportedBy"], list)), "Expected object to be a list"
        assert (len(response_payload["ReportedBy"]) > 0)
        assert (len(response_payload["ReportedBy"][2]["select_options"]) > 0)
        
        assert (isinstance(response_payload["ReportedBy"][0], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["ReportedBy"][1], dict)), "Expected object to be a dictionary"

        assert ("question_1" in response_payload["ReportedBy"][0]), "Expected question_1 to be in ReportedBy response"
        assert ("question_2" in response_payload["ReportedBy"][1]), "Expected question_2 to be in ReportedBy response"
        assert ("question_3" in response_payload["ReportedBy"][2]), "Expected question_3 to be in ReportedBy response"
        assert ("select_options" in response_payload["ReportedBy"][2]), "Expected select_options to be in ReportedBy response"
        assert ("question_4" in response_payload["ReportedBy"][3]), "Expected question_4 to be in ReportedBy response"
        
        assert (response_payload["ReportedBy"][0]["question_1"] == "Please enter your email to start the report:"), "Expected question text to contain: 'Please enter your email to start the report:'"
        assert (response_payload["ReportedBy"][1]["question_2"] == "Please re-enter your email to complete the report:"), "Expected question to contain: 'Please re-enter your email to complete the report:'"
        assert (response_payload["ReportedBy"][2]["question_3"] == "Are you a witness or a victim?"), "Expected question text to contain: 'Are you a witness or a victim?'"
        assert (response_payload["ReportedBy"][2]["select_options"][0]["option_1"] == "witness"), "Expected question option to contain: 'witness'"
        assert (response_payload["ReportedBy"][2]["select_options"][1]["option_2"] == "victim"), "Expected question option to contain: 'victim'"
        assert (response_payload["ReportedBy"][3]["question_4"] == "Enter the date of the incident:"), "Expected question text to contain: 'Enter the date of the incident:'"

        assert (isinstance(response_payload["ReportedBy"][0]["question_1"], str)), "Expected question_1 to be a string"
        assert (isinstance(response_payload["ReportedBy"][1]["question_2"], str)), "Expected question_2 to be a string"
        assert (isinstance(response_payload["ReportedBy"][2]["question_3"], str)), "Expected question_3 to be a string"
        assert (isinstance(response_payload["ReportedBy"][2]["select_options"][0]["option_1"], str)), "Expected question option 'witness' to be a string"
        assert (isinstance(response_payload["ReportedBy"][2]["select_options"][1]["option_2"], str)), "Expected question option 'victim' to be a string"
        assert (isinstance(response_payload["ReportedBy"][3]["question_4"], str)), "Expected question_4 to be a string"


@then("the VictimInformation question objects should be displayed in the Questions response payload in the expected format.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[3]["Questions"][1]

        # check the data type of VictimInformation response object
        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["VictimInformation"], list)), "Expected object to be a list"
        
        # check if VictimInformation response is empty
        assert (len(response_payload["VictimInformation"]) > 0), "Expected more than 1 select options"
        
        # check if select_options for each question is not empty
        assert (len(response_payload["VictimInformation"][0]["select_options"]) > 0), "Expected more than 1 select options for question_6"
        assert (len(response_payload["VictimInformation"][1]["select_options"]) > 0), "Expected more than 1 select options for question_12"
        assert (len(response_payload["VictimInformation"][2]["select_options"]) > 0), "Expected more than 1 select options for question_13"
        assert (len(response_payload["VictimInformation"][3]["select_options"]) > 0), "Expected more than 1 select options for question_14"

        # Check the type of each object within the VictimInformation response
        assert (isinstance(response_payload["VictimInformation"][0], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["VictimInformation"][1], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["VictimInformation"][2], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["VictimInformation"][3], dict)), "Expected object to be a dictionary"

        # check if expected questions are in object block
        assert ("question_6" in response_payload["VictimInformation"][0]), "Expected question_6 to be in VictimInformation response"
        assert ("question_12" in response_payload["VictimInformation"][1]), "Expected question_12 to be in VictimInformation response"
        assert ("question_13" in response_payload["VictimInformation"][2]), "Expected question_13 to be in VictimInformation response"
        assert ("question_14" in response_payload["VictimInformation"][3]), "Expected question_14 to be in VictimInformation response"

        # check the select_options in expected questions
        assert ("select_options" in response_payload["VictimInformation"][0]), "Expected select_options to be in question_6"
        assert ("select_options" in response_payload["VictimInformation"][1]), "Expected select_options to be in question_12"
        assert ("select_options" in response_payload["VictimInformation"][2]), "Expected select_options to be in question_13"
        assert ("select_options" in response_payload["VictimInformation"][3]), "Expected select_options to be in question_14"

        # check if questions are equal to expected questions
        assert (response_payload["VictimInformation"][0]["question_6"] == "How many victim were involved in the incident?"), "Expected question text to contain: 'How many victim were involved in the incident?'"
        assert (response_payload["VictimInformation"][1]["question_12"] == "How old was the person or people involved?"), "Expected question text to contain: How old was the person or people involved?"
        assert (response_payload["VictimInformation"][2]["question_13"] == "What was the gender of the person or people involved?"), "Expected question text to contain: What was the gender of the person or people involved?"
        assert (response_payload["VictimInformation"][3]["question_14"] == "What is the race of the person or people involved?"), "Expected question text to contain: What is the race of the person or people involved?"

        # check if select_options are euqal expected options for each question
        assert (response_payload["VictimInformation"][0]["select_options"][0]["option_1"] == "Unknown"), "Expected question option to contain: 'Unknown'"
        assert (response_payload["VictimInformation"][0]["select_options"][1]["option_2"] == "1"), "Expected question option to contain: '1'"
        assert (response_payload["VictimInformation"][0]["select_options"][11]["option_12"] == "10+"), "Expected question option to contain: '10+'"
        assert (response_payload["VictimInformation"][1]["select_options"][0]["option_1"] == "Unknown"), "Expected question option to contain: 'Unknown'"
        assert (response_payload["VictimInformation"][1]["select_options"][1]["option_2"] == "15 - 17"), "Excpected question option to contain: '15 - 17'"
        assert (response_payload["VictimInformation"][1]["select_options"][8]["option_9"] == "50+"), "Expected question option to contain: '50+'"
        assert (response_payload["VictimInformation"][2]["select_options"][0]["option_1"] == "Unknown"), "Expected question option to contain: 'Unknown'"
        assert (response_payload["VictimInformation"][2]["select_options"][1]["option_2"] == "Man"), "Expected question option to contain: 'Man'"
        assert (response_payload["VictimInformation"][2]["select_options"][8]["option_9"] == "Group from LGBT community"), "Expected question option to contain: 'Group from LGBT community'"
        assert (response_payload["VictimInformation"][3]["select_options"][0]["option_1"] == "Unknown"), "Expected question option to contain: 'Unknown'"
        assert (response_payload["VictimInformation"][3]["select_options"][1]["option_2"] == "Arab"), "Expected question option to contain: 'Arab'"
        assert (response_payload["VictimInformation"][3]["select_options"][9]["option_10"] == "Group of White people"), "Expected question option to contain: 'Group of White people'"
        

        # check the data type of each question & select_option
        assert (isinstance(response_payload["VictimInformation"][0]["question_6"], str)), "Expected question_6 to be a string"
        assert (isinstance(response_payload["VictimInformation"][1]["question_12"], str)), "Expected question_12 to be a string"
        assert (isinstance(response_payload["VictimInformation"][2]["question_13"], str)), "Expected question_13 to be a string"
        assert (isinstance(response_payload["VictimInformation"][3]["question_14"], str)), "Expected question_14 to be a string"

        assert (isinstance(response_payload["VictimInformation"][0]["select_options"][0]["option_1"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][0]["select_options"][1]["option_2"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][0]["select_options"][11]["option_12"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][1]["select_options"][0]["option_1"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][1]["select_options"][1]["option_2"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][1]["select_options"][8]["option_9"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][2]["select_options"][0]["option_1"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][2]["select_options"][1]["option_2"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][2]["select_options"][8]["option_9"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][3]["select_options"][0]["option_1"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][3]["select_options"][1]["option_2"], str)), "Expected question option to be a string"
        assert (isinstance(response_payload["VictimInformation"][3]["select_options"][9]["option_10"], str)), "Expected question option to be a string"


@then("the PolicePublicRelations question objects should be displayed in the Questions response payload in the expected format.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[3]["Questions"][2]

        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["PolicePublicRelations"], list)), "Expected object to be a list"
        
        assert (len(response_payload["PolicePublicRelations"]) > 0), "Expected more than 1 select options" 
        assert (len(response_payload["PolicePublicRelations"][0]["select_options"]) > 0), "Expected more than 1 select options for question_5"
        assert (len(response_payload["PolicePublicRelations"][1]["select_options"]) > 0), "Expected more than 1 select options for question_8"
        assert (len(response_payload["PolicePublicRelations"][2]["select_options"]) > 0), "Expected more than 1 select options for question_9"
        
        assert (isinstance(response_payload["PolicePublicRelations"][0], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["PolicePublicRelations"][1], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["PolicePublicRelations"][2], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["PolicePublicRelations"][3], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["PolicePublicRelations"][4], dict)), "Expected object to be a dictionary"

        assert ("question_5" in response_payload["PolicePublicRelations"][0]), "Expected question_5 to be in PolicePublicRelations response"
        assert ("question_8" in response_payload["PolicePublicRelations"][1]), "Expected question_8 to be in PolicePublicRelations response"
        assert ("question_9" in response_payload["PolicePublicRelations"][2]), "Expected question_9 to be in PolicePublicRelations response"
        assert ("question_15" in response_payload["PolicePublicRelations"][3]), "Expected question_15 to be in PolicePublicRelations response"
        assert ("question_16" in response_payload["PolicePublicRelations"][4]), "Expected question_16 to be in PolicePublicRelations response"

        assert ("select_options" in response_payload["PolicePublicRelations"][0]), "Expected select_options to be in question_5"
        assert ("select_options" in response_payload["PolicePublicRelations"][1]), "Expected select_options to be in question_8"
        assert ("select_options" in response_payload["PolicePublicRelations"][2]), "Expected select_options to be in question_9"
        
        assert (response_payload["PolicePublicRelations"][0]["question_5"] == "Where did this incident happen?"), "Expected question text to contain: 'Where did this incident happen?'"
        assert (response_payload["PolicePublicRelations"][1]["question_8"] == "What was the reason for the stop?"), "Expected question text to contain: 'What was the reason for the stop?'"
        assert (response_payload["PolicePublicRelations"][2]["question_9"] == "Was the search moderate or aggressive?"), "Expected question text to contain: 'Was the search moderate or aggressive?'"
        assert (response_payload["PolicePublicRelations"][3]["question_15"] == "Please add any additional notes here:"), "Expected question text to contain: 'Please add any additional notes here:'"
        assert (response_payload["PolicePublicRelations"][4]["question_16"] == "Please upload any media you have here:"), "Expected question text to contain: 'Please upload any media you have here:'"

        assert (response_payload["PolicePublicRelations"][0]["select_options"][0]["option_1"] == "Automatic Address"), "Expected question option to contain: 'Automatic Address'"
        assert (response_payload["PolicePublicRelations"][0]["select_options"][1]["option_2"] == "Manual Address"), "Expected question option to contain: 'Manual Address'"
        assert (response_payload["PolicePublicRelations"][1]["select_options"][0]["option_1"] == "Unknown"), "Expected question option to contain: 'Unknown'"
        assert (response_payload["PolicePublicRelations"][1]["select_options"][1]["option_2"] == "A police officer has the power to search someone if they have reasonable grounds of:"), "Expected question option to contain: 'A police officer has the power to search someone if they have reasonable grounds of:'"
        assert (response_payload["PolicePublicRelations"][1]["select_options"][9]["option_10" ] == "In a location where crime is high"), "Expected question option to contain: 'In a location where crime is high'"        
        assert (response_payload["PolicePublicRelations"][2]["select_options"][0]["option_1"] == "Unknown"), "Expected question option to contain: 'Unknown'"
        assert (response_payload["PolicePublicRelations"][2]["select_options"][1]["option_2"] == "Moderate"), "Expected question option to contain: 'Moderate'"
        assert (response_payload["PolicePublicRelations"][2]["select_options"][2]["option_3"] == "Aggressive"), "Expected question option to contain: 'Aggressive'"

        assert (isinstance(response_payload["PolicePublicRelations"][0]["question_5"], str)), "Expected question_5 to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][1]["question_8"], str)), "Expected question_8 to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][2]["question_9"], str)), "Expected question_9 to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][3]["question_15"], str)), "Expected question_15 to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][4]["question_16"], str)), "Expected question_16 to be a string"

        assert (isinstance(response_payload["PolicePublicRelations"][0]["select_options"][0]["option_1"], str)), "Expected question_5 option to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][0]["select_options"][1]["option_2"], str)), "Expected question_5 option to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][1]["select_options"][0]["option_1"], str)), "Expected question_8 option to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][1]["select_options"][1]["option_2"], str)), "Expected question_8 option to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][1]["select_options"][9]["option_10"], str)), "Expected question_8 option to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][2]["select_options"][0]["option_1"], str)), "Expected question_8 option to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][2]["select_options"][1]["option_2"], str)), "Expected question_8 option to be a string"
        assert (isinstance(response_payload["PolicePublicRelations"][2]["select_options"][2]["option_3"], str)), "Expected question_8 option to be a string"


@then("the PoliceInformation question objects should be displayed in the Questions response payload in the expected format.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[3]["Questions"][3]
        
        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["PoliceInformation"], list)), "Expected object to be a list"
        
        assert (len(response_payload["PoliceInformation"]) > 0), "Expected more than 1 select options" 
        assert (len(response_payload["PoliceInformation"][0]["select_options"]) > 0), "Expected more than 1 select options for question_7"
        assert (len(response_payload["PoliceInformation"][1]["select_options"]) > 0), "Expected more than 1 select options for question_10"

        assert (isinstance(response_payload["PoliceInformation"][0], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["PoliceInformation"][1], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["PoliceInformation"][2], dict)), "Expected object to be a dictionary"

        assert ("question_7" in response_payload["PoliceInformation"][0]), "Expected question_7 to be in PoliceInformation response"
        assert ("question_10" in response_payload["PoliceInformation"][1]), "Expected question_10 to be in PoliceInformation response"
        assert ("question_11" in response_payload["PoliceInformation"][2]), "Expected question_11 to be in PoliceInformation response"

        assert ("select_options" in response_payload["PoliceInformation"][0]), "Expected select_options to be in question_7"
        assert ("select_options" in response_payload["PoliceInformation"][1]), "Expected select_options to be in question_10"
        
        assert (response_payload["PoliceInformation"][0]["question_7"] == "Approximately how many police could you see?"), "Expected question text to contain: 'Approximately how many police could you see?'"
        assert (response_payload["PoliceInformation"][1]["question_10"] == "Did you get the police officer's name, badge number etc?"), "Expected question text to contain: 'Did you get the police officer's name, badge number etc?'"
        assert (response_payload["PoliceInformation"][2]["question_11"] == "Enter the police officer's information where possible:"), "Expected question text to contain: 'Enter the police officer's information where possible:'"

        assert (response_payload["PoliceInformation"][0]["select_options"][0]["option_1"] == "Unknown"), "Expected question text to contain: 'Unknown'"
        assert (response_payload["PoliceInformation"][0]["select_options"][1]["option_2"] == "1 - 2"), "Expected question text to contain: '1 - 2'"
        assert (response_payload["PoliceInformation"][0]["select_options"][7]["option_8"] == "20+"), "Expected question text to contain: '20+'"
        assert (response_payload["PoliceInformation"][1]["select_options"][0]["option_1"] == "yes"), "Expected question option to contain: 'yes'"
        assert (response_payload["PoliceInformation"][1]["select_options"][1]["option_2"] == "no"), "Expected question option to contain: 'no'"

        assert (isinstance(response_payload["PoliceInformation"][0]["question_7"], str)), "Expected question_7 to be a string"
        assert (isinstance(response_payload["PoliceInformation"][1]["question_10"], str)), "Expected question_10 to be a string"
        assert (isinstance(response_payload["PoliceInformation"][2]["question_11"], str)), "Expected question_15 to be a string"
        
        assert (isinstance(response_payload["PoliceInformation"][0]["select_options"][0]["option_1"], str)), "Expected question_7 option to be a string"
        assert (isinstance(response_payload["PoliceInformation"][0]["select_options"][1]["option_2"], str)), "Expected question_7 option to be a string"
        assert (isinstance(response_payload["PoliceInformation"][0]["select_options"][7]["option_8"], str)), "Expected question_7 option to be a string"
        assert (isinstance(response_payload["PoliceInformation"][1]["select_options"][0]["option_1"], str)), "Expected question_10 option to be a string"
        assert (isinstance(response_payload["PoliceInformation"][1]["select_options"][1]["option_2"], str)), "Expected question_10 option to be a string"