from abc import ABC, abstractmethod

class FileLinkManipulator(ABC):
    @abstractmethod
    def extractBankName(self, fileLink:str) -> str:
        pass
    
    @abstractmethod
    def generateFileName(self, fileLink:str) -> str:
        pass
    
    @abstractmethod
    def generateFileUrl(self, fileLink:str) -> str:
        pass
    
    @abstractmethod
    def generateOutputDirectory(self, fileLink:str) -> str:
        pass

