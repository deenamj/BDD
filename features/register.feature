Feature: Register test

  @register
  Scenario: Validating all mandatory fields
    Given I land into Register page
    When I entering the below details
      |firstname|lastname|email          |telephone |password |confirm  |
      |deena    |dhayalan|deena@gmail.com|1234567890|deena1996|deena1996|

    And Click on the Continue button
    #Then I Should get valid Message "Your Account Has Been Created!"

  @register
  Scenario: Validating all mandatory without giving any fields values
    Given I land into Register page
    When I entering the below details
      |firstname|lastname|email          |telephone |password |confirm  |
      |||||||

    And Click on the Continue button
    Then I Should get valid Message "Your Account Has Been Created!"