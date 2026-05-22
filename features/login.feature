Feature: Login

  Scenario: Successful login with valid credentials
    Given user opens login page
    When user logs in with valid credentials
    Then user should see products page