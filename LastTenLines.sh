#!/bin/bash

echo Please enter your filename :
read file

if [[ -f $file ]]
then
    while IFS= read line
    do
    	# display $line or do something with $line
    	echo "$line"
    done < <(tail -n 10 $file)
    
else 
    echo There is no such a file with the filename that you entered!
    
fi

