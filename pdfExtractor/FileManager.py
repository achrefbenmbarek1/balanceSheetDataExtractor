import re
import shutil
import os

from pdfExtractor.PatternSelector import PatternSelector
from FileLinksExtractor import FileLinksExtractor
from pdfExtractor.DataImporterLocally import DataImporterLocally
from pdfExtractor.FileLinkManipulator import FileLinkManipulator
from pdfExtractor.DataFormatterFactory import DataFormatterFactory

class FileManager():
    def __init__(self ,fileLinkManipulator:FileLinkManipulator, fileLinksExtractor:FileLinksExtractor, dataImporterLocally:DataImporterLocally, patternSelector:PatternSelector, dataFormatterFactory:DataFormatterFactory) -> None:
        self.filesLinks = fileLinksExtractor.extractFileLinks()
        self.fileLinkManipulator = fileLinkManipulator
        self.dataImporterLocally = dataImporterLocally
        self.patternSelector = patternSelector
        self.dataFormatterFactory = dataFormatterFactory
        self.outputFileNames = [ "Créances sur la clientèle", "Dépôts et avoirs de la clientèle", "Intérêts et revenus assimilés", "Commissions (en produits)", "Gains sur portefeuille-titres commercial et opérations financières", "Revenus du portefeuille d’investissement", "Intérêts encourus et charges assimilées", "Commissions encourues", "corrections de valeurs sur créances, hors bilan et passif", "corrections de valeurs sur portefeuille d'investissement", "Autres produits d'exploitation", "Frais de personnel", "Charges générales d'exploitation" ]
        
    def write(self, fileLink:str) -> None:
        data = self.dataImporterLocally.importDataLocally(fileLink)
        outputDirectory = self.fileLinkManipulator.generateOutputDirectory(fileLink)
        bankName = self.fileLinkManipulator.extractBankName(fileLink)
        fieldNames = self.patternSelector.selectPattern(bankName)
        index = -1
        for fieldName in fieldNames:
            index += 1
            outputFile = os.path.join(outputDirectory, self.outputFileNames[index] + ".csv") 
            for datum in data:
                potentialDatum = re.search( r'.*' + re.escape(fieldName) + r'.*' ,datum)
                if(potentialDatum):
                    dataFormatter = self.dataFormatterFactory.createDataFormatter(bankName)
                    with open(outputFile,"w") as f1:
                         targetData = dataFormatter.format(potentialDatum.group())
                         f1.write("%s" % targetData) 
                    break
             

    def writeFiles(self) -> None:
        isExistingOutput = os.path.exists("Data")
        if(not isExistingOutput):
            os.makedirs("Data")
        for bankName in self.filesLinks:
            for fileLink in self.filesLinks[bankName]:
                dataDirectory = os.path.join("Data",bankName + fileLink[-11:].replace('/','-'))
                isExistingDirectory = os.path.exists(dataDirectory)
                if(not isExistingDirectory):
                    os.makedirs(dataDirectory)
                    print(dataDirectory)
                print(fileLink)
                self.write(fileLink);
            
    def remove(self) -> None:
         shutil.rmtree("Data") 
    
       
