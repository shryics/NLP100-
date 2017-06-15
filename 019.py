# -*- coding: utf-8 -*-

import sys

count = 0
f = open('hightemp.txt', 'r')
text = f.read()
f.close()


for moji in text:
    if moji == '\t':
        count = count + 1
    if count == 0:
        sys.stdout.write(moji)
    if moji == '\n':
        count = 0
        print ''
