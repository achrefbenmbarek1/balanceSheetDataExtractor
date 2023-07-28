from pdfExtractor.DataFormatter import DataFormatter
from pdfExtractor.DefaultDataFormatter import DefaultDataFormatter
from pdfExtractor.BiatDataFormatter import BiatDataFormatter
from pdfExtractor.DataFormatterFactory import DataFormatterFactory

class DataFormatterFactoryImp(DataFormatterFactory):
    def __init__(self) -> None:
        self.conditions = dict({"BIAT":BiatDataFormatter()})
    def createDataFormatter(self, bankName) -> DataFormatter:
       if bankName in self.conditions:
            return self.conditions[bankName] 
       else:
           return DefaultDataFormatter()
