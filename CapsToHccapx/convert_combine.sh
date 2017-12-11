#!/bin/bash
FILES=./*.cap
NETWORKS="NETWORK1 NETWORK2 GUESTNETWORK"
for network in $NETWORKS
do
  #echo $network
  for f in $FILES
  do
    #echo $f
    ~/tools/hashcat-utils/src/cap2hccapx.bin $f $f-temp.hccapx $network
  done
done
HCCAPX=./*.hccapx
for i in $HCCAPX
do
  cat "$i" >> combined.hccapx
  rm "$i"
done