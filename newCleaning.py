import os

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
        "Total CH1",
        "Total CH2",
        "Total PR7",
        "Total CH6",
        "Total CH7"
        ]

for beginningOfField in beginningsOfFields:
    outputFile = beginningOfField[6::] + ".csv"
    file = f"{beginningOfField[6::]}/{beginningOfField[6::]}.1.csv"
    with open(file, "r") as f:
        for line_number, line in enumerate(f, start=1):
            if beginningOfField[:-2] in line:
                with open(outputFile,"w") as f1:
                     f1.write("%s" % line) 
                break


