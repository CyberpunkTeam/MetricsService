Feature: CRUD tracks


  Scenario: Create track

    When creo un track del path "/session" con el uid "123" y created_date "2023-02-03"

    Then se me informa que se creo exitosamente

  Scenario: Get metrics

    Given creo un track del path "/session" con el uid "123" y created_date "2023-02-03"

    And se me informa que se creo exitosamente

    When pido las metricas

    Then se me informa que se creo una session
