
Feature: Test for amazon main page

  Scenario: Hamburger menu is present
    Given Open amazon page
    Then Verify hamburger menu is present

  Scenario: Footer has correct amount of links
    Given Open amazon page
    Then Verify that footer has 38 links

 Scenario Outline: User can select and search in a department
   Given Open amazon page
   When Select department by value <value>
   And Search for blender
   Then Verify <department> department is selected
   Examples:
   |value         |department    |
   |appliances    |appliances    |