import copy

moji1 = "paraparaparadise"
moji2 = "paragraph"
wa = []
seki = []
sa = []
i = 0
j = 0
c = 0
d = 0
e = 0
f = 0
array1 = [0] * (len(moji1)-1)
array2 = [0] * (len(moji2)-1)

for i in range(len(moji1)-1):
    array1[i] = moji1[i:i+2]

for i in range(len(moji2)-1):
    array2[i] = moji2[i:i+2]

for i in range(len(moji1)-1):
    for j in range(i):
        if array1[i] == array1[j]:
            array1[i] = 0

for i in range(len(moji2)-1):
    for j in range(i):
        if array2[i] == array2[j]:
            array2[i] = 0

for i in range(len(moji1)-1-c):
    if array1[i-c] == 0:
        del array1[i-c]
        c = c + 1

for i in range(len(moji2)-1-d):
    if array2[i-d] == 0:
        del array2[i-d]
        d = d + 1
print ("Xの集合")
print (array1)
print ("Yの集合")
print (array2)

for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] == array2[j]:
            seki.append(array1[i])
print ("積集合")
print (seki)

sa = copy.deepcopy(array1)

for i in range(len(sa)-e):
    for j in range(len(seki)):
        if sa[i-e] == seki[j]:
            del sa[i-e]
            e = e + 1
print ("差集合")
print (sa)

for i in range(len(array1)):
    wa.append(array1[i])



for i in range(len(array2)):
    for j in range(len(wa)):
        if wa[j] == array2[i]:
            flag = 1
            break

    if flag != 1:
        wa.append(array2[i])
    flag = 0
print ("和集合")
print (wa)

se_flag = 0
for i in range(len(array1)):
    if "se" == array1[i]:
        print("Xに'se'というbi-gramが含まれます")
        se_flag = 1
        break
if se_flag == 0:
    print("Xに'se'というbi-gramが含まれません")

se_flag = 0

for i in range(len(array2)):
    if "se" == array2[i]:
        print("Yに'se'というbi-gramが含まれます")
        se_flag = 1
        break
if se_flag == 0:
    print("Yに'se'というbi-gramが含まれません")
