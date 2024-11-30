Feature:  Setup Account Credentials  and Submit the KYC update Application.
  As a Client
  I want to Setup Account Credentials and Login into the Client Portal
  So that I can Submit the KYC update Application.
@order4

  Scenario: Client should Setup Account Credentials and Login into the Client Portal and Submit his KYC update Application.
    When Setup Account Credentials and Login into the Client Portal and Update require data, Submit the KYC update Application
    When Approve KYC update Application from all back off users