from pdfExtractor.GeneratePatternBiatImp import GeneratePatternBiatImp


class PatternSelector:
    def __init__(self) -> None:
        self.conditions = dict({"BIAT":GeneratePatternBiatImp()})
    
    def selectPattern(self,bankName:str):
       if bankName in self.conditions:
        return self.conditions[bankName].generatePattern() 
       else:
           return [ "AC3", "PA3", "PR1", "PR2", "PR3", "PR4", "CH1", "CH2", "PR7", "CH6", "CH7", "PR5", "PR6" ]
