@ReportEndpoint
Feature: Test Report Endpoint

    Scenario: Load questions from Backend to Frontend Endpoint Using GET request
    Given the report_endpoint is running 
    When a GET request is made to the report_endpoint
    Then questions should be displayed in the correct format.