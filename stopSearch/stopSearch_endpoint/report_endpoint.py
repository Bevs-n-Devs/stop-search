import os
import requests
import json
from stopSearch import app
from flask import jsonify, request, render_template, url_for
from dotenv import load_dotenv
load_dotenv()


@app.route("/report", methods=["GET", "POST"])
def report_endpoint():
    if request.method == "GET":
        # get the form questions from BE route
        api_request = requests.get("http://localhost:8000/questions")
        api_request.raise_for_status()  # Check for request errors
            
        # Parse the JSON response
        response = api_request.json()
        questions = response[3]["Questions"]

        # questions
        question_1 = questions[0]["ReportedBy"][0]["question_1"]
        question_2 = questions[0]["ReportedBy"][1]["question_2"]
        question_3 = questions[0]["ReportedBy"][2]["question_3"]
        question_4 = questions[0]["ReportedBy"][3]["question_4"]
        question_5 = questions[2]["PolicePublicRelations"][0]["question_5"]
        question_6 = questions[1]["VictimInformation"][0]["question_6"]
        question_7 = questions[3]["PoliceInformation"][0]["question_7"]
        question_8 = questions[2]["PolicePublicRelations"][1]["question_8"]
        question_9 = questions[2]["PolicePublicRelations"][2]["question_9"]
        question_10 = questions[3]["PoliceInformation"][1]["question_10"]
        question_11 = questions[3]["PoliceInformation"][2]["question_11"]
        question_12 = questions[1]["VictimInformation"][1]["question_12"]
        question_13 = questions[1]["VictimInformation"][2]["question_13"]
        question_14 = questions[1]["VictimInformation"][3]["question_14"]
        question_15 = questions[2]["PolicePublicRelations"][3]["question_15"]
        question_16 = questions[2]["PolicePublicRelations"][4]["question_16"]

        # question options
        question_3_option_1 = questions[0]["ReportedBy"][2]["select_options"][0]["option_1"]
        question_3_option_2 = questions[0]["ReportedBy"][2]["select_options"][1]["option_2"]

        question_5_option_1 = questions[2]["PolicePublicRelations"][0]["select_options"][0]["option_1"]
        question_5_option_2 = questions[2]["PolicePublicRelations"][0]["select_options"][1]["option_2"]

        question_6_option_1 = questions[1]["VictimInformation"][0]["select_options"][0]["option_1"]
        question_6_option_2 = questions[1]["VictimInformation"][0]["select_options"][1]["option_2"]
        question_6_option_3 = questions[1]["VictimInformation"][0]["select_options"][2]["option_3"]
        question_6_option_4 = questions[1]["VictimInformation"][0]["select_options"][3]["option_4"]
        question_6_option_5 = questions[1]["VictimInformation"][0]["select_options"][4]["option_5"]
        question_6_option_6 = questions[1]["VictimInformation"][0]["select_options"][5]["option_6"]
        question_6_option_7 = questions[1]["VictimInformation"][0]["select_options"][6]["option_7"]
        question_6_option_8 = questions[1]["VictimInformation"][0]["select_options"][7]["option_8"]
        question_6_option_9 = questions[1]["VictimInformation"][0]["select_options"][8]["option_9"]
        question_6_option_10 = questions[1]["VictimInformation"][0]["select_options"][9]["option_10"]
        question_6_option_11 = questions[1]["VictimInformation"][0]["select_options"][10]["option_11"]
        question_6_option_12 = questions[1]["VictimInformation"][0]["select_options"][11]["option_12"]

        question_7_option_1 = questions[3]["PoliceInformation"][0]["select_options"][0]["option_1"]
        question_7_option_2 = questions[3]["PoliceInformation"][0]["select_options"][1]["option_2"]
        question_7_option_3 = questions[3]["PoliceInformation"][0]["select_options"][2]["option_3"]
        question_7_option_4 = questions[3]["PoliceInformation"][0]["select_options"][3]["option_4"]
        question_7_option_5 = questions[3]["PoliceInformation"][0]["select_options"][4]["option_5"]
        question_7_option_6 = questions[3]["PoliceInformation"][0]["select_options"][5]["option_6"]
        question_7_option_7 = questions[3]["PoliceInformation"][0]["select_options"][6]["option_7"]
        question_7_option_8 = questions[3]["PoliceInformation"][0]["select_options"][7]["option_8"]

        question_8_option_1 = questions[2]["PolicePublicRelations"][1]["select_options"][0]["option_1"]
        question_8_option_2 = questions[2]["PolicePublicRelations"][1]["select_options"][1]["option_2"]
        question_8_option_3 = questions[2]["PolicePublicRelations"][1]["select_options"][2]["option_3"]
        question_8_option_4 = questions[2]["PolicePublicRelations"][1]["select_options"][3]["option_4"]
        question_8_option_5 = questions[2]["PolicePublicRelations"][1]["select_options"][4]["option_5"]
        question_8_option_6 = questions[2]["PolicePublicRelations"][1]["select_options"][5]["option_6"]
        question_8_option_7 = questions[2]["PolicePublicRelations"][1]["select_options"][6]["option_7"]
        question_8_option_8 = questions[2]["PolicePublicRelations"][1]["select_options"][7]["option_8"]
        question_8_option_9 = questions[2]["PolicePublicRelations"][1]["select_options"][8]["option_9"]
        question_8_option_10 = questions[2]["PolicePublicRelations"][1]["select_options"][9]["option_10"]

        question_9_option_1 = questions[2]["PolicePublicRelations"][2]["select_options"][0]["option_1"]
        question_9_option_2 = questions[2]["PolicePublicRelations"][2]["select_options"][1]["option_2"]
        question_9_option_3 = questions[2]["PolicePublicRelations"][2]["select_options"][2]["option_3"]

        question_10_option_1 = questions[3]["PoliceInformation"][1]["select_options"][0]["option_1"]
        question_10_option_2 = questions[3]["PoliceInformation"][1]["select_options"][1]["option_2"]

        question_12_option_1 = questions[1]["VictimInformation"][1]["select_options"][0]["option_1"]
        question_12_option_2 = questions[1]["VictimInformation"][1]["select_options"][1]["option_2"]
        question_12_option_3 = questions[1]["VictimInformation"][1]["select_options"][2]["option_3"]
        question_12_option_4 = questions[1]["VictimInformation"][1]["select_options"][3]["option_4"]
        question_12_option_5 = questions[1]["VictimInformation"][1]["select_options"][4]["option_5"]
        question_12_option_6 = questions[1]["VictimInformation"][1]["select_options"][5]["option_6"]
        question_12_option_7 = questions[1]["VictimInformation"][1]["select_options"][6]["option_7"]
        question_12_option_8 = questions[1]["VictimInformation"][1]["select_options"][7]["option_8"]
        question_12_option_9 = questions[1]["VictimInformation"][1]["select_options"][8]["option_9"]
        
        question_13_option_1 = questions[1]["VictimInformation"][2]["select_options"][0]["option_1"]
        question_13_option_2 = questions[1]["VictimInformation"][2]["select_options"][1]["option_2"]
        question_13_option_3 = questions[1]["VictimInformation"][2]["select_options"][2]["option_3"]
        question_13_option_4 = questions[1]["VictimInformation"][2]["select_options"][3]["option_4"]
        question_13_option_5 = questions[1]["VictimInformation"][2]["select_options"][4]["option_5"]
        question_13_option_6 = questions[1]["VictimInformation"][2]["select_options"][5]["option_6"]
        question_13_option_7 = questions[1]["VictimInformation"][2]["select_options"][6]["option_7"]
        question_13_option_8 = questions[1]["VictimInformation"][2]["select_options"][7]["option_8"]
        question_13_option_9 = questions[1]["VictimInformation"][2]["select_options"][8]["option_9"]
        
        question_14_option_1 = questions[1]["VictimInformation"][3]["select_options"][0]["option_1"]
        question_14_option_2 = questions[1]["VictimInformation"][3]["select_options"][1]["option_2"]
        question_14_option_3 = questions[1]["VictimInformation"][3]["select_options"][2]["option_3"]
        question_14_option_4 = questions[1]["VictimInformation"][3]["select_options"][3]["option_4"]
        question_14_option_5 = questions[1]["VictimInformation"][3]["select_options"][4]["option_5"]
        question_14_option_6 = questions[1]["VictimInformation"][3]["select_options"][5]["option_6"]
        question_14_option_7 = questions[1]["VictimInformation"][3]["select_options"][6]["option_7"]
        question_14_option_8 = questions[1]["VictimInformation"][3]["select_options"][7]["option_8"]
        question_14_option_9 = questions[1]["VictimInformation"][3]["select_options"][8]["option_9"]
        question_14_option_10 = questions[1]["VictimInformation"][3]["select_options"][9]["option_10"]

        return render_template(
            "report_page.html",
            question_1=question_1, question_2=question_2, question_3=question_3, question_4=question_4, question_5=question_5,
            question_6=question_6, question_7=question_7, question_8=question_8, question_9=question_9, question_10=question_10,
            question_11=question_11, question_12=question_12, question_13=question_13, question_14=question_14, question_15=question_15,
            question_16=question_16, question_3_option_1=question_3_option_1, question_3_option_2=question_3_option_2,
            question_5_option_1=question_5_option_1, question_5_option_2=question_5_option_2, question_6_option_1=question_6_option_1,
            question_6_option_2=question_6_option_2, question_6_option_3=question_6_option_3, question_6_option_4=question_6_option_4,
            question_6_option_5=question_6_option_5, question_6_option_6=question_6_option_6, question_6_option_7=question_6_option_7,
            question_6_option_8=question_6_option_8, question_6_option_9=question_6_option_9, question_6_option_10=question_6_option_10,
            question_6_option_11=question_6_option_11, question_6_option_12=question_6_option_12, question_7_option_1=question_7_option_1,
            question_7_option_2=question_7_option_2, question_7_option_3=question_7_option_3, question_7_option_4=question_7_option_4,
            question_7_option_5=question_7_option_5, question_7_option_6=question_7_option_6, question_7_option_7=question_7_option_7,
            question_7_option_8=question_7_option_8, question_8_option_1=question_8_option_1, question_8_option_2=question_8_option_2,
            question_8_option_3=question_8_option_3, question_8_option_4=question_8_option_4, question_8_option_5=question_8_option_5,
            question_8_option_6=question_8_option_6, question_8_option_7=question_8_option_7, question_8_option_8=question_8_option_8,
            question_8_option_9=question_8_option_9, question_8_option_10=question_8_option_10, question_9_option_1=question_9_option_1,
            question_9_option_2=question_9_option_2, question_9_option_3=question_9_option_3, question_10_option_1=question_10_option_1,
            question_10_option_2=question_10_option_2, question_12_option_1=question_12_option_1, question_12_option_2=question_12_option_2,
            question_12_option_3=question_12_option_3, question_12_option_4=question_12_option_4, question_12_option_5=question_12_option_5,
            question_12_option_6=question_12_option_6, question_12_option_7=question_12_option_7, question_12_option_8=question_12_option_8,
            question_12_option_9=question_12_option_9, question_13_option_1=question_13_option_1, question_13_option_2=question_13_option_2,
            question_13_option_3=question_13_option_3, question_13_option_4=question_13_option_4, question_13_option_5=question_13_option_5,
            question_13_option_6=question_13_option_6, question_13_option_7=question_13_option_7, question_13_option_8=question_13_option_8,
            question_13_option_9=question_13_option_9, question_14_option_1=question_14_option_1, question_14_option_2=question_14_option_2,
            question_14_option_3=question_14_option_3, question_14_option_4=question_14_option_4, question_14_option_5=question_14_option_5,
            question_14_option_6=question_14_option_6, question_14_option_7=question_14_option_7, question_14_option_8=question_14_option_8,
            question_14_option_9=question_14_option_9, question_14_option_10=question_14_option_10)
    else:
        pass