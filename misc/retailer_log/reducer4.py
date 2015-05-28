#!/usr/bin/python

import sys

count = 0 # the total number of sales
sale_total = 0 # the total sales value

# Loop around the data
# It will be in the format key\tval
# Where key is the entry line number, val is the sale amount

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    count += 1
    sale_total += float(thisSale)

print count, "\t", sale_total

