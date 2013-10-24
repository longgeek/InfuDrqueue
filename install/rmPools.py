#!/usr/bin/python2.6

import drqueue.base.libdrqueue as drqueue

drqueue.request_computer_list(drqueue.CLIENT)[0].remove_pool('mentalray', 0)
