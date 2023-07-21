from abc import ABC, abstractmethod

class CommandExtractBna(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def unexecute(self):
        pass

