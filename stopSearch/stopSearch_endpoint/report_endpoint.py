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

        # below we get the questions for the report

        # enter email
        question_1 = questions[0]["ReportedBy"][0]["question_1"]
        # confirm email
        question_2 = questions[0]["ReportedBy"][1]["question_2"]
        # victim or witness ?
        question_3 = questions[0]["ReportedBy"][2]["question_3"]
        # incident date
        question_4 = questions[0]["ReportedBy"][3]["question_4"]
        # incident location
        question_5 = questions[2]["PolicePublicRelations"][0]["question_5"]
        # number of victims involved
        question_6 = questions[1]["VictimInformation"][0]["question_6"]
        # how many police visisble
        question_7 = questions[3]["PoliceInformation"][0]["question_7"]
        # reason for stop
        question_8 = questions[2]["PolicePublicRelations"][1]["question_8"]
        # the type of seacrh (unknown, moderate, aggressive)
        question_9 = questions[2]["PolicePublicRelations"][2]["question_9"]
        # obtain officer information - yes / no
        question_10 = questions[3]["PoliceInformation"][1]["question_10"]
        # enter police officer information
        question_11 = questions[3]["PoliceInformation"][2]["question_11"]
        # victim age
        question_12 = questions[1]["VictimInformation"][1]["question_12"]
        # victim gender
        question_13 = questions[1]["VictimInformation"][2]["question_13"]
        # victim race
        question_14 = questions[1]["VictimInformation"][3]["question_14"]
        # additional notes
        question_15 = questions[2]["PolicePublicRelations"][3]["question_15"]
        # upload media files
        question_16 = questions[2]["PolicePublicRelations"][4]["question_16"]
        # body camnera worn
        question_17 = questions[2]['PoliceInformation'][3]['question_17']
        # search outcome
        question_18 = questions[2]['PolicePublicRelations'][5]['question_18']
        # offcier interaction with the victim and or witness
        question_19 = questions[2]['PoliceInformation'][3]['question_19']

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
        # question_6_option_13 = questions[1]["VictimInformation"][0]["select_options"][12]["option_13"]

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
        question_12_option_10 = questions[1]["VictimInformation"][1]["select_options"][9]["option_10"]
        question_12_option_11 = questions[1]["VictimInformation"][1]["select_options"][10]["option_11"]
        question_12_option_12 = questions[1]["VictimInformation"][1]["select_options"][11]["option_12"]
        question_12_option_13 = questions[1]["VictimInformation"][1]["select_options"][12]["option_13"]
        
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
        question_14_option_11 = questions[1]["VictimInformation"][3]["select_options"][10]["option_11"]
        question_14_option_13 = questions[1]["VictimInformation"][3]["select_options"][11]["option_12"]
        question_14_option_14 = questions[1]["VictimInformation"][3]["select_options"][12]["option_13"]
        question_14_option_15 = questions[1]["VictimInformation"][3]["select_options"][13]["option_14"]
        question_14_option_16 = questions[1]["VictimInformation"][3]["select_options"][14]["option_15"]
        question_14_option_17 = questions[1]["VictimInformation"][3]["select_options"][15]["option_16"]
        question_14_option_18 = questions[1]["VictimInformation"][3]["select_options"][16]["option_17"]
        question_14_option_19 = questions[1]["VictimInformation"][3]["select_options"][17]["option_18"]
        question_14_option_20 = questions[1]["VictimInformation"][3]["select_options"][18]["option_19"]
        question_14_option_21 = questions[1]["VictimInformation"][3]["select_options"][19]["option_20"]
        question_14_option_21 = questions[1]["VictimInformation"][3]["select_options"][20]["option_21"]
        question_14_option_22 = questions[1]["VictimInformation"][3]["select_options"][21]["option_22"]
        question_14_option_23 = questions[1]["VictimInformation"][3]["select_options"][22]["option_23"]
        question_14_option_24 = questions[1]["VictimInformation"][3]["select_options"][23]["option_24"]
        question_14_option_25 = questions[1]["VictimInformation"][3]["select_options"][24]["option_25"]
        question_14_option_26 = questions[1]["VictimInformation"][3]["select_options"][25]["option_26"]
        question_14_option_27 = questions[1]["VictimInformation"][3]["select_options"][26]["option_27"]
        question_14_option_28 = questions[1]["VictimInformation"][3]["select_options"][27]["option_28"]
        question_14_option_29 = questions[1]["VictimInformation"][3]["select_options"][28]["option_29"]
        question_14_option_30 = questions[1]["VictimInformation"][3]["select_options"][29]["option_30"]
        question_14_option_31 = questions[1]["VictimInformation"][3]["select_options"][30]["option_31"]
        question_14_option_32 = questions[1]["VictimInformation"][3]["select_options"][31]["option_32"]

        # body camera questions
        question_17_option_1 = questions[1]['PoliceInformation'][3]['select_options'][0]['option_1']
        question_17_option_2 = questions[1]['PoliceInformation'][3]['select_options'][1]['option_2']
        question_17_option_3 = questions[1]['PoliceInformation'][3]['select_options'][2]['option_3']

        # search outcome questions
        question_18_option_1 = questions[2]['PolicePublicRelations'][5]['select_options'][0]['option_1']
        question_18_option_2 = questions[2]['PolicePublicRelations'][5]['select_options'][1]['option_2']
        question_18_option_3 = questions[2]['PolicePublicRelations'][5]['select_options'][2]['option_3']
        question_18_option_4 = questions[2]['PolicePublicRelations'][5]['select_options'][3]['option_4']
        question_18_option_5 = questions[2]['PolicePublicRelations'][5]['select_options'][4]['option_5']
        question_18_option_6 = questions[2]['PolicePublicRelations'][5]['select_options'][5]['option_6']
        question_18_option_7 = questions[2]['PolicePublicRelations'][5]['select_options'][6]['option_7']
        question_18_option_8 = questions[2]['PolicePublicRelations'][5]['select_options'][7]['option_8']
        question_18_option_9 = questions[2]['PolicePublicRelations'][5]['select_options'][8]['option_9']

        # officer interaction questions
        question_19_option_1 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_1']
        question_19_option_2 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_2']
        question_19_option_3 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_3']
        question_19_option_4 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_4']
        question_19_option_5 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_5']
        question_19_option_6 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_6']
        question_19_option_7 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_7']
        question_19_option_8 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_8']
        question_19_option_9 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_9']
        question_19_option_10 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_10']
        question_19_option_11 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_11']
        question_19_option_12 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_12']
        question_19_option_13 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_13']
        question_19_option_14 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_14']
        question_19_option_15 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_15']
        question_19_option_16 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_16']
        question_19_option_17 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_17']
        question_19_option_18 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_18']
        question_19_option_19 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_19']
        question_19_option_20 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_20']
        question_19_option_21 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_21']
        question_19_option_22 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_22']
        question_19_option_23 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_23']
        question_19_option_24 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_24']
        question_19_option_25 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_25']
        question_19_option_26 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_26']
        question_19_option_27 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_27']
        question_19_option_28 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_28']
        question_19_option_29 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_29']
        question_19_option_30 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_30']
        question_19_option_31 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_31']
        question_19_option_32 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_32']
        question_19_option_33 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_33']
        question_19_option_34 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_34']
        question_19_option_35 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_35']
        question_19_option_36 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_36']
        question_19_option_37 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_37']
        question_19_option_38 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_38']
        question_19_option_39 = questions[2]['PoliceInformation'][3]['select_options'][0]['option_39']


        """
        TODO: RESTRUCTURE QUESTIONS INTO NESTED QUESTION OBJECT

        questions = {
            'question_1': {'text': question_1},
            'question_2': {'text': question_2},
            'question_3': {
                'text': question_3,
                'options': {'option_1': question_3_option_1, 'option_2': question_3_option_2}
            },
            # Add all other questions and options
        }

        return render_template(
            "report_page.html",
            questions=questions,
        )

        Modified report_page.html:
        <h2>{{ questions['question_3']['text'] }}</h2>
        <ul>
            {% for option_id, option_text in questions['question_3']['options'].items() %}
                <li>{{ option_id }}: {{ option_text }}</li>
            {% endfor %}
        </ul>
        """

        # put questions in single object to pass to report page
        report_questions = {
            'question_1': {'text': question_1},  # enter email
            'question_2': {'text': question_2},  # confirm email
            'question_3': {
                'text': question_3,  # victim or witness?
                'options': {'option_1': question_3_option_1, 'option_2': question_3_option_2}
            },
            'question_4': {'text': question_4},  # incident date
            'question_5': {
                'text': question_5,  # incident location
                'options': {'option_1': question_5_option_1, 'option_2': question_5_option_2}
            },
            'question_6': {
                'text': question_6,  # number of victims involved
                'options': {
                    'option_1': question_6_option_1, 'option_2': question_6_option_2, 'option_3': question_6_option_3,
                    'option_4': question_6_option_4, 'option_5': question_6_option_5, 'option_6': question_6_option_6,
                    'option_7': question_6_option_7, 'option_8': question_6_option_8, 'option_9': question_6_option_9,
                    'option_10': question_6_option_10, 'option_11': question_6_option_11, 'option_12': question_6_option_12
                }
            },
            'question_7': {
                'text': question_7,  # how many police visible
                'options': {
                    'option_1': question_7_option_1, 'option_2': question_7_option_2, 'option_3': question_7_option_3,
                    'option_4': question_7_option_4, 'option_5': question_7_option_5, 'option_6': question_7_option_6,
                    'option_7': question_7_option_7, 'option_8': question_7_option_8
                }
            },
            'question_8': {
                'text': question_8,  # reason for stop
                'options': {
                    'option_1': question_8_option_1, 'option_2': question_8_option_2, 'option_3': question_8_option_3,
                    'option_4': question_8_option_4, 'option_5': question_8_option_5, 'option_6': question_8_option_6,
                    'option_7': question_8_option_7, 'option_8': question_8_option_8, 'option_9': question_8_option_9,
                    'option_10': question_8_option_10
                }
            },
            'question_9': {
                'text': question_9,  # type of search
                'options': {'option_1': question_9_option_1, 'option_2': question_9_option_2, 'option_3': question_9_option_3}
            },
            'question_10': {
                'text': question_10,  # obtain officer information - yes / no
                'options': {'option_1': question_10_option_1, 'option_2': question_10_option_2}
            },
            'question_11': {'text': question_11},  # enter police officer information
            'question_12': {
                'text': question_12,  # victim age
                'options': {
                    'option_1': question_12_option_1, 'option_2': question_12_option_2, 'option_3': question_12_option_3,
                    'option_4': question_12_option_4, 'option_5': question_12_option_5, 'option_6': question_12_option_6,
                    'option_7': question_12_option_7, 'option_8': question_12_option_8, 'option_9': question_12_option_9,
                    'option_10': question_12_option_10, 'option_11': question_12_option_11, 'option_12': question_12_option_12,
                    'option_13': question_12_option_13
                }
            },
            'question_13': {
                'text': question_13,  # victim gender
                'options': {
                    'option_1': question_13_option_1, 'option_2': question_13_option_2, 'option_3': question_13_option_3,
                    'option_4': question_13_option_4, 'option_5': question_13_option_5, 'option_6': question_13_option_6,
                    'option_7': question_13_option_7, 'option_8': question_13_option_8, 'option_9': question_13_option_9
                }
            },
            'question_14': {
                'text': question_14,  # victim race
                'options': {
                    'option_1': question_14_option_1, 'option_2': question_14_option_2, 'option_3': question_14_option_3,
                    'option_4': question_14_option_4, 'option_5': question_14_option_5, 'option_6': question_14_option_6,
                    'option_7': question_14_option_7, 'option_8': question_14_option_8, 'option_9': question_14_option_9,
                    'option_10': question_14_option_10, 'option_11': question_14_option_11, 'option_12': question_14_option_13,
                    'option_13': question_14_option_14, 'option_14': question_14_option_15, 'option_15': question_14_option_16,
                    'option_16': question_14_option_17, 'option_17': question_14_option_18, 'option_18': question_14_option_19,
                    'option_19': question_14_option_20, 'option_20': question_14_option_21, 'option_21': question_14_option_22,
                    'option_22': question_14_option_23, 'option_23': question_14_option_24, 'option_24': question_14_option_25,
                    'option_25': question_14_option_26, 'option_26': question_14_option_27, 'option_27': question_14_option_28,
                    'option_28': question_14_option_29, 'option_29': question_14_option_30, 'option_30': question_14_option_31,
                    'option_31': question_14_option_32
                }
            },
            'question_15': {'text': question_15},  # additional notes
            'question_16': {'text': question_16},  # upload media files
            'question_17': {
                'text': question_17,  # body camera worn
                'options': {'option_1': question_17_option_1, 'option_2': question_17_option_2, 'option_3': question_17_option_3}
            },
            'question_18': {
                'text': question_18,  # search outcome
                'options': {
                    'option_1': question_18_option_1, 'option_2': question_18_option_2, 'option_3': question_18_option_3,
                    'option_4': question_18_option_4, 'option_5': question_18_option_5, 'option_6': question_18_option_6,
                    'option_7': question_18_option_7, 'option_8': question_18_option_8, 'option_9': question_18_option_9
                }
            },
            'question_19': {
                'text': question_19,  # officer interaction with the victim/witness
                'options': {
                    'option_1': question_19_option_1, 'option_2': question_19_option_2, 'option_3': question_19_option_3,
                    'option_4': question_19_option_4, 'option_5': question_19_option_5, 'option_6': question_19_option_6,
                    'option_7': question_19_option_7, 'option_8': question_19_option_8, 'option_9': question_19_option_9,
                    'option_10': question_19_option_10, 'option_11': question_19_option_11, 'option_12': question_19_option_12,
                    'option_13': question_19_option_13, 'option_14': question_19_option_14, 'option_15': question_19_option_15,
                    'option_16': question_19_option_16, 'option_17': question_19_option_17, 'option_18': question_19_option_18,
                    'option_19': question_19_option_19, 'option_20': question_19_option_20, 'option_21': question_19_option_21,
                    'option_22': question_19_option_22, 'option_23': question_19_option_23, 'option_24': question_19_option_24,
                    'option_25': question_19_option_25, 'option_26': question_19_option_26, 'option_27': question_19_option_27,
                    'option_28': question_19_option_28, 'option_29': question_19_option_29, 'option_30': question_19_option_30,
                    'option_31': question_19_option_31
                }
            }
        }


        return render_template(
            "report_page.html",
            report_questions=report_questions
            )
    else:
        # TODO: Handle the error handling
        return 'This page could not load'
    #     # get data from form
        
    #     # send data to backend
    #     api_response = requests.post("http://localhost:8000/submit_report", json=form_data)
    #     api_response.raise_for_status() # check for request errors

    #     response = api_response.json()

    #     if response["status"] == "success":
    #         return render_template("report_page.html", success_message=response["message"])
    #     else:
    #         return render_template("report_page.html", error_message=response["message"])
 