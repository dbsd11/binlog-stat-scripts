parsebinlog_txt="$1.txt"
parsebinlog_result="$1_$2_$3.txt"
parsebinlog_result_final="$1_$2_$3_final.txt"

rm -rf $parsebinlog_result
rm -rf $parsebinlog_result_final

python parsebinlog.py $*
rm -rf $parsebinlog_txt

sed -ri 's/#[0-9]+ .*/\n\n/g' $parsebinlog_result

sed -ri 's/(\@[0-9]+)=.*/\1=?/g' $parsebinlog_result

awk -v RS="" '{gsub("\n"," ");print}' $parsebinlog_result > $parsebinlog_result_final

sed -i 's/###/ /g' $parsebinlog_result_final

rm -rf $parsebinlog_result
