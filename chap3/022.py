#coding: utf-8
from __future__ import unicode_literals
import json
import sys
n =0
i =0
base = []
flag = 0
ccount = 0
f = open('jawiki-country.json', 'r', encoding = 'utf-8')
word = 'イギリス'
word2 = 'Category:'
ccount = 0
check_c = 0
e_word2 = word2.encode('utf-8')
for line in f:
    temp = json.loads(line) #206記事ある。
    if '{}'.format(temp['title']) == word: #lineはイギリスに関して
        for line2 in ('{}'.format(temp['text'])): #line2は一文字　イギリスの本文記事数が37013
            if line2 == '\n':
                ccount = ccount + 1
            if (word2[i]) == line2:
                if i < len(word2)-1:
                    i = i + 1
                else:
                    i = 0
                    check_c = ccount
                    break
            else:
                i = 0
        ccount = 0
        for line2 in ('{}'.format(temp['text'])): #line2は一文字　イギリスの本文記事数が37013
            if line2 == '\n':
                ccount = ccount + 1
                flag = 0
            if ccount >= check_c:
                if line2 == '\n':
                    sys.stdout.write(line2)
                if flag == 1 and line2 != ']':
                    sys.stdout.write(line2)
                if line2 == ':':
                    flag = 1


print ('')
