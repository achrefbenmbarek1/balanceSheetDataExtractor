import re
import os

words = [
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

notes = [
    "Note 2.3",
    "Note 3.3",
    "Note 5.1",
    "Note 5.2",
    "Note 5.3",
    "Note 5.4",
    "Note 5.5",
    "Note 5.6",
    "Note 5.9",
    "Note 5.10",
    "Note 5.11"
]
index = [
        "AC",
        "PA",
        "HB",
         "PR",
         "CH"
        ] 

file = "tables.csv"

for note in notes:
    
    if note[-2].isnumeric():
        suffix = int(note[-2] + note[-1]) - 4
        section = "CH" + str(suffix)
    elif note[-3] == "5" and int(note[-1]) - int(note[-3]) >= 2:
        suffix = int(note[-1]) - 2
        section = "PR" + str(suffix)
    elif note[-3] == "5" and 0 <= int(note[-1]) - int(note[-3]) <= 1:
        suffix = int(note[-1]) - 4
        section = "CH" + str(suffix)
    else:
        section = index[int(note[-3]) - 2] + note[-1]    
    os.makedirs(section)
    with open(file, "r") as f:
        for line_number, line in enumerate(f, start=1):
            indexCode = ""
            if note in line:
                start = line_number + 4
                stringEnd = re.search(r"\d+\.\d+", note).group() 
                if stringEnd[-1] == "9":
                    stringEnd = stringEnd[:-1] + "10"
                    print(stringEnd)
                else :
                    stringEnd = stringEnd[:-1] + str(int(stringEnd[-1]) + 1)
                limit_line = 0
                with open(file, "r") as f2:
                    for num, line2 in enumerate(f2, start=1):
                        if f"Note {stringEnd}" in line2:
                            limit_line = num
                            break

                extracted_lines = []
                with open(file, "r") as f3:
                    subsectionSuffixIdentifier = 2
                    for num, line3 in enumerate(f3, start=1):
                        if num >= start and num < limit_line:
                            indexCode = section + f".{subsectionSuffixIdentifier - 1}"
                            nextIndexCode = section + f".{subsectionSuffixIdentifier}"
                            if re.match(r".*" + re.escape(nextIndexCode)+r'.*', line3):
                                subsectionSuffixIdentifier += 1
                                # output_file = f"{section}/{indexCode}.csv"
                                output_file = os.path.join(f"{section}",f"{indexCode}.csv")
                                with open(output_file, "w") as output:
                                    output.writelines(extracted_lines)
                                extracted_lines.clear()
                            extracted_lines.append(line3)

                # output_file = f"{section}/{indexCode}.csv"
                output_file = os.path.join(f"{section}", f"{indexCode}.csv")
                with open(output_file, "w") as output:
                    output.writelines(extracted_lines)
                break


