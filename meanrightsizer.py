from abstractrightsizerclass import RightSizer
class MeanRightSizer(RightSizer):
    
    def __init__(self,get_ram,list_of_ram_gb,get_cpu,list_of_cpu_cores,os):
        self.get_ram = get_ram
        self.list_of_ram_gb =list_of_ram_gb
        self.get_cpu = get_cpu
        self.list_of_cpu_cores = list_of_cpu_cores
        self.os = os
        
    
    #this method calculates the right sizing of the resources            
    def RightSize(self):
        '''the average value is calculated and ckecked if it is less than 40 percent of value, if it is
           we reduce it to half for both ram_gb and cpu_cores
           Reference: https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/tips-for-right-sizing-your-workloads.html
        '''
        total_length_ram_and_cpu = len(self.list_of_ram_gb)
        self.avg_ram_usage = sum(self.list_of_ram_gb) / (total_length_ram_and_cpu)
        self.avg_cpu_usage = sum(self.list_of_cpu_cores) / (total_length_ram_and_cpu)
        
        
        
        if self.avg_ram_usage >= 90:
            self.get_ram *=2
        if self.avg_ram_usage <= 50:
            self.get_ram /=2
        if self.avg_cpu_usage <= 50:
            self.get_cpu /=2
        if self.avg_cpu_usage >= 90:
            self.get_cpu *=2
        return self.get_ram, self.get_cpu, self.os