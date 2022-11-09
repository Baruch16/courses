for file in $(find $1 -type f)
do
  hashFile= (md5sum file | cut -d ' ' -f1)
  cat hash_list.txt | while read line || [[ -n $line ]]
    do 
     if [ hashFile == "$( cut -d ' ' -f1 $line )" ]; then echo "is virus"
     else echo " You are protected"
      exit;fi
      done 
 done       
