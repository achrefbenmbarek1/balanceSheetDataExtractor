import tabula 

path = "https://www.bvmt.com.tn/sites/default/files/societes/bt/etats-financiers/bt-etats-financiers-annuels-individuels-31-12-2022.pdf"
dfs = tabula.io.read_pdf(path,pages='14')
print(len(dfs))
tabula.io.convert_into(path,"tables.csv",output_format="csv",pages="all")
# for table in dfs:
#     i = (( i+1 ))
#     print("I'm a new table !!!")
#     print(table)
#     # table.to_csv("table"+str(i)+".csv")
