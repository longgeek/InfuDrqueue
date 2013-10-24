#!/usr/bin/env python

from baseprocess import daemonization
import subprocess, time

daemonization()

cmd = "compinfo.Linux.x86_64 -l| awk -F 'Name: ' '{print $2}'"

while 1:
    pp = subprocess.Popen(cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    txt = pp.stdout.read()
    with open('/opt/complist.txt', 'w') as f:
        f.write(txt)
    time.sleep(60)
