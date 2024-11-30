
  Feature: Login with  Back off Users and Approve the Application.
  As a Back off User
  I want to Login into the Admin Portal
  So that I can Approve the Account Opening Application.
@order3

  Scenario: Admin should login into the portal and Approve the Account Opening Application
    When BD Admin login into the Admin  portal with valid Credentials and Approved the application
    When Compliance Manager login into the Admin  portal with valid Credentials and Send the application for Screening
    When Compliance Officer login into the Admin  portal with valid Credentials and Set Risk type and Send Back application to the Compliance Manager
    When Compliance Manager login into the Admin  portal with valid Credentials and Approve the application
    When CEO login into the Admin  portal with valid Credentials and Approve the application
    When BD-Head login into the Admin  portal with valid Credentials and Approve the application