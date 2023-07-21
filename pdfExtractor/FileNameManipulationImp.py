from .FileNameManiputlation import FileNameManipulation

class FileNameManiputlationImp(FileNameManipulation):
    def extractBankName(self, fileUrl: str):
        indexOfTheBeginningOfTheName = fileUrl.find('-')
        indexOfTheEndOfTheName = fileUrl.rfind('-')
        fileName = fileUrl[indexOfTheBeginningOfTheName + 1:indexOfTheEndOfTheName-1]
        return fileName
    
    def generateFileName(self,extractedFileName:str) -> str:
        firstHyphen = extractedFileName.find('-')
        lastHyphen = extractedFileName.rfind('-')
        generatedFileName = extractedFileName[firstHyphen + 1:lastHyphen-1].lower() + '-' + extractedFileName[lastHyphen + 2].lower() + extractedFileName[lastHyphen + 3:].replace('au ','').replace(' ','-').replace('/','-') + '.pdf'
        fullPathFileName = "http://www.bvmt.com.tn/sites/default/files/societes/" + self.extractBankName(extractedFileName).lower() + '/etats-financiers/' + generatedFileName
        return fullPathFileName

