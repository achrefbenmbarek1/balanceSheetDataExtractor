from pdfExtractor.CommandExtractData import CommandExtractData
class Invoker():
    def __init__(self, commandExtractData: CommandExtractData) -> None:
        self.commandExtractData = commandExtractData

    def extractData(self) -> None:
        self.commandExtractData.execute()

    def removeData(self) -> None:
        self.commandExtractData.unexecute()
