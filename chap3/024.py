#coding: utf-8
from __future__ import unicode_literals
import json
import sys
i = 0
flag = 0 #word3が検出されてから次の改行までの文字列表示のフラグ
flag2 = 0 #改行直後でふぁいる
flag3 = 0
e_count = 0
pickup_cnt = 0
f = open('jawiki-country.json', 'r', encoding = 'utf-8')
word = 'イギリス'
word2 = 'Category:'
word3 = 'ファイル:'
e_word2 = word2.encode('utf-8')
for line in f:
    temp = json.loads(line) #206記事ある。
    if '{}'.format(temp['title']) == word: #lineはイギリスに関して
        for line2 in ('{}'.format(temp['text'])): #line2は一文字　イギリスの本文記事数が37013
            if line2 == '\n':
                flag = 0
                flag2 = 1
                i = 0
            if flag == 1:
                sys.stdout.write(line2)
            if word3[i] == line2:
                i = i + 1
                if i == len(word3):
                    #sys.stdout.write(word3)
                    flag = 1
                    i = 0
                if i == 4 and flag2 == 1:
                    flag2 = 0
                    print ('')
            else:
                i = 0
print ('')
