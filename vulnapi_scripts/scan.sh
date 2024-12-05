#!/bin/bash
echo $1 > url.txt
echo $2 > type.txt
vulnapi scan curl $1 > inter.txt
cat inter.txt | grep High | awk -F'|' '{print $(NF-1)}' > High.txt
cat inter.txt | grep Medium | awk -F'|' '{print $(NF-1)}' > Medium.txt
cat inter.txt | grep Low | awk -F'|' '{print $(NF-1)}' > Low.txt
cat inter.txt | grep Info | awk -F'|' '{print $(NF-1)}' > Info.txt
