import pandas as pd
class CsvLoadData():
    
    def __init__(self):
        self.price_csv = 0
    
    def load_csv(self):
        #load the csv file
        self.price_csv = pd.read_csv('EC2_pricing.csv')
        return self.price_csv