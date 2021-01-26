from meanrightsizer import MeanRightSizer
from medianrightsizer import MedianRightSizer
class ShapeFactory():
    def create_right_sizer(self,rightsize,avg_ram_usage,avg_cpu_usage):
        m1 = MeanRightSizer(avg_ram_usage,avg_cpu_usage)
        m2 = MedianRightSizer(avg_ram_usage,avg_cpu_usage)
        if rightsize == 'mean':
            return m1
        if rightsize == 'median':
            return m2