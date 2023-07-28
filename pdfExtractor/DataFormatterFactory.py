from abc import ABC, abstractmethod

class DataFormatterFactory(ABC):
    @abstractmethod
    def createDataFormatter(self,bankName):
        pass

