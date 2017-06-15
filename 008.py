
import sys

def cipher(moji):
    sentence = []
    for i in range(len(moji)):
        if 97 <= ord(moji[i]) and ord(moji[i]) <= 122: #暗号化
            sentence.append(chr(219 - ord(moji[i])))
            print ((chr(219 - ord(moji[i]))), end="")
        else:
            sentence.append(moji[i])
            print ((moji[i]), end="")
    print("")
    return sentence


base = 'Hello world!'
print (base)
sentence2 = cipher(base)
cipher(sentence2)
