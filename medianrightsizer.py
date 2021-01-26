from abstractrightsizerclass import RightSizer
class MedianRightSizer(RightSizer):
    
    def __init__(self,list_of_ram_gb,list_of_cpu_cores):

        self.list_of_ram_gb =list_of_ram_gb
        self.list_of_cpu_cores = list_of_cpu_cores

    
    #this method calculates the right sizing of the resources            
    def RightSize(self):
        '''the average value is calculated and ckecked if it is less than 40 percent of value, if it is
           we reduce it to half for both ram_gb and cpu_cores
           Reference: https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/tips-for-right-sizing-your-workloads.html
           '''
        total_length_ram_and_cpu = len(self.list_of_ram_gb)
        
        self.list_of_ram_gb.sort()
        self.list_of_cpu_cores.sort()
        
        if total_length_ram_and_cpu % 2 == 0: 
            median1_ram = self.list_of_ram_gb[total_length_ram_and_cpu//2] 
            median2_ram = self.list_of_ram_gbm[total_length_ram_and_cpu//2 - 1] 
            self.median_ram_usage = (median1_ram + median2_ram)/2
            
            median1_cpu = self.list_of_cpu_cores[total_length_ram_and_cpu//2] 
            median2_cpu = self.list_of_cpu_cores[total_length_ram_and_cpu//2 - 1] 
            self.median_cpu_usage = (median1_cpu + median2_cpu)/2
        else: 
            self.median_ram_usage = self.list_of_ram_gb[total_length_ram_and_cpu//2] 
            self.median_cpu_usage = self.list_of_cpu_cores[total_length_ram_and_cpu//2]
        
        
#         if self.median_ram_usage >= 90:
#             self.get_ram *=2
#         if self.median_ram_usage <= 50:
#             self.get_ram /=2
#         if self.median_cpu_usage <= 50:
#             self.get_cpu /=2
#         if self.median_cpu_usage >= 90:
#             self.get_cpu *=2
        return self.median_ram_usage, self.median_cpu_usage