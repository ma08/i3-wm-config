#!/bin/bash
while [ "true" ]
do
  used="$(free -m | sed '3q;d' | sed 's/.*cache:\s*\([0-9]*\)\s.*/\1/')"
  cmp="$(echo "$used > 2900" | bc)" 
  #echo $cmp
  if [[ "$cmp" == "1" ]]; then
    #echo "aa"
    notify-send "$used MB of RAM is being used. Wake up."
  fi
  sleep 5
done

