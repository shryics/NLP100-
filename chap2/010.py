# -*- coding: utf-8 -*-
import sys
n = 0
f = open('hightemp.txt',encoding ='utf-8')

text = f.read()
f.close()

for moji in text:
    if moji == '\n':
        n = n + 1


print (n)
