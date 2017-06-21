# -*- coding: utf-8 -*-
import sys

args = sys.argv
tab_c = 0
count = 1
args[1] = int(args[1])
f = open('hightemp.txt', 'r', encoding ='utf-8')
text = f.read()

for moji in text:
    if count <= args[1]:
        sys.stdout.write(moji)
    if moji == '\n':
        count = count + 1
