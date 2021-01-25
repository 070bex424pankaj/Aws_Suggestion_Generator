from parseawspricing import ParseAWSPricingData

class PreProcessingExtractedCsvFile():
    
    def __init__(self):
        self.extracted_price_csv = ParseAWSPricingData().extract_only()
        
    def repalce_null_values(self,data):
        #remove null values
        self.extracted_price_csv[data].fillna(0, inplace = True)
    
    def repalce_NA_values(self,data):
        #remove not available values
        self.extracted_price_csv[data].replace({"NA": 0}, inplace=True)

    
    def extract_only_number(self,data):
        #extract only the number from the string from the column values
        self.extracted_price_csv[data] = self.extracted_price_csv[data].str.extract('(\d+)')

    
    def convert_to_float(self,data):
        #convert string values to float data type
        self.extracted_price_csv[data] = self.extracted_price_csv[data].astype(float)
        return self.extracted_price_csv
        
    def convert_to_int(self,data):
        #convert string values to integer data type
        self.extracted_price_csv[data] = self.extracted_price_csv[data].astype(int)
        
    def select_only_hrs_or_quantity(self):
        #there are other fileds in unit, but we require only hrs and quantity
        self.extracted_price_csv = self.extracted_price_csv.loc[(self.extracted_price_csv['Unit'] == 'Hrs') | (self.extracted_price_csv['Unit'] == 'Quantity')]
        
    def convert_3yrs_to_hr(self):
        # converting all upfront 3 yrs to 1 yr for suitable comparison 
        self.extracted_price_csv.loc[self.extracted_price_csv.LeaseContractLength == 3, 'PricePerUnit'] = self.extracted_price_csv.PricePerUnit / (3*365*24)  

    def convert_1yr_to_hr(self):
        #converting unit hrs of partial, noupfront to 1 year value for suitable comparison
        self.extracted_price_csv.loc[self.extracted_price_csv.Unit == 'Hrs', 'PricePerUnit'] = self.extracted_price_csv.PricePerUnit/(24*365)
