#!/usr/bin/python2.6

import drqueue.base.libdrqueue as drqueue
from baseprocess import daemonization
import time

daemonization()

while 1:
    try:
        for client in drqueue.request_computer_list(drqueue.CLIENT):
            client.add_pool('mentalray', 0)
    except Exception:
        pass

    time.sleep(60)
