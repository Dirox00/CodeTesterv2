#!/bin/bash

attempt_file=$1
correct_file=$2
generator_file=$3

for (( i=0; i<10; i++ ))
do
    echo Running test $i
    echo ---------------
    ./$generator_file > test
    attemp=$(./$attempt_file < test)
    true=$(./$correct_file < test)
    if [[ $attemp != $true ]]
    then
        ./$attempt_file < test > attempt
        ./$correct_file < test > correct
        echo "Test $i has failed" > result
        exit
    fi
done

echo "All tests passed" > result
