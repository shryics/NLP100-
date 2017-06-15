# -*- coding: utf-8 -*-
import sys

f1 = open('col1.txt', 'r')
f2 = open('col2.txt', 'r')
f3 = open('col3.txt', 'w')
text1 = f1.read()
text2 = f2.read()

f1.close()
f2.close()
i = 0
j = 0

for moji in text1:
    if moji != '\n':
        sys.stdout.write(moji)
        f3.write(moji)
    else:
        sys.stdout.write('\t')
        f3.write('\t')
        i = 0
        for moji2 in text2:
            i = i + 1
            if i > j:
                if moji2 == '\n':
                    print ''
                    f3.write(moji2)
                    j = i
                    break
                sys.stdout.write(moji2)
                f3.write(moji2)

f3.close()
