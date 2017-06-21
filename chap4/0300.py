import sys
from natto import MeCab

f = open('neko.txt')

data = f.read()
f.close()

#m = MeCab.Tagger("-0chasen")
mc = MeCab()


fw = open('neko.txt.mecab', 'w')

fw.write(mc.parse(data))

fw.close()
