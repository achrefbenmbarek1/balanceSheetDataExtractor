from abc import ABC, abstractmethod

class CommandGeneratePattern(ABC):
    @abstractmethod
    def execute(self):
        pass
    
