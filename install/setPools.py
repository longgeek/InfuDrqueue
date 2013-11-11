#!/usr/bin/python2.6

import logging
import drqueue.base.libdrqueue as drqueue

def initLog():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] [%(asctime)s] [%(process)d] [%(module)s.%(name)s.%(funcName)s] [%(message)s]",
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='/opt/setPools.log',
        filemode='a',
    )
    logger = logging.getLogger(name='setPoolsLogger')

    return logger

def set_pools():
    while 1:
        try:
            logger.info('setting pools...')
            for client in drqueue.request_computer_list(drqueue.CLIENT):
                try:
                    if len(client.list_pools()) < 2:
                        logger.info('add pool to %s' % client.hwinfo.name)
                        client.add_pool('mentalray', 0)
                except Exception, e:
                    logger.error(e)
                    continue
            logger.info('finished.')
        except Exception, e:
            logger.error(e)
            pass

if __name__ == '__main__':
    logger = initLog()
    set_pools()
