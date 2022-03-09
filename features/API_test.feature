Feature: Testing APIs

    Scenario: Testing Add Book API
      Given I set url to http://216.10.245.166/Library/Addbook.php
      And set request body to the following
      """
        {
            "name":"Kumu Sample book",
            "isbn":"bcd2348",
            "aisle":"2274",
            "author":"John Kumu"
        }
      """
      When I send a post request
      Then response should return a status code 200
      And response should return Msg with value successfully added
      And response should return ID with value bcd23482274
    
    Scenario: Testing Get Book API
      Given I set url to http://216.10.245.166/Library/GetBook.php
      And set AuthorName parameter as John Kumu
      When I send a get request
      Then response should return a status code 200
      And Get Book API response should return book_name with value Kumu Sample book
      And Get Book API response should return isbn with value bcd2348
      And Get Book API response should return aisle with value 2274