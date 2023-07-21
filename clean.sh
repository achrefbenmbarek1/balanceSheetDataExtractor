#!/bin/bash

words=("dépôts de la clientèle"
"Crédit de la clientèle"
"Créances sur la clientèle"
"intérêts produit" 
"commission produit"
"frais personnel" 
"charge general d'exploitation" 
"intérêts charge" 
"commission charge"
"gains sur portfeuil"
"revenu du portfeuil"
)
codes=("AC3 " 
  "PA3 "
)
limits=(
  "AC4"
  "PA4"
  )
file="output.txt"

  # matched_line=$(grep -inm 1 "^$word" "$file")
  #word="comptes ordinaires débiteurs"
  # echo $matched_line  |  sed 's/,/ /g' 
for str in "${codes[@]}"; do
  matched_line=$(grep -inm 1 "^$str" "$file")
  echo $matched_line  |  sed 's/,/ /g' >> /dev/null 
  start=$(echo "$matched_line" | grep -o '[0-9]\+' | head -n 1)
  echo "$start"
  done

