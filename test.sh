#!/bin/bash

attempt_file=$1
correct_file=$2
generator_file=$3

for (( i=0; i<50; i++ ))
do
    echo Running test $i
    echo ---------------
    $generator_file > test
    $attempt_file < test > attempt
    $correct_file < test > correct
    diff attempt correct || { echo "Test $i has failed" > result; $attempt_file < test > attempt; $correct_file < test > correct  exit; }
done

echo "All tests passed" > result
