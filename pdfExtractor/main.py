from pdfExtractor.BankNameExtractorImp import BankNameExtractorImp
from pdfExtractor.CommandExtractData import CommandExtractData
from pdfExtractor.CommandExtractDataImp import CommandExtractDataImp
from pdfExtractor.BankNameExtractor import BankNameExtractor
from pdfExtractor.FileNamesExtractor import FileNamesExtractor
from pdfExtractor.FileManager import FileManager
from pdfExtractor.PatternSelector import PatternSelector
from pdfExtractor.Invoker import Invoker



if __name__ == "__main__":
    # beginningsOfFields = [ "Total PA3", "Total AC3", "Total PR1", "Total PR2", "Total PR3", "Total PR4", "Total CH 1", "Total CH2", "Total PR7", "Total CH6", "Total CH7", "Total PR5", "Total PR6" ]
    # fileNameExtractor:FileNamesExtractor = FileNamesExtractor()
    # fileManager:FileManager = FileManager(beginningsOfFields, fileNameExtractor) 
    # fileManager.debug()
    # commandExtractBna:CommandExtractBna = CommandExtractBnaImp(fileManager)
    # invoker:Invoker = Invoker(commandExtractBna)
    # dataExtractor:DataExtractor = DataExtractor();
    # dataExtractor.extractData()
    bankNameExtractor:BankNameExtractor = BankNameExtractorImp()
    fileNamesExtractor:FileNamesExtractor = FileNamesExtractor(bankNameExtractor)
    fileNamesExtractor.extractFileNames()
    patternSelector:PatternSelector = PatternSelector()
    fileManager:FileManager = FileManager(bankNameExtractor, fileNamesExtractor, patternSelector) 
    commandExtractData:CommandExtractData = CommandExtractDataImp(fileManager)
    dataExtractorInvoker:Invoker = Invoker(commandExtractData)
    dataExtractorInvoker.extractData()
    
