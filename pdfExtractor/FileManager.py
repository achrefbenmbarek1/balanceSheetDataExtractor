import re
import shutil
import os
from FileNameManiputlation import FileNameManipulation
import tabula
from pdfExtractor.PatternSelector import PatternSelector
from FileNamesExtractor import FileNamesExtractor

# beginningsOfFields = [ "Total PA3", "Total AC3", "Total PR1", "Total PR2", "Total PR3", "Total PR4", "Total CH 1", "Total CH2", "Total PR7", "Total CH6", "Total CH7", "Total PR5", "Total PR6" ]

class FileManager():
    def __init__(self ,fileNameManipulation:FileNameManipulation, fileNamesExtractor:FileNamesExtractor, patternSelector:PatternSelector) -> None:
        # self.beginningsOfFields = beginningsOfFields
        # self.file = "tables.csv"
        self.files = fileNamesExtractor.extractFileNames()
        self.patternSelector = patternSelector
        self.fileNameManipulation = fileNameManipulation
        
    
        
    def write(self, fileUrl, outputDirectory:str):
        bankName:str = self.fileNameManipulation.extractBankName(fileUrl)
        beginningsOfFields = self.patternSelector.selectPattern(bankName)
        fileFullName = self.fileNameManipulation.generateFileName(fileUrl[:-1])
        fileName = fileFullName[fileFullName.rfind('/') + 1:]
        fileNameCsv = fileName[:-4]+'.csv'
        print(fileNameCsv)
        tabula.io.convert_into(fileFullName,fileNameCsv,output_format="csv",pages="all")
        for beginningOfField in beginningsOfFields:
            outputFile = os.path.join(outputDirectory, beginningOfField + ".csv") 
            with open(fileNameCsv, "r") as f:
                for lineNumber, line in enumerate(f, start=1):
                    valuableData = re.search( r'.*' + re.escape(beginningOfField) + r'.*' ,line) 
                    if(valuableData):
                        with open(outputFile,"w") as f1:
                             f1.write("%s" % valuableData.group()) 
                        break
                    else:
                        print("searching ...")

    def writeFiles(self):
        for bankName in self.files:
            for fileName in self.files[bankName]:
                outputDirectory = bankName + fileName[-11:].replace('/','-')
                isExistingDirectory = os.path.exists(outputDirectory)
                if(not isExistingDirectory):
                    os.makedirs(outputDirectory)
                    print(outputDirectory)
                    
                print(fileName)
                self.write(fileName, outputDirectory);
            
    def remove(self):
        shutil.rmtree(self.files[2][-5:-1]) 
       
