import sys
import csv
import pandas as pd
from natto import MeCab

flag = 0
count = 0 #名詞　の　名詞　の　カウント用
max_len = -9999
max_noun_phrase = ''
noun_phrase = ""
header = 'surface,pos,pos1,pos2,pos3,活用型,活用形,base,読み,発音'
dic = {}
dic['surface'] = []
dic['pos'] = []
dic['pos1'] = []
dic['base'] = []
sentence = [] #一文ごとのリスト

f = open('neko.txt.mecab')
data = f.read()
f.close()
data = data.replace('\t', ',')

fw = open('neko.txt.mecab2', 'w')
fw.write(header)
fw.write(data)
fw.close()

data2 = pd.read_csv('neko.txt.mecab2')
data2.to_csv('neko.txt.mecab.csv')

#neko.txt.csv.mecab.csvは整形されたneko.txt.mecab
#これを使ってタプルを使ったマッピング型を形成する

fileread = open('neko.txt.mecab.csv', 'r')
dr = csv.reader(fileread)
for row in dr:
    if 'EOS' not in row and flag == 1:
        dic['surface'].append(row[1])
        dic['pos'].append(row[2])
        dic['pos1'].append(row[3])
        dic['base'].append(row[8])
        #print (row[1], row[2], row[3], row[8])
        if row[1] == '。':
            sentence.append(dic)
            dic = {}
            dic['surface'] = []
            dic['pos'] = []
            dic['pos1'] = []
            dic['base'] = []
    else:
        #print('')
        flag = 1

for moji in sentence:
    for i in range(len(moji['pos'])):
        if '名詞' == moji['pos'][i]:
            noun_phrase = noun_phrase + moji['base'][i]
        else:
            if max_len < len(noun_phrase):
                max_noun_phrase = noun_phrase
                max_len = len(noun_phrase)
            noun_phrase = ''

print (max_noun_phrase)
