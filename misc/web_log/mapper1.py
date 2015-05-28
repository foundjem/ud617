#!/usr/bin/python

# Input is in Common Log Format
#
# Key is the request
# Value is 1 (we just want to count the hits per file on the Web site)
# We write them out to standard output, separated by a tab

import sys
import re

for line in sys.stdin:
    match = re.search(r'"(?P<request>.*?)"',line)
    if match:
        request =  match.group(1)
        query = request.split()
        if len(query)==3:
             print "{0}\t{1}".format(query[1], 1)

