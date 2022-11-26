@smoke
Feature: Search feature
  Scenario: Validating the search feature
    Given I navigate to google.com
    When I validate the page title
    Then I enter the text as "Hello Selenium"
    And click the search button

  Scenario: Validating the search feature with new text
    Given I navigate to google.com
    When I validate the page title
    Then I enter the text as "Hello Behave"
    And click the search button

