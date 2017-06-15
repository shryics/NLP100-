#coding: utf-8
from __future__ import unicode_literals
import json
import sys
i = 0
count = 2
str_count = 0
flag = 0 #word3が検出されてから次の改行までの文字列表示のフラグ
flag0 = 0 #word3が見つかり次第オン
flag2 = 0 #改行直後でふぁいる
b_flag = 0
array_key = []
array_value = []
dic = {}
moji = ''
moji2 = ''
f = open('jawiki-country.json', 'r', encoding="utf-8")
#win環境ではencoding必須。UnicodeDecodeError: 'cp932' codec can't decode byte 0x85 in position 62: illegal multibyte sequence　しないと左のようなエラーが出る。
#win環境ではデフォルトでcp932でコーディングされるらしい。
word = 'イギリス'
word2 = 'Category:'
word3 = '基礎情報'
word4 = '}}'
for line in f:
    temp = json.loads(line) #206記事ある。
    if '{}'.format(temp['title']) == word: #lineはイギリスに関して
        for line2 in ('{}'.format(temp['text'])): #line2は一文字　イギリスの本文記事数が37013

            if word3[i] == line2 and flag0 == 0:
                i = i + 1
                if i == len(word3)-1:
                    flag0 = 1
                    flag  = 999
                    flag2 = 999
            else:
                i = 0

            if flag0 == 1:
                if line2 == '\n':
                        str_count = 0
                        b_flag = 1

                if str_count == 1 and line2 == '|':
                        if len(moji)  != 0:
                            array_value.append(moji)
                        if len(moji2) != 0:
                            array_key.append(moji2)
                        flag      = 0
                        flag2     = 1
                        str_count = 0
                        moji      = ''
                        moji2     = ''

                elif str_count == 1 and line2 != '|':
                        str_count = 3

                if (flag == 1 and str_count != 1) or b_flag == 1:
                        moji = moji + line2

                if line2 == '=':
                    flag = 1

                if flag == 0 and flag2 == 0:
                    moji2 = moji2 + line2

                #####################基礎情報の範囲を出たらbreak
                if line2 == '}':
                    count = count - 1
                    if count == 0:
                        array_key.append(moji2)
                        array_value.append(moji)
                        break
                elif line2 == '{':
                    count = count + 1
                ####################

                flag2 = 0
                b_flag = 0
                str_count = str_count + 1

array_value[51] = array_value[51].rstrip('}}\n')
for i in range(len(array_key)):
    array_key[i] = array_key[i].rstrip(' ')
    array_value[i] = array_value[i].lstrip()
    array_value[i] = array_value[i].rstrip('\n')

    if len(array_value[i]) == 0:
        del array_value[i]
    dic[array_key[i]] = array_value[i]


for k,v in dic.items():
    print (k,'            ',v)
