from processingextractedcsvfile import PreProcessingExtractedCsvFile
class PricingValidator():
    def validate(csv_file_location):
        preprocessingobject = PreProcessingExtractedCsvFile(csv_file_location)
        #replace null value of Memory with zero
        preprocessingobject.repalce_null_values('Memory')
        #replace not available values with zero
        preprocessingobject.repalce_NA_values('Memory')
        #extract number from Memory column. for eg extract 15 from 15 GiB
        preprocessingobject.extract_only_number('Memory')
        #convert to float value 
        preprocessingobject.convert_to_float('Memory')
        #extract number from LeaseContractLengyh column
        preprocessingobject.extract_only_number('LeaseContractLength')
        #replace null values with zero for LeaseContractLength
        preprocessingobject.repalce_null_values('LeaseContractLength')
        #replace not available values with zero for LeaseContractLength
        preprocessingobject.repalce_NA_values('LeaseContractLength')
        #convert to float for the values of LeaseContractLength
        preprocessingobject.convert_to_float('LeaseContractLength')
        #select only hrs or quantity value from unit column
        preprocessingobject.select_only_hrs_or_quantity()
        #convrt upfront 3 yrs price to 1 yr for standard scaling
        preprocessingobject.convert_3yrs_to_hr()
        #convert unit hrs of noupfront and partial upfront to 1 year for standard scaling
        preprocessingobject.convert_1yr_to_hr()    
        #convert to integer for the value of Priceperunit column
        extracted_price_csv = preprocessingobject.convert_to_float("PricePerUnit")
        
        return extracted_price_csv
        