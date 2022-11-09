for file in $(find $1 -type f)
do
  viruses=hash_list.txt
  hashFile=$(md5sum $file | cut -d ' ' -f1) 
  cross=$(grep $hashfile $viruses)
  echo aa
  if  [  -n "$cross" ]; then echo "Found a virus"
  else echo "You are safe";
  
  fi
  done
