from meanrightsizer import MeanRightSizer
from medianrightsizer import MedianRightSizer
class ShapeFactory():
    def create_right_sizer(self,rightsize,get_ram, avg_ram_usage, get_cpu, avg_cpu_usage, os):
        if rightsize == 'mean':
            return MeanRightSizer(get_ram, avg_ram_usage, get_cpu, avg_cpu_usage, os).RightSize()
        if rightsize == 'median':
            return MedianRightSizer(get_ram, avg_ram_usage, get_cpu, avg_cpu_usage, os).RightSize()