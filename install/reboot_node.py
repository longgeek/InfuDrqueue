#!/usr/bin/env python2.6

import os, logging, time
import drqueue.base.libdrqueue as drqueue
import socket

ilo_user = 'Administrator'
ilo_pass = 'Aa123456'

COMPARISON_LIST = [
    'C01-01', 'C01-02', 'C01-03', 'C01-04',
    'C01-05', 'C01-06', 'C01-07', 'C01-08',
    'C01-09', 'c01-10', 'c01-11', 'c01-12',
    'C01-13', 'c01-14', 'c01-15', 'c01-16',
    'C02-01', 'C02-02', 'C02-03', 'C02-04',
    'C02-05', 'C02-06', 'C02-07', 'C02-08',
    'C02-09', 'C02-10', 'C02-11', 'C02-12',
    'C02-13', 'C02-14', 'C02-15', 'C02-16',
    'C03-01', 'C03-02', 'C03-03', 'C03-04',
    'C03-05', 'C03-06', 'C03-07', 'C03-08',
    'C03-09', 'C03-10', 'C03-11', 'C03-12',
    'C03-13', 'C03-14', 'C03-15', 'C03-16',
    'C04-01', 'C04-02', 'C04-03', 'C04-04',
    'C04-05', 'C04-06', 'C04-07', 'C04-08',
    'C04-09', 'C04-10', 'C04-11', 'C04-12',
    'C04-13', 'C04-14', 'C04-15', 'C04-16',
    'C05-01', 'C05-02', 'C05-03', 'C05-04',
    'C05-05', 'C05-06', 'C05-07', 'C05-08',
    'C05-09', 'C05-10', 'C05-11', 'C05-12',
    'C05-13', 'C05-14', 'C05-15', 'C05-16',]

def initLog():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] [%(asctime)s] [%(process)d] [%(module)s.%(name)s.%(funcName)s] [%(message)s]",
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='/opt/reboot_node.log',
        filemode='a',
    )
    logger = logging.getLogger(name='rebootLog')

    return logger

def main():
    while True:
        logger.info('starting...')
        try:
            logger.info('get missed node...')
            miss_nodes = [socket.gethostbyname(c) for c in
                set(COMPARISON_LIST) - set([i.hwinfo.name for i in
                drqueue.request_computer_list(drqueue.CLIENT)])]
            miss_nodes_ilo = []
            if not miss_nodes:
                logger.info('no died node.')
                pass
                
            else:
                for host in miss_nodes:
                    logger.info('reboot host: %s' % host)
                    nodes_ilo = os.popen("grep %s /etc/ilo | awk '{print $2}'" % host).read().rstrip()
                    miss_nodes_ilo.append(nodes_ilo)
                    ilo_status = os.popen("ipmitool -H %s -I lanplus -U %s -P %s chassis power status | awk '{print $NF}'" % (nodes_ilo, ilo_user, ilo_pass)).read().rstrip()
                    if ilo_status == 'off':
                        os.system("ipmitool -H %s -I lanplus -U %s -P %s chassis power on" % (nodes_ilo, ilo_user, ilo_pass))
                    elif ilo_status == 'on':
                        os.system("ipmitool -H %s -I lanplus -U %s -P %s chassis power reset" % (nodes_ilo, ilo_user, ilo_pass))
            logger.info('reboot finished.')

        except Exception, e:
            logger.error(e.message)
            logger.error(e)
            pass

        logger.info('waitting...')
        time.sleep(900)

if __name__ == '__main__':
    logger = initLog()
    main()
