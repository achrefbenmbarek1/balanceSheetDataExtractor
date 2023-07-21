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
codes=("Note 2.3" 
  "Note 3.3"
)
file="tables.csv"

  # matched_line=$(grep -inm 1 "^$word" "$file")
  #word="comptes ordinaires débiteurs"
  # echo $matched_line  |  sed 's/,/ /g' 
for str in "${codes[@]}"; do

  matched_line=$(grep -inm 1 "^$str" "$file")
  start=$(echo "$matched_line" | grep -o '[0-9]\+' | head -n 1) 
# end=$(echo "$str" | awk 'BEGIN{FS=OFS=""} {for(i=1;i<=length;i++){if($i~/[0-9]/){$i=(substr($i,1)+1); break}}}1')
end=$(echo "$str" | awk 'BEGIN{FS=OFS="."} {if ($1 ~ /Note [0-9]+\.[0-9]+/) {$2+=0.1}} {print $1"."$2+1}')
limitLine=$(grep -in -F -m 1 -- "$end" "$file" | cut -d ':' -f 1)

sed -n "$(($start+4)),$(($limitLine-1)) p" "$file" >> "$str.txt"  
done

