from abc import ABC, abstractmethod

class CommandGeneratePatternBiat(ABC):
    @abstractmethod
    def execute(self):
        pass
    
