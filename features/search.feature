Feature: Search Option

  @search
  Scenario: Valid search
    Given Landing page
    When I search Valid Product in search box
    And Click on the search button
    Then I should I see the Valid Result

  @search
  Scenario: InValid search - product not listed
    Given Landing page
    When I search InValid Product in search box
    And Click on the search button
    Then I should I see the InValid Result


