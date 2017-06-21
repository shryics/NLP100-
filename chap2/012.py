# -*- coding: utf-8 -*-
import sys
tab_count = 0
switch = 0
f = open('hightemp.txt')
f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')
text = f.read()
f.close()
for moji in text:
    if moji == '\t':
        tab_count = tab_count + 1
        switch = 1
    if tab_count == 0 and switch == 0:
        sys.stdout.write(moji)
        f1.write(moji)
    if tab_count == 1 and switch == 0:
        sys.stdout.write(moji)
        f2.write(moji)
    if switch == 1:
        sys.stdout.write(' ')
    switch = 0
    if moji == '\n':
        f1.write(moji)
        f2.write(moji)
        tab_count = 0
        print ('')

f1.close()
f2.close()


#flag1がオンの時かつ　次のタブが来るまでライトし続ける
