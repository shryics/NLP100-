# -*- coding: utf-8 -*-
import sys
import codecs
count = 0
f = open('hightemp.txt',encoding ='utf-8')

text = f.read()
text = text.replace('\ufeff', '')
lis = []
stri = ''
for moji in text:
    if moji == '\t':
        count = 1
    if count != 1:
        #sys.stdout.write(moji)
        stri = stri + moji
    if moji == '\n':
        count = 0
        if stri not in lis:
            lis.append(stri)
        stri = ''
        #print ('')


for moji in lis:
    print(moji)
