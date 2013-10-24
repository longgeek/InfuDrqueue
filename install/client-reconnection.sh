#!/bin/bash

while sleep 60
do
    num=$(ps aux | grep 'slave' | wc -l)
    if [ "$num" -lt "1" ]; then
        kill -9 $(ps aux | grep slave | grep -v 'grep' | awk '{print $1}')
        nohup slave -f > /dev/null 2>&1 &
    fi
done
#while sleep 60
#do
#    ps aux | grep 'slave'
#    if [ "$?" != "0" ]; then
#        nohup slave -f > /dev/null 2>&1 &
#    fi
#done

