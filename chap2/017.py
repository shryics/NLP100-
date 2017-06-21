# -*- coding: utf-8 -*-
import sys
import codecs
count = 0
f = open('hightemp.txt', 'r')
text = f.read()
lis = []
for moji in text:
    if moji == '\t':
        count = 1
    if count != 1:
        sys.stdout.write(moji)
        lis.append(moji)
    if moji == '\n':
        count = 0
        print ''


for i in range(len(lis)):
    sys.stdout.write(lis[i])
