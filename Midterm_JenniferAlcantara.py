import json, argparse

class Midterm:
    def __init__(self, filename):
        parser = argparse.ArgumentParser() #how?
        with open (filename,'r') as f:
            data = json.load(f)
            self.timestamp = data["timestamp"]
            self.name = data["name"]
            self.phone = data["phone"]
            self.items = data["items"]
            self.notes = data["notes"]

            for phone,name in data: #not sure
                del data[name,phone]

            with open('customers.json','w') as f: #how does it take number and  name & specific format?
                json.dumps(data, f)

            count = 0
            if name in data ["items"] == name:
                count += 1
            
            with open('items.json','w') as f: #how does it take item, price and orders & specific format?)
                json.dumps(data, f)