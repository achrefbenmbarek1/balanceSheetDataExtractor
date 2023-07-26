from abc import ABC, abstractmethod

class FileLinksExtractor(ABC):
    @abstractmethod
    def extractFileLinks(self) -> dict:
        pass

