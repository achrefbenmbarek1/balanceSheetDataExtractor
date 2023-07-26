from urllib.request import urlopen
from bs4 import BeautifulSoup
from pdfExtractor.FileLinkManipulator import FileLinkManipulator
from pdfExtractor.FileLinksExtractor import FileLinksExtractor

import re


class FileLinksExtractorImp(FileLinksExtractor):
    def __init__(self, fileLinkManipulator:FileLinkManipulator) -> None:
       self.fileLinksPerBank = dict() 
       self.urls = ["https://www.bvmt.com.tn/fr/documents/44/18/list","http://www.bvmt.com.tn/fr/documents/26/18/list"]
       self.fileLinkManipulator = fileLinkManipulator
    
    def extractFileLinks(self) -> dict:
        for url in self.urls:
            page = urlopen(url)
            htmlBytes = page.read()
            html = htmlBytes.decode("utf-8")
            doc = BeautifulSoup(html, "html.parser")
            paragraphsWithClassTitle = doc.find_all("p", class_= "titre")
            fileLinksBilanIndividuel = []
            numberOfFilesExtractedFromABank = 0
            rightPointer = 0
            while numberOfFilesExtractedFromABank < 3:
                fileLinks = paragraphsWithClassTitle[rightPointer].find_all(string = True, recursive = False)
                fileLinkBilanIndividuel = re.search(r'.*' + re.escape('individuels') + r'.*',fileLinks[-1])
                if fileLinkBilanIndividuel:
                    fileLinksBilanIndividuel.append(fileLinkBilanIndividuel.group()[:-5])
                    numberOfFilesExtractedFromABank += 1
                rightPointer += 1
                
            bankName = self.fileLinkManipulator.extractBankName(fileLinksBilanIndividuel[-1][:-5])
            self.fileLinksPerBank[bankName] = fileLinksBilanIndividuel
        return self.fileLinksPerBank
        

