import json, argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

with open (args.filename,'r') as f:
    data = json.load(f)

    customers = {}
    items = {}
    for order in data:
        name = order["name"]
        phone = order["phone"]
        customers[phone] = name
        for item in order["items"]:
            item_name = item["name"]
            price = item["price"]
            if item_name in items:
                items[item_name]["orders"] += 1
            else:
                items[item_name] = {
                    "price": price,
                    "orders": 1,
                }

with open('customers.json','w') as f:
    json.dump(customers, f)

with open('items.json','w') as f:
    json.dump(items, f)