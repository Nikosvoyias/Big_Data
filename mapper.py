# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    
    ip = ""
    date = ""
    time = ""
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line by commas into fields
    splits = line.split(',')
    # assign the fields into variables
    ip = splits[0]     
    date = splits[1]
    time = splits[2]     
    
    # tab-delimited; composite-key and count 1 for every visit output
    print('%s\t%s\t%s\t%s' % (ip,date,time, 1))
