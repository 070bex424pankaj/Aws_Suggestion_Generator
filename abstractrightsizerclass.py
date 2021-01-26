import abc
class RightSizer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def RightSize():
        pass
    def right_size_algorithm(get_ram,avg_ram_usage,get_cpu,avg_cpu_usage):
        if avg_ram_usage >= 90:
            get_ram *=2
        if avg_ram_usage <= 50:
            get_ram /=2
        if avg_cpu_usage <= 50:
            get_cpu /=2
        if avg_cpu_usage >= 90:
            get_cpu *=2
        return get_ram, get_cpu