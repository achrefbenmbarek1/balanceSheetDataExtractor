import re

targetedData = [
    "Dépôts de la clientèle"
    "Crédit de la clientèle",
    "Créances sur la clientèle"
    "intérêts produit",
    "Commissions (en produits)"
    "Frais de personnel"
    "Charges générales d'exploitation"
    "intérêts charge",
    "commission charge",
    "Gains sur portefeuille-titres commercial et opérations financières"
    "Revenus du portefeuille d'investissement"
]
beginningsOfFields = [
        "Total PA3",
        "Total AC3",
        "Total PR1",
        "Total PR2",
        "Total PR3",
        "Total PR4",
        "Total CH 1",
        "Total CH2",
        "Total PR7",
        "Total CH6",
        "Total CH7",
        "Total PR5",
        "Total PR6"
        ]

file = "tables.csv"
for beginningOfField in beginningsOfFields:
    outputFile = beginningOfField[6::] + ".csv"
    with open(file, "r") as f:
        for line_number, line in enumerate(f, start=1):
            valuableData = re.search( r'.*' + re.escape(beginningOfField) + r'.*' ,line) 
            if(valuableData):
                with open(outputFile,"w") as f1:
                     f1.write("%s" % valuableData.group()) 
                break
            else:
                print("still searching ...")
                    


