#!/bin/bash
collection="collection.txt"

cd vulnapi_scripts

while read -r url category
do
    ./scan.sh $url $category
    cd ..
    python3 ./main.py
    cd vulnapi_scripts
    ./clean.sh
done < "../$collection"
