from abc import ABC, abstractmethod

class CommandExtractData(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def unexecute(self):
        pass

