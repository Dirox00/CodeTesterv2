#!/usr/bin/bash

for (( i=0; i<10; i++ ))
do
    echo Running test $i
    echo ---------------
    ./generator.py > test
    attemp=$(./try.py < test)
    true=$(./correct.py < test)
    if [[ $attemp != $true ]]
    then
        $(./try.py < test > attempt)
        $(./correct.py < test > correct)
        break
    fi
done