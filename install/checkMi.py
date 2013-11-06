#!/usr/bin/env python2.6

import sys
import os
import shutil

src_file = sys.argv[1]

with open(src_file) as f:
    tmp_file = src_file + '_tmp'
    with open(tmp_file, 'w') as tmp_f:
        for line in f.readlines():
            if 'filename' in line:
                target = ''.join([i if i != '\\' else ',' for i in line]).split(',')[-1]
                tmp_f.write(line[:line.find('"')+1]+target)
            elif 'clip true' in line:
                tmp_f.write('\n')
            else:
                tmp_f.write(line)

shutil.move(tmp_file, src_file)
