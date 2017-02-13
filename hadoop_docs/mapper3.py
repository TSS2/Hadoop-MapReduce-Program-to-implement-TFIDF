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
    #print key
    word = key[0]
    tmp_key = key[1]
    filenames = re.split(r'\t+',tmp_key)
    #print filenames
    file_name = filenames[0]
    tmp = filenames[1].split('/')
    n = tmp[0]
    N = tmp[1]
    value = str(file_name)+' - '+str(n)+'/'+str(N).rstrip('\n')+'&'+str(1)
    print '%s\t%s' % (word, value)
