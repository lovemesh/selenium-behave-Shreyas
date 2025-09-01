Feature: Navigate to Google and validate redirection
    Scenario: Open Google homepage
        Given I navigate to "https://www.amazon.in/"
        Then I maximize browser window
        #Then element having id "nav-cart-text-container" should have text as "Cart"
        Then I refresh page
        Then I enter "shreyas patil" into input field having id "twotabsearchtextbox"
        Then I wait for 2 sec
        Then I clear input field having id "twotabsearchtextbox"
        Then I wait for 2 sec
        Then I enter "cycling helmet" into input field having id "twotabsearchtextbox"
        Then I wait for 2 sec
        Then I click on element having id "nav-cart"
        Then I wait for 5 sec
        