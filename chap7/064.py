
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

#keys = r.keys()
#vals = r.mget(keys)
#print(vals)

name = 'Benedicte Riis'
tags = (r.get(name).decode('utf-8'))
tags = tags.replace('[', '')
tags = tags.replace(']', '')
tags = tags.replace('{', '')
tags = tags.replace('}', '')
tags = tags.split(',')
print(name)
for i in range(int(len(tags)/2)):
    print(tags[i*2], tags[i*2-1])
