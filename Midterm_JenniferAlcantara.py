import json

class Midterm:
    def __init__(self, filename):
        with open (filename,'r') as f:
            data = json.load(f)
            self.timestamp = data["timestamp"]
            self.name = data["name"]
            self.phone = data["phone"]
            self.items = data["items"]
            self.notes = data["notes"]

    def get_phone(self):
        return
