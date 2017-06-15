#coding: utf-8
from __future__ import unicode_literals
import json
import sys

flag = 0
flag2 = 0
flag3 = 0
e_count = 0
pickup_cnt = 0
f = open('jawiki-country.json', 'r', encoding = 'utf-8')
word = 'イギリス'
word2 = 'Category:'
e_word2 = word2.encode('utf-8')

for line in f:
    temp = json.loads(line) #206記事ある。
    if '{}'.format(temp['title']) == word: #lineはイギリスに関して
        for line2 in ('{}'.format(temp['text'])): #line2は一文字　イギリスの本文記事数が37013
            if line2 == '\n' and flag2 == 1:
                if flag == 1:
                    sys.stdout.write(' ' + str(pickup_cnt))
                    sys.stdout.write(line2)
                e_count = 0
                flag = 0
                flag2 = 0
                flag3 = 0

            if line2 == '=':
                flag = 1
                e_count = e_count + 1
            else:
                if e_count >= 2:
                    pickup_cnt = e_count
                e_count = 0

            if e_count >= 2 and flag3 == 0:
                sys.stdout.write(line2)
                flag3 = 1

            if e_count >= 2 or flag2 == 1:
                flag2 = 1
                sys.stdout.write(line2)
