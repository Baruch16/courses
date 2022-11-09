
for f in $1*
do
 if [ -d ${f} ]
  then echo "${f} is a directory"
 elif [ -f ${f} ]
  then echo "${f} is a file"
else echo "${f} is not valid" 
exit;fi
 
done 
