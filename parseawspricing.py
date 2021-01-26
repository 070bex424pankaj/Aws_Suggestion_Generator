from csvloaddata import CsvLoadData
class ParseAWSPricingData():
    
    def __init__(self,location_csv):
        self.location_csv = location_csv
        self.price_csv = CsvLoadData(self.location_csv).load_csv()
        self.extracted_price_csv = 0
    
    
    def extract_only(self):
        #extract only the column we require for easier processing
        self.extracted_price_csv = self.price_csv[["SKU","TermType","OfferTermCode",
                           "PriceDescription",
                           "Unit","PricePerUnit",
                           "LeaseContractLength",'PurchaseOption', 'OfferingClass',
                           'Instance Type','vCPU','Clock Speed',
                           'Memory','Operating System']]
        return self.extracted_price_csv