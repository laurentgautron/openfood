# openfood

openfood is an application to improve health through diet:
it offers the user the opportunity to replace his usual foods with others that are better for his health.

For this, the user must launch the application in a console or terminal with the command 

`python3 openfood.py`

the application loads data into a database (Mysql), retrieved via the *openfoodfact API*
the extracted data will then allow:

- displaying a menu of 20 categories, asking to make a choice by selecting a number (between 1 and 20).
- displaying a second menu: a list of 30 foods, allowing you to choose a food by a number (between 1 and 30).
the program will ask the user again as long as it does not enter a number belonging to the pre-displayed list


The application, will then search the database for a substitute food. research is done on the nutriscore (a letter between A and E).
the food with the best nutriscore is displayed with:
- his name
- the name of the store where the food is sold
- a description of the food
- a link to the openfoodfacts website

The application subsequently proposes to the user to record or not the result of his search.
