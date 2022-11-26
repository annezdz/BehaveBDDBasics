@regression
Feature: Search feature
  Scenario Outline: Validating the search feature
    Given I navigate to google.com
    When I validate the page title
    Then I enter the text as "<search_title>"
    And click the search button
    Examples:
      | search_title |
      | Hello BBD    |
      | Hello TDD    |



