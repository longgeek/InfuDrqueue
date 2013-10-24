#!/usr/bin/env python2.6

import os
import time

ilo_user = 'Administrator'
ilo_pass = 'Aa123456'

while True:
    time.sleep(900)
    miss_nodes = os.popen("python2.6 /opt/missing_node.py").read().rstrip()
    miss_nodes_ilo = []
    if not eval(miss_nodes):
        pass
        
    else:
        for host in eval(miss_nodes):
            nodes_ilo = os.popen("grep %s /etc/ilo | awk '{print $2}'" % host).read().rstrip()
            miss_nodes_ilo.append(nodes_ilo)
            ilo_status = os.popen("ipmitool -H %s -I lanplus -U %s -P %s chassis power status | awk '{print $NF}'" % (nodes_ilo, ilo_user, ilo_pass)).read().rstrip()
            if ilo_status == 'off':
                os.system("ipmitool -H %s -I lanplus -U %s -P %s chassis power on" % (nodes_ilo, ilo_user, ilo_pass))
            elif ilo_status == 'on':
                os.system("ipmitool -H %s -I lanplus -U %s -P %s chassis power reset" % (nodes_ilo, ilo_user, ilo_pass))
