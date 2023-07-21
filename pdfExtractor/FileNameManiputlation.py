from abc import ABC, abstractmethod

class FileNameManipulation(ABC):
    @abstractmethod
    def extractBankName(self, fileUrl:str) -> str:
        pass
    
    @abstractmethod
    def generateFileName(self, extractedFileName:str) -> str:
        pass

