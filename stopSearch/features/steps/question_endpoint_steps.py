import json
import requests
from stopSearch.main import app
from behave import given, when, then
from flask import request

@given("the report_endpoint is running")
def step_implementation(context):
    with app.app_context():
        context.client = app.test_client()

@when("a GET request is made to the report_endpoint")
def step_implementation(context):
    with app.app_context():
        context.response = requests.get("http://localhost:8000/report")
        context.response_status_code = context.response.status_code
        context.response_text = context.response.text  # Capture raw response text
        try:
            context.response_json = context.response.json()  # Attempt to parse JSON
        except ValueError as e:
            context.response_json = None  # Set to None if JSON parsing fails
            context.json_error = str(e)

@then("questions should be displayed in the correct format.")
def step_implementation(context):
    with app.app_context():
        assert (context.response_status_code == 200), "Expected status code to be 200"

        assert ("question1" in context.response_text), "Expected 'question1' to be in text"
        assert ("question2" in context.response_text), "Expected 'question2' to be in text"
        assert ("question3" in context.response_text), "Expected 'question3' to be in text"
        assert ("question4" in context.response_text), "Expected 'question4' to be in text"
        assert ("question5" in context.response_text), "Expected 'question5' to be in text"
        assert ("question6" in context.response_text), "Expected 'question6' to be in text"
        assert ("question7" in context.response_text), "Expected 'question7' to be in text"
        assert ("question8" in context.response_text), "Expected 'question8' to be in text"
        assert ("question9" in context.response_text), "Expected 'question9' to be in text"
        assert ("question10" in context.response_text), "Expected 'question10' to be in text"
        assert ("question11" in context.response_text), "Expected 'question11' to be in text"
        assert ("question12" in context.response_text), "Expected 'question12' to be in text"
        assert ("question13" in context.response_text), "Expected 'question13' to be in text"
        assert ("question14" in context.response_text), "Expected 'question14' to be in text"
        assert ("question15" in context.response_text), "Expected 'question15' to be in text"
        assert ("question16" in context.response_text), "Expected 'question16' to be in text"
