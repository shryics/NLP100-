# -*- coding: utf-8 -*-
import sys
import codecs
i = 0
count = 0
st = ''
lis = []
f = open('hightemp.txt', 'r', encoding ='utf-8')
text = f.read()
f.close()


for moji in text:
    if moji == '\t':
        count = count + 1
    if count == 2 and moji != '\t':
        #sys.stdout.write(moji)
        st = st + moji
    if moji == '\n':
        count = 0
        st = float(st)
        lis.append(st)
        st = ''
lis.sort(reverse=True) #降順
#lis.sort() #昇順

count = 0
for moji in text:
    if moji == '\t':
        count = count + 1
    if count == 2 and i <= len(lis):
        sys.stdout.write('\t')
        sys.stdout.write(str(lis[i]))
        count = 3
    elif count != 2 and count != 3:
        sys.stdout.write(moji)
    if moji == '\n':
        count = 0
        i = i + 1
