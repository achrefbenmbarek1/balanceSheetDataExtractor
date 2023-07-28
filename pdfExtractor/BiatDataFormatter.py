from pdfExtractor.DataFormatter import DataFormatter

class BiatDataFormatter(DataFormatter):
    def format(self,targetData:str) -> str:
        separatorPosition = targetData.find('-')
        allCharactersAfterTheSeperator =targetData[separatorPosition + 1:].split() 
        allCharactersBeforeTheSeperator = targetData[:separatorPosition + 1]
        numberOfWhiteSpaces = len(allCharactersAfterTheSeperator)
        twoValuesSeparatorPosition = int(numberOfWhiteSpaces / 2) 
        separatedEndAndStartOfTheValues = allCharactersAfterTheSeperator[twoValuesSeparatorPosition] + ',' + allCharactersAfterTheSeperator[twoValuesSeparatorPosition + 1] 
        leftSideOfAllCharactersAfterTheWhiteSpaces =  " ".join(allCharactersAfterTheSeperator[1:twoValuesSeparatorPosition])
        rightSideOfAfterThefirstPartOfTheFirstValue = " ".join(allCharactersAfterTheSeperator[twoValuesSeparatorPosition + 2:])
        formattedData = allCharactersBeforeTheSeperator + allCharactersAfterTheSeperator[0] + ',' + leftSideOfAllCharactersAfterTheWhiteSpaces + ' '+ separatedEndAndStartOfTheValues + ' ' + rightSideOfAfterThefirstPartOfTheFirstValue 
        return formattedData

