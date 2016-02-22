#!/usr/bin/env python

import sys, time, re

#erase tweets
eraser = open('tweets2.txt', 'w+')
eraser.close()

file = open('tweets1.txt', 'r')
f=file.readlines()
file.close()

justtexts = ""

# print str(f)
pattern = r'["]text["]:["].+?["],'

for match in re.finditer(pattern, str(f)):
    # justtexts +" "+ match.group(0)
    print match.group(0)
