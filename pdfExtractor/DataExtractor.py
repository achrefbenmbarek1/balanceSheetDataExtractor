import tabula
import re

class DataExtractor():
    def __init__(self) -> None:
       self.path =  "https://www.bvmt.com.tn/sites/default/files/societes/atb/etats-financiers/atb-etats-financiers-annuels-31-12-2022.pdf"
       self.beginningsOfFields = ["PA3" ,"AC3", "PR1", "PR2", "PR3", "PR4", "CH 1", "CH2", "PR7", "CH6", "CH7", "PR5", "PR6"]

    
    def extractData(self) :
        tabula.io.convert_into(self.path,"tables2.csv",output_format="csv",pages="all")
        output = "output1"
        for beginningOfField in self.beginningsOfFields:
            with open("tables2.csv", "r") as f:
                for line_number, line in enumerate(f, start=1):
                    valuableData = re.search( r'.*' + re.escape(beginningOfField) + r'.*' ,line) 
                    if(valuableData):
                        output = output[:-1] +str(int(output[-1])+1)
                        outputFile = output+ ".csv"
                        print(outputFile)
                        with open(outputFile,"w") as f1:
                             f1.write("%s" % valuableData.group()) 
                        break
                    else:
                        print("searching ...")



