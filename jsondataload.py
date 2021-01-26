import json

class JsonDataLoad():
    
    def __init__(self,file_location):
        self.data_json = 0
        self.file_location = file_location
    
    def load_file(self):
        #load the json files
        with open(self.file_location) as f:
            self.data_json = json.load(f)
        return self.data_json