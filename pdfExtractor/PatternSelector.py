from pdfExtractor.CommandGeneratePatternBtImp import CommandGeneratePatternBtImp


class PatternSelector:
    def __init__(self) -> None:
        self.conditions = dict({"BT":CommandGeneratePatternBtImp()})
    
    def selectPattern(self,fileName:str):
       if fileName in self.conditions:
        return self.conditions[fileName].execute() 
       else:
           return ["PA3" ,"AC3", "PR1", "PR2", "PR3", "PR4", "CH 1", "CH2", "PR7", "CH6", "CH7", "PR5", "PR6"]
