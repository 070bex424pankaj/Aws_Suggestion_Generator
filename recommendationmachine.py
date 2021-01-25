from rightsizer import RightSizer
class RecommendationMachine():
           
          
    def get_right_sized_data(self,get_ram, avg_ram_usage, get_cpu, avg_cpu_usage, os):
        ram_gb, cpu_cores, os =  RightSizer().RightSize(get_ram, avg_ram_usage, get_cpu, avg_cpu_usage, os)
        return ram_gb, cpu_cores, os
        
        
    def filter_based_on_preference(self, extracted_price_csv, ram_gb, cpu_cores, os):
        #we filter out the data based on right sizing of resources and the selection is done only on no upfront
        #print(self.ram_gb,self.cpu_cores,self.os)
        self.filtereddata =  extracted_price_csv[(extracted_price_csv['Memory'] >= ram_gb) & 
                                           (extracted_price_csv['vCPU'] >= cpu_cores) & 
                                           (extracted_price_csv['Operating System'] == os) &
                                           (extracted_price_csv['PurchaseOption'] == 'No Upfront')]
        return self.filtereddata
    def group_by(self,filtereddata):
        #we group by SKU
        f_g = {'PricePerUnit': 'sum', 'Instance Type': 'first', 'vCPU': 'first', 'Operating System': 'first', 'Memory':'first','PurchaseOption':'first'}
        filtereddata = filtereddata.groupby(['SKU','OfferTermCode','LeaseContractLength'], as_index=False).agg(f_g)
        return filtereddata
    
    def select_minimum(self,filtereddata):
        #selection of minimim price based on Priceperunit. All prices are compared with 1 year
        self.minimum_instance_row = filtereddata[filtereddata.PricePerUnit == filtereddata.PricePerUnit.min()]
        return(self.minimum_instance_row)
        #print(self.min.head())