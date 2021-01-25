class RightSizer():
    
    def __init__(self):
        pass
    
    #this method calculates the right sizing of the resources            
    def RightSize(self,get_ram,avg_ram_usage,get_cpu,avg_cpu_usage,os):
        '''the average value is calculated and ckecked if it is less than 40 percent of value, if it is
           we reduce it to half for both ram_gb and cpu_cores
           Reference: https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/tips-for-right-sizing-your-workloads.html
           '''
        if avg_ram_usage >= 90:
            get_ram *=2
        if avg_ram_usage <= 50:
            get_ram /=2
        if avg_cpu_usage <= 50:
            get_cpu /=2
        if avg_cpu_usage >= 90:
            get_cpu *=2
        return get_ram, get_cpu, os