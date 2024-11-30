
Feature: Create Invitation Link
  As a RM user
  I want to create Invitation link for Client
  So that I can access my dashboard
@order1
  Scenario: RM should create Invitation link for Client
    When RM Login with valid Credentials and Create Invitation Link
   # When Click on the Create Invitation Link
    #When Enter Email Address
    #Then Click on the Create Link
    Then Open Invitation Link on Email
    #Then Click on the Setup Account Link


