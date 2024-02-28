Name : Jennifer Alcantara
This README file is for my midterm project for class: IS6011J2-Web Systems Development

The following script does as follows:

(Two libraries needed to be imported for this project. Libraries 'json' and 'argparse'.)

First, the script reads in a JSON file whose name is passed in as the first positional argument. Argparse helped accomplish this in lines 3-8.
The JSON file read in should be formatted such as the "example_orders.json" file in this git repository. This was the file used for this script.
It contains the customer's names and contact information, as well as the food items they ordered and their prices.

Based on the information from the JSON file that was read, the script then instructs how to format and/or what to add to the two new JSON files that need to be created (see below).

One JSON file is named 'Customers.json' and displays the following information in this format: 
{
    "609-555-0124": "Karl",
    "732-555-1234": "Mike",
    ...
}
(Implemented by lines 10, 12-15.)

The second JSON file is named 'Items.json' and displays the following information in this format: 
"Butter Masala Dosa": {
        "price": 12.95,
        "orders": 52
}
(Implemented by lines 11, 16-25.) 

For the second JSON file ('Items.json'), instead of just reordering the data, a calculation was needed for the "orders".
The number of times an item was ordered was counted and displayed where it says "orders": 52. 
The Butter Masala Dosa was ordered 52 times.

Finally, these 2 JSON files were created (and closed) in lines 27 - 31.
