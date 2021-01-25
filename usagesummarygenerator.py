from jsondataload import JsonDataLoad
class UsageSummaryGenerator():
    #this method groups the data from all the source together and then passed to calculate function for right sizing
    def __init__(self,source):
        self.value_cpu = 0
        self.value_memory = 0
        self.count = 0
        self.data_parsed = JsonDataLoad().load_file()
        self.get_ram = 0
        self.get_cpu = 0
        self.os = 0
        self.source = source
    
    def calculate_mean_usage(self):
        #check if the source is matched or not
        for i in range(len(self.data_parsed)):
            if self.data_parsed[i]['source'] == self.source:
                self.ram_gb = self.data_parsed[i]['data'][0]['ram_gb']
                self.cpu_cores = self.data_parsed[i]['data'][0]['cpu_cores']
#                 print(self.ram_gb,self.cpu_cores)
                # get operating system from the json file
                if ('Windows' in self.data_parsed[i]['data'][0]['operating_system']):
                    self.os='Windows'
                if ('Linux' in self.data_parsed[i]['data'][0]['operating_system']):
                    self.os='Linux'
                self.count +=1
                #it calculates total memory value
                if self.data_parsed[i]['data'][0]['usage'][0]['metric_group'] == 'mem':
                    self.value_memory += self.data_parsed[i]['data'][0]['usage'][0]['metric_value']

                #it calculates total cpu value
                if self.data_parsed[i]['data'][0]['usage'][1]['metric_group'] == 'cpu':
                    self.value_cpu  += self.data_parsed[i]['data'][0]['usage'][1]['metric_value']
        self.avg_ram_usage = float(self.value_memory)/(self.count)
        self.avg_cpu_usage = float(self.value_cpu)/(self.count)
        
        return self.ram_gb, self.avg_ram_usage, self.cpu_cores, self.avg_cpu_usage, self.os
    
                
