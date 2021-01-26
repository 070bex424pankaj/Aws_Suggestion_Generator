from processingextractedcsvfile import PreProcessingExtractedCsvFile
from recommendationmachine import RecommendationMachine
from usagesummarygenerator import UsageSummaryGenerator
from jsondataload import JsonDataLoad
from shapefactory import ShapeFactory
from abstractrightsizerclass import RightSizer
from csvvalidator import PricingValidator

class Main():
    def __init__(self,source,json_file_location,csv_file_location,rightsize,purchaseoption,extracted_price_csv,offeringclass = None):
        self.rightsize = rightsize
        self.purchaseoption = purchaseoption
        self.offeringclass = offeringclass
        #get mean usages for corre
        get_ram,avg_ram_usage,get_cpu,avg_cpu_usage, os = UsageSummaryGenerator(source,json_file_location).calculate_usage()
        m = ShapeFactory().create_right_sizer(self.rightsize,avg_ram_usage, avg_cpu_usage)
        ram_usage, cpu_usage = m.RightSize()
        ram_gb,cpu_cores = RightSizer.right_size_algorithm(get_ram,ram_usage,get_cpu,cpu_usage)
        
        filtereddata= RecommendationMachine().filter_based_on_preference(extracted_price_csv, ram_gb, cpu_cores, os,self.purchaseoption,self.offeringclass)
        filtereddata= RecommendationMachine().group_by(filtereddata)
        print(RecommendationMachine().select_minimum(filtereddata))
            
            
#it creates two objects for two sources and calls the run_function of the main class
if __name__ == "__main__":
    #create two objects for two different source
    json_file_location = 'Nov11_2012_81.json'
    csv_file_location = 'EC2_pricing.csv'
    data_parsed = JsonDataLoad(json_file_location).load_file()
    extracted_price_csv = PricingValidator.validate(csv_file_location)
    l = []
    for i in range(len(data_parsed)):
        source = data_parsed[i]['source']
        if source not in l:
            l.append(source)
    for i in l:
        Main(i,json_file_location,csv_file_location,'mean','No Upfront',extracted_price_csv,'convertible')