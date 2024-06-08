@QuestionsRoute
Feature: Test Questions Route

    Scenario: Get the questions via the Questions Route
    Given the questions_route is running 
    When a request is made to the questions_route
    Then the Status information should be displayed.
    Then the AppData information should be displayed.
    Then the Questions should be in the response.
    Then the ReportedBy question objects should be displayed in the Questions response payload in the expected format.
    Then the VictimInformation question objects should be displayed in the Questions response payload in the expected format.
    Then the PolicePublicRelations question objects should be displayed in the Questions response payload in the expected format.
    Then the PoliceInformation question objects should be displayed in the Questions response payload in the expected format.