from urllib.request import urlopen
from bs4 import BeautifulSoup
from .FileNameManiputlation import FileNameManipulation
import re

class FileNamesExtractor():
    def __init__(self, fileNameManipulation:FileNameManipulation) -> None:
       self.fileNamesPerBank = dict() 
       self.urls = ["https://www.bvmt.com.tn/fr/documents/44/18/list","http://www.bvmt.com.tn/fr/documents/26/18/list"]
       self.fileNameManipulation = fileNameManipulation
    
    def extractFileNames(self) -> dict:
        for url in self.urls:
            page = urlopen(url)
            htmlBytes = page.read()
            html = htmlBytes.decode("utf-8")
            doc = BeautifulSoup(html, "html.parser")
            paragraphsWithClassTitle = doc.find_all("p", class_= "titre")
            fileNames = []
            numberOfFilesExtractedFromABank = 0
            rightPointer = 0
            while numberOfFilesExtractedFromABank < 3:
                potentialFileName = paragraphsWithClassTitle[rightPointer].find_all(string = True, recursive = False)
                fileName = re.search(r'.*' + re.escape('individuels') + r'.*',potentialFileName[-1])
                if fileName:
                    fileNames.append(fileName.group()[:-4])
                    numberOfFilesExtractedFromABank += 1
                rightPointer += 1
            
            bankName = self.fileNameManipulation.extractBankName(fileNames[-1][:-4])
            self.fileNamesPerBank[bankName] = fileNames
        return self.fileNamesPerBank
        

