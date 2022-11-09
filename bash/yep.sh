for file in $(find $1 -type f)
do
  hashFile= $(md5sum file | cut -d ' ' -f1)
  #virusline=$(cat hash_list.txt | while read line || [[ -n $line ]])
   #if  [ hashFile == virusline ] then echo "A virus was detected"
   #else echo "You are safe"
   #exit; fi
   #done
   for i in $(cat hash_list.txt | cut -d ' ' -f1)
   
   do 
       if [ "${hashFile}" == "${i}" ]
       then echo "$i is a virus"
       fi
 done  
 done
 echo "You are safe"
