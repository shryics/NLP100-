# -*- coding: utf-8 -*-
import sys
n = 0
f = open('hightemp.txt')
f2 = open ('hightemp011.txt', 'w')
text = f.read()
f.close()

#f2 = oepn('testing.txt')

for moji in text:
    if moji == '\t':
        moji = ' '
    sys.stdout.write(moji)
    f2.write(moji)

f2.close()
