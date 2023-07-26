import re
import shutil
import os

from pdfExtractor.PatternSelector import PatternSelector
from FileLinksExtractor import FileLinksExtractor
from pdfExtractor.DataImporterLocally import DataImporterLocally
from pdfExtractor.FileLinkManipulator import FileLinkManipulator

class FileManager():
    def __init__(self ,fileLinkManipulator:FileLinkManipulator, fileLinksExtractor:FileLinksExtractor, dataImporterLocally:DataImporterLocally, patternSelector:PatternSelector) -> None:
        self.filesLinks = fileLinksExtractor.extractFileLinks()
        self.fileLinkManipulator = fileLinkManipulator
        self.dataImporterLocally = dataImporterLocally
        self.patternSelector = patternSelector
        # self.fieldNames = [ "Dépôts et avoirs de la clientèle", "Créances sur la clientèle", "Intérêts et revenus assimilés", "Commissions (en produits)", "Gains sur portefeuille-titres commercial et opérations financières", "Revenus du portefeuille d’investissement", "Intérêts encourus et charges assimilées", "Commissions encourues", "corrections de valeurs sur créances, hors bilan et passif", "corrections de valeurs sur portefeuille d'investissement", "Autres produits d'exploitation", "Frais de personnel", "Charges générales d'exploitation" ]
        
    def write(self, fileLink:str) -> None:
        data = self.dataImporterLocally.importDataLocally(fileLink)
        outputDirectory = self.fileLinkManipulator.generateOutputDirectory(fileLink)
        bankName = self.fileLinkManipulator.extractBankName(fileLink)
        fieldNames = self.patternSelector.selectPattern(bankName)
        for fieldName in fieldNames:
            print(fieldName)
            outputFile = os.path.join(outputDirectory, fieldName + ".csv") 
            for datum in data:
                potentialDatum = re.search( r'.*' + re.escape(fieldName) + r'.*' ,datum)
                if(potentialDatum):
                    with open(outputFile,"w") as f1:
                         f1.write("%s" % potentialDatum.group()) 
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
        # shutil.rmtree(self.filesLinks[2][-5:-1]) 
         shutil.rmtree("Data") 
    
       
