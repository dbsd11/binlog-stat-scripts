# 输入line 格式为：id columnName
while read -r line
do
  echo "replace @${line%	*} to ${line#*	}" 
  sed -i "s/@${line%	*}=/${line#*	}=/g" $1 
done
