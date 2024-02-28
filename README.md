Name : Jennifer Alcantara
This README file is for my midterm project for class: IS6011J2-Web Systems Development

The following script does as follows:

(Two libraries needed to be imported for this project. Libraries 'json' and 'argparse'.)

First, the script reads in a JSON file whose name is passed in as the first positional argument. Argparse helped accomplish this in lines 3-8.
The JSON file read in should be formatted as the "example_orders.json" file in this git repo. This was the file used for this script.
It contains customers' names, contact information, food names, and prices.

Based on the information from the JSON file that was read. 
The script will then say how to format the two new JSON files in the format below.

One JSON file is named 'Customers.json' and has the following information and format: 
{
    "609-555-0124": "Karl",
    "732-555-1234": "Mike",
    ...
}
(Reorder and format implemented in lines 12-15.)

The second JSON file is named 'Items.json' and has the following information and format: 
"Butter Masala Dosa": {
        "price": 12.95,
        "orders": 52
}
(Reorder and format implemented in lines 16-25.) 

For the second JSON file ('Items.json'), the number of orders per item was counted and displayed here: "orders": 52

These 2 JSON files were created (and closed) in lines 27 - 31.
