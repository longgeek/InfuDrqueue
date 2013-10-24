#!/bin/bash

while sleep 15
do
    [ ! -e /infovolumes/logs/client-reconnection.sh ] && cp /root/client-reconnection.sh /infovolumes/logs/
done
