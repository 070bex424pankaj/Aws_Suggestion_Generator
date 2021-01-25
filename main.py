from processingextractedcsvfile import PreProcessingExtractedCsvFile
from recommendationmachine import RecommendationMachine
from usagesummarygenerator import UsageSummaryGenerator
from jsondataload import JsonDataLoad

class Main():
    def __init__(self,source,json_file_location,csv_file_location,rightsize):
        self.rightsize = rightsize
        
        self.preprocessingobject = PreProcessingExtractedCsvFile(csv_file_location)
        self.u = UsageSummaryGenerator(source,json_file_location)
        self.r =RecommendationMachine()
        #replace null value of Memory with zero
        self.preprocessingobject.repalce_null_values('Memory')
        #replace not available values with zero
        self.preprocessingobject.repalce_NA_values('Memory')
        #extract number from Memory column. for eg extract 15 from 15 GiB
        self.preprocessingobject.extract_only_number('Memory')
        #convert to float value 
        self.preprocessingobject.convert_to_float('Memory')
        #extract number from LeaseContractLengyh column
        self.preprocessingobject.extract_only_number('LeaseContractLength')
        #replace null values with zero for LeaseContractLength
        self.preprocessingobject.repalce_null_values('LeaseContractLength')
        #replace not available values with zero for LeaseContractLength
        self.preprocessingobject.repalce_NA_values('LeaseContractLength')
        #convert to float for the values of LeaseContractLength
        self.preprocessingobject.convert_to_float('LeaseContractLength')
        #select only hrs or quantity value from unit column
        self.preprocessingobject.select_only_hrs_or_quantity()
        #convrt upfront 3 yrs price to 1 yr for standard scaling
        self.preprocessingobject.convert_3yrs_to_hr()
        #convert unit hrs of noupfront and partial upfront to 1 year for standard scaling
        self.preprocessingobject.convert_1yr_to_hr()    
        #convert to integer for the value of Priceperunit column
        extracted_price_csv = self.preprocessingobject.convert_to_float("PricePerUnit")
        
        #old

        get_ram,avg_ram_usage,get_cpu,avg_cpu_usage, os = self.u.calculate_mean_usage()        
        ram_gb, cpu_cores, os = self.r.get_right_sized_data(self.rightsize,get_ram, avg_ram_usage, get_cpu, avg_cpu_usage, os)    
        filtereddata= self.r.filter_based_on_preference(extracted_price_csv, ram_gb, cpu_cores, os)
        filtereddata= self.r.group_by(filtereddata)
        print(self.r.select_minimum(filtereddata))
            

#it creates two objects for two sources and calls the run_function of the main class
if __name__ == "__main__":
    #create two objects for two different source
    json_file_location = 'Nov11_2012_81.json'
    csv_file_location = 'EC2_pricing.csv'
    data_parsed = JsonDataLoad(json_file_location).load_file()
    l = []
    for i in range(len(data_parsed)):
        source = data_parsed[i]['source']
        if source not in l:
            l.append(source)
    for i in l:
        Main(i,json_file_location,csv_file_location,'mean')