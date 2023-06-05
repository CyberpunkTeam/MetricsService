Feature: CRUD User


  Scenario: Create track

    When creo un track del path "/session" con el uid "123" y created_date "2023-02-03"

    Then se me informa que se creo exitosamente
