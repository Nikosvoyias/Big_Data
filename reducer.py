# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys


current_ip = None
current_count = 0
current_date = ""
current_time = ""
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line by tabs into fields
    ip, date, time, count = line.split('\t')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
    # assign first line to variables so we can compare
    if not current_ip:
        current_ip = ip
        current_date = date
        current_time = time
        current_count = count        
    # check for duplicates on a serial logic based on hadoop sorting, increase counter and assign again   
    if ip == current_ip:
        if date == current_date and time[0:5] == current_time[0:5]:
            continue
        else:
            current_count += count
            current_date = date
            current_time = time            
            
    else:
        # write result to STDOUT and reassign variables
        print('%s\t%s' % (current_ip, current_count))
        current_count = count
        current_ip = ip
        current_date = date
        current_time = time
        
# print the last ip or ignore if it is a header; sorting guarantees that header will be last
if current_ip == 'ip':
    pass
else:
    print('%s\t%s' % (current_ip, current_count))


        


        

