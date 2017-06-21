#coding: utf-8
from __future__ import unicode_literals
import json
n =0
f = open('jawiki-country.json', 'r', encoding ='utf-8')
word = 'イギリス'
word2 = 'category'
d_word2 = word2.encode('utf-8')
for line in f:
    temp = json.loads(line) #206記事ある。

    if '{}'.format(temp['title']) == word:
        print('記事:{}'.format(temp['text']))
        #if d_word2 in line:
