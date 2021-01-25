import abc
class RightSizer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def RightSize():
        pass