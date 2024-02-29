Name : Jennifer Alcantara
This README file is for my midterm project for class IS6011J2-Web Systems Development.

The following script does as follows:

(Two libraries needed to be imported for this project. Libraries 'json' and 'argparse')

First, the script reads in a JSON file whose name is passed in as the first positional argument. Argparse helped accomplish this in lines 3-8.
The JSON file read in should be formatted like the "example_orders.json" file in this git repository. This was the file used for this script.
It contains the customer's names and contact information, the food items the customers ordered, and their prices.

Then, based on the information from the JSON file that was read, the script instructs how to format and what to add to the two new JSON files that need to be created for this project (see below).

One JSON file is named 'Customers.json' and displays the following information in this format: 
{
    "609-555-0124": "Karl",
    "732-555-1234": "Mike",
    ...
}
(Implemented by lines 10, 12-15.)
This JSON file contains the phone numbers as keys and the customer's names as values.


The second JSON file is named 'Items.json' and displays the following information in this format: 
"Butter Masala Dosa": {
        "price": 12.95,
        "orders": 52
}
(Implemented by lines 11, 16-25.)
This JSON file contains the item names as keys, an object with the price, and the number of times it has been ordered as a value.
For the orders, this calculation is done in lines 19-24.

These 2 JSON files were finally created (and closed) in lines 27 - 31.
