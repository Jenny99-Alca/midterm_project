Name : Jennifer Alcantara
This README file is for my midterm project for class: IS6011J2-Web Systems Development

The following script is supposed to do as follows:

The script is supposed to reads a JSON file whose name is passed as the first positional argument.
This JSON file contains customers, their information and food orders.

The script will also create 2 JSON files:

One JSON file is named 'Customers.json' and has this format:
{
    "609-555-0124": "Karl",
    "732-555-1234": "Mike",
    ...
}

The second JSON file named 'items.json has the following format:
"Butter Masala Dosa": {
        "price": 12.95,
        "orders": 52
}

 The type for both the JSON files are strings.