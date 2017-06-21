#coding: utf-8
from __future__ import unicode_literals
import json
import sys
import re
pattern = re.compile('\'')
i = 0
count = 2
str_count = 0
mk_count = 0 # [[を検出するためのカウント
lk_count = 0 #[ が現れてから空白が出るまでの文字数をカウント
flag = 0 #word3が検出されてから次の改行までの文字列表示のフラグ
flag0 = 0 #word3が見つかり次第オン
flag2 = 0 #改行直後でふぁいる
flag3 = 0 #　’　が奇数回見つかった時はon
flag4 = 0 #[[の時　オン
flag5 = 0 #< > の　<　が出たときフラグが立ち > が出たときフラグが下がる
flag6 = 0 #flag5の {{ }} バージョン
flag7 = 0 # [ space ] の [フラグ
b_flag = 0

array_key = []
array_value = []
dic = {}
moji = '' #value文字
moji2 = '' #key文字
mk_moji = "" #[[]]内の文字
mk_moji_c = 0 #↑の文字数
chukakko_count = 0
chukakko_moji_count = 0
chukakko_flag = 0
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
                        lk_count = 0
                        b_flag = 1
                        print ('')
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

                    #28a
                    if line2 == '<':
                        flag5 = 1
                        lk_count = 0
                    #28a

                    #####26,27
                    if line2 != '\'' and  flag5 != 1 and line2 != '{' and line2 != '}':
                        moji = moji + line2

                    #####26,27
                    if line2 == ']':
                        flag4 = 0
                        flag7 = 0
                        mk_count = 0
                        mk_moji = ''
                    if line2 == '|' and flag7 == 1:

                        flag4 = 0

                        moji = moji[:-len(mk_moji)]
                        mk_moji = ''
                    if flag4 == 1:
                        mk_moji = mk_moji + moji
                        mk_moji_c = mk_moji_c + 1
                        sys.stdout.write(line2)
                    if line2 == '[':
                        mk_count = mk_count + 1
                        flag7 = 1
                        if mk_count == 2:
                            mk_count = 0
                            flag4 = 1
                            mk_moji_c = 0
                    #####26,27



                    ###########リンクを削除 [[ ]] <> が関係有
                    if flag7 == 1:
                        lk_count = lk_count + 1
                    if line2 == ' ' and flag7 == 1:
                        if 'http' in moji:
                            moji = moji[:-(lk_count)]
                            moji = moji + ' '
                        elif 'ファイル' in moji:
                            pass
                        else:
                            moji = moji[:-(lk_count)+5]
                        flag7 = 0
                        lk_count = 0
                    ###########リンクを削除

                    #28a
                    if line2 == '>':
                        flag5 = 0
                    #28a

                    ###################中カッコ内の処理
                    if line2 == '}':
                        chukakko_moji_count = 0
                        chukakko_flag = 0

                    if chukakko_flag == 1:
                        if line2 != '|':
                            chukakko_moji_count = chukakko_moji_count + 1
                        else:

                            moji = moji[:-(chukakko_moji_count+1)]
                            chukakko_moji_count = 0

                    if line2 == '{':
                        chukakko_count = chukakko_count + 1
                    if chukakko_count == 2:
                        chukakko_flag = 1
                        chukakko_count = 0
                    ###################中カッコ内の処理









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

    if len(array_value[i]) == 0 and i != 50:
        del array_value[i]

    dic[array_key[i]] = array_value[i]




for k,v in dic.items():
    print (k,'                   ',v)
