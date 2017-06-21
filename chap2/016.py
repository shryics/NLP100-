# -*- coding: utf-8 -*-
import sys

args = sys.argv
tab_c = 0
count = 0
args[1] = int(args[1])
f = open('hightemp.txt', 'r')
text = f.read()
cut = text.count('\n') / args[1]

for moji in text:
    if count < cut and moji != '\n':
        sys.stdout.write(moji)
    elif moji != '\n':
        print ('-----------------------------------')
        count = 0
    if moji == '\n':
        print ''
        count = count + 1
#print text.count('\n'), text.count('\n') / 11
