from pdfExtractor.FileLinkManipulatorImp import FileLinkManipulatorImp
from pdfExtractor.FileLinksExtractorImp import FileLinkManipulator, FileLinksExtractorImp
from pdfExtractor.CommandExtractData import CommandExtractData
from pdfExtractor.CommandExtractDataImp import CommandExtractDataImp
from pdfExtractor.FileLinksExtractor import FileLinksExtractor
from pdfExtractor.FileManager import DataImporterLocally, FileManager, PatternSelector
from pdfExtractor.DataFormatterFactory import DataFormatterFactory
from pdfExtractor.DataFormatterFactoryImp import DataFormatterFactoryImp
from pdfExtractor.Invoker import Invoker

if __name__ == "__main__":
    fileNameManipulation:FileLinkManipulator = FileLinkManipulatorImp()
    fileLinksExtractor:FileLinksExtractor = FileLinksExtractorImp(fileNameManipulation)
    dataImporterLocally:DataImporterLocally = DataImporterLocally(fileNameManipulation)
    patternSelector:PatternSelector = PatternSelector()
    dataFormatterFactory:DataFormatterFactory = DataFormatterFactoryImp()
    fileManager:FileManager = FileManager(fileNameManipulation, fileLinksExtractor, dataImporterLocally, patternSelector,dataFormatterFactory) 
    commandExtractData:CommandExtractData = CommandExtractDataImp(fileManager)
    dataExtractorInvoker:Invoker = Invoker(commandExtractData)
    dataExtractorInvoker.removeData()
    dataExtractorInvoker.extractData()
    
