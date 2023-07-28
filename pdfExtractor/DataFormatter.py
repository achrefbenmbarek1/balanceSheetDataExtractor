from abc import ABC, abstractmethod

class DataFormatter(ABC):
    @abstractmethod
    def format(self,targetData:str):
        pass
    

