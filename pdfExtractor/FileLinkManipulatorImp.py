from .FileLinkManipulator import FileLinkManipulator
import os

class FileLinkManipulatorImp(FileLinkManipulator):
    def extractBankName(self, fileUrl: str):
        indexOfTheBeginningOfTheName = fileUrl.find('-')
        indexOfTheEndOfTheName = fileUrl.rfind('-')
        fileName = fileUrl[indexOfTheBeginningOfTheName + 1:indexOfTheEndOfTheName-1]
        return fileName
    
    def generateFileName(self,fileLink:str) -> str:
        firstHyphen = fileLink.find('-')
        lastHyphen = fileLink.rfind('-')
        generatedFileName = fileLink[firstHyphen + 1:lastHyphen-1].lower() + '-' + fileLink[lastHyphen + 2].lower() + fileLink[lastHyphen + 3:].replace('  ',' ').replace(' au','').replace(' ','-').replace('/','-') + '.pdf'
        return generatedFileName

    def generateFileUrl(self, fileLink:str) -> str:
        generatedFileName = self.generateFileName(fileLink)
        fileUrl = "http://www.bvmt.com.tn/sites/default/files/societes/" + self.extractBankName(fileLink).lower() + '/etats-financiers/' + generatedFileName
        return fileUrl

    def generateOutputDirectory(self, fileLink):
        bankName = self.extractBankName(fileLink)
        outputDirectory = os.path.join("Data",bankName + fileLink[-11:].replace('/','-'))
        return outputDirectory

