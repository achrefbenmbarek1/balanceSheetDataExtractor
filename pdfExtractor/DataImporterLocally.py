import pdfplumber
import requests
from pdfExtractor.FileLinkManipulator import FileLinkManipulator
import os

class DataImporterLocally:
    def __init__(self, fileLinkManipulator:FileLinkManipulator) -> None:
        self.fileLinkManipulator = fileLinkManipulator
        
    def importDataLocally(self, fileLink) -> list:
            fileUrl = self.fileLinkManipulator.generateFileUrl(fileLink)
            response = requests.get(fileUrl)
            data = []
            if response.status_code == 200:
                fileName = self.fileLinkManipulator.generateFileName(fileLink)
                filePath = os.path.join("Data",fileName) 
                print(fileName)
                
                with open(filePath, "wb") as f:
                    f.write(response.content)
                    print("PDF downloaded successfully!")
                    
                with pdfplumber.open(filePath) as pdf:
                    for pageNumber in range(4):
                        page = pdf.pages[pageNumber]
                        data += page.extract_text().split('\n')
                        # print(f"Page {pageNumber + 1}:\n{data}\n")
            if(not len(data)):
                raise Exception("a problem occured maybe check your internet connection")
            # print(f"{data}\n")
            return data
            

