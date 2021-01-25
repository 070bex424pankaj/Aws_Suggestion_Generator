import pandas as pd
class CsvLoadData():
    
    def __init__(self,location_csv):
        self.price_csv = 0
        self.location_csv = location_csv
    
    def load_csv(self):
        #load the csv file
        self.price_csv = pd.read_csv(self.location_csv)
        return self.price_csv