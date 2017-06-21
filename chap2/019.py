# -*- coding: utf-8 -*-
import sys
import codecs
count = 0
f = open('hightemp.txt',encoding ='utf-8')

text = f.read()
text = text.replace('\ufeff', '')
lis = []
lis_comp = []
lis_count = []
dic = {}
count = 0
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
        lis_comp.append(stri)
        stri = ''
        #print ('')




for i in range(len(lis)):
    for j in range(len(lis_comp)):
        if lis[i] == lis_comp[j]:
            count = count + 1

    lis_count.append(count)
    count = 0

for  i in range(len(lis)):
    dic[lis[i]] = lis_count[i]

for a,b in sorted(dic.items(), key=lambda x: x[1], reverse = True):
    print (a,b)
