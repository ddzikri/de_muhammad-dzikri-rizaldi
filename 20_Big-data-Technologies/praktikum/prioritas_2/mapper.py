#!/usr/bin/env python

import sys

# Membaca input dari stdin
for line in sys.stdin:
    line = line.strip() # remove leading and trailing white spaces
    try:
        print('%s' % (line))
    except:
        pass