#! usr/bin/bash
read argument
if [ $(ls $1 |wc -l) \<  $argument ]; then echo "You rock" ; else echo "You are fine"; fi
