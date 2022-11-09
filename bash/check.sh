for j in cat Downloads/hash_list.txt | while read line || [[ -n $line ]];
    do 
       if [ md5sum(${d}) == $line ]
         echo "is virus"
          else echo "You are safe"
          exit; fi
 done     
