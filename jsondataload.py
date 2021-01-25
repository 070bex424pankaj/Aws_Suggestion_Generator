import json

class JsonDataLoad():
    
    def __init__(self):
        self.data_json = 0
    
    def load_file(self):
        #load the json files
        with open('Nov11_2012_81.json') as f:
            self.data_json = json.load(f)
        return self.data_json
        