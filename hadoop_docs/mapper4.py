#!/usr/bin/env python
import os
import sys
import re
import math

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    #filename = os.environ["map_input_file"]
    #print (filename,1)
    Line = line.strip()
    #key = line.split(' - ')
    #print key
    #word = key[0]
    #tmp_key = key[1]
    filenames = re.split(r'\t+',line)
    #print filenames
    word_file_name = filenames[0]
    tmp = filenames[1].split('/')
    n = float(tmp[0])
    tmp_first = tmp[1].split('&')
    N = float(tmp_first[0])
    m = float(tmp_first[1].rstrip('\n'))
    D = 10
    TFIDF = n/N * math.log(D/m)

    print '%s\t%s' % (word_file_name, TFIDF)
    

