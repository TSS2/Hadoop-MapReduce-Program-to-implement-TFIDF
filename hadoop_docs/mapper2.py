#!/usr/bin/env python
import os
import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    #filename = os.environ["map_input_file"]
    #print (filename,1)
    Line = line.strip()
    key = line.split(' - ')
    temp = key[1]
    filenames = re.split(r'\t+',temp)
    value = str(key[0])+' - '+(str(filenames[1])).rstrip('\n')
    file_name = filenames[0]
    print '%s\t%s' % (file_name, value)
    #Print filenames
