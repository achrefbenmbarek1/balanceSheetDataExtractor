from pdfExtractor.CommandExtractData import CommandExtractData
from .FileManager import FileManager

class CommandExtractDataImp(CommandExtractData):
    def __init__(self, fileManager:FileManager) -> None:
        self.fileManager = fileManager
        
    def execute(self) -> None:
        self.fileManager.writeFiles()

    def unexecute(self) -> None:
        self.fileManager.remove()
