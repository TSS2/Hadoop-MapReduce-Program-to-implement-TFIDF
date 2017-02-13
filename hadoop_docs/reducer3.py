#!/usr/bin/env python

from operator import itemgetter
import sys
import re

current_word = None
current_count = 0
word = None
tmp_list={}
items_list=[]

# input comes from STDIN
for line in sys.stdin:
    items_display={}
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    temporary_var = re.split(r'\t+',line)

    word = temporary_var[0]
    tmp_first = temporary_var[1].split(' - ')
    tmp_second = tmp_first[1].split('/')
    tmp_third = tmp_second[1].split('&')
    count = tmp_third[1]
    items_display['word'] = temporary_var[0]
    items_display['file_name'] = tmp_first[0]
    items_display['n'] = tmp_second[0]
    items_display['N'] = tmp_third[0]
    items_list.append(items_display)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            #print '%s\t%s' % (current_word, current_count)
            tmp_list[current_word]=current_count
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    #print '%s\t%s' % (current_word, current_count)
    tmp_list[current_word]=current_count
    #print tmp_list


#for line in sys.stdin:
#    line = line.strip()
#    temporary_var = re.split(r'\t+',line)
#    file_name = temporary_var[0]
#    tmp = temporary_var[1].split(' - ')
#    word = tmp[0]
#    n = tmp[1]
#    key = str(word)+' - '+str(file_name)
#    value = n
#    print '%s\t%s' % (key,value)

for item in items_list:
     key = str(item['word'])+' - '+str(item['file_name'])
     value = str(item['n'])+'/'+str(item['N'])+'&'+str(tmp_list[item['word']])
     print '%s\t%s' % (key,value)
