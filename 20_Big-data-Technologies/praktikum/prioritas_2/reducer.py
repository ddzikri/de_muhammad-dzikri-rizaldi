#!/usr/bin/env python

from operator import itemgetter
import sys

number_of_data = 0 
sum_of_data = 0

for line in sys.stdin:
    line = line.strip()
    number_of_data +=1
    sum_of_data += int(line)
print('%f' % (sum_of_data/number_of_data))
